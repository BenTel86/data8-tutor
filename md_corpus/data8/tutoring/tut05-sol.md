# Tutoring 05 Data C8 Spring 2026

## Page 1

## Sampling & Hypothesis Testing

Tutoring 05

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Sampling

![Text panel explaining populations, population parameters, samples, and sample statistics. It lists sampling methods for tables, probability models, and arrays.](images/tut05-sol_page001_vector001.png)

Population and Samples Due to time and resource constraints, it is typically only feasible to analyze samples rather than entire populations. Our goal is to infer some characteristics of the population, called population parameters, by studying our samples. In many cases, we are interested in estimating these parameters using sample statistics, values we compute from a sample of the population.

For example, you may be interested in knowing the percentage of all eligible voters who are planning on voting for Candidate - Since asking everyone in the U.S. who they plan to vote for is clearly infeasible, what we can do is take a sample.

Here are the different methods we use to take samples: - If you are sampling from a pre-existing table: tbl.sample(sample_size) - If you are sampling from a defined probabilistic model: sample_proportions(sample_size, model_proportions) - If you are sampling from an array: np.random.choice(array, sample_size)

#### Practice Problems

- Let’s use the example of rolling a fair die. Is rolling a die sampling with replacement or without replacement?

With replacement.

- Calculate the probability of rolling a 5. Is this an empirical or a theoretical probability? Is there a relationship between

the two?

The probability that we roll a 5 is 1

6.

This is a theoretical probability. We could get an empirical probability by rolling the die over and over again and estimating the theoretical probability of rolling a 5 based on the frequency of 5′s we observe. We expect that the more times we simulate our experiment (rolling the die), the better we will be able to estimate the theoretical probability (hence our empirical probability will converge to the theoretical one). This is often referred to as the Law of Large Numbers.

- Suppose that we have a table called dice, which has one column Side and contains the values 1 through 6. Complete the

function roll_die, which takes in no arguments and uses the dice table to simulate rolling a fair die once. Hint: the function should return an integer between 1 and 6.

def roll_die():

_____________________________________

return np.random.choice(dice.column("Side"))

#### or

return dice.sample(...).column(0).item(0)

Note: Since we are doing .item(0) on the result of .sample(), the sample size (as long as it’s valid) actually does not matter. Additional note: If we specified a sample size in np.random.choice(), we would actually need a .item(0) at the end! Specifying a sample size in np.random.choice() actually returns an array, even if the sample size is just 1.

- Simulate rolling a fair die 10 times and store the results in an array called simulated_rolls, using roll_die().

## Page 2

simulated_rolls = make_array()

for i in ____________________________:

face = ________________________________ simulated_rolls = ______________________________

simulated_rolls = make_array() for i in np.arange(10): face = roll_die() simulated_rolls = np.append(simulated_rolls, face)

- We have generated histograms of simulated rolls for samples of size 10, 100, 1000, and 10,000. Which histograms correspond

to which sample sizes, and why? Do these histograms show a theoretical or empirical distribution?

![Four bar charts A-D show percent per unit for die faces 1-6. A and B are uneven, while C and D are near-uniform around 14-18%; B is dominated by face 2 at 40%.](images/tut05-sol_page002_image001.png)

#### A B C D

#### (A, 100), (B, 10), (C, 10000), (D, 1000)

As the number of trials increases, the empirical distribution (which these histograms are) should converge to the theoretical probability distribution. Intuitively, you can think that in a small number of trials, there is a lot of randomness that might make the distribution diverge from what we would predict. Additionally, you can think about it this way: getting five 6′s in ten rolls is a lot more likely to happen than getting 50 6′s in 100 rolls.

Data C8 Spring 2026 Tutoring 05 | 2

## Page 3

## 2. Hypothesis Testing

#### (a) Suppose your friend Lena is into bottle flipping, and she lets you try out the best bottle in her collection. According to Lena,

#### her best bottle lands right side up with a 2/3 chance and lands on its side with a 1/3 chance. You flip the bottle 60 times and observe a successful bottle flip 45 times.

#### Does the bottle that you are flipping seem consistent with Lena’s model? Why or why not?

Yes, the water bottle you are flipping seems consistent with your friend’s model. The model stated a probability of 2/3 landing right side up, which would mean that we expect 40 flips to land right side up. We observed 45 flips landing right side up, which is not too different from the expected amount. Though simply being “consistent” is not currently well defined, we will soon see how was can make this more concrete.

#### (b) Complete the function flip_bottle, which takes in no arguments and randomly flips the bottle described above 60 times.

