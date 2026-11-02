# Discussion 04 Data C8 Spring 2026

## Page 1

## More Visualizations, Intro to Functions

Discussion 04

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Rents & Ranges

The table below shows the distribution of rents paid by students in Boston. The first column consists of ranges of monthly rent, in dollars. Ranges include the lower bound but not the upper bound. The second column shows the percentage of students who pay rent in each of the ranges.

![Four-bin table of dollar ranges and student percentages, with an empty Bar Height column. Percentages are 15% for $500–800, 25% for $800–1,000, 40% for $1,000–1,200, and 20% for $1,200–1,600.](images/disc04_page001_vector001.png)

#### Dollars Students (%) Bar Height

500 −800 15

800 −1000 25

1000 −1200 40

1200 −1600 20

![Reference panel explains histogram bins and the area principle: intervals generally include the lower bound but exclude the upper, and each bar's area equals its data percentage, calculated as bin width times height.](images/disc04_page001_vector002.png)

Bins: We use bins to group the numerical variable into intervals. They are inclusive of their lower bounds but exclusive of their upper bounds, which are often expressed as [lower, upper). The rightmost bin is inclusive of both endpoints, and its bounds can be expressed as [lower, upper].

Area Principle: The area of a bin is equal to the percentage of data in the bin. The larger the area, the more data lies in that bin.

area of a bar = % of values in a bin = width of the bin × height of the bin

- Calculate the heights of the bars for the bins listed in the table, with correct units. Recall the Area Principle.

#### (b) Draw a histogram of the data. Make sure you label your axes!

## Page 2

#### (c) Based on the information that we have, can we create the following bins? Explain your answer.

#### i. [500, 1000)

#### ii. [500, 650)

#### iii. [800, 1200)

- True or False: If we combine the [500, 800) and [800, 1000) bins together, the height of the new bin would be greater than

the heights of both of the old bins. Please explain your answer and verify it by calculating the height of the new bin.

Data C8 Spring 2026 Discussion 04 | 2

## Page 3

### 2. Fun(ctions)

- After learning about them in Data 8, Max wants to write a function that can calculate the hypotenuse of any right triangle.

He wants to use his function to assign C to the hypotenuse of a right triangle with legs (sides adjacent to the hypotenuse) A and B. However, he’s made many mistakes. Which ones can you identify?

Hint: There are 5 unique issues. Assume that numpy has been imported as np.

def hypotenuse(a, b) squares = make_array(side1, side2) * 2 sum = sum(squares) squareroot = np.sqrt(sum) print(squareroot)

C = hypotenuse(A, B) # C should be the numerical result

#### (b) Write a function that takes in the following arguments:

- tbl: a table.
- col: a string, name of a column in tbl.
- n: an int.

The function should return a table that contains the rows that have the 𝑛 largest values for the specified column.

def top_n(tbl, col, n):

sorted_tbl = __________________________________________________ top_n_rows = __________________________________________________ return ________________________________________________________

Data C8 Spring 2026 Discussion 04 | 3

## Page 4

### 3. Sheng Kee Fridays

Dagny’s favorite activity to celebrate Fridays is buying pastries at Sheng Kee before class. She stores her purchase data in a table,

pastries, to keep track of her spending. Assume she never purchases the same item twice. Each row represents an individual purchase. The first few rows look like this:

![Five-row bakery table with item, sweet or savory category, price, and satisfaction. Prices range from $2.45 to $3.15; Summer Romance has the highest satisfaction at 10.](images/disc04_page004_vector001.png)

#### item category price satisfaction

Hot Dog Bun Savory 2.75 8.5

Yudane Milk Bun Sweet 2.99 9

Summer Romance Sweet 2.79 10

Pineapple Bun Sweet 2.45 7.75

Ham and Cheese Croissant Savory 3.15 7.25

The table has 4 columns:

- item (string): name of the pastry.
- category (string): whether the pastry is sweet or savory.
- price (float): price of the pastry.
- satisfaction (float): how satisfied (out of 10) Dagny was after eating the pastry.

- Write a line of code to calculate the average satisfaction Dagny felt after eating sweet pastries.

_________________(pastries.______________(____________________________________).column(________________))

- Dagny is curious if the average price for savory pastries is higher than the average price for sweet pastries. Write a line of

code that will output the category that is more expensive.

pastries.__________________(____________________, ____________________)

.sort(___________________________, ___________________________) .column(_________________________________________).item(______)

- Dagny’s budget is getting tight, and she wants to buy pastries that will give her the most satisfaction per dollar. Write lines

of code that will help us achieve this.

- First, create an array that contains each purchase’s satisfaction per dollar. Then, add a new column called “satisfaction

per $”, to the pastries table.

score_array = pastries.____________(__________________) / pastries._____________(__________________)

pastries = ____________.with_column(__________________________, ___________________________________)

ii. Dagny defines a function score that takes in satisfaction and price (in that order) and returns the satisfaction per dollar.

Find a different way to compute score_array.

score_array = pastries._________________(__________________, __________________, __________________)

iii. Dagny is interested in finding the pastries in the table with the top 3 satisfaction values per dollar. Write code that will

output the names of these items as an array.

pastries_sorted = pastries.__________(_____________________________________, ______________________)

pastries_sorted.__________(______________________________________________).column(_________________)

Data C8 Spring 2026 Discussion 04 | 4

## Page 5

### 4. Insurance (Optional)

The table insurance contains one row for each beneficiary that is covered by a particular insurance company:

![Three-row insurance table with age, BMI, smoker status, region, and cost. The 25-year-old smoker with BMI 30.2 has by far the highest cost, $33,900.71, versus $3,208.79 and $1,355.50 for nonsmokers.](images/disc04_page005_vector001.png)

#### age bmi smoker region cost

25 20.8 no southwest 3208.79

25 30.2 yes southwest 33900.71

62 32.1 no northeast 1355.50

... (20198 rows omitted)

The table contains five columns:

- age (int): the age of the beneficiary.
- bmi (float): the Body Mass Index (BMI) of the beneficiary.
- smoker (string): indicates whether the beneficiary smokes.
- region (string): the region of the United States where the beneficiary lives.
- cost (float): the total amount in medical costs that the insurance company paid for this beneficiary last year.

(Fall 2018 Midterm Question 2 Modified)

In each part below, fill in the blanks to achieve the desired outputs.

- A scatter plot comparing the amount paid last year vs. BMI (titles are usually written as Y vs. X) for only the beneficiaries

whose costs exceeded $25,000. Each dot on the scatter plot should represent one beneficiary.

high_cost = __________________.____________(_____________, ____________________________________________)

__________.______________________(__________________________________, _________________________________)

- Write a function that takes an age as an argument, and returns the average BMI among all beneficiaries of that age.

def average_bmi(age):

right_age = insurance.where(________________, ________________) bmis = right_age._______________(______________) avg = sum(bmis) / len(bmis) _____________________________________

Data C8 Spring 2026 Discussion 04 | 5
