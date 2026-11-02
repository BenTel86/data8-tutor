---
title: "Lecture 14"
lecture: lec14
course: data8
semester: sp26
source: lectures/data8/sp26/lec14/lec14.ipynb
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

# Lecture 14

## Random Sampling ##

We load in a dataset of all United flights national flights from 6/1/15 to 8/9/15, their destination and how long they were delayed, in minutes.

**Code:**

```python
united = Table.read_table('united.csv')
united = united.with_column('Row', np.arange(united.num_rows)).move_to_start('Row')
united
```

Some deterministic samples:

**Code:**

```python
united.where('Destination', 'JFK')
```

**Code:**

```python
united.take(np.arange(0, united.num_rows, 1000))
```

**Code:**

```python
united.take(make_array(34, 6321, 10040))
```

Random samples:

**Code:**

```python
united.sample(5, with_replacement=False).sort('Row')
```

**Code:**

```python
rows = np.random.choice(np.arange(united.num_rows), 5, replace=False)
united.take(rows).sort('Row')
```

**Code:**

```python
start = np.random.choice(np.arange(1000))
systematic_sample = united.take(np.arange(start, united.num_rows, 1000))
systematic_sample.show()
```

## Distributions ##

**Code:**

```python
die = Table().with_column('Face', np.arange(1, 7))
die
```

**Code:**

```python
die.sample(10)
```

**Code:**

```python
die.hist()
```

**Code:**

```python
roll_bins = np.arange(0.5, 6.6, 1)
```

**Code:**

```python
die.hist(bins=roll_bins)
```

**Code:**

```python
die.sample(10).hist(bins=roll_bins)
```

**Code:**

```python
die.sample(1000).hist(bins=roll_bins)
```

**Code:**

```python
die.sample(100000).hist(bins=roll_bins)
```

## Large Random Samples ##

**Code:**

```python
united
```

**Code:**

```python
united_bins = np.arange(-20, 201, 5)
united.hist('Delay', bins = united_bins)
```

**Code:**

```python
min(united.column('Delay'))
```

**Code:**

```python
max(united.column('Delay'))
```

**Code:**

```python
np.average(united.column('Delay'))
```

**Code:**

```python
united.sample(10).hist('Delay', bins = united_bins)
```

**Code:**

```python
united.sample(1000).hist('Delay', bins = united_bins)
```

## Simulating Statistics ##

**Code:**

```python
np.median(united.column('Delay'))
```

**Code:**

```python
np.median(united.sample(10).column('Delay'))
```

**Code:**

```python
def sample_median(size):
    return np.median(united.sample(size).column('Delay'))
```

**Code:**

```python
sample_median(10)
```

**Code:**

```python
sample_medians = make_array()

for i in np.arange(1000):
    new_median = sample_median(10)
    sample_medians = np.append(sample_medians, new_median)
```

**Code:**

```python
Table().with_column('Sample medians', sample_medians).hist(bins = np.arange(-10,31))
```

**Code:**

```python
sample_medians = make_array()

for i in np.arange(1000):
    new_median = sample_median(1000)
    sample_medians = np.append(sample_medians, new_median)
```

**Code:**

```python
Table().with_column(
    'Sample medians', sample_medians).hist(bins = np.arange(-10,31))
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
