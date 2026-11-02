---
title: "US Census Visualization"
lecture: lec07
course: data8
semester: sp26
source: lectures/data8/sp26/lec07/lec07.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Lecture 7 ##

## Review

**Code:**

```python
united_flights = Table.read_table('united.csv')
united_flights.show(2)
```

**Discussion Question:** On what fraction of days was flight 73 delayed?

**Code:**

```python
#  (# of times that 73 was delayed) / (# of times that 73 existed)
flight73 = united_flights.where('Flight Number', 73)
flight73.where('Delay', are.above(0)).num_rows / flight73.num_rows
```

# US Census Visualization

**Code:**

```python
full = Table.read_table('nc-est2019-agesex-res.csv')
partial = full.where('AGE', are.below(100)).select('SEX', 'AGE', 'POPESTIMATE2019')
us_pop_2019 = partial.relabeled(2, '2019')
us_pop_2019.show(5)
```

**Code:**

```python
us_pop_2019.where('SEX', 0).plot('AGE', '2019')
```

**Code:**

```python
us_pop_2019.where('SEX', 0).scatter('AGE', '2019')
```

What does the expression below compute?

**Code:**

```python
np.average(us_pop_2019.where('SEX', 0).column('AGE'))
```

Answer: 
- Not the average age of a person in the US in 2019!
- The average of all numbers from 0 to 99
- This expression isn't about the US population at all!

How would you compute the average age of people in the US in 2019?
- (Total age of all people) / (# of people)
- (Sum over ages of age times # of people of that age) / (# of people)

**Code:**

```python
everyone = us_pop_2019.where('SEX', 0)
total_years = sum(everyone.column('AGE') * everyone.column('2019'))
total_people = sum(everyone.column('2019'))
total_years / total_people
```

## Males vs Females

**Code:**

```python
# Let's compare male and female counts per age
males = us_pop_2019.where('SEX', 1).drop('SEX')
females = us_pop_2019.where('SEX', 2).drop('SEX')
```

**Code:**

```python
pop_2019 = Table().with_columns(
    'Age', males.column('AGE'),
    'Males', males.column('2019'),
    'Females', females.column('2019')
)
pop_2019
```

**Code:**

```python
pop_2019.plot('Age')
```

## Scatter Plots ##

**Code:**

```python
# Actors and their highest grossing movies
actors = Table.read_table('actors.csv')
actors
```

**Code:**

```python
actors.scatter('Number of Movies', 'Total Gross')
```

**Code:**

```python
actors.scatter('Number of Movies', 'Average per Movie')
```

**Code:**

```python
actors.where('Average per Movie', are.above(400))
```

## Bar Charts ##

**Code:**

```python
# Highest grossing movies as of 2017
top_movies = Table.read_table('top_movies_2017.csv')
top_movies
```

**Code:**

```python
top10_adjusted = top_movies.take(np.arange(10))
top10_adjusted
```

**Code:**

```python
# Convert to millions of dollars for readability
millions = np.round(top10_adjusted.column('Gross (Adjusted)') / 1000000, 3)
top10_adjusted = top10_adjusted.with_column('Millions', millions)
top10_adjusted
```

**Code:**

```python
# A line plot doesn't make sense here: don't do this!
top10_adjusted.plot('Year', 'Millions')
```

**Code:**

```python
top10_adjusted.barh('Title', 'Millions')
```

Exercise: Generate the chart shown in the slides: a bar chart of age (# years since release) for the 10 highest grossing movies (non-adjusted).

**Code:**

```python
# Get a table of the top 10 grossing movies (not adjusted for increasing ticket prices)
#  - sort then take *
# Compute the age of each of these movies
#  - get an array of the years they were released and subtract from 2026 *
# Put it all together in a bar chart
#  - use with_column to put ages into the table and then use barh

top10 = top_movies.sort('Gross', descending=True).take(np.arange(10))
ages = 2026 - top10.column('Year')
top10_with_age = top10.with_column('Age in 2026', ages)
top10_with_age.barh('Title', 'Age in 2026')
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `united.csv`

13,825 rows, 4 columns.

| Column | Type |
| --- | --- |
| `Date` | str |
| `Flight Number` | int |
| `Destination` | str |
| `Delay` | int |

### `nc-est2019-agesex-res.csv`

306 rows, 14 columns.

| Column | Type |
| --- | --- |
| `SEX` | int |
| `AGE` | int |
| `CENSUS2010POP` | int |
| `ESTIMATESBASE2010` | int |
| `POPESTIMATE2010` | int |
| `POPESTIMATE2011` | int |
| `POPESTIMATE2012` | int |
| `POPESTIMATE2013` | int |
| `POPESTIMATE2014` | int |
| `POPESTIMATE2015` | int |
| `POPESTIMATE2016` | int |
| `POPESTIMATE2017` | int |
| `POPESTIMATE2018` | int |
| `POPESTIMATE2019` | int |

### `actors.csv`

50 rows, 6 columns.

| Column | Type |
| --- | --- |
| `Actor` | str |
| `Total Gross` | float |
| `Number of Movies` | int |
| `Average per Movie` | float |
| `#1 Movie` | str |
| `Gross` | float |

### `top_movies_2017.csv`

200 rows, 5 columns.

| Column | Type |
| --- | --- |
| `Title` | str |
| `Studio` | str |
| `Gross` | int |
| `Gross (Adjusted)` | int |
| `Year` | int |
