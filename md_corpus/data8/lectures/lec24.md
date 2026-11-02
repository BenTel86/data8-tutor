---
title: "lec24"
lecture: lec24
course: data8
semester: sp26
source: lectures/data8/sp26/lec24/lec24.ipynb
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

## Average (Mean) ##

**Code:**

```python
values = make_array(2, 3, 3, 9)
values
```

**Code:**

```python
sum(values)/len(values)
```

**Code:**

```python
np.average(values)
```

**Code:**

```python
np.mean(values)
```

**Code:**

```python
(2 + 3 + 3 + 9)/4
```

**Code:**

```python
2*(1/4) + 3*(2/4) + 9*(1/4)
```

**Code:**

```python
2*0.25 + 3*0.5 + 9*0.25
```

**Code:**

```python
values_table = Table().with_columns('value', values)
values_table
```

**Code:**

```python
bins_for_display = np.arange(0.5, 10.6, 1)
values_table.hist('value', bins = bins_for_display)
```

**Code:**

```python
## Make array of 10 2s, 20 3s, and 10 9s

new_vals = make_array(2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                      3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                      9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
```

**Code:**

```python
Table().with_column('value', new_vals).hist(bins = bins_for_display)
```

**Code:**

```python
np.average(new_vals)
```

**Code:**

```python
Table().with_column('value', new_vals).hist(bins = bins_for_display)
plots.ylim(-0.04, 0.5)
plots.plot([0, 10], [0, 0], color='grey', lw=2)
plots.scatter(4.25, -0.015, marker='^', color='red', s=100)
plots.title('Average as a Center of Gravity');
```

## Standard Deviation ##

**Code:**

```python
sd_table = Table().with_columns('Value', values)
sd_table
```

**Code:**

```python
average_value = np.mean(values)
average_value
```

**Code:**

```python
deviations = values - average_value
sd_table = sd_table.with_column('Deviation', deviations)
sd_table
```

**Code:**

```python
sum(deviations)
```

**Code:**

```python
sd_table = sd_table.with_column('Squared Deviation', deviations ** 2)
sd_table
```

**Code:**

```python
# Variance of the data:
# mean squared deviation from average

variance = np.mean(deviations ** 2)
variance
```

**Code:**

```python
# Standard Deviation (SD): 
# root mean squared deviation from average
# = square root of the variance

sd = variance ** 0.5
sd
```

**Code:**

```python
np.std(values)
```

## Chebyshev's Bounds: "Tail" Bounds ##

**Code:**

```python
# Proportion in the range "mean +/- 3.5 SDs"
# Chebyshev's bound: this proportion is AT LEAST
z = 3.5
1 - 1/z**2
```

**Code:**

```python
# Proportion in the range "mean +/- 0.5 SDs"
# Chebyshev's bound: this proportion is AT LEAST
z = 0.5
1 - 1/z**2
```

**Code:**

```python
births = Table.read_table('baby.csv').drop('Maternal Smoker')
```

**Code:**

```python
births.labels
```

**Code:**

```python
births.hist(overlay = False)
```

**Code:**

```python
mpw = births.column('Maternal Pregnancy Weight')
mean = np.mean(mpw)
sd = np.std(mpw)
mean, sd
```

**Code:**

```python
within_3_SDs = births.where(
    'Maternal Pregnancy Weight', are.between(mean - 3*sd, mean + 3*sd))
```

**Code:**

```python
# Proportion within 3 SDs of the mean

within_3_SDs.num_rows / births.num_rows
```

**Code:**

```python
# Chebyshev's bound: 
# This proportion should be at least

1 - 1/3**2
```

**Code:**

```python
births.labels
```

**Code:**

```python
# See if Chebyshev's bounds work for distributions with various shapes

for feature in births.labels:
    values = births.column(feature)
    mean = np.mean(values)
    sd = np.std(values)
    print()
    print(feature)
    for z in make_array(2, 3, 4, 5):
        chosen = births.where(feature, are.between(mean - z*sd, mean + z*sd))
        proportion = chosen.num_rows / births.num_rows
        percent = round(proportion * 100, 2)
        print('Average plus or minus', z, 'SDs:', percent, '%')
```

## Standard Units ##

**Code:**

```python
def standard_units(x):
    """Convert array x to standard units."""
    return (x - np.mean(x)) / np.std(x)
```

**Code:**

```python
ages = births.column('Maternal Age')
ages
```

**Code:**

```python
ages_standard_units = standard_units(ages)
ages_standard_units
```

**Code:**

```python
np.mean(ages_standard_units), np.std(ages_standard_units)
```

## Discussion Question

**Code:**

```python
both = Table().with_columns(
    'Age in Years', ages,
    'Age in Standard Units', ages_standard_units
)
both
```

**Code:**

```python
np.mean(ages), np.std(ages)
```

**Code:**

```python
both.hist('Age in Years', bins = np.arange(15, 46, 2))
```

**Code:**

```python
both.hist('Age in Standard Units', bins = np.arange(-2.2, 3.4, 0.35))
plots.xlim(-2, 3.1);
```

## The SD and Bell Shaped Curves

**Code:**

```python
births.hist('Maternal Height', bins = np.arange(56.5, 72.6, 1))
plots.xticks(np.arange(57, 72, 2));
```

Estimates by eye

The average is approximately: 

Locate the point of inflection on the right. The SD is approximately:

**Code:**

```python
heights = births.column('Maternal Height')
np.mean(heights), np.std(heights)
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

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
