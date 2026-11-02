---
title: "Summer 2024 Midterm — Solution view"
course: Data 8
exam: Su24_Midterm_Sol
semester: su24
term: Summer
year: 2024
exam_type: midterm
view: solution
source: exams/data8/sp26/Su24_Midterm_Sol.pdf
student_file: Su24_Midterm.md
pages: 26
---

# Summer 2024 Midterm — Solution view

> **Solution view.** Staff answers are included: written and coded answers appear inline, and the option the staff selected is marked `[x]` (choose one or more) or `(x)` (choose one). Use these to guide a student or check their reasoning — never hand the answer over directly. The same exam without answers is in [Su24_Midterm.md](Su24_Midterm.md).

## Page 1

## DATA C8: Summer 2024 Midterm Exam

#### Full name: Solutions

#### Email address: data8@berkeley.edu

#### Student ID number: N/A

#### Name of the student to your left: No One

#### Name of the student to your right: No One

#### Instructions:

#### Do not open the exam until you are instructed to do so.

This exam is 95 points total, spread out over 6 questions on 22 pages, and must be completed in the 110-minute class period on July 12, 2024, from 11:10 AM to 1:00 PM with only pencils, erasers, a water bottle, and the midterm reference sheet unless you have pre-approved accommodations otherwise.

There is a line to write your initials in the upper left-hand corner of each page of the exam. Please make sure to write your initials on each page to ensure that your exam is graded properly.

Note that some questions require filling in the blank. Please only write your final answer in the box.

Note that some questions have circular bubbles to select a choice. This means that you should select one choice only. Other questions have square boxes. This means that you should select all choices that apply. Please fully shade in the circle or box to mark your answer.

#### Honor Code [0.5 pt]:

As a member of the UC Berkeley community, I act with honesty, integrity, and respect for others. I am the person whose name is on the exam, and I completed this exam in accordance with the Honor Code.

#### Signature: DATA C8: Foundations of Data Science (Summer 2024)

Good luck!

## Page 2

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 2 of 26

## 1) Potpourri [18 pts]

a)​ [2 pt] Charlie creates a table called crossword with two columns: time, her time (float)

for an individual crossword puzzle, and theme, whether or not the puzzle had a theme (boolean). Which one of the following would be best for Charlie to visualize the time distributions of both themed puzzles and non-themed puzzles?

〇 Line graph 〇 Scatter plot 〇 Overlaid bar chart 〇 Histogram 〇 Overlaid histogram

#### Solution: Overlaid histogram.

b)​ [2 pt] An array can contain data that are not similar (e.g., integers and strings).

〇 True 〇 False

#### Solution: False.

c)​ [2 pt] If the treatment and control groups are similar in all aspects but the treatment, we

may establish that the treatment caused a change in the outcome.

〇 True 〇 False

#### Solution: True.

d)​ [2 pt] Pivot tables are strictly for cross-classifying two categorical variables.

〇 True 〇 False

#### Solution: True.

## Page 3

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 3 of 26

e)​ [2 pt] What would the following code output?

‘20’ + str(round(int(24.8)))

〇 2025 〇 2024 〇 ‘2024.8’ 〇 ‘2025’ 〇 None of the above

#### Solution: None of the above (‘2024’)

#### f)​ [2 pt] Which of the following is correct about Python? Select all that apply.

- (x) ​Functions need not have a return statement.

- (x) ​Conditional statements must have an else statement.

- (x) ​Indenting the body of an if statement is optional.

- (x) ​A function can take zero arguments.
- (x) ​None of the above

#### Solution (1 pt each): The first and fourth choices.

g)​ [2 pt] In a randomized controlled trial, each subject records one observation for the

treatment group and one observation for the control group.

〇 True 〇 False

#### Solution: False.

## Page 4

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 4 of 26

h)​ [2 pt] Which one of the following is true?

〇 Wesley stands in front of Moffitt Library and surveys nearby students. This is a

random sample of UC Berkeley students. 〇 Wesley randomly selects students from the full Data 8 Summer 2024 roster by

