---
title: "Spring 2017 Final — Student view"
course: Data 8
exam: Sp17_Final
semester: sp17
term: Spring
year: 2017
exam_type: final
view: student
source: exams/data8/sp26/Sp17_Final.pdf
solution_file: Sp17_Final_Sol.md
pages: 6
---

# Spring 2017 Final — Student view

> **Student view.** These are the questions exactly as students received them: every multiple-choice option is unmarked (`[ ]` or `( )`) and no answers are present. The staff answers are in [Sp17_Final_Sol.md](Sp17_Final_Sol.md).

## Page 1

## Data 8 Foundations of Data Science Spring 2017 Final

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

Omissions from the study guide:

Expression Description np.std(array) Standard deviation of an array of values. np.median(array) Median of an array of values.

## Page 2

2

#### 1. (13 points) Tables

The cal table describes the name (string), position (string), class (string), and height (int) of Cal basketball players in the 2016-17 season.

name | position | class | height Ivan Rabb | Forward | Sophomore | 83 Charlie Moore | Guard | Freshman | 71 ... (15 rows omitted)

Complete the Python expressions below to compute each result. *** You must ﬁt your solution into the lines and spaces provided to receive full credit. *** A blank can be ﬁlled with multiple expressions, such as two expressions separated by commas. The last line of each answer should evaluate to the result requested; you never need to call print.

#### (a) (2 pt) The proportion of all players whose position is Forward.

___________________________________________________________________________________________________

#### (b) (2 pt) The name of the shortest Freshman. Assume that one is shorter than the rest.

cal.___________(________________________________).___________(________________).row(0).item(’name’)

#### (c) (3 pt) Whether there are at least 3

4 of players that are 80 inches tall or shorter. The result should be True or False.

percentile(______________________________________________________________)_________________________

- (3 pt) The number of players that are (strictly) more than one standard deviation above the mean height.

a = _______________________________________________________ #You are not required to use this line.

cal._________________(________________________________________________________________).___________

- (3 pt) An array of all positions, sorted in increasing order of the average height for all players in that position.

t = cal.select(’position’, ’height’)

t.________________(_____________________________________)._________________(1)._________________(0)

## Page 3

#### Name: 3

#### 2. (18 points) Experiments

The cal table described in the previous question has columns name, position, class, and height. Read the following code used to test a hypothesis about the cal table, then answer the questions below to interpret it.

def diff_of_means(t): forward_mean = t.where(’position ’, ’Forward ’). column(’height ’). mean () guard_mean = t.where(’position ’, ’Guard ’). column(’height ’). mean () return forward_mean - guard_mean

differences = make_array () for i in np.arange (10000):

shuffled_heights = cal.sample( with_replacement =False ). column(’height ’) shuffled = cal.select(’position ’). with_column(’height ’, shuffled_heights ) differences = np.append(differences , abs(diff_of_means(shuffled )))

- (4 pt) Circle all of the following hypotheses that could potentially be tested using the differences array.

- Among guards and forwards on this team, there is an association between height and position.
- Whether a player is a guard or a forward is like ﬂipping a fair coin.
- The forwards on Cal’s team have historically been taller than the guards, on average.
- The heights of guards and forwards are like random samples from the same distribution.

- (4 pt) Circle one option among (A), (B), and (C) for each blank in this description of the hypothesis test:

In this (i) , the null hypothesis states that the heights and positions of players are (ii) .

(i): (A) permutation test

(ii): (A) drawn at random from the same population

- conﬁdence interval test
- bootstrap resampling test

- paired up at random
- normally distributed

- (2 pt) What test statistic is being used to test the null hypothesis in (b)? Describe it in English, not code.

- (2 pt) Circle the letter for the chart below that could plausibly be a histogram of the differences array.

![Image extracted from page 3](images/Sp17_Final_page003_image001.png)

![Image containing text: (C) (A) (B)](images/Sp17_Final_page003_image002.png)

![Image extracted from page 3](images/Sp17_Final_page003_image003.png)

