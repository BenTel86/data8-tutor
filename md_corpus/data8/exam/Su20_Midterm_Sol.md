---
title: "Summer 2020 Midterm — Solution view"
course: Data 8
exam: Su20_Midterm_Sol
semester: su20
term: Summer
year: 2020
exam_type: midterm
view: solution
source: exams/data8/sp26/Su20_Midterm_Sol.pdf
student_file: Su20_Midterm.md
pages: 15
---

# Summer 2020 Midterm — Solution view

> **Solution view.** Staff answers are included: written and coded answers appear inline, and the option the staff selected is marked `[x]` (choose one or more) or `(x)` (choose one). Use these to guide a student or check their reasoning — never hand the answer over directly. The same exam without answers is in [Su20_Midterm.md](Su20_Midterm.md).

## Page 1

#### 1. Arrays and Tables (27 points)

The artists table contains data about numerous artists who have work displayed in the Museum of Modern Art (MoMA). Each artist has a unique ID number that can be used to identify artwork, represented by the column Artist ID. A few rows are shown below:

![Image containing text: The artworks table contains some information about the art pieces displayed in MoMA, and a few rows are shown below:](images/Su20_Midterm_Sol_page001_image001.png)

The artworks table contains some information about the art pieces displayed in MoMA, and a few rows are shown below:

![Image extracted from page 1](images/Su20_Midterm_Sol_page001_image002.png)

Fill in the blanks with the corresponding Python expressions.

a. The nationality of the artist who lived the fourth longest. You can assume that each artist died at a different age. 4 pts

age = artists.with_column(“Age at Death”, _______(i)_______) age._______(ii)_______._______(iii)_______._______(iv)_______

Blank i: artists.column(‘Death Year’) - artists.column(‘Birth Year’) Blank ii: sort(‘Age at Death’, descending = True) Blank iii: column(‘Nationality’) Blank iv: item(3)

b. The name of the artist that was born the earliest in the 20th century (1900s). In answering this question you can assume that no two artists are born in the same year and no artist is born after 1999. 4 pts

filtered_by_birth_year = __________(i)__________

## Page 2

filtered_by_birth_year.__________(ii)__________

Blank i: artists.where(‘Birth Year’, are.between(1900,1999)) Blank ii: sort(‘Birth Year’).column(‘Name’).item(0)

c. The number of art pieces in MoMA that are classified as “Print” and were created after 1. 4 pts

____(i)____.where(“Date”, ____(ii)____).____(iii)____.___(iv)____

Blank i: artworks Blank ii: are.above(1950) Blank iii: where(‘Classification’, are.equal(‘Print)) Blank iv: num_rows

#### d. The birth year of the artist that created the tallest (by height) piece of artwork. 5 pts

artists_and_artwork = artists._____(i)_____ artists_and_artwork._____(ii)_____._____(iii)_____._____(iv)___ __

Blank i: join(‘Artist ID’, artworks) Blank ii: sort(‘Height(cm)’, descending = True) Blank iii: column(‘Birth Year’) Blank iv: item(0)

#### e. The highest mean height among all combinations of department and classification. 5 pts

______(i)_____(______(ii)______.______(iii)______._____(iv)____ _)

Blank i: max Blank ii: artworks Blank iii: group([‘Department’, ‘Classification’], np.average) Blank iv: column(“Height (cm) average’’)

f. Many artists have many pieces of work in MoMA. Create a table with two columns named “Name” and “Width (cm) average” that reflects the mean width of all pieces created by an artist. 5 pts

artists.______(i)______.______(ii)______.______(iii)______

## Page 3

Blank i: join(‘Artist ID’, artworks) Blank ii: group(‘Artist ID’, np.average) Blank iii: select(‘Name’, ‘Width (cm) average’)

## Page 4

#### Data Types, Visualizations, and Histograms (6 points)

#### 2. Data Type Pot Pourri:

#### a) Which pairs of table methods return the same type? Select all that apply. 3 pts

i) .column() and .select() [ ] ii) .relabled() and .group() [X] iii) .pivot() and .join() [X] iv) .take() and .where() [X] v) .drop() and .num_rows [ ] vi) .apply() and .where() [ ]

- Cynthia writes the following code:

#### ‘early_losses = games.where('Opponent', 'UC Berkeley').column(2).num_rows`