flipping a coin for each student, where “Heads” results in the student being surveyed. This is a random sample of UC Berkeley data science majors. 〇 Wesley surveys students who comment on the “Students Materials Megathread”

on Ed Discussion. This is a random sample of current Data 8 students. 〇 Wesley randomly selects students from his lab section roster by flipping a coin for

each student, where “Tails” results in the student being surveyed. This is a random sample of Wesley’s lab section students. 〇 None of the above.

#### Solution: The fourth choice.

i)​ [2 pt] Mia creates a table houses with four columns: city (string), zip code (int), price (float), and sold (boolean). Which columns have categorical data, or data which is best treated categorically rather than numerically? Select all that apply.

- (x) ​city

- (x) ​zip code

- (x) ​price

- (x) ​sold

- (x) ​None of the above

#### Solution (⅔ point each): city, zip code, and sold.

## Page 5

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 5 of 26

## 2) What Would Python Do? [14 pts]

a)​ [14 pts] For each of the Python expressions below, write the output when the expression

is evaluated. If the expression evaluates to an array, you should format your answer like so: array([..., ..., ...]). If you think it would produce an error, write ERROR. You may assume the standard imports:

from datascience import * import numpy as np

And here, we create two arrays, arr1 and arr2.

arr1 = np.arange(2, 7, 2) arr2 = make_array(1, 3, 5)

- len(np.append(arr1, arr2)) == len(arr1 + arr2)

#### Solution (2 pts): False

ii) arr1 / make_array(2, 2, 2, 2)

#### Solution (2 pts): ERROR

iii) sum(make_array(3, 5, 7, 10) % 2 == 0)

#### Solution (2 pts): 1

iv) arr1 * arr2

#### Solution (2 pts): array([2, 12, 30])

- "Data" + "Science" * 3

#### Solution (2 pts): "DataScienceScienceScience" or 'DataScienceScienceScience'

## Page 6

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 6 of 26

vi) str(8) + int(‘7’)

#### Solution (2 pts): ERROR

b)​ [2 pts] Which of the following functions correctly returns the sum of the squares of the

#### numbers from 0 up to and including 𝑛? Select all that apply.

- (x) ​def sum_squares(n):

total = 0 for i in np.arange(0, n+1, 1): total = total + i**2 return total

- (x) ​def sum_squares(n):

return sum(np.arange(1, n+1, 1)**2)

- (x) ​def sum_squares(n):

total = make_array() for i in np.arange(0, n+1, 1): total = np.append(total, i**2) return sum(total)

- (x) ​def sum_squares(n):

return sum(np.arange(0, n+1) * np.arange(0, n+1))​

- (x) ​None of the above

#### Solution (0.5 pt each): All choices except “None of the above”.

## Page 7

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 7 of 26

## 3) For Who? [14.5 pts]

Conan and Bing are avid users of TikTok. They are interested in analyzing Conan’s For You page (fyp) and uncovering why he likes to spend so much time on the app. Each row in the tiktok table below represents one post that Conan has seen in the past month and includes the following columns:

●​ creator: (string) the username of the owner of the post. ●​ views: (int) the number of views (in thousands) the post received. ●​ comments: (int) the number of comments left on the post. ●​ tags: (string) all tags associated with the post (e.g., “#fyp #foryou”). ●​ liked: (boolean) True or False indicating if Conan liked the post or not.

#### creator views comments tags liked

crawly_possessed 95800 69856 True

kaybchung 9100 1441 #dentalstudent #dentalschool

False

#allnighter #studytok…

thebasementyard 9000 2051 False

allmight_31 40700 34359 #frogs #wrestling #foryou

True

#funny

official.mrhungry 32000 59023 #mrhungry #itstimetoeat

True

#easterbunny…

(... 4995 rows omitted)

a)​ [2 pts] Fill in the following blanks to create the most appropriate visualization to display

the comments and views variables on the same plot.

tiktok. (A) ( (B) )

- Fill in blank (A):

#### Solution (1 pt): scatter

ii) Fill in blank (B):

#### Solution (1 pt): “comments”, “views” or ‘comments’, ‘views’

