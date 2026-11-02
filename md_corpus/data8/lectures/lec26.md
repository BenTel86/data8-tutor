---
title: "lec26"
lecture: lec26
course: data8
semester: sp26
source: lectures/data8/sp26/lec26/lec26.ipynb
language: python
---

**Code:**

```python
import warnings
warnings.filterwarnings('ignore')
import matplotlib
from datascience import *
%matplotlib inline
import matplotlib.pyplot as plots
import numpy as np
plots.style.use('fivethirtyeight')

import warnings
warnings.simplefilter(action='ignore')
```

## Distribution of the Sample Average

**Code:**

```python
united = Table.read_table('united.csv')
united_bins = np.arange(-20, 300, 10)
united.hist('Delay', bins=united_bins)
```

**Code:**

```python
delays = united.column('Delay')
population_mean = np.mean(delays)
population_sd = np.std(delays)
population_mean, population_sd
```

**Code:**

```python
def one_sample_mean(sample_size):
    """Take a sample from the population of flights and compute its mean"""
    sampled_flights = united.sample(sample_size)
    return np.mean(sampled_flights.column('Delay'))
```

**Code:**

```python
def ten_thousand_sample_means(sample_size):
    """Approximate the distribution of the sample mean"""
    means = make_array()
    for i in np.arange(10000):
        mean = one_sample_mean(sample_size)
        means = np.append(means, mean)
    return means
```

**Code:**

```python
sample_means_400 = ten_thousand_sample_means(400)
Table().with_column('Mean of 400 flight delays', sample_means_400).hist(bins=20)
print('Population Average:', population_mean)
```

## Center of this Probability Distribution

**Code:**

```python
np.mean(sample_means_400), population_mean
```

## The Number of Possible Samples of size 400
How many possible ways are there that the sample could have come out?

**Code:**

```python
united.num_rows
```

**Code:**

```python
# How many possible samples are there?
united.num_rows ** 400
```

## Increasing the Sample Size

**Code:**

```python
sample_means_900 = ten_thousand_sample_means(900)
```

**Code:**

```python
means_tbl = Table().with_columns(
    '400', sample_means_400,
    '900', sample_means_900
)
```

**Code:**

```python
means_tbl.hist(bins = np.arange(5, 31, 0.5))
plots.title('Distribution of Sample Average');
```

### Relationship Between Population SD and Sample Size

**Code:**

```python
"""Empirical distribution of random sample means"""
def plot_sample_means(sample_size):
    sample_means = ten_thousand_sample_means(sample_size)
    sample_means_tbl = Table().with_column('Sample Means', sample_means)
    
    # Print some information about the distribution of the sample means
    print("Sample size: ", sample_size)
    print("Population mean:", population_mean)
    print("Average of sample means: ", np.mean(sample_means))
    print("Population SD:", population_sd)
    print("SD of sample means:", np.std(sample_means))

    # Plot a histogram of the sample means
    sample_means_tbl.hist(bins=20)
    plots.xlabel('Sample Means')
    plots.title('Sample Size ' + str(sample_size))
```

**Code:**

```python
plot_sample_means(100)
```

**Code:**

```python
# Sample size 100
# population_SD / SD_of_sample_means
39.48 / 3.998
```

**Code:**

```python
plot_sample_means(400)
```

**Code:**

```python
# Sample size 400
# population_SD / SD_of_sample_means
39.48 / 1.992
```

**Code:**

```python
plot_sample_means(625)
```

**Code:**

```python
# Sample size 625
# population_SD / SD_of_sample_means
39.48 / 1.567
```

**Code:**

```python
39.48 / np.sqrt(100)
```

**Code:**

```python
39.48 / np.sqrt(400)
```

**Code:**

```python
39.48 / np.sqrt(625)
```

## Variability of the Sample Mean

**Code:**

```python
# Warning: this cell will take a long time to run!
sample_sizes = np.arange(100, 950, 50)

sample_mean_sds = make_array()
for n in sample_sizes:
    sample_means = ten_thousand_sample_means(n)
    sample_mean_sds = np.append(sample_mean_sds, np.std(sample_means))
```

**Code:**

```python
sd_table = Table().with_columns(
    'Sample size', sample_sizes,
    'SD of simulated sample means', sample_mean_sds,
    'Pop SD / sqrt(sample size)', population_sd / np.sqrt(sample_sizes),
)
sd_table
```

**Code:**

```python
sd_table.scatter('Sample size')
```

## Other distributions

**Code:**

```python
sf_salaries = Table.read_table("san_francisco_2019.csv")
sf_salaries.hist("Salary")
```

**Code:**

```python
def one_sample_mean(sample_size):
    """Take a sample from the population of flights and compute its mean"""
    sampled_salaries = sf_salaries.sample(sample_size)
    return np.mean(sampled_salaries.column('Salary'))
```

**Code:**

```python
def ten_thousand_sample_means(sample_size):
    """Approximate the distribution of the sample mean"""
    means = make_array()
    for i in np.arange(10000):
        mean = one_sample_mean(sample_size)
        means = np.append(means, mean)
    return means
```

**Code:**

```python
sample_means_400 = ten_thousand_sample_means(400)
Table().with_column('Mean of 400 salaries', sample_means_400).hist(bins=20)
print('Population Average:', np.mean(sf_salaries.column("Salary")))
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

### `san_francisco_2019.csv`

44,525 rows, 8 columns.

| Column | Type |
| --- | --- |
| `Organization Group` | str |
| `Department` | str |
| `Job Family` | str |
| `Job` | str |
| `Salary` | float |
| `Overtime` | float |
| `Benefits` | float |
| `Total Compensation` | float |