She receives the following error message: 'numpy.ndarray' object has no attribute 'num_rows', and needs help debugging. 3 pts

What is the best explanation for this error?

i) `games` is a table with no rows [ ] ii) `games` only has 2 columns [ ] iii) the num_rows attribute only exists for rows and not for columns [ ] iv) the num_rows attribute must follow a table type [ x ]

## Page 5

#### 3. GDP Growth Rates (14 points)

Congrats! You’ve just got your dream internship working as a research assistant for the Economics Department’s illustrious Professor Olney! She wants you to analyze the GDP per capita growth rates of African countries. Let’s get started.

Professor Olney provides you with the table below, called gdp_africa, which has two columns:

- Country: The name of the country - GDP per capita Growth(%): the GDP per capita growth rate (2018)

The first five rows are displayed below:

![Image containing text: To visualize the distribution of GDP per capita growth rates in Africa, you plan to generate a histogram using gdp_africa. a) Given that no country in Africa had a GDP per capita growth rate higher than 8% or lower than -10% in 2018, construct bins that reflect this range with bin widths of 2%. 2 pts](images/Su20_Midterm_Sol_page005_image001.png)

To visualize the distribution of GDP per capita growth rates in Africa, you plan to generate a histogram using gdp_africa.

- Given that no country in Africa had a GDP per capita growth rate higher than 8% or

#### lower than -10% in 2018, construct bins that reflect this range with bin widths of 2%. 2 pts

gdp_bins = ___________________ gdp_bins = np.arange(-10, 9, 2)

- Write a line of code that would produce a histogram using the GDP per capita bins you

#### just created. 2 pts

gdp_africa.____________________ gdp_africa.hist(1, bins=gdp_bins)

## Page 6

Now that you’ve run your histogram code, we find that the histogram for 2018 GDP per capita growth rates for African countries looks like this:

![Image extracted from page 6](images/Su20_Midterm_Sol_page006_image001.png)

c) What percentage of countries in Africa had a GDP per capita growth rate between -2% and 0% in 2018? 2 pts

- Between 6% and 7.5% [ ] (ii) Between 12% and 15% [x] (iii) Between 15% and 17.5% [ ] (iv) None of the above [ ]

#### d) How many countries in Africa had a GDP per capita growth rate of between 2% and 3% in 2018? 2 pts

#### (i) 18 [ ] (ii) 36 [ ] (iii) 40 [ ] (iv) Cannot tell with the information given [x]

## Page 7

e) Assume the heights of each bar are as follows:

GDP Growth Range

[-10, -8)

[-8, -6) [-6, -4) [-4, -2) [-2, 0) [0, 2) [2, 4) [4, 6) [6, 8)

Height (%)

0.93 0 1.85 0.93 7.41 16.67 18.52 3.70 0

Using the information above, write a mathematical expression that evaluates to the approximate number of countries in Africa that had a GDP per capita growth rate of between 0% and 6% in 2018. There are 54 countries represented in the table gdp_africa. There is no need to round. 4 pts

2 * (16.67 + 18.52 + 3.70) / 100 * 54 = 42

#### f) Select all statements that are true. 2 pts

- This distribution is left-skewed [ ]
- Most countries had a positive GDP per capita growth percentage in 2018 [ ]
- The GDP per capita growth percentage’s median is smaller than its mean [ ]

- This distribution of GDP per capita growth rates is left-skewed [x]
- Most countries had a positive GDP per capita growth percentage in 2018 [x]
- The GDP per capita growth percentage’s median is smaller than its mean [ ]

## Page 8

#### 4. Probability (22 points)

On a hot summer day, Jo decides to drop by the local creamery for ice cream. The local creamery has four flavors: vanilla, chocolate, strawberry, and the flavor of the month, orange. Jo is worried that he had his craving too late in the day and the creamery might have ran out of his favorite flavor combination: vanilla and orange swirl.

On any given day, the chance that the creamery runs out of vanilla, chocolate, or strawberry is equal to 1/6. Since orange is a speciality flavor, the probability that the creamery runs out orange is ⅓. These events are independent of one another.

Please leave your answers as an unsimplified expression. For example, your answers may take the form of 7/10, (7/10) * (5/8), or (7/10) * (5/8) + (6/10) * (1/8).

#### Show all your work in the provided cells.

a. If Jo visits the creamery right before they close, what is the probability that Jo gets what he wants? 3 points (5/6) * (2/3) = 5/9