## Page 8

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 8 of 26

b)​ [3 pts] Fill in the following blanks to return the username of the creator with the most

viewed post.

tiktok. (A) ( (B) ). (C) (“creator”).item(0)

- Fill in blank (A):

#### Solution (0.5 pt): sort

ii) Fill in blank (B):

#### Solution (1 pt): “views”, descending = True or ​ ‘views’, descending = True

iii) Fill in blank (C):

#### Solution (0.5 pt): column

c)​ [2 pts] Fill in the following blanks to return the number of unique creators in the tiktok

table.

tiktok. (A) (“creator”). (B) .

- Fill in blank (A):

#### Solution (1 pt): group

ii) Fill in blank (B):

#### Solution (1 pt): num_rows

## Page 9

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 9 of 26

Conan becomes excited when he stumbles upon a post with very few tags because he feels destined to see that post. He calls such posts “mythical fyp pulls”. To improve Conan’s TikTok experience, Bing suggests that we analyze how Conan’s likelihood of liking a video varies depending on the number of tags a post has. Bing helps us out by defining a function below:

def count_tags(string):

separated_string = string.split(“ ”) return len(separated_string)

#### d)​ [2 pts] Fill in the following blanks to add a new column called num of tags to the

tiktok table. This will be a column of integers containing the number of tags associated with each post.

tags_array = tiktok. (A) ( (B) , “tags”)

tiktok = tiktok. (C) (“num of tags”, (D) )

- Fill in blank (A):

#### Solution (0.5 pt): apply

ii) Fill in blank (B):

#### Solution (0.5 pt): count_tags

iii) Fill in blank (C):

#### Solution (0.5 pt): with_column or with_columns

iv) Fill in blank (D):

#### Solution (0.5 pt): tags_array

## Page 10

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 10 of 26

e)​ [3.5 pts] Conan is not a fan of posts with numerous tags. First, filter the table to only

include posts with fewer than 10 tags. Then, create a table that illustrates how Conan’s average number of likes varies by how many tags a post has. Finally, use that table to create a bar chart.​

Note: Each bar should represent videos with a certain number of tags, and the lengths of the bars should be determined by Conan’s average number of likes for those videos.

less_than_ten = tiktok. (A) (“num of tags”, (B) )

varies_tbl = less_than_ten.select(“num of tags”, “liked”).

- ( (D) )

varies_tbl. (E) ( (F) , “liked average”)

- Fill in blank (A):

#### Solution (0.5 pt): where

ii) Fill in blank (B):

#### Solution (0.5 pt): are.below(10)

ii) Fill in blank (C):

#### Solution (0.5 pt): group

iv) Fill in blank (D):

#### Solution (1 pt): “num of tags”, np.average or ​ ‘num of tags’, np.average

- Fill in blank (E):

#### Solution (0.5 pt): barh

## Page 11

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 11 of 26

vi) Fill in blank (F):

#### Solution (0.5 pt): “num of tags” or ‘num of tags’ or 0

f)​ [2 pt] Conan and Bing collect more information on three of the creators whose posts they

viewed and have stored them in the creators table below.

#### user followers_mil

kaybchung 1.5

thebasementyard 3.9

official.mrhungry 3

Consider joining just the five-row excerpt of tiktok and the creators tables together.

- How many rows will the joined table have? Enter a number.

#### Solution (1 pt): 3

ii) How many columns will the joined table have? Enter a number.

#### Accepted Solutions (1 pt):

●​ 7 (based on the tiktok table from 3d) ●​ 6 (based on the tiktok table excerpt above 3a)

## Page 12

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 12 of 26

## 4) Summer, Lovin’ Visualizations [17 pts]

Danny, a Data 8 student this summer, wants to learn more about his classmates’ music listening habits. He receives permission from Professor Sanchez to survey the class. All 300 Data 8 summer students respond to his survey, and he organizes the results into a table called music, where each row represents a unique student. The first four rows are presented below.

