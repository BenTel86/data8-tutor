---
title: "Project 1: World Population and Poverty"
assignment: project1
semester: sp26
source: semester_assignments/sp26/project/project1/autograder/project1.ipynb
version: solution (autograder) with student scaffolds
student_source: semester_assignments/sp26/project/project1/student/project1.ipynb
total_points: 65
language: python
---

![Data 8 Logo](project1_assets/data8logo.png)

# Project 1: World Population and Poverty

In this project, you'll explore data from [Gapminder.org](http://gapminder.org), a website dedicated to providing a fact-based view of the world and how it has changed. That site includes several data visualizations and presentations, but also publishes the raw data that we will use in this project to recreate and extend some of their most famous visualizations.

The Gapminder website collects data from many sources and compiles them into tables that describe many countries around the world. All of the data they aggregate are published in the [Systema Globalis](https://github.com/open-numbers/ddf--gapminder--systema_globalis/blob/master/README.md). Their goal is "to compile all public statistics; Social, Economic and Environmental; into a comparable total dataset." All data sets in this project are copied directly from the Systema Globalis without any changes.

This project is dedicated to [Hans Rosling](https://en.wikipedia.org/wiki/Hans_Rosling) (1948-2017), who championed the use of data to understand and prioritize global development challenges.

### Logistics

**Deadline.**  This project is due at **5:00pm PT on Friday 2/27**. Projects will be accepted up to 1 day (24 hours) late. Projects submitted fewer than 24 hours after the deadline will receive 80% credit. It's **much** better to be early than late, so start working now.

**Checkpoint.**  For full credit on the checkpoint, you must complete the questions up to the checkpoint, **pass all _public_ autograder tests** for those sections, and submit to the Pensive Project 1 Checkpoint assignment by **5:00pm PT on Friday, 2/20**. <span style="color: #BC412B">**The checkpoint is worth 1 lab score**</span>. After you've submitted the checkpoint, you may still change your project answers before the final project deadline - only your final submission, to the "Project 1" assignment, will be graded for correctness. You will have some lab time to work on these questions, but we recommend that you start the project before lab and leave time to finish the checkpoint afterward. Additionally, the second half of the project is longer than the first, so if you have time, we encourage you to continue working past the checkpoint.

**Partners.** You may work with one other partner; your partner must be from your assigned lab section. **<span style="color: #BC412B">Only one partner should submit the project notebook to Pensive.</span> If both partners submit, you will be docked 10% of your project grade. On Pensive, the person who submits should also designate their partner so that both of you receive credit.** Once you submit, click into your submission, and there will be an option to Add Group Member in the top right corner. You may also reference [this walkthrough video](https://drive.google.com/file/d/1bs1l_f44tUeF1yKY_iljZMTE1X0dYKLl/view?usp=sharing) on how to add partners on Pensive.


**Rules.** Don't share your code with anybody but your partner. You are welcome to discuss questions with other students, but don't share the answers. The experience of solving the problems in this project will prepare you for exams (and life). If someone asks you for the answer, resist! Instead, you can demonstrate how you would solve a similar problem.

**Support.** You are not alone! Come to office hours, post on Ed, and talk to your classmates. If you want to ask about the details of your solution to a problem, make a private Ed post and the staff will respond. If you're ever feeling overwhelmed or don't know how to make progress, email your TA or tutor for help. You can find contact information for the staff on the [course website](https://www.data8.org/su26/).

**Tests.** <span style="color: #BC412B">The tests that are given are **not comprehensive** and passing the tests for a question **does not** mean that you answered the question correctly.</span> Tests usually only check that your table has the correct column labels. However, more tests will be applied to verify the correctness of your submission in order to assign your final score, so be careful and check your work! You might want to create your own checks along the way to see if your answers make sense. Additionally, before you submit, make sure that none of your cells take a very long time to run (several minutes).

**Free Response Questions:** Make sure that you put the answers to the written questions in the indicated cell we provide. **Every free response question should include an explanation** that adequately answers the question.

**Tabular Thinking Guide:** Feel free to reference [Tabular Thinking Guide](https://drive.google.com/file/d/1NvbBECCBdI0Ku380oPcTUOcpjH3RI230/view) for extra guidance.

**Advice.** Develop your answers incrementally. To perform a complicated table manipulation, break it up into steps, perform each step on a different line, give a new name to each result, and check that each intermediate result is what you expect. You can add any additional names or functions you want to the provided cells. Make sure that you are using distinct and meaningful variable names throughout the notebook. Along that line, **DO NOT** reuse the variable names that we use when we grade your answers. For example, in Question 1 of the Global Poverty section we ask you to assign an answer to `latest`. Do not reassign the variable name `latest` to anything else in your notebook, otherwise there is the chance that our tests grade against what `latest` was reassigned to.

You are **never** restricted to using only one line of code to solve a question in this project or any others. Feel free to use intermediate variables and multiple lines as much as you would like!

---

The point breakdown for this assignment is given in the table below:
| Category | Points |
| --- | --- |
| Autograder (Coding questions) | 65 |
| Written | 35 |
| **Total** | 100 |

---

To get started, load `datascience`, `numpy`, `plots`, and `otter`.

**Code:**

```python
# Run this cell to set up the notebook, but please don't change it. 

# These lines import the NumPy and Datascience modules.
from datascience import *
import numpy as np

# These lines do some fancy plotting magic.
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
```

---
## 0. Hazards with `.show`

As a heads up, please do not run the function `tbl.show()` in this assignment without an argument. For instance if you want to view a table, please type `tbl.show(10)` instead of `tbl.show()`. This may break your notebook and we cannot guarantee that we will have the capacity to aid you in this. Please answer the question below, and set the value to `True` to confirm you have read this and agree.

**Student scaffold:**

```python
i_wont_use_show_without_an_argument = ...
```

**Solution:**

```python
i_wont_use_show_without_an_argument = True # SOLUTION
```

**Test — `q0` (0 points)**

```python
>>> i_wont_use_show_without_an_argument == True
True
```

---
## 1. Global Population Growth

The global population of humans reached 1 billion around 1800, 3 billion around 1960, 7 billion around 2011, and 8 billion around 2022. The potential impact of population growth has concerned scientists, economists, and politicians alike.

The United Nations Population Division estimates that the world population will likely continue to grow throughout the 21st century, but at a slower rate, perhaps reaching and stabilizing at 10 billion by 2100. However, the UN does not rule out scenarios of slower or more extreme growth. These projections help us understand long-term population processes, even if they leave out possible global catastrophic events like war or climate crises.

<a href="https://population.un.org/wpp/Graphs/Probabilistic/POP/TOT/900"> 
 ![UN line chart titled 'World: Total Population', population in billions from 1950 to 2100. A black observed curve rises from about 2.5 billion in 1950 to about 8 billion in 2022, then projections fan out: a red median curve peaking near 10.3 billion around 2080 and easing to about 10.2 billion by 2100, with 80% and 95% prediction intervals, 60 sample trajectories, and a +/- 0.5 child scenario band spanning roughly 6.3 to 14 billion by 2100. Source: UN DESA Population Division, World Population Prospects 2024.](project1_assets/un_population_projection.png) 
</a>

In this part of the project, we will examine some of the factors that influence population growth and how they have been changing over the years and around the world. There are two main sub-parts of this analysis.

- First, we will examine the data for one country, Poland. We will see how factors such as life expectancy, fertility rate, and child mortality have changed over time in Poland, and how they are related to the rate of population growth.
- Next, we will examine whether the changes we have observed for Poland are particular to that country or whether they reflect general patterns observable in other countries too. We will study aspects of world population growth and see how they have been changing.

The first table we will consider contains the total population of each country over time. Run the cell below.

**Code:**

```python
population = Table.read_table('population.csv').where("time", are.below(2026))
population.show(3)
```

*Output:*

| geo | time | population_total |
| --- | --- | --- |
| afg | 1800 | 3280000 |
| afg | 1801 | 3280000 |
| afg | 1802 | 3280000 |

**Note:** The population data can also be found [here](https://www.gapminder.org/data/documentation/gd003/).

### Poland

The Central European nation of Poland has undergone many changes over the centuries. In modern times it was (re)created as a democratic republic in 1919 after World War I. It was invaded and divided in World War II between Germany and the Soviet Union. War and the Holocaust had a devastating impact on its people. Poland was constituted in its current borders at the end of World War II (1945) under a communist government. In 1989, with the fall of the Soviet Union, Poland re-established itself as a democratic republic.

In this section of the project, we will examine aspects of the population of Poland since 1900. Poland's borders have changed, so we will look at the population within its current (2025) borders.

In the `population` table, the `geo` column contains three-letter codes established by the [International Organization for Standardization](https://en.wikipedia.org/wiki/International_Organization_for_Standardization) (ISO) in the [Alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Current_codes) standard. **Use the Alpha-3 link to find the 3-letter code for Poland.**

---

**Question 1.1.** Using the `population` table, create a table called `p_pop` for **Poland's population data since 1900**. It should have two columns labeled `time` and `population_total`. The first column should contain the years from 1900 through 2025 (including both 1900 and 2025) and the second column should contain the population of **Poland** in each of those years. **(5 points)**

**Student scaffold:**

```python
p_pop = ...
p_pop
```

**Solution:**

```python
p_pop = population.where('geo', 'pol').where('time', are.between(1900, 2026)).drop('geo') # SOLUTION
p_pop
```

*Output:*

| time | population_total |
| --- | --- |
| 1900 | 24308265 |
| 1901 | 24485193 |
| 1902 | 24660489 |
| 1903 | 24834119 |
| 1904 | 25008969 |
| 1905 | 25185047 |
| 1906 | 25362361 |
| 1907 | 25540920 |
| 1908 | 25720733 |
| 1909 | 25808244 |

**Test — `q1_1` (5 points)**

```python
>>> p_pop.labels == ('time', 'population_total')
True

>>> all(p_pop.sort('time').column('time') == np.arange(1900, 2026))
True

# hidden test
>>> p_pop.sort('time', descending=True).column('population_total').item(0)
38140910

# hidden test
>>> p_pop.sort('time').column('population_total').item(0)
24308265
```

Run the following cell to create a table called `p_five` that has the population of Poland every five years.

**Code:**

```python
p_pop.set_format('population_total', NumberFormatter)

fives = np.arange(1900, 2026, 5) # 1900, 1905, 1910, ..., 2025
p_five = p_pop.sort('time').where('time', are.contained_in(fives))
p_five.show(3)
```

*Output:*

| time | population_total |
| --- | --- |
| 1900 | 24,308,265 |
| 1905 | 25,185,047 |
| 1910 | 25,803,855 |

Run the following cell to visualize the population over time. Following the devastating effects of World War I and World War II, Poland's population increased steadily from 1950 to 2000 and then leveled off. In the following questions we'll investigate this period of population growth.

**Code:**

```python
p_five.plot(0, 1)
```

![Plot output from cell 18 — see preceding code](project1_assets/cell018_out0.png)

---

**Question 1.2.** Assign `initial` to an array that contains the population for every five year interval from **1900 to 2020** (inclusive). Then, assign `changed` to an array that contains the population for every five year interval from **1905 to 2025** (inclusive). The first array should include both 1900 and 2020, and the second array should include both 1905 and 2025. You should use the `p_five` table to create both arrays, by first filtering the table to only contain the relevant years.

The annual growth rate for a time period is equal to:

$$\left(\left(\frac{\text{Population at end of period}}{\text{Population at start of period}}\right)^{\displaystyle\frac{1}{\text{number of years}}}\right) -1$$

We have provided the code below that uses `initial` and `changed` in order to add a column to `p_five` called `annual_growth`. **Don't worry about the calculation of the growth rates**; run the test below to test your solution.

If you are interested in how we came up with the formula for growth rates, consult the [growth rates](https://inferentialthinking.com/chapters/03/2/1/Growth.html) section of the textbook. **(5 points)**

**Student scaffold:**

```python
initial = ...
changed = ...

p_1900_through_2020 = p_five.where('time', are.below_or_equal_to(2020)) 
p_five_growth = p_1900_through_2020.with_column('annual_growth', (changed/initial)**0.2-1)
p_five_growth.set_format('annual_growth', PercentFormatter)
```

**Solution:**

```python
initial = p_five.where("time", are.below(2021)).column('population_total') # SOLUTION
changed = p_five.where("time", are.above(1900)).column('population_total') # SOLUTION

p_1900_through_2020 = p_five.where('time', are.below_or_equal_to(2020)) 
p_five_growth = p_1900_through_2020.with_column('annual_growth', (changed/initial)**0.2-1)
p_five_growth.set_format('annual_growth', PercentFormatter)
```

*Output:*

| time | population_total | annual_growth |
| --- | --- | --- |
| 1900 | 24,308,265 | 0.71% |
| 1905 | 25,185,047 | 0.49% |
| 1910 | 25,803,855 | -0.87% |
| 1915 | 24,696,678 | -0.75% |
| 1920 | 23,785,820 | 1.32% |
| 1925 | 25,395,008 | 1.52% |
| 1930 | 27,378,955 | 0.75% |
| 1935 | 28,414,953 | 0.32% |
| 1940 | 28,876,472 | -1.58% |
| 1945 | 26,666,588 | -1.46% |

**Test — `q1_2` (5 points)**

```python
>>> first = round(p_five_growth.sort(0).column(2).item(0), 8)
>>> 0.005 <= first <= 0.5
True

>>> max(p_five_growth.column(2)) < 0.03
True

# hidden test
>>> np.allclose(np.round(sum(p_five_growth.column(2)), 5), 0.09136)
False

# hidden test
>>> round(p_five_growth.column(2).item(0), 8) == 0.00711198
True

# hidden test
>>> round(p_five_growth.column(2).item(3), 8) == -0.00748765
True

# hidden test
>>> round(p_five_growth.column(2).item(8), 8) == -0.01579705
True
```

The annual growth rate in Poland has been declining since 1950, as shown in the table below.

**Code:**

```python
# Run this cell to view annual growth rates in Poland since 1950.
p_five_growth.where('time', are.above_or_equal_to(1950)).show()
```

*Output:*

| time | population_total | annual_growth |
| --- | --- | --- |
| 1950 | 24,780,161 | 1.78% |
| 1955 | 27,063,640 | 1.79% |
| 1960 | 29,575,966 | 1.13% |
| 1965 | 31,288,336 | 0.79% |
| 1970 | 32,542,633 | 0.86% |
| 1975 | 33,964,399 | 0.93% |
| 1980 | 35,576,519 | 0.90% |
| 1985 | 37,200,853 | 0.46% |
| 1990 | 38,055,455 | 0.16% |
| 1995 | 38,364,667 | -0.06% |
| 2000 | 38,258,071 | -0.07% |
| 2005 | 38,124,379 | -0.02% |
| 2010 | 38,095,351 | 0.09% |
| 2015 | 38,266,314 | -0.05% |
| 2020 | 38,171,012 | -0.02% |

Next, we'll try to understand what has changed in Poland that might explain the slowing population growth rate. Run the next cell to load three additional tables of measurements about countries over time.

**Code:**

```python
life_expectancy = Table.read_table('life_expectancy.csv').where('time', are.below(2026))
child_mortality = Table.read_table('child_mortality.csv').relabel(2, 'child_mortality_under_5_per_1000_born').where('time', are.below(2026))
fertility = Table.read_table('fertility.csv').where('time', are.below(2026))
```

The `life_expectancy` table contains a statistic that is often used to measure how long people live, called _life expectancy at birth_. This number, for a country in a given year, [does not measure how long babies born in that year are expected to live](http://blogs.worldbank.org/opendata/what-does-life-expectancy-birth-really-mean). Instead, it measures how long someone would live, on average, if the _mortality conditions_ in that year persisted throughout their lifetime. These "mortality conditions" describe what fraction of people for each age survived the year. So, it is a way of measuring the proportion of people that are staying alive, aggregated over different age groups in the population.

The `child_mortality` table has the column _child_mortality_under_5_per_1000_born_ which records the number of children who died before age 5, per 1,000 births.

The `fertility` table contains a statistic that is often used to measure how many babies are being born, the _total fertility rate_. This number describes the [number of children a woman would have in her lifetime](https://www.data4impactproject.org/prh/family-planning/fertility/total-fertility-rate/), on average, if the current rates of birth by age of the mother persisted throughout her child bearing years, assuming she survived through age 49.

Run the following cells below to see `life_expectancy`, `child_mortality`, and `fertility`. Refer back to these tables as they will be helpful for answering further questions!

**Code:**

```python
life_expectancy.show(3)
```

*Output:*

| geo | time | life_expectancy_years |
| --- | --- | --- |
| afg | 1800 | 28.21 |
| afg | 1801 | 28.2 |
| afg | 1802 | 28.19 |

**Code:**

```python
child_mortality.show(3)
```

*Output:*

| geo | time | child_mortality_under_5_per_1000_born |
| --- | --- | --- |
| afg | 1800 | 468.58 |
| afg | 1801 | 468.58 |
| afg | 1802 | 468.58 |

**Code:**

```python
fertility.show(3)
```

*Output:*

| geo | time | children_per_woman_total_fertility |
| --- | --- | --- |
| afg | 1800 | 7 |
| afg | 1801 | 7 |
| afg | 1802 | 7 |

---

**Question 1.3.** Is population growing more slowly perhaps because people aren’t living as long? Use the `life_expectancy` table to draw a line graph with the years 1950 and later on the horizontal axis that shows how the _life expectancy at birth_ has changed in Poland. **(5 points)**

_Hint_: Make sure you filter the table properly; otherwise, the graph may look funky!

**Student scaffold:**

```python
# Fill in code here
...
```

**Solution:**

```python
# Fill in code here
life_expectancy.where("geo", are.equal_to("pol")).where("time", are.above_or_equal_to(1950)).plot("time", "life_expectancy_years") # SOLUTION
```

![Plot output from cell 32 — see preceding code](project1_assets/cell032_out0.png)

---

**Question 1.4.** Assuming no other factors, such as birth rates or fertility rates, have changed, could the trends in life expectancy in the graph above directly explain why the population growth rate decreased since 1950 in Poland? Why or why not? **(5 points)**

**SOLUTION:** No. This graph indicates that people are living longer, which would increase population growth if everything else stayed the same.

---

**Question 1.5.** Complete the function `fertility_over_time`. It takes two input arguments, the Alpha-3 code of a country (given as `country_code`) and a year to start from (given as `start`). It returns a two-column table with the column labels `Year` and `Children per woman`. These columns can be used to generate a line chart of the country’s fertility rate each year (starting from the year given by `start`). The plot should include the start year and all later years that appear in the fertility table.

Then, determine the Alpha-3 code for **Poland**. The code at the very bottom for `poland_code` and the year `1950` are inputted to your `fertility_over_time` function. The function returns a table which we use in order to plot how Poland's fertility rate has changed since `1950`. Note that the function `fertility_over_time` should not return the plot itself – it returns a two-column table. The expression that draws the line plot is provided for you; please don’t change it. **(5 points)**

_Hint_: Read about `tbl.relabeled` in the [Python Reference](https://www.data8.org/su26/reference/) to rename columns.


_Hint_: You might find [8.0](https://inferentialthinking.com/chapters/08/Functions_and_Tables.html) helpful.

**Student scaffold:**

```python
def fertility_over_time(country_code, start):
    """Create a two-column table that describes a country's total fertility rate each year."""
    # It's a good idea (but not required) to use multiple lines in your solution.
    ...


poland_code = ...
fertility_over_time(poland_code, 1950)
```

**Solution:**

```python
def fertility_over_time(country_code, start):
    """Create a two-column table that describes a country's total fertility rate each year."""
    # It's a good idea (but not required) to use multiple lines in your solution.
    # BEGIN SOLUTION
    country_fertility = fertility.where('geo', are.equal_to(country_code))
    country_fertility_after_start = country_fertility.where('time', are.above_or_equal_to(start))
    cleaned_table = country_fertility_after_start.select('time', 'children_per_woman_total_fertility').relabeled('time', 'Year').relabeled('children_per_woman_total_fertility', 'Children per woman')
    return cleaned_table
    # END SOLUTION


poland_code = 'pol' # SOLUTION
fertility_over_time(poland_code, 1950)
```

*Output:*

| Year | Children per woman |
| --- | --- |
| 1950 | 3.66 |
| 1951 | 3.68 |
| 1952 | 3.64 |
| 1953 | 3.6 |
| 1954 | 3.56 |
| 1955 | 3.54 |
| 1956 | 3.45 |
| 1957 | 3.44 |
| 1958 | 3.34 |
| 1959 | 3.21 |

**Test — `q1_5` (5 points)**

```python
>>> fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')
True

>>> all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2026))
True

>>> all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2026))
True

# hidden test
>>> print(fertility_over_time('pol', 2012))
Year | Children per woman
2012 | 1.33
2013 | 1.29
2014 | 1.32
2015 | 1.32
2016 | 1.39
2017 | 1.47
2018 | 1.44
2019 | 1.44
2020 | 1.38
2021 | 1.32
... (4 rows omitted)

# hidden test
>>> print(fertility_over_time('usa', 2015))
Year | Children per woman
2015 | 1.83
2016 | 1.8
2017 | 1.75
2018 | 1.72
2019 | 1.68
2020 | 1.62
2021 | 1.63
2022 | 1.67
2023 | 1.62
2024 | 1.62
... (1 rows omitted)

# hidden test
>>> print(fertility_over_time('hti', 2015))
Year | Children per woman
2015 | 3.11
2016 | 3.05
2017 | 2.99
2018 | 2.92
2019 | 2.86
2020 | 2.8
2021 | 2.75
2022 | 2.7
2023 | 2.66
2024 | 2.63
... (1 rows omitted)
```

Plotting the fertility rate in Poland since 1950, we see a downward trend.

**Code:**

```python
fertility_over_time(poland_code, 1950).plot(0, 1)
```

![Plot output from cell 40 — see preceding code](project1_assets/cell040_out0.png)

---

**Question 1.6.** Assuming everything else is constant, could the trends in fertility in the graph above help directly explain why the population growth rate decreased since 1950 in Poland? Why or why not? **(5 points)**

**SOLUTION:** Yes, a declining fertility rate shows that fewer babies are being born each year, which contributes to decreasing population growth. (It's ok to point out that the population growth curve and the fertility curve do not match up exactly, but this is not necessary for a correct solution.)

It has been [observed](https://www.ageing.ox.ac.uk/download/143) that lower fertility rates are often associated with lower child mortality rates. We can see if this association is evident in Poland by plotting the relationship between total fertility rate and [child mortality rate per 1000 children](https://en.wikipedia.org/wiki/Child_mortality).

---

**Question 1.7.** Create a table `poland_since_1950` that contains one row per year starting with 1950 and:

- A column `Year` containing the year
- A column `Children per woman` describing total fertility in Poland that year
- A column `Child deaths per 1000 born` describing child mortality in Poland that year

**(5 points)**

**Student scaffold:**

```python
pol_fertility = fertility_over_time(poland_code, 1950)  # Try starting with the table you built already!
# It's a good idea (but not required) to use multiple lines in your solution.
pol_child_mortality = ...
pol_fertility_and_child_mortality = ...
poland_since_1950 = ...
poland_since_1950
```

**Solution:**

```python
pol_fertility = fertility_over_time(poland_code, 1950)  # Try starting with the table you built already!
# It's a good idea (but not required) to use multiple lines in your solution.
pol_child_mortality = child_mortality.where('geo', are.equal_to('pol')).drop('geo') # SOLUTION
pol_fertility_and_child_mortality = pol_fertility.join('Year', pol_child_mortality, 'time') # SOLUTION
poland_since_1950 = pol_fertility_and_child_mortality.relabel('child_mortality_under_5_per_1000_born', 'Child deaths per 1000 born') # SOLUTION
poland_since_1950
```

*Output:*

| Year | Children per woman | Child deaths per 1000 born |
| --- | --- | --- |
| 1950 | 3.66 | 164.08 |
| 1951 | 3.68 | 177.18 |
| 1952 | 3.64 | 140.16 |
| 1953 | 3.6 | 127.65 |
| 1954 | 3.56 | 118.9 |
| 1955 | 3.54 | 110.38 |
| 1956 | 3.45 | 94.19 |
| 1957 | 3.44 | 86.72 |
| 1958 | 3.34 | 81.28 |
| 1959 | 3.21 | 72.1 |

**Test — `q1_7` (5 points)**

```python
>>> poland_since_1950.num_rows
76

>>> all([label in poland_since_1950.labels for label in ['Children per woman', 'Child deaths per 1000 born']])
True

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(1).item(0), 164.08)
True

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(1).item(-1), 3.71)
False

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(0).item(-1), 1.3)
False

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(0).item(0), 3.66)
True

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(1).mean(), 32.679733333333)
False

# hidden test
>>> facm = poland_since_1950.select('Children per woman', 'Child deaths per 1000 born')
>>> np.allclose(facm.column(0).mean(), 2.08946666666666)
False
```

Run the following cell to generate a scatter plot from the `poland_since_1950` table you created.

The plot uses **color** to encode data about the `Year` column. The colors, ranging from dark blue to white, represent the passing of time between 1950 and 2025. For example, a point on the scatter plot representing data from the 1950s would appear as **dark blue** and a point from the 2010s would appear as **light blue**.

**Code:**

```python
x_births = poland_since_1950.column("Children per woman")
y_deaths = poland_since_1950.column("Child deaths per 1000 born")
time_colors = poland_since_1950.column("Year")

plots.figure(figsize=(6,6))
plots.scatter(x_births, y_deaths, c=time_colors, cmap="Blues_r")
plots.colorbar()                  
plots.xlabel("Children per woman")
plots.ylabel("Child deaths per 1000 born");
```

![Plot output from cell 49 — see preceding code](project1_assets/cell049_out0.png)

---

**Question 1.8.** In one or two sentences, describe the association (if any) that is illustrated by this scatter plot. Does the diagram show any causal relation between fertility and child mortality? **(5 points)**

**SOLUTION:** We can observe that fertility rates and child mortality rates decrease together over time, although the association is not entirely linear or consistent. However, this association does not tell us whether one of these changes caused a change in the other. (It's ok to point out that decreases in child mortality sometimes precede decreases in fertility, but this observation is not necessary for a correct response.)

_Optional food for thought_: What other context or information would you need in order to better understand the factors affecting life expectancy, child mortality, and fertility?

### Checkpoint (due Friday 2/18 by 5:00 PM PT)

![White dog](project1_assets/fifi.jpg)
![White dog](project1_assets/yoyo.jpg)

**WOOOHOO!!!** Fifi and Yoyo want to congratulate you on reaching the checkpoint!

**Run the following cells and submit to the Pensive assignment corresponding to the checkpoint: <u>Project 1 Checkpoint</u>**

**<span style="color: #BC412B">Remember to add your project partner to your submission on Pensive!</span>** <u>Only one partner should submit to [Pensive](https://www.pensieve.co/).</u>

Note: If you have the time, we encourage you to continue working past the checkpoint! Some students found that the next section of the project took them a lot longer to complete.

--- 

To double check your work, the cell below will rerun all of the autograder tests for Section 1.

**Code:**

```python
checkpoint_tests = ["q1_1", "q1_2", "q1_5", "q1_7"]
for test in checkpoint_tests:
    display(grader.check(test))
```

*Output (stdout):*

```text
Unexpected exception formatting exception. Falling back to standard exception
```

*Output (stderr):*

```text
Traceback (most recent call last):
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/interactiveshell.py", line 3577, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/folders/xv/tl5mnl5s0mz_ykhsrhdyb_rm0000gn/T/ipykernel_50708/1374029256.py", line 3, in <module>
    display(grader.check(test))
            ^^^^^^
NameError: name 'grader' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/interactiveshell.py", line 2168, in showtraceback
    stb = self.InteractiveTB.structured_traceback(
        etype, value, tb, tb_offset=tb_offset
    )
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1454, in structured_traceback
    return FormattedTB.structured_traceback(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, etype, evalue, etb, tb_offset, number_of_lines_of_context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1345, in structured_traceback
    return VerboseTB.structured_traceback(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, etype, value, tb, tb_offset, number_of_lines_of_context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1192, in structured_traceback
    formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,
                                                           tb_offset)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1082, in format_exception_as_a_whole
    self.get_records(etb, number_of_lines_of_context, tb_offset) if etb else []
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/IPython/core/ultratb.py", line 1179, in get_records
    res = list(stack_data.FrameInfo.stack_data(etb, options=options))[tb_offset:]
          ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 597, in stack_data
    yield from collapse_repeated(
    ...<4 lines>...
    )
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/utils.py", line 83, in collapse_repeated
    yield from map(mapper, original_group)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 587, in mapper
    return cls(f, options)
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/stack_data/core.py", line 551, in __init__
    self.executing = Source.executing(frame_or_tb)
                     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/executing/executing.py", line 283, in executing
    assert_(new_stmts <= stmts)
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/Users/marissalumpkin/Desktop/data8/assignments_new/env/lib/python3.13/site-packages/executing/executing.py", line 80, in assert_
    raise AssertionError(str(message))
AssertionError
```

## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. You only need to submit the zip file for the checkpoint. **Please save before exporting!**

---
### The World

The changes observed in Poland can also be observed in many other countries: except during periods of extended war, famine, and social chaos, health services generally improve, life expectancy increases, and child mortality decreases. At the same time, the fertility rate often plummets, and where it does, the population growth rate decreases despite increasing longevity.

Run the cell below to generate two overlaid histograms, one for 1962 and one for 2010, that show the distributions of total fertility rates for these two years among all 201 countries in the `fertility` table.

**Code:**

```python
Table().with_columns( 
    '1962', fertility.where('time', 1962).column(2),
    '2010', fertility.where('time', 2010).column(2)
).hist(bins=np.arange(0, 10, 0.5), unit='child per woman')
_ = plots.xlabel('Children per woman')
_ = plots.ylabel('Percent per children per woman')
_ = plots.xticks(np.arange(10))
```

![Plot output from cell 61 — see preceding code](project1_assets/cell061_out0.png)

---

**Question 1.9.** Assign `fertility_statements` to an **array** of the numbers of each statement below that can be correctly inferred from these histograms.

For example, if the answer choices you selected were 1, 2, and 3, your code should look like `make_array(1, 2, 3)`.

1. In 1962, less than 20% of countries had a fertility rate below 3.
1. At least half of countries had a fertility rate between 5 and 8 in 1962.
1. In 2010, about 40% of countries had a fertility rate between 1.5 and 2.
1. At least half of countries had a fertility rate below 3 in 2010.
1. More countries had a fertility rate above 3 in 1962 than in 2010.
1. About the same number of countries had a fertility rate between 3.5 and 4.5 in both 1962 and 2010.

**(4 points)**

**Student scaffold:**

```python
fertility_statements = ...
```

**Solution:**

```python
fertility_statements = make_array(1, 2, 4, 5) # SOLUTION
```

**Test — `q1_9` (4 points)**

```python
>>> all((x in range(1, 7) for x in set(fertility_statements)))
True

# hidden test
>>> set(fertility_statements) == set(make_array(1, 2, 4, 5))
True
```

---

**Question 1.10.** Draw a line plot of the **world population** from 1800 through 2025 (inclusive of both endpoints). The world population is the sum of all of the countries' populations. You should use the `population` table defined earlier in the project. **(5 points)**

**Student scaffold:**

```python
#Fill in code here
...
```

**Solution:**

```python
#Fill in code here
population.where('time', are.between(1800, 2026)).drop('geo').group('time', sum).plot('time', "population_total sum") # SOLUTION
```

![Plot output from cell 66 — see preceding code](project1_assets/cell066_out0.png)

---

**Question 1.11.** Create a function `stats_for_year` that takes a `year` and returns a table of statistics. The table it returns should have four columns: `geo`, `population_total`, `children_per_woman_total_fertility`, and `child_mortality_under_5_per_1000_born`. Each row should contain one unique Alpha-3 country code and three statistics: population, fertility rate, and child mortality for that `year` from the `population`, `fertility` and `child_mortality` tables. Only include rows for which all three statistics are available for the country and year.

In addition, restrict the result to country codes that appears in `big_50`, an array of the 50 most populous countries in 2025. This restriction will speed up computations later in the project.

After you write `stats_for_year`, try calling `stats_for_year` on any year between 1960 and 2025. Try to understand the output of `stats_for_year`.

*Hint*: The tests for this question are quite comprehensive, so if you pass the tests, your function is probably correct. However, without calling your function yourself and looking at the output, it will be very difficult to understand any problems you have, so try your best to write the function correctly and check that it works before you rely on the `grader` tests to confirm your work.

*Hint*: What do all three tables have in common (pay attention to column names)?

*Hint*: Create additional cells before directly writing the function.

**(5 points)**

**Student scaffold:**

```python
# We first create a population table that only includes the 
# 50 countries with the largest 2025 populations. We focus on 
# these 50 countries only so that plotting later will run faster.
big_50 = population.where('time', are.equal_to(2025)).sort("population_total", descending=True).take(np.arange(50)).column('geo')
population_of_big_50 = population.where('time', are.above(1959)).where('geo', are.contained_in(big_50))

def stats_for_year(year):
    """Return a table of the stats for each country that year."""
    p = population_of_big_50.where('time', are.equal_to(year)).drop('time')
    f = fertility.where('time', are.equal_to(year)).drop('time')
    c = child_mortality.where('time', are.equal_to(year)).drop('time')
    ...

...
```

**Solution:**

```python
# We first create a population table that only includes the 
# 50 countries with the largest 2025 populations. We focus on 
# these 50 countries only so that plotting later will run faster.
big_50 = population.where('time', are.equal_to(2025)).sort("population_total", descending=True).take(np.arange(50)).column('geo')
population_of_big_50 = population.where('time', are.above(1959)).where('geo', are.contained_in(big_50))

def stats_for_year(year):
    """Return a table of the stats for each country that year."""
    p = population_of_big_50.where('time', are.equal_to(year)).drop('time')
    f = fertility.where('time', are.equal_to(year)).drop('time')
    c = child_mortality.where('time', are.equal_to(year)).drop('time')
    return p.join('geo', f.join('geo', c)) # SOLUTION

stats_for_year(1987) # SOLUTION
```

*Output:*

| geo | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born |
| --- | --- | --- | --- |
| afg | 11387818 | 7.55 | 198.17 |
| ago | 10497858 | 7.41 | 224.1 |
| arg | 31291762 | 3.04 | 29.11 |
| bgd | 104959291 | 5.08 | 161.62 |
| bra | 141104944 | 3.23 | 71.26 |
| can | 26540921 | 1.56 | 9.12 |
| chn | 1096217446 | 2.76 | 53.78 |
| civ | 10851475 | 7.09 | 153.51 |
| cod | 33298904 | 6.65 | 192.52 |
| col | 30499467 | 3.09 | 39.14 |

**Test — `q1_11` (5 points)**

```python
>>> t = stats_for_year(1990)
>>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')
True

>>> t = stats_for_year(1990)
>>> t.num_rows
50

>>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))
geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
can  | 17898790         | 3.84                               | 32.6
deu  | 72811640         | 2.39                               | 40.47
fra  | 46428134         | 2.74                               | 28.5
irn  | 21470434         | 7.37                               | 326.94
kor  | 26115379         | 5.99                               | 112.18
moz  | 6713695          | 6.38                               | 277.4
phl  | 27891897         | 7.03                               | 103.65
tha  | 26851747         | 6.28                               | 146.46
usa  | 180274555        | 3.72                               | 30.05

>>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))
geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
bgd  | 152201981        | 2.38                               | 49.1
cod  | 68563038         | 6.59                               | 115.29
esp  | 46840471         | 1.37                               | 3.85
idn  | 246305322        | 2.46                               | 34.12
jpn  | 128185275        | 1.36                               | 3.2
mex  | 113623895        | 2.34                               | 17.36
pak  | 199239047        | 4.4                                | 87.51
sau  | 25157128         | 2.81                               | 12.08
uga  | 32390802         | 6.02                               | 77.39
yem  | 26754387         | 4.81                               | 55.96
```

---

**Question 1.12.** Create a table called `pop_by_decade` with two columns called `decade` and `population`, in this order. It should contain a row for each year that starts a decade, in increasing order starting with 1960 and ending with 2020. For example, 1960 is the start of the 1960's decade. The `population` column contains the total population of all countries included in the result of `stats_for_year(year)` for the first `year` of the decade. You should see that these countries contain most of the world's population.

*Hint:* One approach is to define a function `pop_for_year` that computes this total population, then `apply` it to the `decade` column.  **Think about how you can use the `stats_for_year` function** from the previous question if you want to implement `pop_for_year`.

This first test is just a sanity check for your helper function if you choose to use it. **You will not lose points for not implementing the function `pop_for_year`**.

**Note:** The cell where you will generate the `pop_by_decade` table is below the cell where you can choose to define the helper function `pop_for_year`. You should define your `pop_by_decade` table in the cell that starts with the table `decades` being defined. 

**(4 points)**

**Student scaffold:**

```python
def pop_for_year(year):
    """Return the total population for the specified year."""
    ...
```

**Solution:**

```python
def pop_for_year(year):
    """Return the total population for the specified year."""
    return sum(stats_for_year(year).column('population_total')) # SOLUTION
```

**Test — `q1_12_0` (0 points)**

```python
>>> pop_for_year(1972) == 3334568709
True

>>> pop_for_year(2020) == 6840687359
True

>>> pop_for_year(1989) == 4556698997
True

# hidden test
>>> pop_for_year(2002) == 5525600587
True
```

---

Now that you've defined your helper function (if you've chosen to do so), define the `pop_by_decade` table.

**Student scaffold:**

```python
decades = Table().with_column('decade', np.arange(1960, 2021, 10))

pop_by_decade = ...
pop_by_decade.set_format(1, NumberFormatter)
```

**Solution:**

```python
decades = Table().with_column('decade', np.arange(1960, 2021, 10))

pop_by_decade = decades.with_column('population', decades.apply(pop_for_year, 'decade')) # SOLUTION
pop_by_decade.set_format(1, NumberFormatter)
```

*Output:*

| decade | population |
| --- | --- |
| 1960 | 2,604,997,601 |
| 1970 | 3,202,277,698 |
| 1980 | 3,863,485,128 |
| 1990 | 4,639,963,324 |
| 2000 | 5,381,686,829 |
| 2010 | 6,107,215,351 |
| 2020 | 6,840,687,359 |

**Test — `q1_12` (4 points)**

```python
>>> pop_by_decade.labels == ('decade', 'population')
True

>>> pop_by_decade.column(0).item(0) == 1960
True

# hidden test
>>> pop_by_decade.num_rows == 7
True

# hidden test
>>> pop_by_decade.column(0).item(0) == 1960
True

# hidden test
>>> pop_by_decade.column(0).item(6) == 2020
True

# hidden test
>>> pop_by_decade.column(1).item(1) == 3202277698
True

# hidden test
>>> pop_by_decade.column(1).item(5) == 6107215351
True
```

The `countries` table describes various characteristics of countries. The `country` column contains the same codes as the `geo` column in each of the other data tables (`population`, `fertility`, and `child_mortality`). The `world_6region` column classifies each country into a region of the world. Run the cell below to inspect the data.

**Code:**

```python
countries = Table.read_table('countries.csv').where('country', are.contained_in(population.group('geo').column('geo')))
countries.select('country', 'name', 'world_6region')
```

*Output:*

| country | name | world_6region |
| --- | --- | --- |
| afg | Afghanistan | south_asia |
| ago | Angola | sub_saharan_africa |
| alb | Albania | europe_central_asia |
| and | Andorra | europe_central_asia |
| are | United Arab Emirates | middle_east_north_africa |
| arg | Argentina | america |
| arm | Armenia | europe_central_asia |
| atg | Antigua and Barbuda | america |
| aus | Australia | east_asia_pacific |
| aut | Austria | europe_central_asia |

---

**Question 1.13.** Create a table called `region_counts`. It should contain two columns called `region` and `count`. The `region` column should contain regions of the world, and the `count` column should contain the number of countries in each region that appears in the result of `stats_for_year(2025)`. 

For example, one row would have `south_asia` as its `region` value and an integer as its `count` value: the number of large South Asian countries for which we have population, fertility, and child mortality numbers from 2025.

*Hint*: You may have to relabel a column to name it `region`. 

**(4 points)**

**Student scaffold:**

```python
stats_for_2025 = ...
region_counts = ...
region_counts
```

**Solution:**

```python
stats_for_2025 = stats_for_year(2025) # SOLUTION
region_counts = countries.join('country', stats_for_2025, 'geo').group('world_6region').relabeled('world_6region', 'region') # SOLUTION
region_counts
```

*Output:*

| region | count |
| --- | --- |
| america | 7 |
| east_asia_pacific | 9 |
| europe_central_asia | 10 |
| middle_east_north_africa | 7 |
| south_asia | 4 |
| sub_saharan_africa | 13 |

**Test — `q1_13` (4 points)**

```python
>>> region_counts.labels == ('region', 'count')
True

>>> sum(region_counts.column('count')) == 50
True

# hidden test
>>> list(region_counts.sort('count').column('count'))
[4, 7, 7, 9, 10, 13]

# hidden test
>>> print(list(region_counts.sort('count').column('region')))
['south_asia', 'america', 'middle_east_north_africa', 'east_asia_pacific', 'europe_central_asia', 'sub_saharan_africa']
```

The following scatter diagram compares total fertility rate and child mortality rate for each country in 1960. The area of each dot represents the population of the country, and the color represents its region of the world. Run the cell. Do you think you can identify any of the dots?

**Code:**

```python
from functools import lru_cache as cache

# This cache annotation makes sure that if the same year
# is passed as an argument twice, the work of computing
# the result is only carried out once.
@cache(None)
def stats_relabeled(year):
    """Relabeled and cached version of stats_for_year."""
    return stats_for_year(year).relabel(2, 'Children per woman').relabel(3, 'Child deaths per 1000 born')

def fertility_vs_child_mortality(year):
    """Draw a color scatter diagram comparing child mortality and fertility."""
    with_region = stats_relabeled(year).join('geo', countries.select('country', 'world_6region'), 'country')
    with_region.scatter(2, 3, sizes=1, group=4, s=500)
    plots.xlim(0,10)
    plots.ylim(-50, 500)
    plots.title(year)
    plots.show()

fertility_vs_child_mortality(1960)
```

![Plot output from cell 82 — see preceding code](project1_assets/cell082_out0.png)

---

**Question 1.14.** Assign `scatter_statements` to an array of the numbers of each statement below that can be inferred from this scatter diagram for 1960. 
1. All countries in `europe_central_asia` had uniformly low fertility rates.
1. Most countries had a fertility rate above 5.
1. The lowest child mortality rate of any country was from an `east_asia_pacific` country.
1. There was an association between child mortality and fertility.
1. The two largest countries by population also had the two highest child mortality rates.

**(4 points)**

**Student scaffold:**

```python
scatter_statements = ...
```

**Solution:**

```python
scatter_statements = make_array(2, 4) # SOLUTION
```

**Test — `q1_14` (4 points)**

```python
>>> all((x in range(1, 6) for x in set(scatter_statements)))
True

# hidden test
>>> set(scatter_statements) == {2, 4}
True
```

The result of the cell below is interactive. Drag the slider to the right to see how countries have changed over time. You’ll find that in terms of population growth, the divide between the countries of the global North and global South that existed in the 1960s has shrunk significantly. 

This shift in fertility rates is the reason that the global population is expected to grow more slowly in the 21st century than it did in the 19th and 20th centuries. Fertility rates change for reasons that include cultural patterns, better prospects for children surviving to adulthood, and family planning (such as contraception and women’s greater control over their reproduction).

**Note:** Don't worry if a red warning pops up when running the cell below. You'll still be able to run the cell!

**Code:**

```python
_ = widgets.interact(fertility_vs_child_mortality, 
                     year=widgets.IntSlider(min=1960, max=2025, value=1960))
```

*Output:*

```text
interactive(children=(IntSlider(value=1960, description='year', max=2025, min=1960), Output()), _dom_classes=(…
```

Now is a great time to take a break and watch the same data presented by [Hans Rosling in a 2010 TEDx talk](https://www.gapminder.org/videos/reducing-child-mortality-a-moral-and-environmental-imperative) with smoother animation and witty commentary.

When we look at population and fertility as data scientists, we need to learn about the experiences of people in real life, not just abstractly as data. We should also recognize that population studies have sometimes had political undercurrents. Those undercurrents have included population control, control of women’s reproduction, or fears of shifts between racial groups. To do better as data scientists, we should check our assumptions to avoid unthinkingly reproducing past patterns.

---
## 2. Global Poverty

In 1800, 85% of the world's 1 billion people lived in [extreme poverty](https://en.wikipedia.org/wiki/Extreme_poverty), defined by the United Nations as "a condition characterized by severe deprivation of basic human needs, including food, safe drinking water, sanitation facilities, health, shelter, education and information." At the time when the data in this project were gathered, a common definition of extreme poverty was a person living on less than \$1.25 a day.

In 2018, the proportion of people living in extreme poverty was estimated to be [about 9\%](https://unstats.un.org/sdgs/report/2019/goal-01/). Although the world rate of extreme poverty has declined consistently for hundreds of years, the number of people living in extreme poverty is still over 600 million. The United Nations adopted an [ambitious goal](http://www.un.org/sustainabledevelopment/poverty/): "By 2030, eradicate extreme poverty for all people everywhere."

In this part of the project, we will examine some aspects of global poverty that might affect whether the goal is achievable. The causes of poverty are complex. They include global histories, such as colonialism, as well as factors such as health care, economics, and social inequality in each country.

First, load the population and poverty rate by country and year and the country descriptions. While the `population` table has values for every recent year for many countries, the `poverty` table only includes certain years for each country in which a measurement of the rate of extreme poverty was available.

**Code:**

```python
population = Table.read_table('population.csv') 
countries = Table.read_table('countries.csv').where('country', are.contained_in(population.group('geo').column('geo')))
poverty = Table.read_table('poverty.csv')
poverty.show(3)
```

*Output:*

| geo | time | extreme_poverty_percent_people_below_125_a_day |
| --- | --- | --- |
| alb | 1996 | 0.2 |
| alb | 2002 | 0.73 |
| alb | 2004 | 0.53 |

---

**Question 2.1.** Assign `latest_poverty` to a three-column table with one row for each country that appears in the `poverty` table. The first column should contain the 3-letter code for the country. The second column should contain the most recent year for which an extreme poverty rate is available for the country. The third column should contain the poverty rate in that year. **Do not change the last line, so that the labels of your table are set correctly.**

*Hint*: think about how ```group``` works: it does a sequential search of the table (from top to bottom) and collects values in the array in the order in which they appear, and then applies a function to that array. The `first` function may be helpful, but you are not required to use it.

**(4 points)**

**Student scaffold:**

```python
def first(values):
    return values.item(0)

latest_poverty = ...
latest_poverty = latest_poverty.relabeled(0, 'geo').relabeled(1, 'time').relabeled(2, 'poverty_percent') # You should *not* change this line.
latest_poverty
```

**Solution:**

```python
def first(values):
    return values.item(0)

latest_poverty = poverty.sort('time', descending=True).group('geo', first) # SOLUTION
latest_poverty = latest_poverty.relabeled(0, 'geo').relabeled(1, 'time').relabeled(2, 'poverty_percent') # You should *not* change this line.
latest_poverty
```

*Output:*

| geo | time | poverty_percent |
| --- | --- | --- |
| ago | 2009 | 43.37 |
| alb | 2012 | 0.46 |
| arg | 2011 | 1.41 |
| arm | 2012 | 1.75 |
| aus | 2003 | 1.36 |
| aut | 2004 | 0.34 |
| aze | 2008 | 0.31 |
| bdi | 2006 | 81.32 |
| bel | 2000 | 0.5 |
| ben | 2012 | 51.61 |

**Test — `q2_1` (4 points)**

```python
>>> latest_poverty.labels == ('geo', 'time', 'poverty_percent')
True

>>> latest_poverty.num_rows
145

# hidden test
>>> print(latest_poverty.sort('geo').take(np.arange(7, 107, 10)))
geo  | time | poverty_percent
bdi  | 2006 | 81.32
bra  | 2012 | 3.75
cod  | 2006 | 87.72
dom  | 2012 | 2.25
fsm  | 2000 | 31.15
guy  | 1998 | 8.7
isr  | 2010 | 0.39
lbr  | 2007 | 83.76
mex  | 2012 | 1.03
nga  | 2010 | 62.03
```

---

**Question 2.2.** Using both `latest_poverty` and `population`, create a four-column table called `recent_poverty_total` with one row for each country in `latest_poverty`. The four columns should have the following labels and contents:
1. `geo` contains the 3-letter country code,
1. `poverty_percent` contains the most recent poverty percent,
1. `population_total` contains the population of the country in 2010,
1. `poverty_total` contains the number of people in poverty **rounded to the nearest integer**, based on the 2010 population and most recent poverty rate.

*Hint*: You are not required to use `poverty_and_pop`, and you are always welcome to add any additional names. 

**(4 points)**

**Student scaffold:**

```python
poverty_and_pop = ...
recent_poverty_total = ...
recent_poverty_total
```

**Solution:**

```python
""" # BEGIN PROMPT
poverty_and_pop = ...
recent_poverty_total = ...
recent_poverty_total
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
pop_2010 = population.where("time", are.equal_to(2010)).drop('time')
poverty_and_pop = latest_poverty.drop('time').join('geo', pop_2010)
poverty_total_arr = np.round(poverty_and_pop.column('poverty_percent')/100*poverty_and_pop.column('population_total'))
recent_poverty_total = poverty_and_pop.with_column('poverty_total', poverty_total_arr)
recent_poverty_total
# END SOLUTION
```

*Output:*

| geo | poverty_percent | population_total | poverty_total |
| --- | --- | --- | --- |
| ago | 43.37 | 23294825 | 1.0103e+07 |
| alb | 0.46 | 2928722 | 13472 |
| arg | 1.41 | 41288694 | 582171 |
| arm | 1.75 | 2931078 | 51294 |
| aus | 1.36 | 22141581 | 301126 |
| aut | 0.34 | 8365092 | 28441 |
| aze | 0.31 | 9146851 | 28355 |
| bdi | 81.32 | 9376444 | 7.62492e+06 |
| bel | 0.5 | 10936626 | 54683 |
| ben | 51.61 | 9797484 | 5.05648e+06 |

**Test — `q2_2` (4 points)**

```python
>>> recent_poverty_total.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')
True

>>> float(recent_poverty_total.where('geo', 'aus').column(2).item(0)) == 22141581
True

>>> recent_poverty_total.where('geo', 'aus').column(3).item(0) < recent_poverty_total.where('geo', 'aus').column(2).item(0)
True

>>> float(recent_poverty_total.where('geo', 'aus').column(3).item(0)) == 301126
True

# hidden test
>>> sum(recent_poverty_total.column(3)) == 1011667558
True
```

---

**Question 2.3.** Assign the name `poverty_percent` to the known percentage of the world’s 2010 population that were living in extreme poverty. Assume that the `poverty_total` numbers in the `recent_poverty_total` table describe **all** people in 2010 living in extreme poverty. You should get a number that is above the 2018 global estimate of 9%, since many country-specific poverty rates are older than 2018.

*Hint*: The sum of the `population_total` column in the `recent_poverty_total` table is not the world population, because only a subset of the world's countries are included in the `recent_poverty_total` table (only some countries have known poverty rates). Use the `population` table to compute the world's 2010 total population.

*Hint*: We are computing a percentage (value between 0 and 100), not a proportion (value between 0 and 1).

**(4 points)**

**Student scaffold:**

```python
poverty_percent = ...
poverty_percent
```

**Solution:**

```python
""" # BEGIN PROMPT
poverty_percent = ...
poverty_percent
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
total_2010_pop = sum(population.where('time', are.equal_to(2010)).column("population_total"))
poverty_2010_pop = sum(recent_poverty_total.column('poverty_total'))
poverty_percent = 100* poverty_2010_pop/total_2010_pop
poverty_percent
# END SOLUTION
```

*Output:*

```text
14.429159949245513
```

**Test — `q2_3` (4 points)**

```python
>>> 10 <= poverty_percent <= 20
True

# hidden test
>>> np.allclose(np.round(poverty_percent, 2), 14.43)
True
```

The `countries` table includes not only the name and region of countries, but also their positions on the globe.

**Code:**

```python
countries.select('country', 'name', 'world_4region', 'latitude', 'longitude')
```

*Output:*

| country | name | world_4region | latitude | longitude |
| --- | --- | --- | --- | --- |
| afg | Afghanistan | asia | 33 | 66 |
| ago | Angola | africa | -12.5 | 18.5 |
| alb | Albania | europe | 41 | 20 |
| and | Andorra | europe | 42.5078 | 1.52109 |
| are | United Arab Emirates | asia | 23.75 | 54.5 |
| arg | Argentina | americas | -34 | -64 |
| arm | Armenia | europe | 40.25 | 45 |
| atg | Antigua and Barbuda | americas | 17.05 | -61.8 |
| aus | Australia | asia | -25 | 135 |
| aut | Austria | europe | 47.3333 | 13.3333 |

---

**Question 2.4.** Using both `countries` and `recent_poverty_total`, create a five-column table called `poverty_map` with one row for every country in `recent_poverty_total`.  The five columns should have the following labels and contents, in this order:
1. `latitude` contains the country's latitude,
1. `longitude` contains the country's longitude,
1. `name` contains the country's name,
1. `region` contains the country's region from the `world_4region` column of `countries`,
1. `poverty_total` contains the country's poverty total.

**(6 points)**

**Student scaffold:**

```python
poverty_map = ...
poverty_map
```

**Solution:**

```python
""" # BEGIN PROMPT
poverty_map = ...
poverty_map
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
small_countries = countries.select('country', 'latitude', 'longitude', 'name', 'world_4region').relabeled('world_4region', 'region')
small_recent_poverty = recent_poverty_total.select('geo', 'poverty_total')
poverty_map = small_countries.join('country', small_recent_poverty, 'geo' ).drop('country')
poverty_map
# END SOLUTION
```

*Output:*

| latitude | longitude | name | region | poverty_total |
| --- | --- | --- | --- | --- |
| -12.5 | 18.5 | Angola | africa | 1.0103e+07 |
| 41 | 20 | Albania | europe | 13472 |
| -34 | -64 | Argentina | americas | 582171 |
| 40.25 | 45 | Armenia | europe | 51294 |
| -25 | 135 | Australia | asia | 301126 |
| 47.3333 | 13.3333 | Austria | europe | 28441 |
| 40.5 | 47.5 | Azerbaijan | europe | 28355 |
| -3.5 | 30 | Burundi | africa | 7.62492e+06 |
| 50.75 | 4.5 | Belgium | europe | 54683 |
| 9.5 | 2.25 | Benin | africa | 5.05648e+06 |

**Test — `q2_4` (6 points)**

```python
>>> poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')
True

>>> list(np.sort(np.unique(poverty_map.column('region'))))
['africa', 'americas', 'asia', 'europe']

# hidden test
>>> print(poverty_map.sort('name').take(np.arange(10)).drop(4))
latitude | longitude | name       | region
41       | 20        | Albania    | europe
28       | 3         | Algeria    | africa
-12.5    | 18.5      | Angola     | africa
-34      | -64       | Argentina  | americas
40.25    | 45        | Armenia    | europe
-25      | 135       | Australia  | asia
47.3333  | 13.3333   | Austria    | europe
40.5     | 47.5      | Azerbaijan | europe
24       | 90        | Bangladesh | asia
53       | 28        | Belarus    | europe

# hidden test
>>> sum(poverty_map.column(4)) == sum(recent_poverty_total.column(3))
True
```

Run the cell below to draw a map of the world in which the areas of circles represent the number of people living in extreme poverty. Double-click on the map to zoom in.

> ***Note:*** If the cell below isn't loading, you can view the output [here](https://github.jonathanferrari.com/static/poverty_map.html)

**Code:**

```python
# It may take a few seconds to generate this map.
colors = {'africa': 'blue', 'europe': 'black', 'asia': 'red', 'americas': 'green'}
scaled = poverty_map.with_columns(
    'labels', poverty_map.column('name'),
    'colors', poverty_map.apply(colors.get, 'region'),
    'areas', 1e-4 * poverty_map.column('poverty_total')
).drop('name', 'region', 'poverty_total')

Circle.map_table(scaled)
```

*Output:*

Make this Notebook Trusted to load map: File -> Trust Notebook

Although people lived in extreme poverty throughout the world in 2010 (with more than 5 million in the United States), the largest numbers were in Asia and Africa.

---

**Question 2.5.** Assign `largest` to a two-column table with the `name` (not the 3-letter code) and `poverty_total` of the 10 countries with the largest number of people living in extreme poverty.

*Hint*: How can we use `take` and `np.arange` in conjunction with each other?

**(6 points)**

**Student scaffold:**

```python
largest = ...
largest.set_format('poverty_total', NumberFormatter)
```

**Solution:**

```python
largest = poverty_map.sort('poverty_total', descending=True).take(np.arange(10)).select('name', 'poverty_total') #SOLUTION
largest.set_format('poverty_total', NumberFormatter)
```

*Output:*

| name | poverty_total |
| --- | --- |
| India | 293,834,694.00 |
| Nigeria | 103,368,582.00 |
| China | 84,607,751.00 |
| Bangladesh | 65,827,357.00 |
| Congo, Dem. Rep. | 60,143,497.00 |
| Indonesia | 39,901,462.00 |
| Ethiopia | 33,309,119.00 |
| Pakistan | 25,383,055.00 |
| Tanzania | 19,460,991.00 |
| Madagascar | 19,448,134.00 |

**Test — `q2_5` (6 points)**

```python
>>> largest.labels == ('name', 'poverty_total')
True

>>> largest.column(0).item(0)
'India'

>>> largest.num_rows
10

# hidden test
>>> float(largest.take(1).column(1).item(0)) == 103368582
True
```

---

**Question 2.6.** It is important to study the absolute number of people living in poverty, not just the percent. The absolute number is an important factor in determining the amount of resources needed to support people living in poverty. In the next two questions you will explore this.

In Question 7, you will be asked to write a function called `poverty_timeline` that takes **the name of a country** as its argument (not the Alpha-3 country code). It should draw a line plot of the number of people living in poverty in that country with time on the horizontal axis. The line plot should have a point for each row in the poverty table for that country. To compute the population living in poverty from a poverty percentage, multiply by the population of the country **in that year**.

For this question, write out a generalized process for Question 7. Make sure to answer/include the following: 
- What should this function output? 
- Additionally, **make a numbered list** of the steps you take within the function body. If you added/edited, say, 5 lines in the function body, then it would be good to see the numbers 1 through 5 describing what you did (i.e. what functions/methods you used) in each line and why.

As a tip, after finishing question 7, we recommend polishing up your description of the steps for this question. This question will be graded for correctness.

**(5 points)**

**SOLUTION**: The function should output a line plot of people living in extreme poverty in a country. To generate the line plot, we first filter the `countries` table to find the country code of the country we passed into our function. Then, we filter the `poverty` and `population` tables to only contain the rows with our desired country code, and then drop the `geo` columns from each table. Next, we join `poverty` and `population`. Then, we perform array operations to multiply the population with the percent of the population living in extreme poverty to get the number of people living in extreme poverty. Finally, we can add a column to our joined table that contains the number of people in poverty, which will allow us to create a plot.

---

**Question 2.7.** Now, we'll actually write the function called `poverty_timeline`. Recall that `poverty_timeline` takes **the name of a country** as its argument (not the Alpha-3 country code). It should draw a line plot of the number of people living in poverty in that country with time on the horizontal axis. The line plot should have a point for each row in the `poverty` table for that country.

**Note:** You **should <u>not</u>** return anything from your function. Simply call `plots.show()` at the end of your function body.

*Hint 1:* This question is long. Feel free to create cells and experiment. You can create cells by going to the toolbar and hitting the `+` button.

*Hint 2:* Consider using `join` in your code.

*Hint 3:* Remember from Question 6—to compute the population living in poverty from a poverty percentage, multiply the percentage by the country’s population **in that year.**

Feel free to use the markdown cell below to plan out your answer, but you needn't fill it in.

**(5 points)**

**Student scaffold:**

```python
def poverty_timeline(country):
    '''Draw a timeline of people living in extreme poverty in a country.'''
    geo = ...
    # This solution will take multiple lines of code. Use as many as you need
    ...
    # Don't change anything below this line. 
    plots.title(country)
    plots.ylim(bottom=0)
    plots.show() # This should be the last line of your function.
```

**Solution:**

```python
""" # BEGIN PROMPT
def poverty_timeline(country):
    '''Draw a timeline of people living in extreme poverty in a country.'''
    geo = ...
    # This solution will take multiple lines of code. Use as many as you need
    ...
    # Don't change anything below this line. 
    plots.title(country)
    plots.ylim(bottom=0)
    plots.show() # This should be the last line of your function. 
"""; # END PROMPT
# BEGIN SOLUTION NO PROMPT
def poverty_timeline(country):
    geo = countries.where('name', are.equal_to(country)).column('country').item(0)
    country_poverty = poverty.where('geo', are.equal_to(geo)).drop('geo')
    country_population = population.where('geo', are.equal_to(geo)).drop('geo')
    country_pov_and_pop = country_poverty.join('time', country_population)
    num_poverty = country_pov_and_pop.column('population_total') * country_pov_and_pop.column('extreme_poverty_percent_people_below_125_a_day')/100
    final_tbl = country_pov_and_pop.with_column('Number in Poverty', num_poverty)
    final_tbl.plot('time', 'Number in Poverty')
    plots.title(country)
    plots.ylim(bottom=0)
    plots.show() 
# END SOLUTION
```

Finally, draw the line plots below to see how the world is changing. Pay attention to the axes!

**Solution:**

```python
poverty_timeline('Poland')
poverty_timeline('India')
poverty_timeline('Nigeria')
poverty_timeline('China')
poverty_timeline('Colombia')
poverty_timeline('United States')
```

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out0.png)

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out1.png)

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out2.png)

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out3.png)

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out4.png)

![Plot output from cell 121 — see preceding code](project1_assets/cell121_out5.png)

Although the number of people living in extreme poverty increased in some countries including Nigeria and the United States, the decreases in other countries, most notably the massive decreases in China and India, have shaped the overall trend that extreme poverty is decreasing worldwide, both in percentage and in absolute number. 

To learn more, watch [Hans Rosling in a 2015 film](https://www.gapminder.org/videos/dont-panic-end-poverty/) about the UN goal of eradicating extreme poverty from the world. 

Below, we've also added an interactive dropdown menu for you to visualize `poverty_timeline` graphs for other countries. Note that each dropdown menu selection may take a few seconds to run.

**Code:**

```python
# Just run this cell

all_countries = poverty_map.column('name')
_ = widgets.interact(poverty_timeline, country=list(all_countries))
```

*Output:*

```text
interactive(children=(Dropdown(description='country', options=('Angola', 'Albania', 'Argentina', 'Armenia', 'A…
```

![cat](project1_assets/mario.jpg)
![cat](project1_assets/fuzzles.jpg)

**Mario and Mr. Fuzzles wants to tell you, you're finished!** Congratulations on discovering many important facts about global poverty and demonstrating your mastery of table manipulation and data visualization. Time to submit.

**<span style="color: #BC412B">Remember to add your project partner to your submission on Pensive!</span>** <u>Only one partner should submit to Pensive.</u>

---

To double-check your work, the cell below will rerun all of the autograder tests.

## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `population.csv`

59,297 rows, 3 columns.

| Column | Type |
| --- | --- |
| `geo` | str |
| `time` | int |
| `population_total` | int |

### `life_expectancy.csv`

57,496 rows, 3 columns.

| Column | Type |
| --- | --- |
| `geo` | str |
| `time` | int |
| `life_expectancy_years` | float |

### `child_mortality.csv`

57,497 rows, 3 columns.

| Column | Type |
| --- | --- |
| `geo` | str |
| `time` | int |
| `child_mortality_0_5_year_olds_dying_per_1000_born` | float |

### `fertility.csv`

59,297 rows, 3 columns.

| Column | Type |
| --- | --- |
| `geo` | str |
| `time` | int |
| `children_per_woman_total_fertility` | float |

### `countries.csv`

273 rows, 18 columns.

| Column | Type |
| --- | --- |
| `country` | str |
| `g77_and_oecd_countries` | str |
| `income_groups` | str |
| `is--country` | bool |
| `iso3166_1_alpha2` | str |
| `iso3166_1_alpha3` | str |
| `iso3166_1_numeric` | float |
| `iso3166_2` | str |
| `landlocked` | str |
| `latitude` | float |
| `longitude` | float |
| `main_religion_2008` | str |
| `name` | str |
| `un_state` | bool |
| `unicef_region` | str |
| `unicode_region_subtag` | str |
| `world_4region` | str |
| `world_6region` | str |

### `poverty.csv`

1,099 rows, 3 columns.

| Column | Type |
| --- | --- |
| `geo` | str |
| `time` | int |
| `extreme_poverty_percent_people_below_125_a_day` | float |