#### b. Suppose that Jo would be happy with vanilla and orange swirl, or a strawberry

cone. If there are no vanilla and orange swirls left, Jo would order a strawberry cone. Given that Jo is happy, what is the probability he got the vanilla and orange swirl? Recall that flavors run out independently of each other. 5 points P(happy) = P(having swirl) * P(happy | swirl) + P(not having swirl) * P(strawberry doesn’t

run out | not having swirl) = 5/9 * 1 + 5/6 = 41

45

P(having swirl | happy) = P(having swirl) * P(happy | swirl) / P(happy) = 5/9 / 41/45 = 25

41

5/9 / (5/9 * 1 + 4/9* ⅚) = 3/5

c. Suppose that if the creamery runs out of chocolate ice cream, the chance that they also run out of vanilla ice cream by the end of the day increases to 3/4. If you aren’t sure if the shop has run out of chocolate yet, what is the probability that Jo gets what he wants? 5 points P(chocolate doesn’t run out) * P(vanilla doesn’t run out | chocolate doesn’t run out) * P(orange doesn’t run out | chocolate doesn’t run out) + P(chocolate runs out) * P(vanilla doesn’t run out | chocolate runs out) * P(orange doesn’t run out | chocolate doesn’t run out) (5/6 * 5/6 * 2/3) + (1/6 * 1/4 * 2/3)

## Page 9

