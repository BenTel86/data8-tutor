---
title: "Lecture 9: Functions #"
lecture: lec09
course: data8
semester: sp26
source: lectures/data8/sp26/lec09/lec09.ipynb
language: python
---

# Lecture 9: Functions #

**Code:**

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Histogram Example

**Code:**

```python
# From https://womenintheworld.org/highest-paid-actress/
incomes = Table.read_table('2022_female_actors.csv')
incomes.show(3)
```

**Code:**

```python
my_bins = make_array(0, 25, 30, 60)
incomes.hist('Income (millions)', bins=my_bins)
```

**Code:**

```python
min(incomes.column(1))
```

**Code:**

```python
my_bins = make_array(min(incomes.column(1)), 25, 30, 60)
incomes.hist('Income (millions)', bins=my_bins)
```

**Code:**

```python
incomes.hist('Income (millions)')
```

**Code:**

```python
incomes.hist('Income (millions)', bins=20)
```

## Defining Functions ##

Example: Create a function that takes a numerical input and triples it: $\textsf{triple}(x)=3\,x$

**Code:**

```python
def triple(x):
    return 3 * x
```

**Code:**

```python
triple(3)
```

We can also assign a value to a name, and call the function on the name:

**Code:**

```python
num = 4
```

**Code:**

```python
triple(num)
```

**Code:**

```python
triple(num * 5)
```

## The Anatomy of a Function ##  
    
```python
def functionname(Arguments_Parameters_Expressions_or_Values):     
      return return_expression
```

## Functions are Type-Agnostic  ##

**Code:**

```python
triple('ha')
```

**Code:**

```python
np.arange(4)
```

Feed the array above into our function `triple` to see what is produced:

**Code:**

```python
triple(np.arange(4))
```

### Discussion ###

- What does the following function do?
- What type of input does it take?
- What type of output does it produce?
- What's a good name for the function?

```python
def f(s):     
      return np.round(s / sum(s) * 100, 2)
```

**Code:**

```python
def percent_of_total(s):
    return np.round(s / sum(s) * 100, 2)
```

**Code:**

```python
first_four=make_array(1,2,3,4)
first_four
```

**Code:**

```python
percent_of_total(first_four)
```

**Code:**

```python
percent_of_total(make_array(1, 213, 38))
```

### Functions Can Take Multiple Arguments ###

Example: Calculate the Hypotenuse Length of a Right Triangle


Pythagoras's Theorem: If $x$ and $y$ denote the lengths of the right-angle sides, then the hypotenuse length $h$ satisfies:

$$ h^2 = x^2 + y^2 \qquad \text{which implies}\qquad \hspace{20 pt} h = \sqrt{ x^2 + y^2 } $$

**Code:**

```python
def hypotenuse(x, y):
    hypot_squared = (x ** 2 + y ** 2)
    hypot = hypot_squared ** 0.5
    return hypot
```

**Code:**

```python
hypotenuse(1, 2)
```

**Code:**

```python
hypotenuse(3, 4)
```

We could've typed the body all in one line. Do you find this more readable or less readable than the original version?

**Code:**

```python
def hypotenuse(x,y):
    return (x ** 2 + y ** 2) ** 0.5
```

**Code:**

```python
hypotenuse(9, 12)
```

### Example: A function that takes the year of birth of a person and produces their age in years. ###

**Code:**

```python
def age(year):
    age = 2026 - year
    return age
```

**Code:**

```python
age(1980)
```

Now add some bells and whistles:  Take person's name and year of birth (two arguments). Produce a sentence that states how old they are.

**Code:**

```python
def name_and_age(name, year):
    return name + ' is ' + str(age(year)) + ' years old.'
```

**Code:**

```python
name_and_age('John', 1980)
```

### A stratey for defining functions: ###
- Give generic, descriptive names to some example inputs.
- Try writing the code that gives you the right output for that example.
- Once that works, put that code into a `def` statement (without the example; with a `return`).
- Try calling it on some different example inputs (to make sure it's flexible).

For example, to write a function that computes the sum of the first `k` values in a column of a table.

**Code:**

```python
t = incomes                  # A generic name for an example table
label = 'Income (millions)'  # A generic name for an example column label
k = 5                        # A generic name for an example value of k
t.take(np.arange(k)).column(label).sum()
```

**Code:**

```python
def sum_first_k(t, label, k):
    "Sum the first k values in the label column of Table t."
    return t.take(np.arange(k)).column(label).sum()
```

**Code:**

```python
sum_first_k(incomes, 'Income (millions)', 10)
```

## Apply ##

**Code:**

```python
ages = Table().with_columns(
    'Person', make_array('Jim', 'Pam', 'Michael', 'Creed'),
    'Birth Year', make_array(1985, 1988, 1967, 1904)
)
ages
```

**Code:**

```python
ages.apply(age, 'Birth Year')
```

**Code:**

```python
make_array(age(ages.column('Birth Year').item(0)),
           age(ages.column('Birth Year').item(1)),
           age(ages.column('Birth Year').item(2)),
           age(ages.column('Birth Year').item(3)))
```

**Code:**

```python
ages.apply(name_and_age, 'Person', 'Birth Year')
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `2022_female_actors.csv`

20 rows, 2 columns.

| Column | Type |
| --- | --- |
| `Name` | str |
| `Income (millions)` | float |
