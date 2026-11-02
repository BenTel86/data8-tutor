---
title: "Spring 2024 Final — Student view"
course: Data 8
exam: Sp24_Final
semester: sp24
term: Spring
year: 2024
exam_type: final
view: student
source: exams/data8/sp26/Sp24_Final.pdf
solution_file: Sp24_Final_Sol.md
pages: 16
---

# Spring 2024 Final — Student view

> **Student view.** These are the questions exactly as students received them: every multiple-choice option is unmarked (`[ ]` or `( )`) and no answers are present. The staff answers are in [Sp24_Final_Sol.md](Sp24_Final_Sol.md).

## Page 1

#### DATA 8 Final Exam, Spring 2024

#### Instructions You have 2 hours and 50 minutes to complete the exam.

- The exam is closed book, closed notes, closed computer, closed calculator, except the provided reference sheet.

- Mark your answers on the exam itself in the spaces provided. We will not grade answers written on scratch paper or outside the designated answer spaces.

- If you need to use the restroom, bring your phone, exam, and student ID to the front of the room.

- The test is designed to be completed using methods we have learned in this class. We reserve the right to deduct or not score answers using methods out of scope.

For multiple choice questions with circles, you should select exactly one choice. You should indicate your selection by completely ﬁlling in the circle.

⃝ You must choose either this option

⃝ Or this one, but not both!

For multiple choice questions with square checkboxes, you may select multiple choices. You should indicate your selection by completely ﬁlling in the box.

- [ ] You could select this choice.

- [ ] You could select this one, too!

#### Please write your initials at the top of every page as you are taking the exam.

Question Points Score

1 22

2 26

3 26

4 22

5 26

6 0

Total: 122

Name:

TA’s name:

Student ID:

Name of person to your left:

Name of person to your right:

## Page 2

#### 1. True or False

- (2 points) All of the work on this exam is your own.

⃝ True ⃝ False

- (2 points) The posterior probability is deﬁned as the probability of an event before updating it with

additional information.

⃝ True ⃝ False

- (2 points) When constructing a conﬁdence interval for the sample mean, using a 95% conﬁdence

level indicates that the conﬁdence interval will capture the individual values of 95% of the population of interest.

⃝ True ⃝ False

- (2 points) When running a hypothesis test using a p-value cutoﬀof 4%, given that the null hypoth-

esis is true, the probability the test will reach the correct conclusion is 96%.

⃝ True ⃝ False

- (2 points) In an A/B test, shuﬄing the labels and shuﬄing the values are equally valid methods to

test for a diﬀerence between groups.

⃝ True ⃝ False

- (2 points) The intercept of a line of best ﬁt can be interpreted as the predicted increase in y for a

zero-unit increase in x.

⃝ True ⃝ False

- (2 points) A decision boundary for a k-nearest-neighbors classiﬁer may fail to completely separate

the 2 classes represented in the training set (i.e. not achieve perfect accuracy on the training set).

⃝ True ⃝ False

- (2 points) In the lecture on privacy, access (with regards to fair information practices) is deﬁned

as the ability for companies to access information about individuals.

⃝ True ⃝ False

- (2 points) In Professor Sahai’s case study lecture, machine learning is diﬀerentiated from classical

statistics because it involves generalized intelligence whereas classical statistics is focused on solving speciﬁc equations.

⃝ True ⃝ False

- (2 points) By converting data into standard units, the data is transformed into a normal distribution

with mean 0 and a standard deviation of 1.

⃝ True ⃝ False

- (2 points) If A is a random event, the probability of A given no information must be smaller than

the probability of A given strictly more information.

⃝ True ⃝ False

Page 2

## Page 3

#### 2. Psychic Police?

Shawn Spencer, a consultant for the SBPD, claims to have psychic abilities to solve crimes. Shawn’s partner, Gus, wants to analyze the probability of Shawn making a correct “prediction” based on diﬀerent scenarios.

Suppose Shawn claims that he is able to use his psychic abilities to sense the type of crime. In this case, we assume there are only two possible types of crime: theft and fraud, and that all crimes occur independently of one another. Theft crimes occur with a 70% chance, and fraud has a 30% chance.

Additionally, assume the following:

- If the crime is theft, there is a 65% chance that Shawn correctly predicts the type of crime.

- If the crime is fraud, there is an 80% chance that Shawn correctly predicts the type of crime.

