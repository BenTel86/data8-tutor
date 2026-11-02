---
title: "Summer 2017 Midterm — Student view"
course: Data 8
exam: Su17_Midterm
semester: su17
term: Summer
year: 2017
exam_type: midterm
view: student
source: exams/data8/sp26/Su17_Midterm.pdf
solution_file: Su17_Midterm_Sol.md
pages: 12
---

# Summer 2017 Midterm — Student view

> **Student view.** These are the questions exactly as students received them: every multiple-choice option is unmarked (`[ ]` or `( )`) and no answers are present. The staff answers are in [Su17_Midterm_Sol.md](Su17_Midterm_Sol.md).

## Page 1

## Data 8 Midterm

#### Summer 2017

First Name:

Last Name:

Email: @berkeley.edu

Student ID:

GSI:

Name of person to your left:

Name of person to your right:

#### All the work on this exam is my own. (please sign):

### Instructions:

- This exam contains 12 pages (including this cover page) and 4 questions.

#### • This exam must be completed in the 1:50 time period ending at 12:00PM.

- You may use a single handwritten (two-sided) cheat sheet and the two ofﬁcial study guides provided with this exam.

- Work quickly through each question. There are a total of 91 points on this exam.

1

## Page 2

Data 8 Midterm - Page 2 of 12 7/14/2017

This page intentionally left blank.

## Page 3

Data 8 Midterm - Page 3 of 12 7/14/2017

### 1 Counting Calories

1. (14 Pts) The calories table has a list of all food items from McDonald’s and contains the following columns:

#### • Item: A string, the name of the item.

#### • Size: An int, the serving size of the item in grams.

#### • Cal: An int, the number of calories the item has.

- FatCal: An int, the number of calories from fat the item has. The number of calories from fat is always less than or equal to the number of calories.

calories:

Item Size Cal FatCal Egg McMufﬁn 136 300 120 Baked Apple Pie 77 250 110 McRib 208 500 240 Daily Double 190 430 200 ... (257 rows omitted)

The categories table has a list of all food items from McDonald’s and contains the following columns:

- Item: A string, the name of the item. The items in this column are the same as in calories but are not in the same order.

#### • Category: A string, the category of the item.

categories:

Item Category Egg McMufﬁn Breakfast McChicken Chicken & Fish Premium Southwest Salad (without Chicken) Salads Baked Apple Pie Desserts ... (257 rows omitted)

This problem is continued on the next page.

## Page 4

Data 8 Midterm - Page 4 of 12 7/14/2017

Fill in the blanks of the Python expressions to compute the described values. You must use all and only the lines provided. The last (or only) line of each answer should evaluate to the value described. Assume that the statements from datascience import * and import numpy as np have been executed.

- (2 Pts) The total number of calories of all items on the McDonald’s menu.

_____________(calories._____________(_________________))

- (3 Pts) The average serving size of all items with over 200 calories from fat.

____________(

calories._________(________________, ________________)

._____________(___________________) )

- (3 Pts) The serving size of the item with the largest serving size of all breakfast menu

items. Use the provided mcdonalds table.

mcdonalds = calories.join(’Item’, categories)

____________(

mcdonalds._________(________________, ________________)

._____________(___________________) )

## Page 5

Data 8 Midterm - Page 5 of 12 7/14/2017

- (6 Pts) We have access to the following menu table which is a simpler combined version

of the calories and categories tables. It just contains each food item, the number of calories, and the category for the item:

Item Cal Category Egg McMufﬁn 300 Breakfast Baked Apple Pie 250 Desserts McRib 500 Beef & Pork Daily Double 430 Beef & Pork ... (257 rows omitted)

Which of the following Python expressions evaluates to the number of desserts with less

#### than 200 calories? Select all that apply.

- [ ] (menu.where(’Category’, are.equal_to(’Desserts’))

.where(’Calories’, are.below(200)) .num_rows)

- [ ] (menu.where(’Calories’, are.below(200))

.where(’Category’, are.equal_to(’Desserts’)) .num_rows)

