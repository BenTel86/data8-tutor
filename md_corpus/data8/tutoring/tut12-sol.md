# Tutoring 12 Data C8 Spring 2026

## Page 1

## Final Review

Tutoring 12

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Testing Chance Models

Roulette is a casino game in which a ball falls into one pocket in a spinning wheel, and players bet on the color of the pocket in which the ball falls. If the player correctly picks the color, they win. 18 of the 38 pockets in a roulette wheel are red. You play 30 games of roulette, bet on red every time, and win 20 of those games. You become suspicious about the fairness of this roulette game.

#### (a) State a null and alternative hypothesis to see whether the roulette game is biased towards red.

Null Hypothesis:

The roulette game is fair, with an 18/38 chance of the ball falling into a red pocket. The observed number of wins on red is simply due to chance.

Alternative Hypothesis:

The ball is more likely to fall into red pockets. The observed number of wins on red is not just due to chance.

- With your alternative hypothesis in mind, choose a test statistic and calculate its observed value. Your test statistic should

be large for data favoring the alternative hypothesis.

Test Statistic:

The proportion of wins on red in 30 games. You can similarly do: “The proportion of wins on red in 30 games - The expected proportion of wins on red in 30 games”, though the expression will be rather nasty so we will stick to the first test statistic.

Observed Value:

20/30 = 2/3.

- Complete the function prop_wins(), which takes in no arguments and simulates playing the game 30 times and returns the

proportion of wins when you guess red every time.

def prop_wins():

proportions = ____________________________________________________ thirty_games = ___________________________________________________ simulated_prop = _________________________________________________ return simulated_prop

def prop_wins(): proportions = make_array(18/38, 20/38) thirty_games = sample_proportions(30, proportions) simulated_prop = thirty_games.item(0) return simulated_prop

- Complete the code below to simulate an empirical distribution of the test statistic using 10000 iterations, storing the statistics

in an array called simulated_stats.

simulated_stats = _________________________________________________

## Page 2

__________________________________________:

________________________________________________________ ________________________________________________________

simulated_stats = make_array() for i in np.arange(10000): one_sim = prop_wins() simulated_stats = np.append(simulated_stats, one_sim)

#### (e) Write a line of code to calculate the p-value.

_____________________________________________________________________________

p_value = np.count_nonzero(simulated_stats >= (2/3)) / 10000

#### (f) Suppose you find a p-value of 0.0103. What do you conclude about the null hypothesis, at a p-value cutoff of 5%?

#### We should reject the null hypothesis, as the empirical p-value (0.0103) is below the cutoff of 5% or 0.05.

#### Data C8 Spring 2026 Tutoring 12 | 2

## Page 3

### 2. A/B Testing Review

We are examining the weights of a population of cats and dogs. You are given a random sample from this population, stored in the table pets, which has two columns. The first column "Animal" contains a string, either "Cat" or "Dog". The second column

"Weight" contains the weights of each of the animals in pounds as floats. You notice that the average weight of dogs in your sample is 3 pounds heavier than the average weight of cats in your sample.

- State a null and alternative hypothesis to see if dogs weigh more than cats on average in the population.

Null Hypothesis:

The distributions of the weights of dogs and the distribution of the weights of cats is the same. The difference observed in the sample is purely due to chance.

Alternative Hypothesis:

The weights of dogs, on average, are greater than the weights of cats in the population. The difference observed in the sample is not just due to chance.

- With your alternative hypothesis in mind, choose a test statistic and calculate its observed value. Your test statistic should

be large for data favoring the alternative hypothesis.

Test Statistic: The difference between the mean dog weight and the mean cat weight.

Observed Value: 3

- Complete the function one_stat() which takes in no arguments and returns one value of the test statistic.

def one_stat():

shuffled_animals = ________________________________________________________________________ shuffled_table = pets.with_columns("Animal", shuffled_animals) means_table = _____________________________________________________________________________ means_arr = _______________________________________________________________________________ ___________________________________________________________________________________________

def one_stat(): shuffled_animals = pets.sample(with_replacement=False).column("Animal") shuffled_table = pets.with_columns("Animal", shuffled_animals) means_table = shuffled_table.group("Animal", np.mean) means_arr = means_table.column(1) return means_arr.item(1) - means_arr.item(0)

- Complete the below code to simulate an empirical distribution of 5000 test statistics under the assumptions of the null

hypothesis.

diffs = __________________________________________________________________

__________________________________________________________________:

stat = _____________________________________________ ____________________________________________________

diffs = make_array() for i in np.arange(5000): stat = one_stat() diffs = np.append(diffs, stat)

Data C8 Spring 2026 Tutoring 12 | 3

## Page 4

#### (e) Write a line of code to calculate your p-value.

_____________________________________________________________________________

p_value = np.count_nonzero(diffs >= 3) / 5000

#### (f) Suppose you find a p-value of 0.0013. What do you conclude, at a p-value cutoff of 5%?

The empirical p-value of 0.0013 is less than our p-value cutoff of 5%, so we will reject the null hypothesis in favor of the alternative hypothesis.

Data C8 Spring 2026 Tutoring 12 | 4

## Page 5

### 3. Probability Review

Max and Saleh are playing squash in the RSF. Before each game, they draw their rackets from a bucket. Max gets a boost from playing with his favorite racket, the lucky blue racket, while Saleh is unaffected by which racket he draws. Assume that Max has a 25% chance of drawing the lucky blue racket.

Additionally, assume that: - If Max has the lucky blue racket for a game, he has a 90% chance of winning. - If Max does not have the lucky blue racket for a game, he has a 65% chance of winning.

Please leave your answers in a mathematical expression.

#### (a) What is the probability that Max draws the lucky blue racket 4 times in a row?

0.254

#### (b) What is the probability that Max draws the lucky blue racket but loses?

0.25 ∗0.10

#### (c) What is the probability that Saleh wins a randomly chosen game? Assume that there are no ties.

1 −(0.25 ∗0.90 + 0.75 ∗0.65)

#### (d) If Max wins a game, what is the probability that he was playing with the lucky blue racket?

0.25∗0.90 0.25∗0.90+0.75∗0.65

- Suppose Max and Saleh play 9 games in a row, redrawing their rackets each time. What is the chance that Max draws the

lucky blue racket at least once?

1 −0.759

- To increase his advantage, Max buys a second lucky blue racket and places it into the bucket. Fed up, Saleh counts all of the

rackets in the bucket and finds that there are now 5 rackets. He insists on rackets being drawn randomly and getting to draw first. What is the new probability of Max receiving a lucky blue racket?

2 5 ∗ 1 4 + 3 5 ∗ 2 4

Data C8 Spring 2026 Tutoring 12 | 5