## (C) (A) (B)

- (4 pt) Write a Python expression to compute a P-value for this test, using the null hypothesis you deﬁned in

part (b) and the test statistic you described in part (c).

___________________ ( differences >= ___________________________________ ) / ________________

- (2 pt) Using a P-value cutoﬀof 5% to determine signiﬁcance, the null hypothesis from (b), the test statistic from

(c), and the null distribution from (d), what should you conclude if the observed value of the test statistic is 6?

## Page 4

4

#### 3. (14 points) Sampling

This histogram shows sample means for 2,500 random samples. Each sample contains 10,000 trip distances, measured in miles, drawn at random from the distances of 1.4 million trips for New York taxis in January 2016.

sample_means.hist(bins=np.arange(2.65, 2.9, 0.01))

![Image extracted from page 4](images/Sp17_Final_page004_image001.png)

#### (a) (2 pt) What quantity is measured by the horizontal axis of this histogram?

- Total miles for a single randomly chosen trip
- Total miles for a single randomly chosen sample
- Average miles for 10,000 randomly chosen trips
- Average miles for 2,500 randomly chosen samples

- None of the above

#### (b) (2 pt) What quantity is measured by the vertical axis of this histogram?

- Percent of trips per sample
- Percent of trips per mile
- Percent of trips per sample mean
- Percent of sample means per trip

- Percent of sample means per mile

- (2 pt) The percent of sample means represented by the tallest bar (with height about 1400) is closest to:

- 1.4 percent
- 7 percent
- 14 percent
- 28 percent
- 70 percent

- (2 pt) How would the height of the tallest bar change if we drew 10,000 random samples instead of 2,500?

- Grow by about 2 times
- Grow by about 4 times
- Shrink by about 2 times
- Shrink by about 4 times

- Not much change

- (2 pt) How would the height of the tallest bar change if the bars all had width 0.02 instead of 0.01?

The new histogram would be generated by sample_means.hist(bins=np.arange(2.65, 2.9, 0.02)).

- Grow by about 2 times
- Grow by about 4 times
- Shrink by about 2 times
- Shrink by about 4 times

- Not much change

- (2 pt) The standard deviation of taxi trip distances in the population of 1.4 million trips is closest to:

- 0.01 miles
- 0.03 miles
- 0.1 miles
- 0.3 miles
- 3 miles

- (2 pt) In order to construct a 95% conﬁdence interval for the mean trip distance in the population, such

that the width of the interval is 0.4 miles or less, the minimum sample size required is closest to: - 9 - 90 - 900 - 9,000 - 90,000

## Page 5

#### Name: 5

![Image extracted from page 5](images/Sp17_Final_page005_image001.png)

1. (22 points) Linear Regression This scatter plot of a sample of 1,000 trips for New York taxis in January 2016 compares distance and cost. The regression line is shown. Two trips of the same length can vary in cost because of waiting times, special fees, taxes, tolls, tips, discounts, etc.

np.average(t.column(’Distance ’)) = 3 np.std(t.column(’Distance ’)) = 2 np.average(t.column(’Cost ’)) = 13 np.std(t.column(’Cost ’)) = 6 correlation(t, ’Distance ’, ’Cost ’) = 0.9

#### (a) (3 pt) Convert a trip total cost of $9 to standard units.

#### (b) (3 pt) What is the slope of the regression line for this sample in dollars per mile?

#### (c) (3 pt) What is the intercept of the regression line for this sample in dollars?

- (3 pt) If instead we ﬁt a regression line to estimate distance in miles from total cost in dollars, what

would be the slope of that line in miles per dollar? Write not enough info if it’s impossible to say.

- (2 pt) Circle one of (A) True, (B) False, or (C) Not Enough Info to describe the following statement:

The total cost values in this sample are normally distributed.

- (2 pt) Circle one of (A) True, (B) False, or (C) Not Enough Info to describe the following statement:

All of the total cost values in this sample are within 3 standard deviations of the mean.