For all answers, please leave it as a mathematical expression.

- (0 points) SCRATCH WORK: You can use this space to write any extra calculations or diagrams

that may be helpful. Anything written in this box will not be graded.

- (2 points) What is the probability that 5 crimes in a row are all thefts?

- (3 points) For a case chosen at random, what is the probability that Shawn correctly predicts the

type of crime?

- (3 points) Suppose Shawn predicts a crime is theft. What is the probability that the crime type is

actually theft?

Page 3

## Page 4

- (2 points) Suppose a crime is fraud. What is the probability that Shawn incorrectly predicts it as

theft?

- (2 points) Gus compiles 8 random crimes for Shawn to analyze. What is the probability that at

least one of these crimes is theft?

- (2 points) What is the probability that a crime is fraud and Shawn predicts correctly?

- Gus ﬁres Shawn and decides to outsource his predictions to a k-nearest-neighbors classiﬁer. He will

predict the type of crime based on the geographic coordinates of the crime, the monetary value of the damages, and the amount of oﬃcers called to the scene.

- (3 points) Which of the following are steps he should take to implement the classiﬁer? Select

all that apply.

- [ ] Separate his data into a training and test set
- [ ] Calculate the distance from all points in the training set to one another
- [ ] Reserve some data to evaluate the accuracy of the classiﬁer
- [ ] Minimize RMSE of errors on the test set to optimize the classiﬁer
- [ ] Repeatedly adjust the features and values of k depending on the results of rerunning

the classiﬁer on the test set
- [ ] None of the above

ii. (2 points) Gus decides to only use 2 features, the monetary value of the damages and the

amount of oﬃcers at the scene. What are problems that might arise from using these two variables? Select all that apply.

- [ ] The amount of oﬃcers is not a numerical variable since it cannot take on decimal

values.
- [ ] The variables can be positively correlated, which creates a confounding factor.
- [ ] The variables have diﬀerent scales, so one might take more importance than the other

in the classiﬁer, skewing the results.
- [ ] The variables are measured in diﬀerent units, so one might take more importance

than the other in the classiﬁer, skewing the results.
- [ ] None of the above

Page 4

## Page 5

![Image extracted from page 5](images/Sp24_Final_page005_image001.png)

iii. (2 points) Above is a plot of the entire training data. Using k=3, what would a point located

at (0, 0) be classiﬁed as?

⃝ Theft ⃝ Fraud ⃝ Cannot determine

iv. (2 points) Using k=15, what would a point located at (2, -1) be classiﬁed as?

⃝ Theft ⃝ Fraud ⃝ Cannot determine

- (3 points) Which of the following are true statements about the value of k for Gus’s classiﬁer?

Select all that apply.

- [ ] Increasing the value of k always improves accuracy as it allows more data to be used.
- [ ] Odd values guarantee a decision can be made.
- [ ] k=19 is too large for the dataset above.
- [ ] k=1 is equivalent to classifying a point based on its neighbor with the smallest dis-

tance.
- [ ] In a situation where one class has many more points than the other, the k value

should not exceed the number of points in the minority class.
- [ ] None of the above

Page 5

## Page 6

#### 3. Minions Merchandise

Following the release of the latest “Minions” movie, Universal Studios noted a high demand for Minions- themed merchandise.

- (3 points) Kevin is analyzing the individual purchase amounts of Minions-themed merchandise

made in 2023. He wants to create a 95% conﬁdence interval for the population mean with a total width no larger than $1. If the population standard deviation is known to be $10, calculate the minimum sample size Kevin needs to achieve this conﬁdence interval width. Please draw a box around your ﬁnal answer.

- (2 points) Kevin is debating between using a 90% conﬁdence interval and a 95% conﬁdence interval.

Which of the following are true statements about the conﬁdence level? Select all that apply.

- [ ] Given the same dataset and desired parameter, the 90% conﬁdence interval will likely be

narrower than the 95% conﬁdence interval.
- [ ] The 90% conﬁdence level should not be used as it does not align with the Normal dis-

tribution, whereas the 95% conﬁdence interval would correspond to exactly 2 SDs above
and below the sample mean.
- [ ] The 90% conﬁdence interval would correspond to a hypothesis test with p-value cutoﬀof

0.1.
- [ ] The 95% conﬁdence interval would correspond to a hypothesis test with p-value cutoﬀof

