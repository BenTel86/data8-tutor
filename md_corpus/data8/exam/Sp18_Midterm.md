---
title: "Spring 2018 Midterm — Student view"
course: Data 8
exam: Sp18_Midterm
semester: sp18
term: Spring
year: 2018
exam_type: midterm
view: student
source: exams/data8/sp26/Sp18_Midterm.pdf
solution_file: Sp18_Midterm_Sol.md
pages: 6
---

# Spring 2018 Midterm — Student view

> **Student view.** These are the questions exactly as students received them: every multiple-choice option is unmarked (`[ ]` or `( )`) and no answers are present. The staff answers are in [Sp18_Midterm_Sol.md](Sp18_Midterm_Sol.md).

## Page 1

## Data 8 Foundations of Data Science Spring 2018 Midterm

#### INSTRUCTIONS

- You have 45 minutes to complete the exam.

- The exam is closed book, closed notes, closed computer, closed calculator, except the oﬃcial midterm exam reference guide provided with the exam.

#### • Mark your answers on the exam itself. We will not grade answers written on scratch paper.

Last name

First name

Student ID number

CalCentral email (_@berkeley.edu)

GSI

Name of the person to your left

Name of the person to your right

#### All the work on this exam is my own. (please sign)

Question 0 (2 points) Write your name and SID in the space provided on one side of every page of the exam.

## Page 2

2

#### 1. (18 points) Basketball Bonanza

The table nba contains data for the 2016-2017 NBA Season. All numerical values in the table are integers. All other values are strings.

The nba table contains 8 columns. The ﬁrst few rows are shown below. Note that each preﬁx is an abbreviation for a team.

![Image extracted from page 2](images/Sp18_Midterm_page002_image001.png)

Fill in the blanks in the Python expressions to compute the described values. You must use only the lines provided. The last line of each answer should evaluate to the value described. Assume that the statements from datascience import * and import numpy as np have been executed. You may enter anything you would like in the blanks below, but you may not add code outside of the blanks.

#### (a) (3 pt) The age of the oldest NBA player.

______________________(nba._____________________________________(’age’))

- (5 pt) The three-letter preﬁx of the team that had the highest paid player with the position center (C)

in the NBA. You may assume there is only one such player.

centers = nba.___________(’position’, ___________________)

centers.___________(___________________________________).column(_________________).item(0)

## Page 3

#### Name and SID: 3

#### (c) (5 pt) The number of teams that have fewer than 5 players older than 30.

old = nba.__________________(___________________, are._________________________)

num_old = old.______________________(_______________________________)

num_old.__________________(____________________, ____________________)._______________________

- (5 pt) The number of positions for which the total points scored by CLE players in that position was

higher than the total points scored by BOS players in that position.

positions = nba.pivot(’prefix’,___________________________________________________)

sum(________________________________________________________________________________)

#### 2. (5 points) The Range of a Sample

The function data_range takes as its argument an array of numbers. The function returns the range of the numbers in the array, that is, the maximum value minus the minimum value.

The table survey consists of one row for each of the respondents to a survey. The column Age contains the ages of the respondents, measured in years.

Use the function data_range to simulate the range of the ages of a sample of size 55 drawn at random with replacement from the survey respondents. The last line should evaluate to an array consisting of 5000 simulated values of the range.

ranges = _________________________________

for k in _________________________________:

simulated_range = data_range(_________________________________________________________)

________________________________________________________________________

ranges

## Page 4

4

#### 3. (2 points) All Children

In a population, 40% of the people are children, 50% are women, and 10% are men. The array proportions contains the corresponding proportions.

proportions = make_array(0.4, 0.5, 0.1)

A sample of 10 people is drawn at random with replacement from the population. The chance that all 10 people in the sample are children is one of the four options below. Fill in the bubble of the correct option.

proportions.item(0) ** 10

proportions.item(0) * 10

sample_proportions(10, proportions).item(0) ** 10

sample_proportions(10, proportions).item(0) * 10

#### 4. (5 points) Vaccine Eﬀectiveness

Researchers are studying the eﬀectiveness of a particular ﬂu vaccine. A large random sample was taken from the population of people who took the vaccine in 2016. Among the sampled people, 48% did not get the ﬂu. Another large random sample was taken in 2017, from among the people who took the vaccine that year. Among these sampled people, 40% did not get the ﬂu.

- (3 pt) A researcher thinks the vaccine was less eﬀective in 2017 than in 2016. To test this, a null hypothesis

is needed. Exactly one of the following choices is the correct null hypothesis. Fill in the bubble of the correct choice.

