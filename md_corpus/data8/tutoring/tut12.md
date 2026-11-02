# Tutoring 12 Data C8 Spring 2026

## Page 1

## Final Review

Tutoring 12

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Testing Chance Models

Roulette is a casino game in which a ball falls into one pocket in a spinning wheel, and players bet on the color of the pocket in which the ball falls. If the player correctly picks the color, they win. 18 of the 38 pockets in a roulette wheel are red. You play 30 games of roulette, bet on red every time, and win 20 of those games. You become suspicious about the fairness of this roulette game.

#### (a) State a null and alternative hypothesis to see whether the roulette game is biased towards red.

- With your alternative hypothesis in mind, choose a test statistic and calculate its observed value. Your test statistic should

be large for data favoring the alternative hypothesis.

- Complete the function prop_wins(), which takes in no arguments and simulates playing the game 30 times and returns the

proportion of wins when you guess red every time.

def prop_wins():

proportions = ____________________________________________________ thirty_games = ___________________________________________________ simulated_prop = _________________________________________________ return simulated_prop

- Complete the code below to simulate an empirical distribution of the test statistic using 10000 iterations, storing the statistics

in an array called simulated_stats.

simulated_stats = _________________________________________________

__________________________________________:

________________________________________________________ ________________________________________________________

#### (e) Write a line of code to calculate the p-value.

_____________________________________________________________________________

- Suppose you find a p-value of 0.0103. What do you conclude about the null hypothesis, at a p-value cutoff of 5%?

## Page 2

### 2. A/B Testing Review

We are examining the weights of a population of cats and dogs. You are given a random sample from this population, stored in the table pets, which has two columns. The first column "Animal" contains a string, either "Cat" or "Dog". The second column

"Weight" contains the weights of each of the animals in pounds as floats. You notice that the average weight of dogs in your sample is 3 pounds heavier than the average weight of cats in your sample.

- State a null and alternative hypothesis to see if dogs weigh more than cats on average in the population.

- With your alternative hypothesis in mind, choose a test statistic and calculate its observed value. Your test statistic should

be large for data favoring the alternative hypothesis.

- Complete the function one_stat() which takes in no arguments and returns one value of the test statistic.

def one_stat():

shuffled_animals = ________________________________________________________________________ shuffled_table = pets.with_columns("Animal", shuffled_animals) means_table = _____________________________________________________________________________ means_arr = _______________________________________________________________________________ ___________________________________________________________________________________________

- Complete the below code to simulate an empirical distribution of 5000 test statistics under the assumptions of the null

hypothesis.

diffs = __________________________________________________________________

__________________________________________________________________:

stat = _____________________________________________ ____________________________________________________

#### (e) Write a line of code to calculate your p-value.

_____________________________________________________________________________

#### (f) Suppose you find a p-value of 0.0013. What do you conclude, at a p-value cutoff of 5%?

Data C8 Spring 2026 Tutoring 12 | 2

## Page 3

### 3. Probability Review

Max and Saleh are playing squash in the RSF. Before each game, they draw their rackets from a bucket. Max gets a boost from playing with his favorite racket, the lucky blue racket, while Saleh is unaffected by which racket he draws. Assume that Max has a 25% chance of drawing the lucky blue racket.

Additionally, assume that: - If Max has the lucky blue racket for a game, he has a 90% chance of winning. - If Max does not have the lucky blue racket for a game, he has a 65% chance of winning.

Please leave your answers in a mathematical expression.

#### (a) What is the probability that Max draws the lucky blue racket 4 times in a row?

#### (b) What is the probability that Max draws the lucky blue racket but loses?

#### (c) What is the probability that Saleh wins a randomly chosen game? Assume that there are no ties.

#### (d) If Max wins a game, what is the probability that he was playing with the lucky blue racket?

- Suppose Max and Saleh play 9 games in a row, redrawing their rackets each time. What is the chance that Max draws the

lucky blue racket at least once?

- To increase his advantage, Max buys a second lucky blue racket and places it into the bucket. Fed up, Saleh counts all of the

rackets in the bucket and finds that there are now 5 rackets. He insists on rackets being drawn randomly and getting to draw first. What is the new probability of Max receiving a lucky blue racket?

Data C8 Spring 2026 Tutoring 12 | 3