0.95.
- [ ] Since the 95% conﬁdence interval has a higher chance of capturing the true parameter, it

should always be used instead of a 90% conﬁdence interval.
- [ ] None of the above

- (2 points) Kevin decides to use the bootstrap method to create a 95% conﬁdence interval using

a sample size smaller than the one calculated in part (a). Another analyst, Bob, claims that the conﬁdence interval obtained through bootstrapping will most likely have a width greater than $1. Which of the following is true?

⃝ True, because bootstrapping with a smaller sample size generally results in less precise

estimates, hence a wider conﬁdence interval. ⃝ False, as the width of the conﬁdence interval depends on the population standard devia-

tion. ⃝ True, but only if the variability in the sample is unusually high, leading to a wider interval. ⃝ False, as the bootstrap method inherently provides narrower conﬁdence intervals regard-

less of sample size.

Page 6

## Page 7

- Fill in the code below such that the function calculate ci returns an array containing the left and

right endpoints for a conﬁdence interval for the population mean. The function takes in a table with data (tbl), the name of the column containing the values of interest as a string (values col), the conﬁdence level (expressed as a percent from 0 to 100) (level), and the number of repetitions as an integer (repetitions).

def calculate_ci(tbl, values_col, level, repetitions):

simulated_means = ___(a)___ for i in np.arange(repetitions):

resampled_table = tbl.___(b)___ resampled_values = resampled_table.column(values_col) resampled_mean = np.mean(___(c)___) simulated_means = np.append(___(d)___, ___(e)___)

left = percentile(___(f)___, simulated_means) right = percentile(___(g)___, simulated_means) return make_array(left, right)

- (1 point) Fill in blank (a).

ii. (2 points) Fill in blank (b).

iii. (2 points) Fill in blank (c).

iv. (1 point) Fill in blank (d).

- (1 point) Fill in blank (e).

vi. (2 points) Fill in blank (f).

vii. (2 points) Fill in blank (g).

Page 7

## Page 8

- Assume Kevin used the sample size from part (a) and obtained a 95% conﬁdence interval. For the

following two questions, assume that the conﬁdence interval he constructs for the mean purchase amount is [$25, $35].

- (2 points) What is the probability that the actual population mean is outside this interval?

⃝ 2.5% ⃝ 5% ⃝ 95% ⃝ There is not enough information to determine because we don’t know the exact dis-

tribution of the data. ⃝ None of the above

ii. (2 points) Which of the following can be concluded from the bootstrapped conﬁdence interval

above?

⃝ 95% of the purchases in the population are between $25 and $35. ⃝ The mean purchase amount in Kevin’s sample was exactly $30. ⃝ If Bob independently repeats Kevin’s process 1000 times, exactly 950 of the intervals

he creates will contain the true population mean. ⃝ None of the above

iii. (2 points) Kevin thinks that the average price of Minions-merch transactions is less than the

$45 average price of Disney princess merchandise transactions. Based on his conﬁdence interval and a p-value cut-oﬀof 5%, what can Kevin conclude?

⃝ The data are consistent with the hypothesis that the distribution of the transaction

prices is the same for both Minions merchandise and Disney princess merchandise. ⃝ The data are consistent with the hypothesis that Minions merchandise is less expen-

sive than Disney princess merchandise ⃝ The data are consistent with the hypothesis that Minions merchandise is more ex-

pensive than Disney princess merchandise. ⃝ There is not enough information to make a conclusion of any kind.

- (2 points) Kevin is now interested in estimating the 75th percentile of the Minions merchandise

sales for a better understanding of high-end sales performance. Which of the following methods could he use to create a 95% conﬁdence interval for this percentile? Select all that apply.

- [ ] Bootstrapping
- [ ] Central Limit Theorem
- [ ] Randomized Control Experiment
- [ ] Linear regression prediction interval
- [ ] None of the above

Page 8

## Page 9

- (0 points) OPTIONAL: Draw a picture of some Data 8 themed merchandise representing your

experience this semester! Make sure to ﬁnish the rest of the exam, though.

Page 9

## Page 10

#### 4. Streaming Success

Hannah and Lucas are using early streaming data to predict the chart success of pop songs. The dataset, named pop songs, consists of data from 200 randomly selected pop songs released in the past year. The dataset includes the following columns:

- Title: a string, the name of the song.

- Artist: a string, the name of the artist.

- Streams: an integer, the number of streams a song received within the ﬁrst 24 hours of its release.

- Peak Position: an integer, the highest chart position the song achieved, with 1 being the highest.

- (2 points) Fill in blank (a) such that compute su returns the input array in standard units.

def compute_su(array):

mean = np.mean(array) sd = np.std(array) ___(a)___

- Fill in the code to calculate the correlation coeﬃcient between the number of streams a song received

within the ﬁrst 24 hours and the highest chart position the song achieved.

streams_in_su = compute_su(___(a)___) chart_in_su = compute_su(___(b)___) r = ___(c)___

- (1 point) Fill in blank (a).

ii. (1 point) Fill in blank (b).

iii. (2 points) Fill in blank (c).

Page 10

## Page 11

- (2 points) Assume that Hannah calculated r correctly, and got -0.85. Given that the standard

deviation for Streams is 120,000 streams and for Peak Position is 250 positions, ﬁll in blank (a) to compute the slope of the regression line in original units. (Reminder: Hannah is using the number of streams in the ﬁrst 24 hours to predict the peak position.)

slope = ____(a)____

- Hannah is interested in whether there is a linear relationship between Streams and Peak Position,

so she decides to run a hypothesis test.

- (2 points) Which of the following are valid null hypotheses? Select all that apply.

- [ ] The true correlation coeﬃcient between Streams and Peak Position is 0.
- [ ] The true correlation coeﬃcient between Streams and Peak Position is not 0.
- [ ] The true slope between Streams and Peak Position is 0.
- [ ] The true slope between Streams and Peak Position is not 0.
- [ ] None of the above

ii. (2 points) Which of the following are valid alternative hypotheses for this hypothesis test?

Select all that apply.

- [ ] There is a positive linear relationship between Streams and Peak Position.
- [ ] There is a negative linear relationship between Streams and Peak Position.
- [ ] The correlation coeﬃcient between Streams and Peak Position is zero.
- [ ] The correlation coeﬃcient between Streams and Peak Position is not zero.

iii. (2 points) Hannah decides to use bootstrapping to test her hypothesis. She creates a 90% conﬁdence interval for the true correlation coeﬃcient between Streams and Peak Position. The 90% conﬁdence interval is: [-0.15, -0.55]. Using a p-value cutoﬀof 10%, Which of the following is true? Select all that apply.

- [ ] 90% of the data we observe can be explained by the regression line.
- [ ] The data supports the null hypothesis.
- [ ] The data supports the alternative hypothesis.
- [ ] There’s a 90% chance that the true correlation coeﬃcient is between -0.15 and -0.55.
- [ ] If we run this process of collecting data and running a hypothesis test 100 times, we

would expect around 90 of the conﬁdence intervals to contain the true correlation coeﬃcient.

Page 11

## Page 12

- (2 points) Hannah ﬁts a regression line to predict Peak Position from Streams and also creates a

residual plot, as shown below. Based on the residual plot, would linear regression be a good choice for making predictions from this data?

![Image extracted from page 12](images/Sp24_Final_page012_image001.png)

⃝ Yes, linear regression is always a good approach, regardless of the data. ⃝ Yes, linear regression is a good model here because there is a strong negative correlation

between Streams and Peak Position. ⃝ Yes, linear regression is a good model here because the residual plot does not show an

upward trend or a downward trend. ⃝ Yes, linear regression is a good model because the residual plot does not show a linear

trend. ⃝ No, linear regression is not a good model here because the residual plot shows a curved

pattern. ⃝ No, linear regression is not a good model here because this was not a controlled experi-

ment, and an association does not imply causation.

- (4 points) Fill in the code below to complete a function that creates the scatterplot above when

called. The function takes in the following 3 arguments: tbl, a table containing two columns named x vals (string) and resids (string) corresponding to the name of the x-values’ column and the name of the residuals’ column. You do not need to generate the title of the graph.

def residual_plot(tbl, x_vals, resids):

________(a)________

- (2 points) Lucas suggests using a diﬀerent type of technique, such as quadratic regression or poly-

nomial regression, instead of a straight line to improve predictions. But Hannah believes that the regression line gives you the smallest possible RMSE, so there’s no possible way to get a prediction with a lower average error. Is Hannah right or wrong? Select the correct statement below.

