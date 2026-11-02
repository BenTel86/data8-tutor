---
title: "Summer 2019 Midterm — Student view"
course: Data 8
exam: Su19_Midterm
semester: su19
term: Summer
year: 2019
exam_type: midterm
view: student
source: exams/data8/sp26/Su19_Midterm.pdf
solution_file: Su19_Midterm_Sol.md
pages: 11
---

# Summer 2019 Midterm — Student view

> **Student view.** These are the questions exactly as students received them: every multiple-choice option is unmarked (`[ ]` or `( )`) and no answers are present. The staff answers are in [Su19_Midterm_Sol.md](Su19_Midterm_Sol.md).

## Page 1

## Data 8 Foundations of Data Science Summer 2019 Midterm Exam

#### INSTRUCTIONS

- The exam is worth 80 points. You have 110 minutes to complete it. - The exam is closed book, closed notes, closed computer/phone/tablet, closed calculator, except the oﬃcial midterm exam reference guide provided with the exam. - Write/mark your answers on the exam in the blanks/bubbles provided. Answers written anywhere else will not be graded. Unless the question speciﬁcally asks you to explain your answer, you do not need to do so, and if you write an explanation it will not be graded. - If you need scratch paper, you are welcome to use the reference guide and the back of this cover page. Scratch work will not be graded. - For all Python code, you may assume that the statements from datascience import * and import numpy as np have been executed. Do not use features of the Python language that have not been described in this course. - In any part, you are free to use any tables, arrays, or functions that have been deﬁned in previous parts of the same question, and you may assume they have been deﬁned correctly.

Last name

First name

Student ID number

Calcentral email (_@berkeley.edu)

Name of Lab GSI

Your seat number (e.g. A1) & room

### ← Name of the person to your left

### Name of the person to your right →

#### All the work on this exam is my own. (please sign)

## Page 2

2

#### This page is intentionally left blank. You can use it for scratch work but it will not be graded.

## Page 3

#### Name: 3

#### 1. (22 points) Get OﬀYour Phone

A digital media company commissions a Berkeley Data Science club to conduct an analysis about how much time people spend on their phones. The club surveyed 500 people and collected the resulting data in the table phones which has 5 columns:

- Name: The person’s name

- Model: The type of phone the person has, an ’iPhone’, ’Samsung Galaxy’, ’Google Pixel’, or ’Non- smartphone’

- Screentime: The average daily minutes that person spends on their phone

- Data (MB/day): The average daily cell data usage of that person, in megabytes

- Provider: The person’s cell phone carrier: ’AT&T’, ’Verizon’, ’Sprint’, or ’T-Mobile’

Here are the ﬁrst 5 rows of the table, which has 500 rows total:

![Image extracted from page 3](images/Su19_Midterm_page003_image001.png)

Fill in the blanks with Python expressions to compute the desired output. ONLY use the blank lines provided. Some of the chained operations we might normally do in one line have been broken up into two or more lines, storing intermediate results in tables or arrays. Do not write any code outside the blanks provided. The expression in the last line should evaluate to the value described in the question.

- (2 pt) Write code to assign least_screen to the smallest value of daily screentime in the phones table.

least_screen =

- (3 pt) Write code that assigns num_iphones to the number of people with iPhones in the phones table.