#### The function should return the number of successful bottle flips out of the 60 flips. Refer to the Reference Sheet if you need a refresher on sample_proportions!

def flip_bottle():

probabilities = ____________________________________________________________________________________ empirical_props = __________________________________________________________________________________ prop_flipped = _____________________________________________________________________________________ return _____________________________________________________________________________________________

def flip_bottle(): probabilities = make_array(2/3, 1/3) empirical_props = sample_proportions(60, probabilities) prop_flipped = empirical_props.item(0) return prop_flipped * 60

#### (c) Complete the code below to simulate the experiment described above 10000 times, and record the number of bottles flipped

#### in each of these experiments in an array called bottles_flipped.

trials = ________________________________________

bottles_flipped = _______________________________

for i in _________________________________________________________:

one_experiment = _______________________________________________________ _________________ = ____________________(_________________________________________________________) Table().with_column("Successful Flips", bottles_flipped) .hist("Successful Flips", bins=np.arange(25, 60, 1))

trials = 10000 bottles_flipped = make_array() for i in np.arange(trials): one_experiment = flip_bottle() bottles_flipped = np.append(bottles_flipped, one_experiment) Table().with_column("Successful Flips", bottles_flipped).hist("Successful Flips", bins = np.arange(25, 60, 1))

#### (d) Suppose you performed the simulation and plotted a histogram of bottles_flipped. The histogram is shown below. Was

#### observing 45 successful bottle flips consistent with the model you simulated under?

#### Data C8 Spring 2026 Tutoring 05 | 3

## Page 4

![Histogram of successful flips, with percent per unit on the y-axis. The distribution is roughly bell-shaped from about 29 to 51 flips and peaks near 41-42 at about 11%.](images/tut05-sol_page004_image001.png)

Yes, 45 successful bottle flips is consistent with the model we simulated under. If we look for 45, we will see that it still occurred a reasonable number of times (it was not rare in our simulation). Therefore, it is consistent with the model we simulated under.

Data C8 Spring 2026 Tutoring 05 | 4

## Page 5

### 3. Welcome

The table welcome_tbl contains the results of the Fall 2021 Data 8 welcome survey. The first two rows are shown below. Each row corresponds to a student. In the column Extroversion, each student scored themselves on a scale of 1 (not extroverted) to 10 (extremely extroverted).

(Fall 2021 Midterm Question 8)

![Two-row table with columns Year, Extroversion, Number of Texteees, Hours of Sleep, Handedness, First Pant Leg, and Sleep Position. Both rows are second-year, right-handed, right-leg-first, and left-side sleepers.](images/tut05-sol_page005_vector001.png)

#### Year Extroversion Number of Textees Hours of Sleep Handedness First Pant Leg Sleep Position

Second 8 5 6 Right-handed Right Left

Second 7 8 7.5 Right-handed Right Left

- Complete the code below to define a function max_extroversion that takes sample_size as its argument. The function

should sample sample_size many times at random without replacement from all the students, and return the maximum extroversion score among the sampled students.

def max_extroversion(________________________):

sampled_students = ______________________________________________

_________________________________________________________________

def max_extroversion(sample_size): sampled_students = welcome_tbl.sample(sample_size, with_replacement = False) return max(sampled_students.column("Extroversion"))

- We decide to simulate 10,000 values of maximum extroversion score, drawing random samples of size 25 without replacement.

Complete the code below so the last line evaluates to an array of 10,000 simulated values from all students. Your code should use the max_extroversion function that you defined above.

repetitions = ______________________

sim_vals = _________________________

for ______________________ in ______________________:

________________________________________________________________ ________________________________________________________________

repetitions = 10000 sim_vals = make_array() for i in np.arange(repetitions): one_sim_max = max_extroversion(25) sim_vals = np.append(sim_vals, one_sim_max)

- A student mistypes the sample size in the previous question to be 55 instead of 25. One of the histograms below shows the

distribution of the maximum values simulated by this student. The other shows the distribution of the maximum values that you simulated using a sample size of 25. Which is which? Why?

Data C8 Spring 2026 Tutoring 05 | 5

## Page 6

![Side-by-side histograms A and B of sample maximum. A has values 7-10 increasing from about 25% to 41%; B is more concentrated near 10, rising from about 5% at 7-8 to 69% at 9-10.](images/tut05-sol_page006_image001.png)

A is sample of 25, B is sample of 55. The probability of containing 10 (the population maximum) in a given sample is larger for a larger sample size!

You can also think about it this way: are you more likely to get a 6 in one roll of a die, or 10 rolls of a die? A similar principle applies here in this question!

Data C8 Spring 2026 Tutoring 05 | 6
