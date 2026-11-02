---
title: "Be the Jury Program"
lecture: lec16
course: data8
semester: sp26
source: lectures/data8/sp26/lec16/lec16.ipynb
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

## Alameda County Jury Panels ##

**Code:**

```python
jury = Table().with_columns(
    'Ethnicity', make_array('Asian', 'Black', 'Latino', 'White', 'Other'),
    'Eligible', make_array(0.15, 0.18, 0.12, 0.54, 0.01),
    'Panels', make_array(0.26, 0.08, 0.08, 0.54, 0.04)
)

jury
```

**Code:**

```python
jury.barh('Ethnicity')
```

**Code:**

```python
# Under the model, this is the true distribution of people
# from which the jurors are randomly sampled
model = jury.column('Eligible')
```

**Code:**

```python
# Let's simulate a random draw of 1423 jurors from this distribution
simulated = sample_proportions(1423, model)
simulated
```

**Code:**

```python
# The actual observed distribution (Panels) looks quite different
# from the simulation -- try running this several times to confirm!
jury_with_simulated = jury.with_column('Simulated', simulated)
jury_with_simulated
```

**Code:**

```python
jury_with_simulated.barh('Ethnicity')
```

## Distance Between Distributions

**Code:**

```python
# In the last lecture, the difference between observed black/purple
# and their expected values (26%/75%) was our statistic.
#
# In this case, we need to understand how each of the 5 categories
# differ from their expected values according to the model.

diffs = jury.column('Panels') - jury.column('Eligible')
jury_with_difference = jury.with_column('Difference', diffs)
jury_with_difference
```

## Total Variation Distance

**Code:**

```python
def tvd(dist1, dist2):
    return sum(abs(dist1 - dist2))/2
```

**Code:**

```python
# The TVD of our observed data (Panels) from their expected values
# assuming the model is true (Eligbible)
obsvd_tvd = tvd(jury.column('Panels'), jury.column('Eligible'))
obsvd_tvd
```

**Code:**

```python
# The TVD of a model simluation from its expected values
tvd(sample_proportions(1423, model), jury.column('Eligible'))
```

**Code:**

```python
def simulated_tvd():
    return tvd(sample_proportions(1423, model), model)

tvds = make_array()

num_simulations = 10000
for i in np.arange(num_simulations):
    new_tvd = simulated_tvd()
    tvds = np.append(tvds, new_tvd)
```

**Code:**

```python
title = 'Simulated TVDs (if model is true)'
bins = np.arange(0, .05, .005)

Table().with_column(title, tvds).hist(bins = bins)
print('Observed TVD: ' + str(obsvd_tvd))

# Plotting details; ignore this code
plots.ylim(-2, 55)
plots.scatter(obsvd_tvd, 0, color='red', s=30);
```

# Be the Jury Program

**Code:**

```python
# Counts are from the 88% of participants in Be the Jury in 2023 who completed the exit survey and shared their race

sf = Table().with_columns(
    'Race/Ethnicity',
    ['American Indian or Alaska Native',
     'Asian',
     'Black or African American',
     'Hispanic or Latino',
     'Native Hawaiian or Other Pacific Islander',
     'Some Other Race',
     'White'],
    'Count',[4, 168,23,59,4,5,175],
    'SF Census (2020)', [0.005, 0.3440, 0.0520, 0.1540, 0.0040, 0.0490, 0.3920])
sf.set_format(2, PercentFormatter)
```

**Code:**

```python
sum(sf.column('Count'))
```

**Code:**

```python
sf = (sf.with_column('Panels', sf.column('Count') / sum(sf.column('Count')))
        .relabeled('SF Census (2020)', 'Eligible'))
sf.set_format(3, PercentFormatter)
```

**Code:**

```python
sf.select(0, 2, 3).barh(0)
```

**Code:**

```python
jury = sf
obsvd_tvd = tvd(jury.column('Panels'), jury.column('Eligible'))
obsvd_tvd
```

**Code:**

```python
def simulated_tvd():
    return tvd(sample_proportions(438, model), model)

tvds = make_array()

num_simulations = 10000
for i in np.arange(num_simulations):
    new_tvd = simulated_tvd()
    tvds = np.append(tvds, new_tvd)
```

**Code:**

```python
title = 'Simulated TVDs (if model is true)'
bins = np.arange(0, .05, .005)

Table().with_column(title, tvds).hist(bins = bins)
print('Observed TVD: ' + str(obsvd_tvd))

# Plotting details; ignore this code
plots.ylim(-2, 55)
plots.scatter(obsvd_tvd, 0, color='red', s=30);
```
