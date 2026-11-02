---
title: "lec25"
lecture: lec25
course: data8
semester: sp26
source: lectures/data8/sp26/lec25/lec25.ipynb
language: python
---

**Code:**

```python
import matplotlib
from datascience import *
%matplotlib inline
import matplotlib.pyplot as plots
import numpy as np
plots.style.use('fivethirtyeight')
```

## Standard Units

**Code:**

```python
exams = Table.read_table('exams_fa18.csv')
exams.show(5)
```

**Code:**

```python
exams.hist(overlay=False, bins=np.arange(0,101,5))
```

**Code:**

```python
def standard_units(x):
    """Convert array of values to standard units"""
    return (x - np.average(x)) / np.std(x)
```

**Code:**

```python
midterm_su = standard_units(exams.column('Midterm'))
exams = exams.with_column('Midterm in Standard Units', midterm_su)

final_su = standard_units(exams.column('Final'))
exams = exams.with_column('Final in Standard Units', final_su)

exams.show(10)
```

**Code:**

```python
exams.select(
    'Midterm in Standard Units', 'Final in Standard Units'
).hist(overlay=False, bins=np.arange(-4,2,0.1))
```

## The SD and Bell Shaped Curves

**Code:**

```python
births = Table.read_table('baby.csv')
```

**Code:**

```python
births.hist('Maternal Height', bins = np.arange(56.5, 72.6, 1))
```

**Code:**

```python
heights = births.column('Maternal Height')
np.mean(heights), np.std(heights)
```

**Code:**

```python
# 1 SD below & above the mean
np.mean(heights) - np.std(heights), np.mean(heights) + np.std(heights)
```

## Central Limit Theorem ##

**Code:**

```python
united = Table.read_table('united.csv')
united
```

**Code:**

```python
united_bins = np.arange(-20, 300, 10)
united.hist('Delay', bins=united_bins)
```

**Code:**

```python
delays = united.column('Delay')
delay_mean = np.mean(delays)
delay_sd = np.std(delays)
delay_mean, delay_sd
```

**Code:**

```python
percentile(50, delays)
```

**Code:**

```python
def one_sample_mean(sample_size):
    """ 
    Takes a sample from the population of flights 
    and computes its mean
    """
    sampled_flights = united.sample(sample_size)
    return np.mean(sampled_flights.column('Delay'))
```

**Code:**

```python
one_sample_mean(100)
```

**Code:**

```python
def ten_thousand_sample_means(sample_size):
    means = make_array()
    for i in np.arange(10000):
        mean = one_sample_mean(sample_size)
        means = np.append(means, mean)
    return means
```

**Code:**

```python
sample_means_100 = ten_thousand_sample_means(100)
```

**Code:**

```python
sample_means_100
```

**Code:**

```python
len(sample_means_100)
```

**Code:**

```python
Table().with_column(
    'Mean of 100 flight delays', sample_means_100).hist(bins=20)

print('Population Average:', delay_mean)
```

**Code:**

```python
sample_means_400 = ten_thousand_sample_means(400)
Table().with_column(
    'Mean of 400 flight delays', sample_means_400).hist(bins=20)

print('Population Average:', delay_mean)
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `exams_fa18.csv`

1,242 rows, 2 columns.

| Column | Type |
| --- | --- |
| `Midterm` | float |
| `Final` | float |

### `baby.csv`

1,174 rows, 6 columns.

| Column | Type |
| --- | --- |
| `Birth Weight` | int |
| `Gestational Days` | int |
| `Maternal Age` | int |
| `Maternal Height` | int |
| `Maternal Pregnancy Weight` | int |
| `Maternal Smoker` | bool |

### `united.csv`

13,825 rows, 4 columns.

| Column | Type |
| --- | --- |
| `Date` | str |
| `Flight Number` | int |
| `Destination` | str |
| `Delay` | int |
