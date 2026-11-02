---
title: "Bootstrap"
lecture: lec22
course: data8
semester: sp26
source: lectures/data8/sp26/lec22/lec22.ipynb
language: python
---

**Code:**

```python
from datascience import *
%matplotlib inline

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np

import warnings
warnings.simplefilter("ignore")
```

## Percentiles ##

**Code:**

```python
# Manually compute the 55th percentile.
x = make_array(43, 20, 51, 7, 28, 34)
```

**Code:**

```python
# Step 1. Sort the data
np.sort(x)
```

**Code:**

```python
# Step 2. Figure out where 55th percentile would be.
```

**Code:**

```python
np.arange(1, 7)/6
```

**Code:**

```python
np.arange(1, 7)/6 >= 55/100
```

**Code:**

```python
np.sort(x).item(3)
```

**Code:**

```python
# Alternatively: One line of code
percentile(55, x)
```

## Discussion Question

**Code:**

```python
s = make_array(1, 3, 5, 7, 9)
```

**Code:**

```python
percentile(10, s) == 0
```

**Code:**

```python
percentile(39, s) == percentile(40, s)
```

**Code:**

```python
percentile(40, s) == percentile(41, s)
```

**Code:**

```python
percentile(50, s) == 5
```

## Inference: Estimation

**Code:**

```python
sf = Table.read_table('san_francisco_2019.csv')
sf.show(3)
```

**Code:**

```python
# Who made the most money
sf.sort('Total Compensation', descending=True).show(5)
```

**Code:**

```python
# Who made the least money
sf.sort('Total Compensation', descending=False).show(5)
```

**Code:**

```python
# $15/hr, 20 hr/wk, 50 weeks

min_salary = 15 * 20 * 50
sf = sf.where('Salary', are.above(min_salary))
```

**Code:**

```python
# Population Distribution

sf_bins = np.arange(0, 726000, 25000)
sf.hist('Total Compensation', bins=sf_bins)
```

**Code:**

```python
# An Empirical Distribution

our_sample = sf.sample(400, with_replacement=False)
our_sample.hist('Total Compensation', bins=sf_bins)
```

**Code:**

```python
# Parameter: Median Total Compensation 

pop_median = percentile(50, sf.column('Total Compensation'))
pop_median
```

**Code:**

```python
# Estimate: Median of a Sample

percentile(50, our_sample.column('Total Compensation'))
```

## Variability of the Estimate

**Code:**

```python
def generate_sample_median(samp_size):
    new_sample = sf.sample(samp_size, with_replacement=False)
    return percentile(50, new_sample.column('Total Compensation'))
```

**Code:**

```python
generate_sample_median(400)
```

## Quantifying Uncertainty

**Code:**

```python
sample_medians = make_array()

for i in np.arange(1000):
    new_median = generate_sample_median(400)
    sample_medians = np.append(sample_medians, new_median)
```

**Code:**

```python
med_bins = np.arange(120000, 160000, 2000)
Table().with_column('Sample Medians', sample_medians).hist(bins=med_bins)

plots.ylim(-0.000005, 0.00014)
plots.scatter(pop_median, 0, color='red');
```

**Code:**

```python
print('Less than 2.5% of estimates are more than', pop_median - percentile(2.5, sample_medians), 'lower than', pop_median)
print('Less than 2.5% of estimates are more than', percentile(97.5, sample_medians) - pop_median, 'higher than', pop_median)
```

# Bootstrap

Sample randomly
 - from the original sample
 - with replacement
 - the same number of times as the original sample size

**Code:**

```python
# Default behavior of t.sample():
# at random with replacement,
# the same number of times as the number of rows in t

bootstrap_sample = our_sample.sample()
bootstrap_sample.hist('Total Compensation', bins=sf_bins)
percentile(50, bootstrap_sample.column('Total Compensation'))
```

**Code:**

```python
def one_bootstrap_median():
    # draw the bootstrap sample
    resample = our_sample.sample()
    # return the median total compensation in the bootstrap sample
    return percentile(50, resample.column('Total Compensation'))
```

**Code:**

```python
one_bootstrap_median()
```

**Code:**

```python
# Generate the medians of 1000 bootstrap samples
num_repetitions = 1000
bstrap_medians = make_array()
for i in np.arange(num_repetitions):
    bstrap_medians = np.append(bstrap_medians, one_bootstrap_median())
```

**Code:**

```python
resampled_medians = Table().with_column('Bootstrap Sample Median', bstrap_medians)
median_bins=np.arange(120000, 160000, 2000)
resampled_medians.hist(bins = median_bins)

# Plotting parameters; you can ignore this code
parameter_green = '#32CD32'
plots.ylim(-0.000005, 0.00014)
plots.scatter(pop_median, 0, color=parameter_green, s=40, zorder=2)
plots.title('Bootstrap Medians and the Parameter (Green Dot)');
```

## Percentile Method: Middle 95% of the Bootstrap Estimates

**Code:**

```python
left = percentile(2.5, bstrap_medians)
right = percentile(97.5, bstrap_medians)

make_array(left, right)
```

**Code:**

```python
resampled_medians.hist(bins = median_bins)

# Plotting parameters; you can ignore this code
plots.ylim(-0.000005, 0.00014)
plots.plot(make_array(left, right), make_array(0, 0), color='yellow', lw=3, zorder=1)
plots.scatter(pop_median, 0, color=parameter_green, s=40, zorder=2);
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

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