●​ studentID: (int) a categorical variable used to identify each student. ●​ time: (float) the student’s daily music listening time, measured in minutes. ●​ platform: (string) the student’s favorite music streaming platform. ●​ gsi: (string) the student’s lab GSI.

#### studentID time platform gsi

858 56.7 Apple Music Carisma

402 493.5 Spotify Andrew

202 806.4 YouTube Music Kaed

305 273.0 Pandora Lydia

… (296 rows omitted)

a)​ [3 pts] Fill in the following blanks to help Danny create the histogram below. ​

#### Note: The x-axis of the histogram has a range of [0, 1000], and each bin has a width of 100 minutes.

![Image extracted from page 12](images/Su24_Midterm_Sol_page012_image001.png)

## Page 13

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 13 of 26

- . (B) ( (C) , unit = (D) , bins = (E) )

- Fill in blank (A):

#### Solution (0.5 pt): music

ii) Fill in blank (B):

#### Solution (0.5 pt): hist

iii) Fill in blank (C):

#### Solution (0.5 pt): “time” or ‘time’

iv) Fill in blank (D):

#### Solution (0.5 pt): “minute” or ‘minute’

- Fill in blank (E):

Solution (0.5 pt for the function and 0.5 pt for the fully correct arguments): np.arange(0, 1001, 100) or make_array(0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)

b)​ [4 pts] GSI Kaed is interested in students’ specific daily music listening times. Using only

Danny’s table and histogram, help Kaed answer the following questions.

- Which one of the following is the best estimate for the amount of students with a daily music listening time of exactly 100 minutes?

〇 0 students 〇 33 students 〇 24% 〇 28% 〇 32% 〇 None of these estimates are appropriate.

#### Solution (2 pts): None of these estimates are appropriate.

## Page 14

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 14 of 26

ii) Which of the following is the best estimate for the total number of students in our table with a daily music listening time greater than or equal to 500 minutes, but less than 600 minutes?

〇 8 students 〇 16 students 〇 18 students 〇 24 students 〇 30 students 〇 48 students

#### Solution (2 pts): 24 students

●​ (0.075 percent per minute * 100 minutes) ●​ 7.5% of students * 300 total students ●​ 22.5 students

c)​ [3 pts] GSI Andrew likes Danny’s histogram from part (a), but he challenges Danny to

combine the two bins [600, 700) and [700, 800) into one single bin [600, 800).

#### i) Which of the following is the best estimate of the area of the new combined bin?

〇 16% 〇 20% 〇 24% 〇 28% 〇 32% 〇 None of the above

#### Solution (1 pt): 20%

●​ (0.08 percent per minute * 100 minutes) + ​ (0.12 percent per minute * 100 minutes) ●​ 8 percent + 12 percent ●​ 20 percent

## Page 15

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 15 of 26

ii) Calculate the height of the new combined bin, and place your final answer in the box below. You may leave your answer unsimplified or as a fraction. Remember to include the units.

#### Possible Solutions (1 pt for the value and 1 pt for the full units):

●​ 0.1 percent per minute ●​ 20/200 percent per minute ●​ 20/200 percent/minute ●​ 20 percent per 200 minutes ●​ 20 percent / 200 minutes ○​ Percent can be abbreviated or substituted with % ○​ Minute(s) can be abbreviated

d)​ [2 pts] GSI Carisma thinks using bins of 60 minutes would make more sense. Which of

#### the following arguments should she use within music.hist()? Select all that apply.

- (x) ​column = “time” / 60

- (x) ​unit = “hour”

- (x) ​bins = np.arange(60)

- (x) ​bins = np.arange(0, 1000, 60)

- (x) ​bins = np.arange(0, 1030, 60)

- (x) ​Carisma cannot do this with the music table

#### Solution: Only: bins = np.arange(0, 1030, 60)

e)​ [2 pts] GSI Lydia thinks it would be cool to see the distributions of students’ daily music

listening times by GSI. She wants to create one plot with a histogram of a different color for each GSI. Which one of the following arguments should she use within music.hist()?