- (2 pt) Circle one of (A) True, (B) False, or (C) Not Enough Info to describe the following statement:

At least 88% of the total cost values in this sample are within 3 standard deviations of the mean.

- (2 pt) Circle one of (A) True, (B) False, or (C) Not Enough Info to describe the following statement:

The residual costs have a similar average magnitude for short trips (1 mile) and long trips (5+ miles).

- (2 pt) You compute a 95% conﬁdence interval from this sample to estimate the height (ﬁtted value) of

the population regression line at 6 miles. Which one of the following could plausibly be the result?

- 5 to 7
- 7 to 19
- 12 to 14
- 15 to 35
- 24 to 26

## Page 6

6

#### 5. (13 points) Classiﬁcation

You want to predict whether a ﬁnal survey response comes from a ﬁrst-year student (class 1) or not (class 0) based on responses to two questions. The average responses from a random sample of 200 surveys are below.

Class Count Lecture average Text average 1: First-year 80 75% 64% 0: Other 120 67% 68%

Survey questions: - What fraction of lectures did you attend? - What fraction of the text did you read?

- (2 pt) A constant classiﬁer is one that always guesses the same class label, regardless of the example

attributes. What’s the accuracy on this sample of the best constant classiﬁer for predicting the class?

- 50%
- 60%
- 70%
- 80%
- 90%

- (2 pt) Among the following, what is the best reason to expect that a nearest-neighbor classiﬁer that uses

this sample as a training set will have higher accuracy on a held-out test set than any constant classiﬁer?

- The test set may have a diﬀerent distribution of classes than this sample.
- A nearest-neighbor classiﬁer is designed to generalize to unseen examples.
- A nearest-neighbor classiﬁer can predict diﬀerent classes for diﬀerent examples.
- The attributes (lecture and text) are associated with each other.

![Image containing text: (A) The test set may have a diﬀerent distribution of classes than this sample. (B) A nearest-neighbor classiﬁer is designed to generalize to unseen examples. (C) A nearest-neighbor classiﬁer can predict diﬀerent classes for diﬀerent examples. (D) The attributes (lecture and text) are associated with each other. 2 the textbook, and the other read 9 10. What is the distance between these two…](images/Sp17_Final_page006_image001.png)

![Image extracted from page 6](images/Sp17_Final_page006_image003.png)

![Image extracted from page 6](images/Sp17_Final_page006_image002.png)

- The attributes (lecture and text) are both associated with the class.

#### (c) (2 pt) Two roommates always attended exactly the same lectures. One read 1

2 the textbook, and the other read 9 1. What is the distance between these two roommates used by a nearest-neighbor classiﬁer that includes as attributes both the fraction of lectures attended and the fraction of text read?

- (3 pt) For the small training set of 9 examples shown below, how will a k-nearest-neighbor classiﬁer label

each of the two test examples (i) and (ii)? For each example and each value of k, circle either 0 or 1. If it is impossible to determine the predicted label because of tied distances, circle both 0 and 1. Circle your answers in this table:

#### Legend

0.7

- [ ] (i)

#### Prediction for (i) Prediction for (ii)

- [x] Class 0: Other

Fraction of text read

0.6

- [ ] Class 1: First year

#### Using 1 nearest 0 1 0 1

0.5

#### Test example

0.4

#### Using 3 nearest 0 1 0 1

0.3

- [x] (ii)

0.2

#### Using 5 nearest 0 1 0 1

0.4 0.5 0.6 0.7 Fraction of lectures attended

#### (e) (4 pt) Your nearest-neighbor classiﬁer is correct 4

5 of the time on the test set, but it’s so slow that you can only use it for 3

4 of test examples. The rest of the time you use a constant classifer that always guesses “1: First-year”, which is correct only 2

5 of the time on the test set. For a randomly chosen test example,

- What is the chance that it will be classiﬁed correctly?

- What is the chance that you used your nearest-neighbor classiﬁer, given that it was classiﬁed correctly?