⃝ Hannah is correct, as this is the deﬁnition of the regression line. ⃝ Hannah is wrong, as the regression line gives the smallest possible RMSE among all

straight lines, but a diﬀerent type of regression might give an even lower RMSE. ⃝ Hannah is correct, as the regression line is exactly the same as minimizing the RMSE. ⃝ Hannah is wrong, as the regression line may give a diﬀerent result depending on whether

you minimize RMSE or use linear regression equations.

Page 12

## Page 13

#### 5. Restaurant Reviews

Amber, Noah, Haley, and Vivian have a shared database where they leave reviews of restaurants. The table is called reviews and contains the following columns:

- reviewer: string, the name of the reviewer

- name: string, the name of the restaurant

- location: string, containing the city and the state of the restaurant

- rating: integer, rating of the restaurant on a scale of 1 to 10

- cuisine: string, the style/method of cooking

- (3 points) Amber wants to create a table only containing restaurants with a rating of 10. Write a

line of code to do this.

- Fill in the code such that top reviewer is equal to the person with the most reviews.

number_reviews_per_person = reviews.___(a)___(___(b)___) sorting_reviews = number_reviews_per_person.sort(___(c)___) top_reviewer = sorting_reviews.column(___(d)___).item(___(e)___)

- (1 point) Fill in blank (a).

ii. (1 point) Fill in blank (b).

iii. (2 points) Fill in blank (c).

iv. (1 point) Fill in blank (d).

- (1 point) Fill in blank (e).

Page 13

## Page 14

- Haley is interested in each reviewer’s average rating by cuisine. Fill in the code so that cuisine by reviewer

is a table where every cuisine gets its own row, and every reviewer gets its own column.

cuisine_by_reviewer = reviews.___(a)___(___(b)___, ___(c)___, ___(d)___, ___(e)___)

As a reminder, here are the columns in reviews:

- reviewer: string, the name of the reviewer
- name: string, the name of the restaurant
- location: string, containing the city and the state of the restaurant
- rating: integer, rating of the restaurant on a scale of 1 to 10
- cuisine: string, the style/method of cooking

- (2 points) Fill in blank (a).

ii. (1 point) Fill in blank (b).

iii. (1 point) Fill in blank (c).

iv. (1 point) Fill in blank (d).

- (1 point) Fill in blank (e).

- (2 points) Amber has calculated the average rating for each Ethiopian restaurant in the dataset.

She is interested in visualizing the distribution of these averages. Which of the following table functions and methods would help her do this? Select all that apply.

- [ ] .scatter
- [ ] .plot
- [ ] .barh
- [ ] .hist
- [ ] None of the above

Page 14

## Page 15

- Haley is suspicious that Amber’s ratings are consistently higher than hers. She decides to run a

hypothesis test to verify her suspicion. Fill in the code to perform one simulation of an A/B test. Assume that calculate test stat is a function that calculates the diﬀerence in means between Haley and Amber’s ratings. haley amber is a table containing only Haley and Amber’s reviews and contains the same columns as reviews.

shuffled_labels = haley_amber.___(a)___(___(b)___).column(___(c)___) shuffled_table = haley_amber.___(d)___("reviewer", ___(e)___) shuffled_group_means = shuffled_table.___(f)___(___(g)___, np.average) simulated_test_stat = calculate_test_stat(shuffled_group_means)

- (1 point) Fill in blank (a).

ii. (1 point) Fill in blank (b).

iii. (1 point) Fill in blank (c).

iv. (1 point) Fill in blank (d).

- (1 point) Fill in blank (e).

vi. (1 point) Fill in blank (f).

vii. (1 point) Fill in blank (g).

viii. (2 points) Besides the diﬀerence in means, what are other valid test statistics Haley could have

used? Select all that apply.

- [ ] Absolute diﬀerence in means between Haley and Amber’s ratings
- [ ] Diﬀerence in 50th percentile ratings between Haley and Amber’s ratings
- [ ] Absolute diﬀerence in 50th percentile ratings between Haley and Amber’s ratings
- [ ] Total variation distance between Amber and Haley’s rating distribution

Page 15

## Page 16

#### 6. Assumptions

- (0 points) If you felt any question required additional assumptions, please write them here. Be

warned: We will only consider these assumptions if the question indeed required additional infor- mation.

Page 16