〇 column = make_array(“time”, “gsi”) 〇 group = “gsi” 〇 group = make_array(“gsi”) 〇 group = [“time”, “gsi”] 〇 unit = “gsi” 〇 None of the above

#### Solution: group = “gsi”

## Page 16

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 16 of 26

f)​ [3 pts] Based on the information from Danny’s music table and histogram from part (a),

#### which of the following statements are true? Select all that apply.

- (x) ​Being enrolled in Kaed’s lab section causes students to listen to more music.
- (x) ​Danny’s data came from the population of summer 2024 Data 8 students and not

a sample of summer 2024 Data 8 students.
- (x) ​All UC Berkeley students have daily music listening times ranging from 0 to 1000

minutes.
- (x) ​It is appropriate for Danny to create a scatter plot with the gsi variable on the

x-axis and the platform variable on the y-axis.

- (x) ​It is not appropriate for Danny to create a line graph with the time variable on

the x-axis and the gsi variable on the y-axis.

- (x) ​Running this line of code will create a bar chart, where each bar represents a GSI

and the bar’s length represents the number of students that GSI has: music.group(“gsi”).barh(“gsi”)

#### Solution (1 pt each): The second, fifth, and sixth choices.

## Page 17

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 17 of 26

## 5) Boba Bonanza [13 pts]

Two popular boba tea spots near campus, Taiwanese Professional (TP) Tea and Boba Ninja, are in a friendly competition to see which one is preferred by students. The managers of these two establishments want to determine if there is a significant difference in student ratings between their boba teas.

They collected data from 300 randomly sampled student reviews, with the following columns:

●​ name: (string) the name of the boba restaurant. ●​ month: (string) the first three letters of the month the review was made. ●​ rating: (float) the rating given to the boba tea (on a scale from 1 to 5). ●​ topping: (string) the type of topping added ('none', 'regular', or 'extra').

Here are the first five rows of the table, which is named boba:

#### name month rating topping

TP Tea jan 4.5 regular

Boba Ninja feb 4.0 none

TP Tea mar 3.8 extra

Boba Ninja apr 4.2 regular

TP Tea may 4.7 none

… (295 rows omitted)

a)​ [4 pts] Formulate a null hypothesis and an alternative hypothesis that could be used to

test whether there is a difference in the average ratings between TP Tea and Boba Ninja.

- Null Hypothesis:

Possible Solution (2 pt): The average rating of boba teas at TP Tea is equal to the average rating of boba teas at Boba Ninja. Any observed difference is due to chance.

ii) Alternative Hypothesis:

Possible Solution (2 pt): The average rating of boba teas at TP Tea is not equal to the average rating of boba teas at BobaNinja. Any observed difference is not due to chance.

## Page 18

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 18 of 26

b)​ [2 pts] Which one of the following function calls would be helpful for simulating data

under the null hypothesis?

〇 boba.sample()

〇 boba.sample(with_replacement = False) 〇 boba.sample(300, with_replacement = True) 〇 sample_proportions(300, make_array(0.5, 0.5)) 〇 np.random.choice(boba.column(‘rating’)) 〇 None of the above

#### Solution: The second choice.

c)​ [5 pts] Suppose you decide to use a test statistic such that higher values favor the

alternative hypothesis. You simulate 1,000 values of the test statistic and assign them to the array test_stats. You then write the following code, which assigns the p-value to p_val.

num_extreme_test_stats = (A) .

p_val = num_extreme_test_stats / (B) .

Assume the observed test statistic has been assigned to observed_stat.

- Fill in blank (A):

#### Solution (3 pt): sum(test_stats >= observed_stat) or np.count_nonzero(test_stats >= observed_stat)

●​ Students can also use >

ii) Fill in blank (B):

#### Solution (2 pt): len(test_stats) or 1000

## Page 19

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 19 of 26

d)​ [2 pts] Suppose that num_extreme_test_stats from part (c) is equal to 45.

#### Assuming you use a 5% cutoff, which of the following can you conclude? Select all that apply.

- (x) ​You can reject the null hypothesis.
- (x) ​You can fail to reject the null hypothesis.
- (x) ​You can accept the alternative hypothesis.
- (x) ​There is evidence that the average ratings of TP Tea and Boba Ninja are different