Alternate solution (if students assumed that joe wanted an vanilla-orange swirl or a strawberry cone:

![Image extracted from page 9](images/Su20_Midterm_Sol_page009_image001.jpeg)

When Jo gets to the creamery, he finds out that they’re having a special promotion! The store has a box full of coupons that customers can draw from. The discount listed on the coupon drawn is applied to the customer’s purchase. After the transaction is complete, the coupon is placed back into the box.

There are 50 coupons in the box: 30 coupons are for a 25% discount, 10 coupons are for a 50% discount, 8 coupons are for a 75% discount and 2 coupons are for a 100% discount.

#### d. What is the chance that Jo gets at least 50% off his ice cream? 3 pts

1 - 30/50

e. Suppose that Jo brought his friend Jackie to the creamery with him. What is the chance that at least one of them got 100% off their ice cream? 3 pts (2/50) ** 2 + 2*(2/50)*(48/50)

or 1-(48/50)^2

f. Jo forgot to put his ticket back before Jackie drew from the box! Given this information, what is the chance that at least one of them got 100% off their ice cream? 3 pts

(2/50) * (1/49) + 2 * (2/50) * (48/49)

or

1-(48/50)(47/49)

## Page 10

## Page 11

#### 5. Sampling and Iteration (21 points)

Suppose you and your friends are playing a special game that involves 50 cards, numbered from 1 to 50.

On a player’s turn, they draw 5 cards with replacement and are assigned a score that is equal to the sum of the cards drawn. If the score is divisible by 3, the player is awarded 33 additional points.

Each player gets one turn. The player with the highest score at the end of the game wins. If there is a tie, no one wins.

a. Write a function one_turn() that simulates one player’s turn. The function should take no arguments and returns the player’s score at the end of their turn. 5 points

def one_turn():

cards = np.arange(1, 51, 1) draw = np.random.choice(_____(i)_____, _____(ii)_____) score = _____(iii)_____(_____(iv)_____) if _____(v)_____:

score = score + 33 return score

Blank i: cards Blank ii: 5 Blank iii: sum Blank iv: draw Blank v: score % 3 == 0

b. Write a function play that simulates one play of the game. The function takes in one argument num_players, the number of players in the game. It should return the number of the player that wins (If the first player to go wins, return 1. If the second player wins, return 2. etc.) If no one wins, return 0. 7 points

def play(num_players):

scores = make_array() winning_score = 0 winning_player = 0

for i in np.arange(________(i)________):

score = ________(ii)________ if score > ________(iii)________:

## Page 12

winning_score = score winning_player = ________(iv)________ scores = ________(v)________ if ________(vi)________ > 1:

return 0 else:

return winning_player

Blank i: num_players Blank ii: one_turn() Blank iii: winning_score Blank iv: i +1 Blank v: np.append(scores, score) Blank vi: np.count_nonzero(scores == winning_score)

c. You soon get bored of playing the game. Your group of friends decides to eat lunch instead, and you conclude that in the time you spend eating, you could have played 100 games. Write a function that simulates 100 rounds of the game. The function takes in one argument, num_players, the number of players in the game, and draws a bar chart that visualizes the number of times each player won. 9 points

def a_hundred_games(num_players):

winners = ________(i)________ ________(ii)________:

winner = ________(iii)________ ________(iv)________= ________(v)________ win_count_tbl = ________(vi)________.________(vii)________ ________(viii)________.________(ix)________(“Winners”)

Blank i: make_array() Blank ii: for i in np.arange(100) Blank iii: play(num_players) Blank iv: winners Blank v: np.append(winners, winner) Blank vi: Table().with_column(“Winners”, winners) Blank vii: group(“Winners”) Blank viii: win_count_tbl Blank ix: barh

## Page 13

#### 6. Hypothesis Testing (20 points)

Chloe is a big fan of Trader Joes’ frozen mac n cheese, and has noticed that the cheese used varies from box to box. A Trader Joe's employee provides her with some data describing the four different cheeses used:

Cheese Probability*

Velveeta 0.05

Gruyère 0.55

Sharp Cheddar 0.25

Monterey Jack 0.15

*Only one type of cheese is used in any given box of mac n cheese.

Chloe is suspicious of this distribution. For example, Velveeta is much cheaper than Gruyère. Also, she has never bought a box that uses Monterey Jack.

Chloe decides to conduct a hypothesis test and buys a random sample of 100 mac n cheese boxes. She finds that 20% of her boxes have velveeta, 30% have Gruyère, 45% have Sharp Cheddar, and 15% have Monterey Jack.

#### a. What null hypothesis, alternative hypothesis and test statistic should Chloe use? 6 points

Null Hypothesis: The types of cheese in the frozen mac n cheese boxes follow the distribution provided by the employee.

Alternative Hypothesis: The types of cheese in the frozen mac n cheese boxes do not follow the distribution provided by the employee.

Test Statistic: The total variation distance, because she’s comparing the two different distributions (observed and the one provided by Trader Joes)

## Page 14

b. Define the function one_simulated_test_stat to simulate a random sample according to the null hypothesis and return the test statistic for that sample. 4 points

observed_proportions = make_array(0.2, 0.3, 0.45, 0.05) employee_proportions = make_array(0.05, 0.55, 0.25, 0.15)

def one_simulated_test_stat():

sample_prop = ________(i)____________ test_stat = ________(ii)____________ return test_stat

Blank i: sample_proportions(100, employee_proportions) Blank ii: [np.]sum(abs(employee_proportions - sample_prop))/2

c. Generate 10,000 simulated statistics using one_simulated_test_stat, and store them in simulated_stats. Calculate the empirical p-value, and assign it to the p_value variable. Assume that the test statistic computed from the sample is provided by the observed_stat variable. 6 points

simulated_stats = ___________(i)___________ repetitions = 10000

for ___________(ii)___________:

one_stat = ___________(iii)___________ simulated_stats = ___________(iv)___________

p_value = ___________(v)___________

Blank i: make_array() Blank ii: i in np.arange(repetitions) Blank iii: one_simulated_test_stat() Blank iv: np.append(simulated_stats, one_stat) Blank v: np.count_nonzero(simulated_stats >= observed_stat)/len(simulated_stats)

Or np.count_nonzero(simulated_stats > observed_stat)/len(simulated_stats) Or np.count_nonzero(simulated_stats > observed_stat)/repetitions Or np.count_nonzero(simulated_stats >= observed_stat)/repetitions

## Page 15

d. Chloe defined a cutoff of 0.10 for her hypothesis test prior to conducting the analysis, and she finds that p_value is equal to 0.02. Is the data more consistent with the null hypothesis or alternative hypothesis? 2 pts

i. Consistent with the null hypothesis [] ii. Consistent with the alternative hypothesis [X] iii. Can’t say [ ]

- Suppose the true distribution of mac n cheese flavours and the distribution provided by the employee are identical. If Chloe were to repeat this entire sampling and testing process 2000 times using a pre-specified cutoff of 10%, she should expect to reject the null hypothesis roughly _____ times. 2 pts

#### i) 0 [ ] ii) 100 [ ] iii) 200 [x] iv) 900 [ ] v) 800 [ ] vi) Can’t say [ ]
