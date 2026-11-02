---
title: "Spring 2016 Final — Solution view"
course: Data 8
exam: Sp16_Final_Sol
semester: sp16
term: Spring
year: 2016
exam_type: final
view: solution
source: exams/data8/sp26/Sp16_Final_Sol.pdf
student_file: Sp16_Final.md
pages: 9
---

# Spring 2016 Final — Solution view

> **Solution view.** Staff answers are included: written and coded answers appear inline, and the option the staff selected is marked `[x]` (choose one or more) or `(x)` (choose one). Use these to guide a student or check their reasoning — never hand the answer over directly. The same exam without answers is in [Sp16_Final.md](Sp16_Final.md).

## Page 1

## Data 8 Foundations of Data Science Spring 2016 Final Solutions

#### INSTRUCTIONS

- You have 3 hours to complete the exam.

- The exam is closed book, closed notes, closed computer, closed calculator, except one hand-written 8.5” × 11” crib sheet of your own creation and the two oﬃcial study guides provided with the exam.

#### • Mark your answers on the exam itself. We will not grade answers written on scratch paper.

Last name

First name

Student ID number

BearFacts email (_@berkeley.edu)

GSI

Name of the person to your left

Name of the person to your right

#### All the work on this exam is my own. (please sign)

## Page 2

2

#### 1. (16 points) Tables

The cafe table (left) describes the Yelp reviews for three cafes on Euclid. Every cafe has a count for the number of 3-star, 4-star, and 5-star reviews, in that order. The price table (right) describes coﬀee prices.

name | stars | count name | $ Nefeli | 3 | 37 Nefeli | 3 Nefeli | 4 | 75 Brewed | 3 Nefeli | 5 | 50 Abe | 2 Brewed | 3 | 56 Brewed | 4 | 71 ... (4 rows omitted)

Complete the Python expressions below to compute each result. For example, if the result prompt said, “The total number of reviews of all cafes,” then you would write: sum ( cafe.column( 2 ) ) *** You must ﬁt your solution into the lines and spaces provided to receive full credit. *** The last line of each answer should evaluate to the result requested; you never need to call print.

#### (a) (2 pt) The total number of reviews of the cafe named Nefeli.

sum(cafe.where(’name’, ’Nefeli’).column(’count’))

#### (b) (2 pt) The total number of reviews of the cafe with the fewest reviews.

min(cafe.group(’name’, sum).column(2))

#### (c) (2 pt) The average number of stars for reviews of the cafe named Nefeli.

n = cafe.where(’name’, ’Nefeli’)

sum(n.column(’stars’) * n.column(’count’)) / sum(n.column(’count’))

#### (d) (3 pt) The total variation distance between the distributions of stars for Nefeli and Brewed.

a = cafe.where(’name’, ’Nefeli’).column(’count’)

b = cafe.where(’name’, ’Brewed’).column(’count’)

0.5 * sum(abs(a/sum(a) - b/sum(b)))

#### (e) (2 pt) An array containing the names of all cafes that have above-average coﬀee prices.

price.where(price.column(’$’) > np.average(price.column(’$’))).column(’name’)

#### (f) (3 pt) Among all reviews of cafes with $3 coﬀee, the proportion that are 3-star reviews.

j = cafe.join(’name’, price).where(’$’, 3)

sum(j.where(’stars’, 3).column(’count’)) / sum(j.column(’count’))

- (2 pt) The table below, in which each row describes the number of reviews with a particular star rating for every

cafe.

stars | Abe | Brewed | Nefeli 3 | 1 | 56 | 37 4 | 2 | 71 | 75 5 | 17 | 37 | 50

cafe.pivot(’name’, ’stars’, ’count’, sum))

## Page 3

#### Name: 3

#### 2. (17 points) Distributions

500 women age 25 to 49 in steady relationships were surveyed. Each woman was asked her age in years and whether she was married to her partner. There were 400 unmarried and 100 married women among those surveyed. The histograms below visualize the ages of these two groups of women.

unmarried.hist(’Age’,bins=[25,30,40,45,50]) married.hist(’Age’,bins=[25,30,40,45,50])