in the population.
- (x) ​There is no evidence that the average ratings of TP Tea and Boba Ninja are

different in the population.
- (x) ​None of the above

#### Solution (1 pt each): The first and fourth choices.

## Page 20

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 20 of 26

## 6) Inside Out Lottery [19 pts]

On any given day, one of Andrew’s emotions can be found in charge at the control center. The emotion is chosen at random with replacement by drawing a ticket out of a box containing 100 tickets total. The tickets in the box have the following breakdown:

#### Emotion Tickets

Anger 11

Anxiety 28

Disgust 8

Fear 9

Joy 28

Sadness 16

a)​ [2 pts] Suppose Fear and Sadness were to pool their tickets together. What is the

probability that one of their tickets would be chosen two days in a row?

〇 (0.16 + 0.09)**2 〇 0.16 + 0.09 〇 (0.16**2) + (0.09**2) 〇 0.16 * 0.09 〇 (0.16 * 0.09)**2 〇 None of the above

#### Solution: The first choice.

●​ P(choosing Fear or Sadness) = (0.16 + 0.09). ●​ This needs to happen twice, so we square it.

## Page 21

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 21 of 26

b)​ [2 pts] Out of four consecutive days, what is the probability that Anger is in charge at

least once?

〇 0.11 + (0.11)**2 + (0.11)**3 〇 1 - (0.89)* (0.11)**2 〇 (3 * 0.11) + (3 * (0.11)**2) + (0.11)**3 〇 1 - (0.89)**4 〇 0.11 * (0.89)**3 〇 None of the above

#### Solution: The fourth choice.

c)​ [2 pts] Disgust thinks it is unfair that she has fewer tickets than everyone else. She

proposes that the tickets should be drawn without replacement, and the emotions agree to give it a try. Select all of the following statements that are true.

- (x) ​ The probability that Disgust will be chosen the first two days in a row is less than

it was when tickets were being drawn with replacement.
- (x) ​ The probability that Disgust will be chosen the first two days in a row is the same

as it was when tickets were being drawn with replacement.
- (x) ​The probability of Disgust being chosen on the first day is the same as the

probability of her being chosen on the tenth day.
- (x) ​The probability of Disgust being chosen on the second day is higher if she is not

chosen on the first day.
- (x) ​In any given six days, it is guaranteed that all emotions will have been chosen

once.
- (x) ​None of the statements are true.

#### Solution (1 pt each): The first and fourth choices.

●​ The probability that Disgust will be chosen two days in a row is less than it was when tickets were being drawn with replacement.

○​ (8/100)**2 > (8/100)* (7/99) ●​ The probability of Disgust being chosen on the second day is higher if she is not chosen on the first day.

○​ If chosen on the first day, P(second day) = 7/99. ○​ If not chosen on the first day, P(second day) = 8/99.

## Page 22

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 22 of 26

The emotions keep losing tickets when drawing without replacement and have decided to go back to drawing with replacement. Sadness notices that Joy is being drawn many times. She begins to keep track and notices that over the next 50 days, Joy is drawn 25 times. This worries Sadness, who knows the importance of all emotions and suspects Joy might be rigging the system by replacing other tickets with her own tickets to increase her chances of being drawn. Having taken Data 8 in the past, Sadness decides to investigate.

d)​ [2 pts] Given the information above, provide a clear and complete null hypothesis for

Sadness’s investigation.

#### Possible Solutions:

●​ Over the last 50 days, emotions were randomly chosen according to the ticket distribution. ●​ Each emotion has the same probability of being chosen each day, regardless of past days’ draws. ●​ Joy has a 0.28 chance of being chosen each day and each day is independent of other days. Any deviation is due to chance.

e)​ [2 pts] Provide an alternative hypothesis.

#### Possible Solution:

●​ The chance that Joy is being chosen on an arbitrary day is greater than 28%. This is due to something other than chance.

## Page 23

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 23 of 26

f)​ [2 pts] Which one of the following test statistics is the best to assess whether Joy’s

probability of being chosen is higher than it should be according to the original ticket drawing system?

〇 The difference between the sampled proportion of times Joy is drawn and the

expected proportion 〇 The absolute difference between the sampled proportion of times Joy is drawn

and the expected proportion 〇 The expected proportion of times Joy is drawn under the alternate hypothesis 〇 The expected proportion of times Joy is drawn under the null hypothesis 〇 The expected proportion 〇 None of the above

#### Solution: The first choice.

●​ It is directional and testable through simulation.

Upon closer examination of recent drawing results, Sadness notices that Joy may not be the only one whose probability of being chosen seems to have changed. She is now adjusting her investigation to see if there is a difference between the expected distribution and the one she has observed. Here are the hypotheses she is going to use:

●​ Null: The probability that each emotion is chosen is the same as described in the original distribution. ●​ Alternative: The distribution of emotions chosen in these 50 days is different from the original distribution.

g)​ [2 pts] Sadness wants to use TVD to assess if a difference exists but is rusty on this

#### topic. Select all of the following statements that are true.

- (x) ​We use np.abs when calculating TVD because we only care about the

instances when the differences are positive.
- (x) ​We use np.abs when calculating TVD because otherwise, the differences would

sum to 0.
- (x) ​TVD will be the same regardless of whether you subtract the expected

distribution from the simulated, or vice versa.
- (x) ​TVD is a good test statistic to use when assessing whether one emotion is being

chosen more than it should be.
- (x) ​It is necessary to divide TVD by 2 because TVD takes an average of the two

distributions.
- (x) ​None of the statements are true.

#### Solution (1 pt each): The second and third choices.

## Page 24

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 24 of 26

h)​ [3 pts] Sadness now writes a function to calculate one test statistic but is struggling. Help

her by filling in the blanks.

def simulate_test_statistic():

expected_props = make_array(0.28, 0.16, 0.08, 0.28, 0.11,

0.09) simulated_props = (A) ( (B) ) test_stat = sum( (C) ( (D) )) / 2 return test_stat

- Fill in blank (A):

#### Solution (0.5 pt): sample_proportions

ii) Fill in blank (B):

#### Solution (1 pt): 50, expected_props

iii) Fill in blank (C):

#### Solution (0.5 pt): abs or np.abs

iv) Fill in blank (D):

#### Solution (1 pt): expected_props - simulated_props or ​ simulated_props - expected_props

## Page 25

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 25 of 26

i)​ [2 pts] Suppose after Sadness runs her simulation 10,000 times, she gets a p-value of 0.035 and uses a cut-off value of 0.05. Which of the following statements is correct? Select all that apply.

- (x) ​There is a 0.035 chance that the alternative hypothesis is true.
- (x) ​There is a 0.035 chance that the null hypothesis is true.
- (x) ​There is a 0.035 chance that the TVD simulated under the null hypothesis is

equal to or less than the observed test statistic.
- (x) ​There is a 0.05 chance that Sadness will falsely reject the null hypothesis if the

null is true.
- (x) ​Since the p-value is less than the cut-off value, Sadness can conclude that the

null hypothesis is more reasonable than the alternative hypothesis.
- (x) ​None of the statements are correct.

#### Solution (1 pt each): The fourth choice.

## Page 26

Initials: D8 . DATA C8: Midterm Exam (Solutions). Page 26 of 26

## 7) Congratulations [0 pts, Optional]

Congratulations! You have completed the Midterm Exam.

●​ Please make sure that you have written your initials on each page of the exam. You may lose points on pages where you have not done so. ●​ Also, make sure that you have signed the Honor Code on the cover page of the exam for 0.5 point.

a)​ [0 pts] If there was any question on the exam that you thought was ambiguous and

required clarification to be answerable, please identify the question (including the title of the section, e.g., “Boba Bonanza”), and state your assumptions. Be warned: We only plan to consider this information if we agree that the question was erroneous or ambiguous and we consider your assumption reasonable.

b)​ [0 pts] Draw and caption your favorite Data 8 experience or staff member!
