---
title: "lec37"
lecture: lec37
course: data8
semester: sp26
source: lectures/data8/sp26/lec37/lec37.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

import warnings
warnings.simplefilter("ignore")
```

**Code:**

```python
# np.array(list) converts list to an array
# provided all the elements of list are of the same type

n = 100
second = round(n * 0.6)
third = round(n * 0.4)

year = np.array(['Second'] * second + ['Third'] * third)
major = np.array(['Declared'] * (round(second * 0.5)) + ['Undeclared'] * (round(second * 0.5)) + \
                 ['Declared'] * (round(third * 0.8))  + ['Undeclared'] * (round(third * 0.2)))
                 
students = Table().with_columns(
    'Year', year,
    'Major', major
)
```

**Code:**

```python
def create_population(prior_disease_prob, n):
    disease = round(n * prior_disease_prob)
    no_disease = round(n * (1 - prior_disease_prob))

    status = np.array(['Disease'] * disease  +  ['No disease'] * no_disease)
    result = np.array(['Test +'] * (disease) + ['Test +'] * (round(no_disease * 0.05))  + \
                 ['Test -'] * (round(no_disease * 0.95)))
                 
    t = Table().with_columns(
    'Status', status,
    'Test Result', result
    )
    return t.pivot('Test Result', 'Status')
```

## More Likely Than Not ##

**Code:**

```python
students.show(3)
```

*Output:*

| Year | Major |
| --- | --- |
| Second | Declared |
| Second | Declared |
| Second | Declared |

**Code:**

```python
students.group('Year')
```

*Output:*

| Year | count |
| --- | --- |
| Second | 60 |
| Third | 40 |

**Code:**

```python
students.where('Year', 'Second').group('Major')
```

*Output:*

| Major | count |
| --- | --- |
| Declared | 30 |
| Undeclared | 30 |

**Code:**

```python
students.where('Year', 'Third').group('Major')
```

*Output:*

| Major | count |
| --- | --- |
| Declared | 32 |
| Undeclared | 8 |

**Code:**

```python
32 / (32 + 8)
```

*Output:*

```text
0.8
```

**Code:**

```python
students.pivot('Major', 'Year')
```

*Output:*

| Year | Declared | Undeclared |
| --- | --- | --- |
| Second | 30 | 30 |
| Third | 32 | 8 |

**Code:**

```python
# Chance of second year, given that they have declared
# P(second year | declared)

30 / (30 + 32)
```

*Output:*

```text
0.4838709677419355
```

**Code:**

```python
# P(third year | declared)

32 / (30 + 32)
```

*Output:*

```text
0.5161290322580645
```

## Tree Diagram Calculation

**Code:**

```python
# P(second year | declared), from tree diagram

(0.6 * 0.5) / (0.6 * 0.5 + 0.4 * 0.8)
```

## Decisions ##

**Code:**

```python
create_population(1/1000, 10000)
```

**Code:**

```python
10 / 510
```

**Code:**

```python
# P(disease | tested +)

# = P(disease & tested +) / P(tested +)

# if prior probability of disease is 1/10

(0.1 * 1) / (0.1*1 + 0.9*0.05)
```

*Output:*

```text
0.689655172413793
```

**Code:**

```python
create_population(1/10, 10000)
```

**Code:**

```python
# P(disease | tested +)
# if prior probability of disease is 0.5

(0.5 * 1) / (0.5*1 + 0.5*0.05)
```

**Code:**

```python
create_population(1/2, 10000)
```