- [ ] (menu

.with_column(’Below200’, menu.column(’Calories’) < 200) .pivot(’Category’, ’Below200’) .num_rows)

- [ ] (menu

.with_column(’Below200’, menu.column(’Calories’) < 200) .pivot(’Category’, ’Below200’) .where(’Below200’, are.equal_to(True)) .num_rows)

- [ ] (menu.group(’Category’)

.where(’Calories’, are.below(200)) .where(’Category’, are.equal_to(’Desserts’)) .column(’count’).item(0))

- [ ] (menu.where(’Calories’, are.below(200))

.group(’Category’) .where(’Category’, are.equal_to(’Desserts’)) .column(’count’).item(0))

## Page 6

Data 8 Midterm - Page 6 of 12 7/14/2017

### 2 License Samples

1. (14 Pts) The table license contains the name and age of every person who got a new driver’s license from the Berkeley DMV in 2016, sorted by age in descending order.

name age Arvind 49 Nanxi 38 Emma 25 ... (347 rows omitted)

Sample 1: license.take(np.arange(30, 100)) Sample 2: license.take(np.arange(0, license.num rows, 10)) Sample 3:

start = np.random.choice(np.arange(10)) license.take(np.arange(start, license.num_rows, 10))

- (2 Pts) Select all true statements about the three samples.

- [ ] Sample 1 is a deterministic sample.
- [ ] Sample 2 is a probability sample.
- [ ] Samples 2 and 3 are systematic samples.
- [ ] All three samples are taken at random without replacement.

- (2 Pts) What is the probability that Arvind is included in Sample 2? Assume that each

name only appears once in the table. Select one choice.

⃝ 0 ⃝ 1 10 ⃝ 1 2 ⃝ 1 3 ⃝ 1

- (2 Pts) What is the probability that Arvind is included in Sample 3? Assume that each

name only appears once in the table. Select one choice.

⃝ 0 ⃝ 1 10 ⃝ 1 2 ⃝ 1 3 ⃝ 1

## Page 7

Data 8 Midterm - Page 7 of 12 7/14/2017

- (2 Pts) Fred calculates the average age of all the people in sample 1. Select all choices

that accurately complete the sentence. This value is:

- [ ] the population parameter.
- [ ] a statistic.
- [ ] an unbiased estimate of the population parameter.
- [ ] a biased estimate of the population parameter.

- (6 Pts) Fred writes the following code to take samples from license. For each of the

questions in this part, select one choice.

num_trials = 1 mystery = make_array() for i in np.arange(200):

something = np.mean(

license.sample(100, with_replacement=False)

.column(‘age’) ) mystery = np.append(mystery, something)

- How many samples did Fred take with this code?

⃝ 1 sample. ⃝ 100 samples. ⃝ 200 samples. ⃝ Can’t tell from this code alone.

ii. How large was each sample?

⃝ 1 person. ⃝ 100 people. ⃝ 200 people. ⃝ Can’t tell from this code alone.

iii. At the end of this code, what does the mystery array contain?

⃝ Unbiased estimates of the population mean. ⃝ Biased estimates of the population mean. ⃝ Unbiased estimates of Sample 2’s mean. ⃝ Biased estimates of Sample 2’s mean.

## Page 8

Data 8 Midterm - Page 8 of 12 7/14/2017

### 3 Smoking Weights

1. (13 Pts) 600 women were surveyed after giving birth. Each woman was asked whether she regularly smoked and the weight of their newborns were recorded. There were 100 smokers and 500 non-smokers among those surveyed. The histograms below visualize the babies’ weights of these two groups of women.

Both histograms have bins that are multiples of 10. The bar heights of both histograms are multiples of 0.1 percent per ounce.

![Image extracted from page 8](images/Su17_Midterm_page008_image001.png)

![Image extracted from page 8](images/Su17_Midterm_page008_image002.png)

- (8 Pts) For each pair of quantities, select one choice for the correct statement.