![Image containing text: Unmarried (in relationships)](images/Sp16_Final_Sol_page003_image002.png)

![Image containing text: Married](images/Sp16_Final_Sol_page003_image001.png)

### Unmarried (in relationships)

### Married

- (10 pt) For each pair of quantities, compare them using the information above and choose one of following:

(A): (I) is larger. (B): (II) is larger. (C): (I) and (II) are about the same. (D): There is not enough information to compare (I) and (II). *** You must brieﬂy justify your answer to receive full credit. ***

#### • (I) The number of unmarried women age 25-29 vs (II) The number of unmarried women age 30-39

(C): Both are about 30% of 400; also accept (A) with justiﬁcation 31% ¿ 30%

- (I) Among the unmarried women, the proportion who are of age 25-29 vs (II) Among the married women, the proportion who are of age 45-49

(A): 30% vs 25%

#### • (I) The number of unmarried women age 30-39 vs (II) The number of married women

(A): 120 vs 100

#### • (I) The proportion of married women age 30-34 vs (II) The proportion of married women age 35-39

(D): You can’t tell how ages are distributed within a bin.

- (I) The 20th percentile age of unmarried women vs (II) The 20th percentile age of married women

(B): Somewhere within 25-29 vs somewhere within 30-39.

#### (b) (3 pt) What proportion of everyone surveyed were in the age range 30-39?

(0.3 * 400 + 0.4 * 100) / 500 = 8/25 or 32%

- (4 pt) If you select a woman uniformly at random from those surveyed and ﬁnd out that her age is in

the range 30-39, what is the chance that she is married?

(2/5) * (1/5) / (8/25) = 1/4 or 25%

## Page 4

4

#### 3. (25 points) Regression

The lead table (left) contains one row per child in a study of 1000 children’s Blood Lead Levels (BLL) measured in micrograms per deciliter and their intelligence quotients (IQ). Assume that the data were collected by sampling children at random from a very large population. Summary statistics (middle) and a scatter diagram (right) are shown below. All BLLs are measured to one decimal place, and all IQ scores are integers.

![Image extracted from page 4](images/Sp16_Final_Sol_page004_image001.png)

#### BLL IQ 7.9 90 6.2 78 3.2 110 4.1 128 7.3 88 (995 rows omitted)

Expression Value np.average(lead.column(’BLL’)) 6 np.std(lead.column(’BLL’)) 2 np.average(lead.column(’IQ’)) 100 np.std(lead.column(’IQ’)) 15 correlation(lead, ’BLL’, ’IQ’) -0.1

#### (a) (2 pt) What is the value of correlation(lead, ’IQ’, ’BLL’)?

Hint: The correlation function appears on your midterm study guide.

-0.1

- (3 pt) What is the estimated average IQ of a child with a BLL that is 2 standard deviations above the

mean BLL? Use the regression line to ﬁnd this estimate, assuming BLL and IQ are linearly related.

2 ∗−0.1 ∗ 15 + 100 = 97

- (4 pt) Write the equation of the regression line through this sample for the IQ y in terms of the BLL x.

y = −0.1 · 15

2 · x + 100 − 6 · (−0.1 · 15 2 ) = −0.75x + 104.5

- (4 pt) Complete the code below so that the last line prints out a 95% conﬁdence interval for the IQ value

at a BLL of 10.0 on the regression line of the population from which this sample was collected. Hint: The slope and intercept functions appears on your midterm study guide.

