---
title: "Lecture 11 #"
lecture: lec11
course: data8
semester: sp26
source: lectures/data8/sp26/lec11/lec11.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter(action='ignore',category=np.VisibleDeprecationWarning)
```

# Lecture 11 #

### Rows from lists

**Code:**

```python
Table().with_columns('Numbers', [1, 2, 3])
```

**Code:**

```python
drinks = Table(['Drink', 'Cafe', 'Price'])
drinks
```

**Code:**

```python
drinks = drinks.with_rows([
    ['Milk Tea', 'Asha', 5.5],
    ['Espresso', 'Strada',  1.75],
    ['Latte',    'Strada',  3.25],
    ['Espresso', "FSM",   2]
])
drinks
```

## Cross-classification: grouping by two columns

**Code:**

```python
survey = Table.read_table('welcome_survey_sp26.csv')
survey.show(3)
```

**Code:**

```python
survey.group(['Handedness', 'Sleep Position']).show()
```

**Code:**

```python
survey.group(['Handedness', 'Sleep Position'], np.average).show()
```

## Pivot Tables

**Code:**

```python
survey.group('Handedness')
```

**Code:**

```python
survey.pivot('Sleep Position', 'Handedness')
```

**Code:**

```python
survey.pivot('Sleep Position', 
             'Handedness', 
             values='Sleep Hours', 
             collect=np.average)
```

## Discussion Questions ##

**Code:**

```python
# From the CORGIS Dataset Project
# By Austin Cory Bart acbart@vt.edu
# Version 2.0.0, created 3/22/2016
# https://corgis-edu.github.io/corgis/csv/skyscrapers/

sky = Table.read_table('skyscrapers.csv')
sky = (sky.with_column('age', 2022 - sky.column('completed'))
          .drop('completed'))
sky.show(3)
```

**Code:**

```python
# 1. For each city, what’s the height of the tallest building for each material?

sky.pivot('material', 'city', 'height', max)
```

**Code:**

```python
# 2. For each city, what’s the height difference between the tallest 
#    steel building and the tallest concrete building?
```

**WARNING: ANSWERS BELOW**

**Code:**

```python
sky.select('material', 'city', 'height').group(['city', 'material'], collect=max)
```

**Code:**

```python
tallest = sky.pivot('material', 'city', values='height', collect=max)
tallest.show()
```

**Code:**

```python
diffs = Table().with_columns(
    'city', tallest.column('city'),
    'difference', abs(tallest.column('steel') - tallest.column('concrete'))
)
diffs
```

**Code:**

```python
diffs.sort('difference', descending=True)
```

**Code:**

```python
# 3. Generate a table of the names of the oldest buildings for each 
#    material for each city:

# Hint: You can use sort to find the name of the oldest building in the dataset
sky.sort('age', descending=True).column('name').item(0)
```

**WARNING: ANSWERS BELOW**

**Code:**

```python
def first(s):
    "Return the first element in an array."
    return s.item(0)

(sky
 .sort('age', descending=True)
 .pivot('material', 'city', 'name', first)
)#.where('city', 'San Francisco')
```

## Joins ##

**Code:**

```python
drinks
```

**Code:**

```python
discounts = Table().with_columns(
    'Coupon % off', make_array(10, 25, 5),
    'Location', make_array('Asha', 'Strada', 'Asha')
)
discounts
```

**Code:**

```python
combined = drinks.join('Cafe', discounts, 'Location')
combined
```

**Code:**

```python
discounted_frac = 1 - combined.column('Coupon % off') / 100
combined.with_column(
    'Discounted Price', 
    combined.column('Price') * discounted_frac
)
```

**Code:**

```python
drinks.join('Cafe', drinks, 'Cafe')
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `welcome_survey_sp26.csv`

1,067 rows, 7 columns.

| Column | Type |
| --- | --- |
| `Year` | int |
| `Extroversion` | int |
| `Text Recipients` | int |
| `Sleep Hours` | float |
| `Handedness` | str |
| `Sleep Position` | str |
| `Piercings` | int |

### `skyscrapers.csv`

1,781 rows, 5 columns.

| Column | Type |
| --- | --- |
| `name` | str |
| `material` | str |
| `city` | str |
| `height` | float |
| `completed` | int |