iphones = phones. ("Model", ( )

num_iphones = iphones.

- (4 pt) Write code that assigns high_provider to the cell phone provider of the person with the highest

data usage. You can assume that data usages are unique in the phones table.

sorted = phones. ( , )

high_provider = sorted. .( ). ( )

## Page 4

4

- (3 pt) Write code that assigns average to a table with two columns: one containing all of the phone

models, and another containing the average screentime for each model.

average = phones. ( , ).select( , )

- (6 pt) Later on in the project, a club member creates a table with information about cell phone providers

and data costs. The providers table has two columns:

- Company: The name of the cell phone provider (AT&T, Verizon, Sprint, or T-Mobile)

- Price ($/MB): The price the company charges per megabyte of data used.

![Image extracted from page 4](images/Su19_Midterm_page004_image001.png)

Write code to generate a table called costs which contains two columns:

- Name: The name of the person in the study

- Monthly Cost: The price the person has to pay for 30 days of data usage. Assume that every day, the person used the usage amount listed in the phones table.

all_info = phones. ( , , )

daily_usage = . ( )

prices = . ( )

daily_cost = daily_usage * prices

monthly_cost = daily_cost * 30

costs = Table(). (

’Name’, ,

’Monthly Cost’, )

## Page 5

#### Name: 5

#### (f) (2 pt) Write code so that summary results in the following table:

![Image extracted from page 5](images/Su19_Midterm_page005_image001.png)

The value in each cell represents the number of people in the survey that had the corresponding phone/provider combination.

summary = phones.

#### (g) (2 pt) The following is a plot displaying the count of each phone model in the phones table:

![Image extracted from page 5](images/Su19_Midterm_page005_image002.png)

Which line of code generated the above plot?

phones.barh(’Model’)

phones.group(’Model’).barh(’Model’)

phones.hist(’Model’)

phones.group(’Model’).hist(’Model’)

## Page 6

6

#### 2. (8 points) Street Smarts

In 2015, economists Melissa Kearney and Phillip Levine published a study investigating the eﬀects of watching Sesame Street on the future academic performance of young viewers in the early 1970s. Sesame Street is a popular childrens show that was ﬁrst introduced in 1969 and provides free educational content on public television to children who are too young to attend school.

However, there was variation in exposure to Sesame Street across the country, due to technological constraints. Approximately 1/3 of US viewers lived in counties where they were unlikely to be able to view Sesame Street. Whether or not a county had high rates of access to Sesame Street was close to random and was not associated with any particular characteristics of the county, such as income.

Since the researchers did not have data on whether individual children watched Sesame Street, they instead investigated county-level elementary-school success metrics of groups of children who started school after the show debuted and who lived in locations where broadcast reception for the show was high, and compared these metrics to those among older groups of children (who would not have watched Sesame Street before starting school) and those who lived in locations with limited broadcast reception (poor likelihood of access to Sesame Street).

The authors found that ”children who lived in places with better access to the show did better [on average] in elementary school, as compared to those with limited access and those who were older at the time the show was introduced. They were more likely to start school on time and progress at the appropriate grade for age.”

#### (a) (2 pt) Who were the individuals in this study?

Individual children who started school after Sesame Street debuted in the United States

Individual children who started school just before or after Sesame Street debuted in the United States

Groups of children in diﬀerent counties in the United States

Groups of children in diﬀerent counties with high likelihood of access to Sesame Street in the United States

#### (b) (2 pt) The authors made two comparisons:

- They compared the educational outcomes of groups of children in counties with high likelihood of access to Sesame Street to the educational outcomes of groups of children with low likelihood of access to Sesame Street. - They compared the educational outcomes of groups of children in counties with high access to Sesame Street, and who started school after Sesame Street debuted, to groups of children in those same high-access counties who started school before Sesame Street debuted on television.

Why did the authors include both comparisons in their study?

The authors thought children may have moved from one county to another, so they wanted to study the children who moved by looking at the same group over time.

By studying the same children before and after they watched Sesame Street, the authors could deter- mine whether Sesame Street was the reason that some individual students performed better than others.

The authors wanted to include more children in their study (a larger sample size) so that the children would be more representative of the population of all children in the United States, instead of just looking at one age group.

Making both comparisons helps eliminate the possibility of confounding factors due to broadcast variability (which counties had Sesame Street access) or variation in educational quality across years (if education in general improved or got worse over the study period).

## Page 7

#### Name: 7

#### (c) (4 pt) Select all correct statements:

This was an observational study.

This was a randomized controlled experiment.

It is only possible to investigate a causal link with a randomized controlled experiment, and this study did not help establish a causal link between Sesame Street and better educational outcomes.

Whether or not a child lived somewhere with access to Sesame Street was random, because the researchers split the groups of children into a treatment and a control group.

The authors were attempting to use a natural experiment, the variation in TV signals, to establish a causal link between watching Sesame Street and better educational outcomes.

## Page 8

8

#### 3. (12 points) Boba Distributions

Anna is curious about her boba spending habits. The following is a histogram of her weekly spending on boba, over the span of 50 weeks (she doesnt drink boba on her yearly two week vacation):

![Image extracted from page 8](images/Su19_Midterm_page008_image002.png)

The spending is divided into bins of width 2: [0,2), [2,4) ... [18,20).

Assume that all of the data is shown on the histogram (Anna never spent $20 or more in a given week).

For the following questions, write a mathematical expression for the answer, or write Not possible if it is not possible to calculate the desired quantity with the information in the given histogram.

#### (a) (3 pt) In what percent of weeks did Anna spend $16 or more on boba?

#### (b) (3 pt) In what percent of weeks did Anna spend between $12 and $15 on boba?

#### (c) (3 pt) During how many weeks did Anna spend between $10 and $13 dollars?

11 weeks

Between 5 and 11 weeks

22 weeks

Between 10 and 22 weeks

Not possible to calculate using the histogram

- (3 pt) After looking over her notes, Anna ﬁnds that she entered the wrong data for two of the weeks

when constructing the histogram. She is not sure whether her spending in those weeks should go in the [12, 14) or [14, 16) bin, so she decides to combine all of the data in those two bins into one bin of width 4, from [12,16). What is the height of this new bin?

## Page 9

#### Name: 9

#### 4. (10 points) Steph Curry Fan Club

A group of current Data 8 students who are big fans of Steph Curry are inspired by the current course material to conduct an analysis of Curry’s basketball shot record. It turns out Steph Curry has a 58% chance of successfully shooting the ball in the basket any time he tries.

- (2 pt) Curry shoots the ball twice. What is the probability that both of the shots make it in the basket?

58 100 × 58 99

0.582

0.422

2 × 0.58

- (2 pt) Curry shoots the ball twice. What is the probability that one shot makes it into the basket, and

one shot does not?

(0.58 × 0.42)2

0.58 × 0.42

1 − (0.58)2

(0.58 × 0.42) + (0.42 × 0.58)

Digging deeper into Steph Curry’s basketball record, the students ﬁnd that 80% of Currys shots are contested - that is, someone is actively trying to block his shot or make him miss. When a shot is contested, Curry has a 55% chance of successfully shooting the ball in the basket any time he tries. When his shots are not contested, Curry has a 70% chance of shooting the ball in the basket.

- (2 pt) Given that Steph Curry’s shot was uncontested, what is the probability the shot did not make it

in the basket?

0.2 × 0.3 (0.2 × 0.3 + 0.8 × 0.45)

0.42

(0.2 × 0.3) + (0.8 × 0.45)

0.30

- (2 pt) Given that Steph Curry took three contested shots in a row, what is the probability that at least

one of them went in?

1 − (0.45)3

1 − (3 × 0.45)

0.80 × 0.55 [(0.80 × 0.55) + (0.20 × 0.70)]3

0.553

#### (e) (2 pt) Given that Steph Curry made the shot, what is the probability the shot was contested?

0.20 × 0.70  

1 − (0.45)3



(0.80 × 0.55) + (0.20 × 0.70)

0.80 × 0.55  

0.8



(0.80 × 0.55) + (0.20 × 0.70)

## Page 10

10

#### 5. (28 points) Issues with Inﬂuenza

The national news reports widespread hospitalizations from ﬂu this year in the United States. Since you don’t remember the media reporting on this in the past, you want to know if this year’s incidence rate of ﬂu (the proportion of the population who become infected with inﬂuenza) in the U.S. is higher than usual. Since you only have the resources to take a random survey of 1000 people, you decide to conduct a hypothesis test to ﬁnd out.

After conducting your random survey of 1000 people, you ﬁnd that the incidence rate among this sample is 0.35. In modern history (since the invention of the inﬂuenza vaccine), the expected incidence rate is 0.2.

#### (a) (3 pt) What is the appropriate null hypothesis?

Our sample is large enough to represent the US population.

The true incidence rate is 0.35, and 0.2 is an inaccurate estimate of historical incidence rates.

The true incidence rate of inﬂuenza this year is greater than 0.2, and our survey incidence rate is representative of the true incidence rate.

The true incidence rate of inﬂuenza this year is 0.2, and any deviation from this rate is due to chance in the selection of the random sample.

#### (b) (3 pt) What is the appropriate alternative hypothesis?

Our sample was not representative of the US population.

The inﬂuenza vaccine is not very eﬀective this year.

The true incidence rate of inﬂuenza this year is greater than 0.2.

The true incidence rate of inﬂuenza this year is less than 0.2.

#### (c) (3 pt) What is an appropriate test statistic?

Number of inﬂuenza cases in our sample

Population proportion of inﬂuenza cases

Sample proportion of inﬂuenza cases

- (8 pt) Write code below so that test_proportions evaluates to 10,000 simulated values of your test

statistic under the null hypothesis.

expected_props = make_array( , )

sample_size = 1000

def simulated_proportion(expected_props, sample_size):

null_props = ( , )

prop_sick = null_props. ( )

return

test_props =

for :

one_statistic =

= ( , one_statistic)

## Page 11

#### Name: 11

#### (e) (3 pt) Select one of the options from parts i-iii to ﬁll in the corresponding blanks in the

sentence below. To calculate the p-value for this test, we would ﬁnd the proportion of (i) under the (ii) that were (iii) our observed test statistic.

i.

observed test statistic

simulated test statistics

years in the past century

ii.

null hypothesis

alternative hypothesis

iii.

equal to

less than or equal to

greater than or equal to

- (2 pt) You ﬁnd your p-value to be 0.04. Under which of these p-value cutoﬀlevel(s) would you fail to

reject the null? Select all that apply.

0.10

0.07

0.05

0.03

0.01

- (3 pt) With a 5% p-value cutoﬀand your p-value of 4%, and considering your original hypothesis, would

you conclude that the inﬂuenza vaccine was not very eﬀective this year?

No, because you did not reject the null hypothesis.

Yes, because you found a signiﬁcant diﬀerence in the inﬂuenza rates.

No, because the null hypothesis was about the incidence rate, not vaccine eﬃcacy.

Yes, because your p-value was above 0%.

- (3 pt) You are discussing your survey methodology with a friend and reveal that the population from

which your survey participants were selected was the population of all Berkeley undergraduates. Assuming you carried out the steps in parts e-f, would your method successfully test the null hypothesis that the incidence rate is higher than expected in the U.S. population? Select one option.

Yes, because you selected students at random for your survey.

Yes, because your p-value was small.

No, because 1000 individuals is not a big enough sample to run a hypothesis test.

No, because your sample is not representative of the US population.

1. (0 points) Write your name in the space provided on one side of every page of the exam. You’re done!