estimate_table = Table ([’Resample #’, ’Estimate ’])

for i in np.arange (400):

r = lead.sample( with_replacement =True)

e = slope(r, 0, 1) * 10 + intercept(r, 0, 1)

estimate_table.append ([i, e])

estimates = estimate_table.column (1)

print(percentile (2.5, estimates), percentile (97.5 , estimates ))

## Page 5

#### Name: 5

![Image extracted from page 5](images/Sp16_Final_Sol_page005_image001.png)

The data from the previous page are repeated here for your reference.

#### BLL IQ 7.9 90 6.2 78 3.2 110 4.1 128 7.3 88 (995 rows omitted)

Expression Value np.average(lead.column(’BLL’)) 6 np.std(lead.column(’BLL’)) 2 np.average(lead.column(’IQ’)) 100 np.std(lead.column(’IQ’)) 15 correlation(lead, ’BLL’, ’IQ’) -0.1

#### (e) (6 pt) Mark each of the following statements about the conﬁdence interval you computed in part

- as True or False based on the deﬁnition of a conﬁdence interval and the details of your implementation. The terms “most” should be interpreted as around 95%.

- CircleTrue orFalse: It contains most IQ scores in the population for children with a BLL of 10.0. False.

- CircleTrue orFalse: It contains most IQ scores in the sample for children with a BLL of 10.0. False.

- Circle True or False: If with_replacement=False were used (line 3), the interval would have 0 width. True.

- CircleTrue orFalse: If the study were repeated many times, most conﬁdence intervals computed in this way would overlap. True.

- CircleTrue orFalse: If the study were repeated many times, the average IQ in the population would fall within most intervals computed in this way. False.

- CircleTrueorFalse: If the study were repeated many times, the average IQ in the population for children with a BLL of 10.0 would fall within most intervals computed in this way. True.

- (2 pt) What null hypothesis would you evaluate in a statistical test to determine whether BLL and IQ

are negatively correlated in the population?

The correlation coeﬃcient (or slope) is greater than or equal to 0.

- (2 pt) Based on the summary statistics provided, what is the minimum proportion of IQ scores in the

sample that are between 70 and 130 according to Chebyshev’s inequality?

1 − ( 1 2)2 = 75% because 130 - 100 = 100 - 70 = 30 IQ, which is 2 standard deviations.

- (2 pt) Based on the scatter diagram and summary statistics, what proportion of IQ scores in the sample

#### do you think are between 70 and 130? Describe your reasoning. Hint: You don’t need to count dots.

95% because 130 - 100 = 100 - 70 = 30 IQ, which is 2 standard deviations, and both IQ and BLL appear to be normally distributed in the scatter diagram.

## Page 6

6

#### 4. (12 points) Experiments

To test whether lead exposure aﬀects cognitive function, a researcher conducts the following experiment. 90 goldﬁsh are placed in a tank and left to swim around for 24 hours. Then, a glass plate is inserted, separating the tank into two equal sides that cannot mix. Each ﬁsh ends up on one side. The researcher adds a high level of lead to the left side only. After 1 week, the IQ of each ﬁsh is measured. The fish table (left), counts of ﬁsh on each side (middle), and the average IQs on each side (right) describe the results.

#### Side Fish IQ Left 98 Right 118 Left 105 (87 rows omitted)

#### fish.group(’Side’) Side count Left 44 Right 46

#### fish.group(’Side’, np.average) Side Fish IQ average Left 94.6 Right 103.9

#### (a) (4 pt) Complete the null hypothesis in this experiment about lead exposure aﬀecting ﬁsh IQ.

Among the ﬁsh in the experiment,

the distribution of hypothetical IQ scores for all the ﬁsh, had none been exposed to lead

is the same as hypothetical IQ scores for all the ﬁsh, had they all been exposed to lead.

- (2 pt) You choose as your test statistic the absolute diﬀerence in average ﬁsh IQ scores for the two groups.

Complete absolute_difference_of_averages. The argument t is a two-column table such as fish in which column 0 indicates to which group each example belongs, and column 1 contains quantitative data.

def absolute_difference_of_averages (t):

averages = t.group (0, np.average ). column (1)

return abs(np.diff(averages ). item (0))

#### (c) (4 pt) Complete the permutation_test function, which returns an approximate P-value from a per-

mutation test. It takes a two-column table t and a test statistic function f. An example call would be permutation_test(fish, absolute_difference_of_averages). The body of your function should not refer to fish or absolute_difference_of_averages; only t and f.

def permutation_test (t, f):

stats = Table (["Test statistic for a shuffled table"])

for i in np.arange (1000):

r = Table (). with_columns (["X", t.column (0), "Y", t.sample (). column (1)])

stats.append ([f(r)])

more_extreme = stats.column (0) >= f(t)

return np.count_nonzero(more_extreme) / 1000

- (2 pt) CircleTrue orFalse: Assuming that ﬁsh are randomly distributed among the two sides, a P-value

#### of 0.003 indicates that lead exposure causes a change in IQ. Brieﬂy justify your answer.

Yes. This is a randomized controlled experiment.

## Page 7

#### Name: 7

#### 5. (12 points) Sampling

#### (a) (6 pt) For each statement below, choose one:

(A): Almost always true for any uniform random sample with replacement. (B): Almost always true for large uniform random samples with replacement (e.g., n=1000), but not reliably for small ones (e.g., n=5). (C): Never true. (D): None of the above.

- For categorical data with three categories, the total variation distance between the population distribu- tion and an observed sample distribution will be small.

(B): For a large sample, the empirical distribution almost always looks like the population distribution.

- For quantitative data, the sample average is an unbiased estimate of the population average.

(A): Sample averages are unbiased estimators of population averages.

- For quantitative data, a histogram of the values in a sample will have a bell shape.

(D):The sampling distribution of a statistic such as the average is normal, but the values in the sample are distributed like the population, which can have any shape.

- (6 pt) You have a table named t with at least 20 rows. All rows are diﬀerent. Write a Python expression

that computes each of the following probabilities. Use t.num_rows for the number of rows in t.

- Row 10 of t appears among the rows in t.sample(20, with_replacement=False).

20 / t.num_rows

#### • Row 10 of t does not appear among the rows in t.sample(20, with_replacement=True).

((t.num_rows - 1)/t.num_rows) ** 20

- All rows of t.sample(20, with_replacement=True) are diﬀerent (no repeats).

np.prod(1-np.arange(20)/t.num_rows)

## Page 8

![Image containing text: 6. (8 points) Classiﬁcation *** The horizontal and vertical axes have diﬀerent scales in this scatter diagram! ***](images/Sp16_Final_Sol_page008_image001.png)

![Image containing text: Some squirrels on the Berkeley campus are wild animals and some are pets! Your friend is a Berkeley squirrel expert. She says that two useful features for classifying squirrels are the proportion of their fur that is clean (vertical axis) and their weight in ounces (horizontal axis). She identiﬁes several squirrels for you, but leaves two “Unknown” squirrels for you to classify. No two…](images/Sp16_Final_Sol_page008_image003.png)

8

#### 6. (8 points) Classiﬁcation

Some squirrels on the Berkeley campus are wild animals and some are pets! Your friend is a Berkeley squirrel expert. She says that two useful features for classifying squirrels are the proportion of their fur that is clean (vertical axis) and their weight in ounces (horizontal axis). She identiﬁes several squirrels for you, but leaves two “Unknown” squirrels for you to classify. No two squirrels have exactly the same features.

You decide to construct a classiﬁer for the “Unknown” squirrels using all of the known “Pet” and “Wild” squirrels as the training set.

#### *** The horizontal and vertical axes have diﬀerent scales in this scatter diagram! ***

![Image containing text: Weight](images/Sp16_Final_Sol_page008_image002.png)

### Clean Fur

### Weight

- (2 pt) What is the distance in this feature space, roughly, between the bottom-left unknown squirrel and

its nearest neighbor in the training set? Use both features to compute the distance. Show your work! Hint: The distance function appears on your ﬁnal study guide.

(0.34 - 0.12) ** 2 ** 0.5 = 0.22

- (2 pt) How would each unknown squirrel be classiﬁed by a 1-nearest-neighbor classiﬁer that uses only

the “clean fur” feature on the vertical axis and ignores the weight?

Bottom-left unknown: Wild

Middle unknown: Pet

- (2 pt) On the scatter plot at the top of the page, circle the three nearest neighbors in the training set to

the bottom-left unknown squirrel, using both features to compute distance.

- (2 pt) CircleTrueorFalse: Every possible pair of feature values would be classiﬁed as Wild for a 9-nearest-

#### neighbor classiﬁer using this training set. Brieﬂy justify your answer or describe a counterexample.

True. There are only four Pets, so Wild will always have a majority among 9 points.

## Page 9

#### Name: 9

#### 7. (0 points) (Optional) The Art of Data Science

Draw a picture (or better yet, a data visualization) of life before, during, and/or after taking Data 8.
