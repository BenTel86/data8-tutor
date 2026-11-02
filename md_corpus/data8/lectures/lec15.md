---
title: "lec15"
lecture: lec15
course: data8
semester: sp26
source: lectures/data8/sp26/lec15/lec15.ipynb
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

## Empirical Distributions of a Statistic

**Code:**

```python
united = Table.read_table('united.csv')
united = united.with_column('Row', np.arange(united.num_rows)).move_to_start('Row')
```

**Code:**

```python
def sample_median(size):
    return np.median(united.sample(size).column('Delay'))
```

**Code:**

```python
# (Population) Parameter
np.median(united.column('Delay'))
```

**Code:**

```python
# (Sample) Statistic
sample_median(10)
```

**Code:**

```python
# (Sample) Statistic
sample_median(100)
```

**Code:**

```python
sample_medians_10 = make_array()
sample_medians_100 = make_array()
sample_medians_1000 = make_array()

num_simulations = 2000

for i in np.arange(num_simulations):
    new_median_10 = sample_median(10)
    sample_medians_10 = np.append(sample_medians_10, new_median_10)
    new_median_100 = sample_median(100)
    sample_medians_100 = np.append(sample_medians_100, new_median_100)
    new_median_1000 = sample_median(1000)
    sample_medians_1000 = np.append(sample_medians_1000, new_median_1000)
```

**Code:**

```python
sample_medians = Table().with_columns('Size 10', sample_medians_10, 
                                      'Size 100', sample_medians_100,
                                      'Size 1000', sample_medians_1000)
```

**Code:**

```python
sample_medians.hist(bins = np.arange(-5, 30))
```

## Swain vs. Alabama ##

**Code:**

```python
population_proportions = make_array(.26, .74)
population_proportions
```

**Code:**

```python
sample_proportions(100, population_proportions)
```

**Code:**

```python
def panel_proportion():
    return sample_proportions(100, population_proportions).item(0)
```

**Code:**

```python
panel_proportion()
```

**Code:**

```python
panels = make_array()

for i in np.arange(10000):
    new_panel = panel_proportion() * 100
    panels = np.append(panels, new_panel)
```

**Code:**

```python
Table().with_column(
    'Number of Black Men on Panel of 100', panels
).hist(bins=np.arange(5.5,40.))

# Plotting details; ignore this code
plots.ylim(-0.002, 0.09)
plots.scatter(8, 0, color='red', s=30);
```

## Mendel and Pea Flowers ##

**Code:**

```python
## Mendel had 929 plants, of which 709 had purple flowers
observed_purples = 709 / 929
observed_purples
```

**Code:**

```python
predicted_proportions = make_array(.75, .25)
sample_proportions(929, predicted_proportions)
```

**Code:**

```python
def purple_flowers():
    return sample_proportions(929, predicted_proportions).item(0) * 100
```

**Code:**

```python
purple_flowers()
```

**Code:**

```python
purples = make_array()

for i in np.arange(10000):
    new_purple = purple_flowers()
    purples = np.append(purples, new_purple)
```

**Code:**

```python
Table().with_column('Percent of purple flowers in sample of 929', purples).hist()

# Plotting details; ignore this code
plots.ylim(-0.02, 0.25)
plots.scatter(observed_purples * 100, 0, color='red', s=30);
```

**Code:**

```python
Table().with_column('Discrepancy in sample of 929 if the model is true', abs(purples- 75)).hist()

# Plotting details; ignore this code
plots.ylim(-0.02, 0.6)
plots.scatter(abs(observed_purples * 100 - 75), 0, color='red', s=30);
```

**Code:**

```python
abs(observed_purples * 100 - 75)
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