The vaccine was less eﬀective in the 2017 population than in the 2016 population, due to chance.

The vaccine was equally eﬀective in the two samples but its eﬀectiveness was diﬀerent in the two populations due to chance.

The vaccine was equally eﬀective in the two populations but its eﬀectiveness was diﬀerent in the two samples due to chance.

- (2 pt) The researcher says, “The observed value of my test statistic is 40% − 48% = −8%.” To perform

the test, the statistic is simulated under the null hypothesis. One of the ﬁgures below is the empirical histogram of the simulated values. Which is it? Fill in the bubble of the correct histogram.

![Image extracted from page 4](images/Sp18_Midterm_page004_image002.png)

![Image extracted from page 4](images/Sp18_Midterm_page004_image003.png)

![Image extracted from page 4](images/Sp18_Midterm_page004_image004.png)

Histogram (i)

Histogram (ii)

Histogram (iii)

## Page 5

#### Name and SID: 5

#### 5. (10 points) Births and Days of the Week

Births in the United States are more common on weekdays than on weekends. The chart below shows the percent of births on each day of the week in the U.S. in 2016. The total number of births was 3,945,875. The chart also shows the percent of babies born on each day to the respondents of an internet survey. The number of respondents was 14,600.

Day Sunday Monday Tuesday Wednesday Thursday Friday Saturday U.S. % 9.62 14.94 16.30 16.06 16.05 15.91 11.12 Survey % 11.9 14.2 14.8 14.6 17.4 14.6 12.5

- (2 pt) Complete the statement below using the options given. Fill in the bubble of the day of the week

that corresponds to the ﬁrst blank. Next, ﬁll in the bubble of the reasoning that should be in the second blank. If we draw a large number of times at random from the distribution of U.S. births in the chart, we expect that the largest number of sampled births will be on ______________________ because ______________.

#### First Blank: Second Blank:

Monday

Thursday

there are confound- ing factors.

it is predicted by the law of averages.

Friday

Tuesday

random samples can be diﬀerent from each other.

association is not the same as causa- tion.

Saturday

Wednesday

Sunday

#### (b) (3 pt) The table births contains the data in the chart. The ﬁrst two rows are shown below.

![Image extracted from page 5](images/Sp18_Midterm_page005_image002.png)

Complete the statement below to make it a null hypothesis that can be used to test whether or not the survey results are like random draws from the distribution of births in the U.S. Fill in the bubble of the correct option to complete each of the blanks. Null Hypothesis: The births in the survey are like ________________________ random draws from the distribution in ________________________.

#### First Blank:

#### Second Blank:

(1/7) * np.ones(7)

14,600

births.column(’US’)

3,945,875

births.column(’Survey’)

- (3 pt) Fill in the line of code so that observed statistic is the observed value of the test statistic that

is appropriate for testing the hypotheses in Part (b) above.

observed_statistic = ___________________________________________________________________

- (2 pt) The array simulated_statistics contains 10,000 values of the test statistic simulated under the

null hypothesis. Complete the expression below so that it evaluates to the P-value of the test.

_______________________(simulated_statistics _________ observed_statistic)/ _____________

## Page 6

6

#### 6. (8 points) Ages

Last Sunday’s San Francisco Chronicle reported data from the Centers for Disease Control about the eﬀective- ness of the ﬂu vaccine. The histogram below shows the distribution of the ages of the people who took the ﬂu vaccine this year and did not get the ﬂu.

As usual, bins include the left endpoint but not the right. The numbers on the vertical axis are the heights of the bars. For example, the height of the bar over the 65-100 bin is 0.2. Units are provided in the axis labels.

![Image extracted from page 6](images/Sp18_Midterm_page006_image001.png)

- (2 pt) Pick only one of the two options to complete the sentence, and ﬁll in the blank for that option.

“The percent of people in the 0-5 bin is two times the percent of people in the 5-18 bin.” This quoted statement is

- True because ______________________________________________________________________________

(ii) False because ______________________________________________________________________________

- (2 pt) Deﬁne school-age children to be those who are at least 5 years old but less than 18 years old. Fill

in the blank with a number or arithmetic expression:

____________________________________% of the people are school-age children.

- (4 pt) Deﬁne adults to be people who are at least 18 years old. Among the adults, the proportion who

are less than 50 years old is equal to a/b where a and b are whole numbers. Fill in the blanks with any two numbers or arithmetic expressions that result in the correct proportion. Show your work!

a = ____________________________________ b = ____________________________________
