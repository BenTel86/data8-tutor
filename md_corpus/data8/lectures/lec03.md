---
title: "lec03"
lecture: lec03
course: data8
semester: sp26
source: lectures/data8/sp26/lec03/lec03.ipynb
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

## New material

### Python fundamentals

Python as a calculator:

**Code:**

```python
2 + 9
```

**Code:**

```python
2 * 4
```

**Code:**

```python
# The line below errors
# * 4
```

**Code:**

```python
2 ** 4
```

**Code:**

```python
# The line below errors 
# 2 * * 4
```

**Code:**

```python
2/9
```

Python understands the order of operations!

**Code:**

```python
2 + 3 * 9
```

**Code:**

```python
(2 + 3) * 9
```

**Code:**

```python
-1 - 1 + 2 * (3 * 4 * 5 / 6) ** 3 + 7 + 8 + 12
```

Floating point vs integer representation

**Code:**

```python
8
```

**Code:**

```python
64 / 8
```

Strings!

**Code:**

```python
'hello'
```

**Code:**

```python
'Data 8'
```

**Code:**

```python
"hello"
```

**Code:**

```python
'I don't ever want to miss class'
```

**Code:**

```python
"I don't ever want to miss class"
```

### Names

**Code:**

```python
a = 2
```

**Code:**

```python
a
```

Names must first be assgined to a value! The line below causes a name error since `b` isn't assigned yet.

**Code:**

```python
b
```

**Code:**

```python
b = 3
```

**Code:**

```python
b
```

**Discussion Question 1**: What will the value of `a` be once the code in the following cell has finished running?

**Code:**

```python
a = 2 
a + 5
```

**Code:**

```python
a = a + 5
a
```

______

**Code:**

```python
a * b
```

**Code:**

```python
a
```

**Code:**

```python
b
```

**Discussion Question 2**: What will the value of `total` be once the code in the following cell has finished running?

**Code:**

```python
total = a + b
total

a = 10
total
```

______

**Code:**

```python
total
```

**Code:**

```python
a
```

**Code:**

```python
total = a + b
total
```

The line below causes a *syntax error*.

**Code:**

```python
a + b = total
```

#### Why Names?

A cell with arithmetic but no names is difficult to interpret.

**Example:** On January 1, 2025, the CA Minimum Wage for Employers with 26 Employees or More increased to $16.50/hour. Calculate the yearly minimum wage of an employee who works for such an employer.

Method 1:

**Code:**

```python
40 * 16.5
```

**Code:**

```python
40 * 52 * 16.5
```

Method 2:

**Code:**

```python
ca_hourly_minimum_wage = 16.50
hours_per_week = 40
weeks_per_year = 52
```

**Code:**

```python
weekly_wages = hours_per_week * ca_hourly_minimum_wage
weekly_wages
```

**Code:**

```python
yearly_wages = weekly_wages * weeks_per_year
yearly_wages
```

### Call Expressions and Arguments

**Code:**

```python
abs(-5)
```

**Code:**

```python
abs(1 - 3)
```

Names can help us with inputs (called **arguments** in computer science jargon) to functions!

**Code:**

```python
day_temp = 52
night_temp = 47
abs(night_temp - day_temp)
```

Functions can take multiple arguments.

**Code:**

```python
min(14, 15)
```

Some functions can be called with a single argument *or* with multiple arguments!

**Code:**

```python
round(123.456)
```

**Code:**

```python
round(123.456, 1)
```

**STOP**

**Code:**

```python
round(123.456, ndigits=1)
```

In the third line, `ndigits` is a **named argument**.

How did I know that `ndigits` would work as a name? You can use `?` to figure out everything you want to know about a function.

**Code:**

```python
round?
```

**Code:**

```python
round(number=123.456)
```

The line below causes a type error because the wrong name was used.

**Code:**

```python
round(123.456, digs=1)
```

### Tables

#### Example: Ice cream

**Code:**

```python
cones = Table.read_table('cones.csv')
cones
```

**Code:**

```python
cones.show(3)
```

**Code:**

```python
cones.show()
```

**Table Operations**

**Code:**

```python
cones.select('Flavor')
```

**Code:**

```python
cones.select('Flavor', 'Price')
```

The line below causes an error because `Flavor` is not a name, but rather, a *column* in the `cones` table.

**Code:**

```python
cones.select(Flavor, 'Price')
```

**Code:**

```python
cones.drop('Price')
```

**Code:**

```python
cones
```

**Code:**

```python
cones_without_price = cones.drop('Price')
cones_without_price
```

**Code:**

```python
cones.where('Flavor', 'chocolate')
```

**Code:**

```python
cones.sort('Price')
```

**Code:**

```python
cones.sort('Price', descending=True)
```

**Code:**

```python
cones.sort('Flavor', descending=True)
```

### Example 2: Basketball

**Code:**

```python
# From https://github.com/erikgregorywebb/datasets/blob/master/nba-salaries.csv
nba = Table.read_table('nba_salaries.csv')
nba
```

**Code:**

```python
point_guards = nba.where('position', 'PG').where('season', 2020)
```

**Code:**

```python
point_guards
```

**Code:**

```python
point_guards.drop('position')
```

**Code:**

```python
point_guards
```

**Code:**

```python
point_guards = point_guards.drop('rank', 'position', 'season')
```

**Code:**

```python
point_guards.show(10)
```

**Code:**

```python
point_guards.sort('salary').show(10)
```

**Code:**

```python
point_guards.sort('salary', descending=True).show(10)
```

The order of the computations does matter!

**Discussion Question**: Which one of the following two lines of code fail?

**Code:**

```python
nba.drop('position').where('position', 'PG')
```

**Code:**

```python
nba.where('position', 'PG').drop('position')
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `cones.csv`

6 rows, 3 columns.

| Column | Type |
| --- | --- |
| `Flavor` | str |
| `Color` | str |
| `Price` | float |

### `nba_salaries.csv`

9,456 rows, 6 columns.

| Column | Type |
| --- | --- |
| `rank` | int |
| `name` | str |
| `position` | str |
| `team` | str |
| `salary` | int |
| `season` | int |
