---
title: "Summer 2018 Final — Solution view"
course: Data 8
exam: Su18_Final_Sol
semester: su18
term: Summer
year: 2018
exam_type: final
view: solution
source: exams/data8/sp26/Su18_Final_Sol.pdf
student_file: Su18_Final.md
pages: 22
---

# Summer 2018 Final — Solution view

> **Solution view.** Staff answers are included: written and coded answers appear inline, and the option the staff selected is marked `[x]` (choose one or more) or `(x)` (choose one). Use these to guide a student or check their reasoning — never hand the answer over directly. The same exam without answers is in [Su18_Final.md](Su18_Final.md).

## Page 1

## Data 8 Foundations of Data Science Summer 2018 Final Solutions

#### INSTRUCTIONS

- You have 2 hours and 50 minutes to complete the exam.

- The exam is closed book, closed notes, closed computer, closed calculator, except for the oﬃcial reference guide provided with the exam.

#### • Mark your answers on the exam itself. We will not grade answers written on scratch paper.

- You may leave numerical calculations unsimpliﬁed throughout the exam.

- You may assume that the statements import numpy as np and from datascience import * have been exe- cuted throughout the exam.

- No questions will be allowed during the time of the ﬁnal. If something is unclear, you may state an assumption. If the assumption is valid, we will grade based on your assumption.

Question 0 (1 point) Write your name and SID (Student ID Number) in the space provided on one side of every page of the exam.

Last name

First name

Student ID number

CalCentral email (_@berkeley.edu)

GSI name and Lab Time

Name of the person to your left

Name of the person to your right

#### All the work on this exam is my own. (please sign)

## Page 2

2

#### 1. (13 points) YouTable

You are interested in ﬁnding out who the most popular YouTube content producers in the United States are. Your colleague used the YouTube online statistics API to ﬁnd out the top 250 YouTubers in the United States as of August 2018, based on total number of video views. The ﬁrst few rows of her dataset yt are shown below.

![Image extracted from page 2](images/Su18_Final_Sol_page002_image001.jpeg)

In the table above, the entries in the columns Username and Category are of type string while the entries in all other columns are of type int. Uploads corresponds to number of video uploads per artist, Subs is number of active subscribers, and Views is total amount of views in all the videos a YouTube artist has released.

Fill in the blanks of the Python expressions to compute the described values. You must use only the lines provided to get full credit.The last line of each answer should evaluate to the value described. Assume that the statements import numpy as np and from datascience import * have been executed. You may enter anything you would like in the blanks below, but you may not add code outside of the blanks.

#### (a) (1 pt) The total number of YouTubers in this table who have more than 1000 video uploads.

yt.________________________________________________________________________________

yt.where(’Uploads’, are.above(1000)).num_rows

- (2 pt) You realize that the music video streaming platform VEVO contributes a lot of the top US YouTube

artist accounts like ”TaylorSwiftVEVO” and ”shakiraVEVO”. Create a table that only contains channels from VEVO, with the artists with the most subscribers at the top.

yt._________________________________________________________________________________

yt.where(’Username’, are.containing(’VEVO’)).sort(’Subs’, descending=True)

- (3 pt) You are interested in ﬁnding the category (ex. Sports, Music, News) with the largest average

number of subscribers. Fill in the lines below so that the last line evaluates to said category. only_sub_and_cat = yt.______________________________________________________________

only_sub_and_cat.___________________________________________________________________

## Page 3

#### Name: 3

only_sub_and_cat = yt.select(’Category’, ’Subs’)

only_sub_and_cat.group(0, np.mean).sort(1, descending = True).column(0).item(0)

Many people used take incorrectly. Remember take expects an array of row indicies to take from the table.

- (3 pt) Your friend proposes that a more eﬀective popularity metric for YouTube content creators might

be view count per video upload. Create a table with one column that contains only the usernames of the 5 top US YouTubers, sorted by highest view count per video upload.

views_per_upload = ____________________________________________________________________

yt_new_metric = yt.with_column(________________________________________________________)

yt_new_metric.__________________________________________________________________________

views_per_upload = yt.column(’Views’)/yt.column(’Uploads’)

yt_new_metric = yt.with_column(’views_per_upload’, views_per_upload)

yt_new_metric.sort(’views_per_upload’, descending=True).take(np.arange(5)).select(’Username’)

In addition to the top 250 US YouTube accounts table from before, your friend ﬁnds a second table for the top 250 UK (United Kingdom) YouTube accounts, sorted by subscriber count. The ﬁrst few rows of the yt uk table are shown below.

![Image extracted from page 3](images/Su18_Final_Sol_page003_image001.jpeg)

#### (e) (4 pt) Find the number of YouTubers that are only present in one of the top 250 subscriber lists

between the two countries.

num_youtubers_in_both =__________________________________________________________________

__________________________________________________________________________________________

num_youtubers_in_both = yt_uk.join(’Username’, yt)

yt.num_rows + yt_uk.num_rows - 2*num_youtubers_in_both.num_rows

## Page 4

4

#### 2. (10 points) Spotify Shuﬄe

Fahad creates a Spotify music playlist by randomly sampling 100 songs from a large collection of tunes from the Data 8 staﬀmusic library. It is known that staﬀlibrary contains 20% Hip-Hop songs, 35% Pop songs, 15% Rock songs, 25% Dance songs, and 5% Country songs.

Vinitra notices that in Fahad’s playlist, there are 30% Hip-Hop songs, 30% Pop songs, 20% Rock songs, 18% Dance songs, and 2% Country songs.

Initially, Vinitra believes that Fahad’s claim that he randomly sampled 100 songs from the large staﬀlibrary is false. Speciﬁcally, she believes he purposefully sampled more Hip-Hop songs.

- (3 pt) Describe a test statistic that we could compute given a sample that can help us pick between the

two viewpoints: Fahad sampled the songs randomly and any diﬀerence is due to chance, or he was biased in his sampling technique and sampled more Hip-Hop songs.

The percentage of songs that are Hip-Hop or the diﬀerence between actual number of hip hop songs and expected number of hip hop songs. TVD does not work because we speciﬁcally care if Hip Hop was higher than expected, not the whole distribution. Moreover, absolute value was incorrect because we care about a direction.

#### (b) (2 pt) Fill in the blank with the best number possible. No need to show your work.

If the null hypothesis was true, we expect our test statistic to be roughly equal to , and any diﬀerence in our sample is just due to random chance.

20% if your answer is percentage of hip hop songs above, or 0 otherwise. Your answer here depends on what you wrote on part a and was graded accordingly. Now, Vinitra decides that she does not care about Fahad’s bias towards Hip-Hop. Instead, she simply does not believe that Fahad truly created his playlist by randomly sampling the 100 songs from the large staﬀlibrary. She does not know how he sampled, but she believes it is not completely random.

- (3 pt) Describe a test statistic that can help pick between the two viewpoints: Fahad sampled the songs

randomly and any diﬀerence is due to chance, or he did not sample the songs randomly from the staﬀ playlist.

The TVD between Fahad’s claimed distribution of music genres and the sample that we obtain.

#### (d) (2 pt) Fill in the blank with the best number possible. No need to show your work.

If the null hypothesis was true, we expect our test statistic to be roughly equal to , and any diﬀerence in our sample is just due to random chance.

0

#### 3. (8 points) You’re Samply Too Mean

The average weights of all people in Berkeley is 146 lb. Through some experimentation, we note that the probability of seeing a sample of 100 people (with replacement) in Berkeley whose average weight is higher than 151 lb is 2.5%.

- (4 pt) Solve for the standard deviation of all weights in Berkeley. Show your work and box your ﬁnal

answer, which may be left unsimpliﬁed.

## Page 5

#### Name: 5

If we have a 2.5% chance of seeing an average sample weight higher than 146 lb, we know that is two stan- dard deviations above the sample average distributions average (which is the population average weight), by the CLT. The SD of the sample means is PopSD / sqrt(Sample Size). In this case, we get that 2 * PopSD / 10 = 5. The PopSD is then 25.

- (4 pt) We would like to reduce the chance of seeing an average weight of a sample (drawn with replace-

ment) that is higher than 151 lb to roughly .15%. Solve for the smallest sample size which would achieve this goal. Show your work and box your ﬁnal answer, which may be left unsimpliﬁed. Assume your answer to Part A is assigned to the variable PopSD and use this variable in your ﬁnal expression, if needed.

For 151 and above to represent .15% of the data, that means 151 is 3 SDs above the sample mean (146). So, we want 5 to be 3 SDs of the sample mean. So, 3 * PopSD / sqrt(SampSize) = 5. Solving for Sample Size, we get (3/5 ∗ PopSD)2

## Page 6

6

#### 4. (6 points) Error Probabilities Probably

A researcher conducts 1000 of the same hypothesis tests (same null, alternative, and test statistic) with diﬀerent samples of observed data from a population. Throughout her hypothesis tests, she uses a p-value cutoﬀof .25.

Suppose the following is a histogram of the p-values recorded during the conclusion for each of the 1000 hypothesis tests. The bin sizes are all a multiple of .05.

![Image extracted from page 6](images/Su18_Final_Sol_page006_image001.png)

- (3 pt) Assume the null hypothesis in these tests happened to be true. If you can tell, did we reject the

null hypothesis more than expected, less than expected, or exactly as many times as we would expect? Explain your answer. If we can not determine with this information, explain why not.

More than expected

Less than expected

Exactly equal to expected

Cannot determine

Explanation: Option 1. With a P-Value cut-oﬀof 25%, we expect to reject 25% of all null hypotheses if they were indeed true. Here, we reject at-least 350 ∗ .05 + 60 ∗ .15 which is greater than 25.

- (3 pt) Assume the alternative hypothesis in these tests happened to be true. If you can tell, did we fail to

reject the null hypothesis more than expected, less than expected, or exactly as many times as we would expect? Explain your answer. If we can not determine with this information, explain why not.

More than expected

Less than expected

Exactly equal to expected

Cannot determine

Explanation: Option 4. We have no information about anything assuming the alternative hypothesis was true because we never simulated anything under the alternative.

## Page 7

#### Name: 7

#### 5. (19 points) Linear Regret-ssion

We are interested in seeing how the Per Capita Income was related with Infant Mortality rate for various countries in the early 1950s. The data is encapsulated in a table named countries, whose ﬁrst few rows are shown below:

![Image extracted from page 7](images/Su18_Final_Sol_page007_image001.png)

We are interested in looking at the relationship between Per Capita Income and Infant Mortality Rate. We plot two lines that we will use to predict infant mortality rate in a country (on average), given a per capita income. One is the regression line, and one is the constant line at the average of infant mortality rate.

![Image extracted from page 7](images/Su18_Final_Sol_page007_image002.png)

Here are some relevant lines of code and their outputs. Assume all of the functions below (descriptions of which appear on your study guide) are deﬁned already.

Expression Output

correlation(countries, 1, 2) -.74 np.mean(countries.column(1)) 534.1 np.mean(countries.column(2)) 52.5 np.std(countries.column(1)) 384.8 np.std(fitted values(countries, 1, 2)) 21.6

## Page 8

8

- (4 pt) If possible, calculate the slope of the regression line in the plot above. Show your work with

arithmetic. Please do not write any Python expressions. Box your ﬁnal answer, which you may leave unsimpliﬁed. If it is not possible, explain why not.

Slope is r times the SD of y over SD of x. We have everything but SD of y. But, we can calculate that using the fact that we have the SD of the ﬁtted values. The SD of the y is then 21.6/.74. We can then calculate for the slope using r ∗ SD(Y )

SD(X) - (2 pt) At what value of per capita income would we predict the infant mortality rate to be 0 given the

regression line on the previous page?

0

52.5

80

534.1

1500

None of the above

Option 5 – based on graph

- (2 pt) At what value of per capita income would we predict the infant mortality rate to be 0 given the

average line on the previous page?

0

52.5

80

534.1

1500

None of the above

Option 6 – based on graph

- (3 pt) Assume the RMSE (root mean squared error) of the regression line is 19.3. If possible, calculate

the RMSE of the constant line representing the average of the infant mortality rate on this data. Show your work with arithmetic. Please do not write any Python expressions. Box your ﬁnal answer, which you may leave unsimpliﬁed. If it is not possible, explain why not.

The RMSE of the average line is actually just the SD of Infant Mortality Rate. We calculate that in Part a as 21.6/.74.

- (3 pt) If possible, ﬁll in the blank with a mathematical expression. Box your ﬁnal answer, which you

may leave unsimpliﬁed. If it is not possible, explain why not.

We use our regression line to estimate infant mortality rate using per capita income. At-least 88.9% of our predictions of infant mortality rate will be correct within plus or minus units. We notice that at least 88.9% points us to three SDs both ways can be answered using Chebyshev’s. We are trying to quantify the error, which is the residuals. So, we look at 3 SDs of the residuals both ways. We

## Page 9

#### Name: 9

1 − (−.742 ∗ SD(Y ). We calculated SD(Y) above, so our ﬁnal answer is 3 ∗ √1 − .74 ∗∗2 ∗ 21.6/.74 We move our attention to only the regression line and we would like to determine whether or not linear regression was a good idea to begin with. We show the regression line plotted on the scatter plot below again for convenience.

p

need to calculate the standard deviation of the residuals, which is

![Image extracted from page 9](images/Su18_Final_Sol_page009_image003.png)

- (2 pt) Which of the following plots is the best approximation to the residual plot, along with the line

y=0?

![Image extracted from page 9](images/Su18_Final_Sol_page009_image004.png)

![Image extracted from page 9](images/Su18_Final_Sol_page009_image005.png)

![Image extracted from page 9](images/Su18_Final_Sol_page009_image001.png)

Option 2

#### (g) (1 pt) What is the approximate average value of the residuals?

-10

0

52.5

534.1

Need more information

Option 2 – Average of the residuals is always 0.

#### (h) (2 pt) Based on the information above, select the most appropriate statement below.

Our residual plot shows no obvious pattern, so linear regression is a good ﬁt for this data.

Our residual plot shows a deﬁnitive pattern, but based on our original plot, linear regression is still a good ﬁt for this data.

## Page 10

10

Our residual plot shows a linearly decreasing trend, so linear regression is not a good ﬁt for this data.

Our residual plot shows a deﬁnitive pattern, so linear regression is not a good ﬁt for this data.

None of the above

Option 4 – a pattern is present, but it is not decreasing linearly. It goes down, then comes back up. Since there is pattern in the residual plot, linear regression is not a good idea.

## Page 11

#### Name: 11

#### 6. (18 points) HA/Biness Among Countries

We are interesting in studying the distribution of human happiness across the world. To do so, we have a table called happiness. The table has 140 rows, and the ﬁrst few rows are shown below:

![Image extracted from page 11](images/Su18_Final_Sol_page011_image001.png)

Each row contains the region and happiness score for a sampled country. The countries are not shown in the table above. Throughout this question, our goal will be to measure if the distribution of happiness scores across regions in the whole world are roughly equivalent.

#### (a) (2 pt) Deﬁne a function region happiness which takes in a table like happiness and returns a two

column table. The output table should have one column with the names of the unique regions, and a second column with the average happiness score in that region. The ﬁrst few rows of an output table are shown below, with one row for each unique region. Note that the input table may not have the same labels as happiness, but will have the same ordering of columns.

![Image extracted from page 11](images/Su18_Final_Sol_page011_image002.png)

def region_happiness(tbl):

return ____________________________________________________________________________ def region_happiness(tbl):

return tbl.group(0, np.average) We are in an abnormal situation, in which we have 10 diﬀerent regions and we are interested in ﬁguring out if the numerical distributions of all of the regions happiness scores are roughly equivalent. To do this, we will use a variant of A/B testing called multivariate testing. The only diﬀerence between the two methods is we have more than two groups (in this case, 10), and we are comparing the numerical distributions of all of these groups at the same time.

The important thing to notice is that our null hypothesis and alternative hypotheses retain the same structure as they have for A/B testing, as well as our method for simulating a sample under the null. The only diﬀerence will be the test statistic we decide to use to diﬀerentiate between our two viewpoints.

We are interested in testing if the distributions of happiness scores of all the regions come from the

## Page 12

12

same underlying population distribution or not using our sample we have above.

## Page 13

#### Name: 13

- (4 pt) Describe a speciﬁc null and alternative hypothesis that will help us pick between the two viewpoints

presented above.

#### Null:

#### Alternative:

Null: The distributions of happiness scores for all regions are sampled from the same population dis- tribution. Any diﬀerence in our sample is due to chance. Alternative: The distributions of happiness scores for all regions do not come from the same population distribution.

- (2 pt) To help us diﬀerentiate between our two hypotheses, we need to choose a test statistic. Choose

the best test statistic and corresponding explanation.

We should choose the TVD between the average happiness of each region and the expected average happiness of each region as our test statistic because only small values of our test statistic will point to the alternative hypothesis.

We should choose the TVD between the average happiness of each region and the expected average happiness of each region as our test statistic because only large values of our test statistic will point to the null hypothesis.

We should choose the standard deviation of the average happiness per region as our test statistic because only large values of our test statistic will point to the alternative hypothesis.

We should choose the standard deviation of the average happiness per region as our test statistic because only small values of our test statistic will point to the alternative hypothesis.

We should choose the median of the average happiness per region as our test statistic because only large values of our test statistic will point to the alternative hypothesis.

Option 3 – standard deviation ﬁnds the overall variation from the average. If the null was true, each av- erage human happiness score would be close to each other so our standard deviation would be low. If the alternative was true, the averages happiness will be further apart, and result in a large standard deviation.

TVD does notwork because we do not have any expected distribution of happiness scores. If the op- tion talked about proportions of of happiness, then that would work, but notice that if you try to code some expected distribution of happiness score in the next question, you would be at an impass.

- (2 pt) Deﬁne a function test statistic which takes in a table like happiness and returns the test

statistic you chose from the last question. Note that the input table will not have the same labels, but will have the same ordering of columns. You may use your region happiness function from above and assume it is fully correct.

def test_statistic(tbl):

regions = _________________________________________________________________________

return ___________________________________________________________________________ def test_statistic(tbl):

regions = region_happiness(tbl)

return np.std(regions.column(1))

## Page 14

14

- (3 pt) Complete the deﬁnition of sample under null, which takes in no arguments and returns one value

of the test statistic applied to a random sample simulated under the null hypothesis. You may use your test statistic function from above and assume it is fully correct.

def sample_under_null():

shuffled_hap = happiness.______________________________________________________________

r_and_h = Table().with_column(________________________________________________________)

return _________________________________________________________________________________

def sample_under_null():

shuffled_hap = happiness.sample(with_replacement = False).column(‘Happiness Score’)

r_and_h = Table().with_column(’Shuffled’, shuffled_hap, ’Labels’, ’Region’, happiness.column(’Regi

return test_statistic(region_and_happiness)

- (3 pt) We would now like to simulate 1000 test statistics under the null hypothesis. Complete the code

below to assign simulated stats to 1000 values of test statistics applied to diﬀerent samples simulated under the null hypothesis. You may use your sample under null function from above and assume it is fully correct.

simulated_stats = ________________________________________________________

for i in np.arange(1000):

stat = __________________________________________________________________________________

simulated_stats = ________________________________________________________________________

simulated_stats = make_array()

for i in np.arange(1000):

stat = sample_under_null()

simulated_stats = np.append(simulated_stats, stat) The following is a histogram of the simulated test statistics, and the dot (on the right) is the value of your calculated test statistic on the original observed data from the sample.

![Image extracted from page 14](images/Su18_Final_Sol_page014_image001.png)

#### (g) (2 pt) Select the best conclusion from the options below:

Our data is more consistent with the null hypothesis.

## Page 15

#### Name: 15

Our data is more consistent with the alternative hypothesis.

It is impossible to decide given just the histogram above.

Option 2

#### 7. (8 points) You Studied for these Studies

- (2 pt) A medical observational study ﬁnds a high positive association between drinking coﬀee and hav-

ing lung cancer in a group of individuals. Which of the following statements, if true, could present a confounding factor to the study? Choose the best answer.

There is a strong positive association between having lung cancer and drinking coﬀee in this group.

There is a strong positive association between drinking coﬀee and smoking in this group.

There is a no association between smoking and having lung cancer in this group.

All of the above

None of the above

Option 2

- (2 pt) Researchers decide to test their new disease treatment equipment against their older equipment.

However, their new disease equipment requires patients remain hydrated. Researchers select a group of 300 patients for this study; some of the participants will use the new equipment, while the others will use the old equipment. Mark all of the following options which would help control for confounding factors in this study.

Requiring patients who are treated with the older equipment remain hydrated.

Requiring patients who are treated with the newer equipment remain dehydrated.

Assigning patients to groups at random.

Assigning diﬀerent amounts of water randomly to individuals in both groups.

None of the above

Option 1 and 3

- (4 pt) A local store is the only umbrella store in a large radius. They decide to test whether or not

the quality of their umbrellas impacts their yearly sales. In 2016, their umbrellas were of a very high quality and they sold 1,500 umbrellas. In 2017, their umbrellas were of average quality and they sold 1,000 umbrellas.

The store is tempted to explain this phenomenon by claiming that a higher quality of umbrellas causes more sales. As data scientists, however, we are more hesitant to come to this conclusion. Give two diﬀerent speciﬁc alternative explanations that could explain the results of the experiment above. You may not simply claim that this is an observational study.

1.

2.

## Page 16

16

Two reasons include: 1. It didn’t rain as much in 2017. No need to buy umbrellas 1. People who bought their umbrellas in 2016 didn’t need a new one for 2017, so they didn’t buy again in 2017. Many options were accepted, if they didn’t mention observational study and were speciﬁc; We enjoyed the creativity!

#### 8. (8 points) P-Value Puzzle

Deﬁne the function p value calculation, which takes in the following 3 arguments:

- sim vals is an array of simulated test statistics under a speciﬁc null hypothesis.

- observed ts is the value of a test statistic from a speciﬁc observed sample.

- larger alt is a boolean which is either True if only large values of the test statistic above point towards the alternative, and False otherwise (small values of the test statistic point towards the alternative).

The function should calculate the P-Value of the observed ts (observed statistic), with respect to the null hypothesis under which sim vals was simulated. You may not need all of the lines.

def p_value_calculation(sim_vals, observed_ts, larger_alt):

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

________________________________________________________________________________

def p_value_calculation(sim_vals, observed_ts, larger_alt): if larger_alt:

return sum(sim_vals >= observed_ts) / len(sim_vals)

else:

return sum(sim_vals <= observed_ts) / len(sim_vals)

## Page 17

#### Name: 17

#### 9. (6 points) Minimize That!

- (2 pt) Assume we have a table, tbl, which has two columns. We also have a function which takes in two

numbers that represent column indices, and returns the negative of the correlation between the two columns speciﬁed by the indices in tbl. The ﬁrst number passed in to the function is the column index for x, and the second number passed in is the column index for y. Assume the correlation between the two columns in tbl is .7. If multiple arguments minimize a function, minimize randomly chooses one. Which of the following could be the result of calling minimize on our function above?

array([0,1])

array([1,0])

Both of the above.

None of the above.

Cannot tell with this information.

Option 4 – array([0,0]), and array([1,1]) would have resulted in a correlation of 1, which results in the function returning -1. Since the function returns negative of correlation, this is the smallest value possible.

- (4 pt) We are interested in using minimize to ﬁnd the column with the smallest element in a table tbl2.

Assume tbl2 only contains numbers. Deﬁne a function minimized fn which, when passed in to minimize, gives the column index (number) of the column which contains the smallest element in the table. You may not need all of the lines provided below. Afterwards, use your new function to assign smallest to the smallest entry in tbl2.

def minimized_fn(_____________________________________):

_______________________________________________________________________________

_______________________________________________________________________________

smallest = ___________________________________________________________________________

def minimized_fn(index)

return min(tbl2.column(index))

smallest = min(tbl2.column(minimize(minimized_fn)))

Minimize expects a function, and returns the arguments of the function which minimize it. The arguments to the function must be numerical. Taking in a table wouldn’t make sense.

#### 10. (16 points) Conﬁdence in Crime

In 1968, the United States Census Bureau took a large random sample of metropolitan areas and measured their crime rates, measured in proportion per 100,000. The information is encapsulated in a one column table called crimes.

## Page 18

18

- (2 pt) Which of the following pieces of information can we determine given the sample? Mark all that

#### apply.

The average crime rate in all metropolitan areas in the US in 1968.

The approximate distribution of crime rates in metropolitan areas in the US in 1968.

The range of crime rates in all metropolitan areas in the US in 1968.

None of the above Option 2 Assume we bootstrap our sample many times to get an approximate 90% conﬁdence interval for the av- erage crime rate of the population. The resulting interval is (0.0256, 0.0287).

- (2 pt) What is the probability that the true average crime rate in the population lies in this interval?

100%

0%

90%

95%

None of the above

Option 5, or writing both 100% or 0% - (2 pt) True or False: Approximately 90% of the population crime rates lie between .0256 and .0286.

True

False

Option 2 – Only looking at averages. - (2 pt) True or False: Approximately 90% of the sample crime rates lie between .0256 and .0286.

True

False

Option 2 – Only looking at averages - (3 pt) Suppose the Census Bureau went out and actually sampled two times as many metropolitan areas,

so our sample became larger. Would our 90% conﬁdence interval we calculate using the new data be larger, smaller, around the same size as our original interval, or can we not tell?

Larger

Smaller

Same size

Cannot determine

Option 2 – Sample Size has gotten larger, so by CLT, our width of our conﬁdence interval will becomes- maller - (3 pt) Assume we want to test the hypothesis that the average population crime rate is .03, with our al-

ternative being that it’s not. Give an interval of p-value cutoﬀs such that we can reject the null hypothesis that the average population crime rate is .03 given our conﬁdence interval above. Explain your answer. Your range should be contained within the interval [0,1].

[.1,1]. We know that any conﬁdence interval of conﬁdence less than 90% is contained in the interval we created, so they would reject the null in all of these scenarios. If we increase the conﬁdence, our interval gets larger, and we don’t know, then, if our interval will contain .03.

## Page 19

#### Name: 19

- (2 pt) Suppose we repeat the process of creating 90% conﬁdence intervals many times using diﬀerent

samples from the population each time, with the hope of approximately 2,700 intervals containing the true population average crime rate. How many conﬁdence intervals should we create?

900

2,430

2,700

2,850

3,000

3,300

None of the above

Option 5 – 3000*.9 = 2700, so we should make 3000 CIs.

## Page 20

20

#### 11. (7 points) K-Nearest Bobas

Tawainese Pearl Milk Tea (also known as boba) is a very common drink on the Berkeley campus. The two main concentrations of boba cafes are on Southside and Downtown Berkeley. Your friend is a Berkeley boba expert. He says that two useful features for classifying boba are the amount of sugar (y-axis) and the amount of money (x-axis) for a standard black milk tea with pearls. He identiﬁes several boba places for you, but leaves one unknown boba cafe for you to classify, because he hasn’t tried it yet. No two boba places have exactly the same features.

You decide to construct a classiﬁer for the unknown boba cafe using all of the known boba cafes as the training set. Note that the x and y axes have diﬀerent scales.

![Image extracted from page 20](images/Su18_Final_Sol_page020_image001.jpeg)

#### (a) (1 pt) The prediction scheme outlined above is a unsupervised machine learning algorithm.

True

False

Cannot determine

False. Classiﬁcation is a supervised machine learning algorithm.

#### (b) (1 pt) Using a 5-nearest neighbor classiﬁer, what would the unknown boba cafe be classiﬁed as?

Southside

Downtown

Cannot determine

Southside – 3 southside, 2 downtown

- (3 pt) What is the problem with using a 4-nearest neighbor classiﬁer for our unknown boba cafe? Provide

one possible solution to this problem.

It would tie with 2 southside, 2 downtown and then we would need to have a tie breaking scheme Any valid tie breaking scheme is accepted – one could be to choose the class of the point closest, or look at k+1 nearest neighbors when we tie.

- (2 pt) Every possible pair of feature values for a new boba cafe would be classiﬁed as Southside for a

11-nearest neighbor classiﬁer using this training set.

True

## Page 21

#### Name: 21

False

Cannot determine

True. The majority vote will always be southside.

## Page 22

22

#### 12. (0 points) (Optional) Data Visualization!

Draw a data visualization about Data 8.

Enjoyed the creativity! Check your rubric to see which staﬀmembers enjoyed your drawings!