You must brieﬂy justify your answer in the space provided to receive full credit. When possible, use a mathematical justiﬁcation.

#### i. (I) The proportion of weights between 100 (inclusive) and 110 (exclusive) for smok-

#### ers vs. (II) The proportion of weights between 100 (inclusive) and 110 (exclusive) for non-smokers.

⃝ (I) is larger. ⃝ (II) is larger. ⃝ (I) and (II) are roughly equal. ⃝ There is not enough information to compare (I) and (II).

## Page 9

Data 8 Midterm - Page 9 of 12 7/14/2017

#### ii. (I) The number of newborn weights between 80 (inclusive) and 90 (exclusive) for

smokers vs. (II) The number of newborn weights between 80 (inclusive) and 90 (exclusive) for non-smokers.

⃝ (I) is larger. ⃝ (II) is larger. ⃝ (I) and (II) are roughly equal. ⃝ There is not enough information to compare (I) and (II).

#### iii. (I) The proportion of newborn weights under 100 (exclusive) for smokers vs. (II)

#### The proportion of newborn weights above 130 (inclusive) for non-smokers.

⃝ (I) is larger. ⃝ (II) is larger. ⃝ (I) and (II) are roughly equal. ⃝ There is not enough information to compare (I) and (II).

#### iv. (I) The number of newborn weights between 100 (inclusive) and 115 (exclusive) for

smokers vs. (II) The number of newborn weights between 115 (inclusive) and 130 (exclusive) for smokers.

⃝ (I) is larger. ⃝ (II) is larger. ⃝ (I) and (II) are roughly equal. ⃝ There is not enough information to compare (I) and (II).

## Page 10

Data 8 Midterm - Page 10 of 12 7/14/2017

- (3 Pts) What proportion of all babies (with smoking and non-smoking mothers) were

between 140 and 150 ounces? You may leave your answer as a mathematical expression.

## Page 11

Data 8 Midterm - Page 11 of 12 7/14/2017

### 4 Cookie Questions

1. Cookie Monster owns a cookie factory. His factory produces cookie ﬂavors in the following proportions:

Sugar Chocolate Chip Trash 0.2 0.6 0.2

Sam is unhappy that his box of 10 cookies had 4 Trash-ﬂavored cookies in it. However, he doesn’t remember whether he got his cookies from Cookie Monster’s factory or another factory. You decide to run a hypothesis test to ﬁgure out whether Sam’s box came from Cookie Monster’s factory or not.

- (3 Pts) Select the correct option from each set of choices to state an appropriate null

hypothesis for this problem. Null hypothesis: Sam’s box ⃝ did ⃝ did not come from Cookie Monster’s factory.

Thus, the chance that any one cookie in Sam’s box was Trash-ﬂavored is ⃝ 0.2. ⃝ computable but not 0.2. ⃝ unknown given this information.

Because ⃝ of random chance, ⃝ the box didn’t come from Cookie Monster’s factory, Sam got a higher number of Trash-ﬂavored cookies in his box.

#### (b) (4 Pts) As a test statistic, you choose to compare the proportion of Trash-ﬂavored cookies

in boxes of 10 cookies. Complete the lines below to compute a single test statistic using a random sample from the population, storing the value into test stat. You may write expressions as long as you need to on each line, but you may not use extra lines.

outcomes = make_array(

________________________________________________

________________________________________________ )

sample = np.random.choice(outcomes, ______________)

test_stat = ______________________________________

## Page 12

Data 8 Midterm - Page 12 of 12 7/14/2017

- (4 Pts) Given that your ﬁnal computed p-value is less than 0.05, select all histograms

corresponding to the possible probability distributions of the test statistic.

![Image extracted from page 12](images/Su17_Midterm_page012_image001.png)

![Image extracted from page 12](images/Su17_Midterm_page012_image002.png)

![Image extracted from page 12](images/Su17_Midterm_page012_image003.png)

![Image extracted from page 12](images/Su17_Midterm_page012_image004.png)

#### Brieﬂy justify your answer below:
