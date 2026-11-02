# Discussion 02 Data C8 Spring 2026

## Page 1

## Intro to Tables & Causation

Discussion 02

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Warmup

A study followed 369 people with cardiovascular disease, randomly selected from all hospital patients with cardiovascular disease. A year later, those who owned a dog were four times more likely to be alive than those who did not. For all of the following questions, please provide a brief explanation. (Spring 2017 Practice Midterm Question 3b)

#### (a) True or False. This study is a randomized controlled experiment.

False. The researchers did not randomly assign individuals to a treatment group (having a dog) and a control group (not having a dog). The experimenters had no control over who owned a dog.

#### (b) True or False. This study shows that dog owners live longer than cat owners on average.

False. The experiment compares those who owned a dog to those who didn’t (not specifically cat owners). Also, the experiment only involves people with cardiovascular disease, not all people.

- True or False. This study shows that for someone with cardiovascular disease, adopting a dog causes them to live longer.

False. An observational study does not imply causation. There may be confounding factors that contribute to the correlation between adopting a dog and living longer.

### 2. Fun with Arrays

Suppose we have executed the following lines of code. Answer each question with the appropriate output associated with each line of code, or write ERROR if you think the operation is not possible.

odd = make_array(1, 3, 5, 7) even = np.arange(2, 10, 2) nums = make_array('1', '2', '3', '4')

#### (a) odd + even

array([3, 7, 11, 15])

#### (b) odd + nums

ERROR. Arrays can only be added together if they have the same size, and are of similar data types (i.e. ints and floats). In this case, one array contains integers and the other contains strings, so the operation is invalid.

#### (c) even.item(3) * odd.item(1)

24

#### (d) odd * 3

array([3, 9, 15, 21])

#### (e) odd + 1 == even

array([True, True, True, True]). Remember array operations are performed element-wise, including comparison operators.

#### (f) nums.item(3) + '0'

## Page 2

'40'

- sum(odd > 4) Hint: Boolean values of True and False are equivalent to integer values of 1 and 0 respectively.

1. This computes the number of elements in odd that are strictly greater than 4.

#### (h) sum(odd > 4) / len(odd > 4). What does this output represent? Discuss with peers.

0.5. This computes the proportion of values strictly greater than 4! It is equivalent to np.mean(odd > 4). We will revisit this during the hypothesis testing topic.

#### (i) odd + make_array(True, True, False, False)

array([2, 4, 5, 7]). Boolean values of True and False are equivalent to integer values of 1 and 0 respectively.

### 3. Rise and Shine

Tables are a fundamental way of representing data. A table can be viewed in two ways:

- A sequence of named columns that each describe a single attribute of all entries in a data set, or
- A sequence of rows where each row contains all the attribute information about that entry in the data set

Data 8 uses a library consisting of many Table functions that will allow you to manipulate and visualize data. All of the functions we will use in this course are listed on the Data 8 website under Python Reference, and a similar reference sheet will be provided during exams.

In this question, let’s look at an example table called weather. The table has 8 rows, each corresponding to a day of the year. Each row has three attributes: the date, the outdoor temperature in Celsius, and the number of students at lecture that day.

![Eight-row table of dates, outdoor temperatures, and lecture attendance. Values span June 21–30, 26–36°C, and 370–435 students; June 21 has the highest attendance at 435.](images/disc02-sol_page002_vector001.png)

#### Date Outdoor Temp. (Celsius) Students at Lecture

June 21 28 435

June 22 30 417

June 23 34 394

June 24 36 398

June 27 34 410

June 28 26 385

June 29 26 370

June 30 28 373

- Using just the information provided in the weather table, can you generate the following tables and visualizations? If not,

what additional information do you need? Note: You do not need to know/write the specifics of the code that you would use to generate these outputs.

![Table and scatter plot compare outdoor temperature with lecture attendance. Mean attendance rises from 377.5 at 26°C to 417 at 30°C, then falls to 398 at 36°C; individual points vary widely at 26–34°C.](images/disc02-sol_page002_image001.png)

Data C8 Spring 2026 Discussion 02 | 2

## Page 3

Yes / No Yes/No

Yes, Yes.

- Miriam likes using Fahrenheit more than Celsius. Suppose that she has access to a function called fahrenheit that takes

in a number (temperature in Celsius) and returns the temperature in Fahrenheit.

#### i. Write an expression that evaluates to 30°C in Fahrenheit. Hint: which function can we use?

fahrenheit(30)

#### ii. What will fahrenheit("thirty") output?

ERROR. fahrenheit takes in a number, so we should only pass numbers into the function. Passing in something that is not a number will result in an error.

iii. Miriam assigns a variable temperature to the number 25. What will fahrenheit(temperature * 2) output?

The Fahrenheit value for 50°C, 122°F.

Data C8 Spring 2026 Discussion 02 | 3

## Page 4

### 4. Made with ♡ & Coffee

Carisma collected the following information about her coworkers’ methods of getting to work and their coffee consumption. The data is stored in a table called coworkers:

![Five-row table listing student name, travel method, and average cups of coffee. Drivers range from 1.5 to 2.3 cups, while bus riders average 0.8 and 1.2 cups.](images/disc02-sol_page004_vector001.png)

#### Name Method Average Cups of Coffee

Dagny drive 2.3

Marissa drive 1.5

Isaac bus 0.8

Tiffany drive 1.8

Wesley bus 1.2

... (60 rows omitted)

The table contains three columns: - Name (string): The name of the coworker. - Method (string): The coworker’s way of commuting to work. - Average Cups of Coffee (float): The average number of cups of coffee consumed per day by the coworker.

#### (a) Help Carisma analyze her coworkers’ coffee consumption habits by creating the following tables.

- Carisma wants to focus on her coworkers who commute by driving to work. Create a table titled drivers that only

includes coworkers who drive to work.

drivers = __________________.__________________(_______________________, _______________________)

drivers = coworkers.where("Method", "drive")

ii. Carisma wants to see which of her coworkers consume the most coffee. Create a table titled consumption that organizes

her coworkers from the highest average cups of coffee per day to the lowest.

consumption = _________________._________________(______________________, ______________________)

consumption = coworkers.sort("Average Cups of Coffee", descending=True)

iii. Carisma decides she only wants to focus on her coworkers’ average coffee consumption and method of commuting to

work. Create a table titled coffee_and_commute that includes only the Average Cups of Coffee and Method columns in that order.

coffee_and_commute = _________________._________________(_______________________________________)

coffee_and_commute = coworkers.select("Average Cups of Coffee", "Method")

- Carisma wants to determine whether she is spending more money on coffee compared to boba over the course of 1 semester

(15 weeks long). Assume she purchases 4 coffees and 3 bobas per week. Complete the following lines of code, which should assign result to True if Carisma spends strictly more on coffee and False otherwise.

cost_coffee = 6.0 cost_boba = 7.0

total_coffee = ______________ * ______ * ______

total_boba = ________________ * ______ * ______

result = ______________________________________

Data C8 Spring 2026 Discussion 02 | 4

## Page 5

cost_coffee = 6.0 cost_boba = 7.0 total_coffee = cost_coffee * 4 * 15 total_boba = cost_boba * 3 * 15 result = total_coffee > total_boba

#### Data C8 Spring 2026 Discussion 02 | 5
