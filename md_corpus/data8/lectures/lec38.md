---
title: "lec38"
lecture: lec38
course: data8
semester: sp26
source: lectures/data8/sp26/lec38/lec38.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
%matplotlib inline
```

## The Broste Thesis

**Code:**

```python
summary = Table(['Age', 'Condition', 'Total', 'Deaths', 'CHD Deaths']).with_rows([
    ['0-34',  'Diet',    1367, 3, 0],
    ['35-44', 'Diet',    728, 3, 0],
    ['45-54', 'Diet',    767, 14, 4],
    ['55-64', 'Diet',    870, 35, 7],
    ['65+',   'Diet',    953, 190, 42],
    ['0-34',  'Control', 1337, 7, 1],
    ['35-44', 'Control', 731, 4, 1],
    ['45-54', 'Control', 816, 16, 4],
    ['55-64', 'Control', 896, 33, 12],
    ['65+',   'Control', 958, 162, 34],   
])
summary
```

**Code:**

```python
np.arange(12) < 3
```

**Code:**

```python
subjects = Table(['Age', 'Condition', 'Participated', 'Died'])
for row in summary.rows:
    i = np.arange(0, row.item('Total'))
    t = Table().with_columns('Died', i < row.item('Deaths'))
    t.append_column('Age', row.item('Age'))
    t.append_column('Condition', row.item('Condition'))
    t.append_column('Participated', True)
    subjects.append(t)
subjects
```

**Code:**

```python
subjects.group(['Age', 'Condition'], sum)
```

**Code:**

```python
def hazard_rate(counts):
    return counts.item('Died sum') / counts.item('Participated sum')

def rate_difference(t):
    counts = t.drop('Age').group('Condition', sum)
    return abs(hazard_rate(counts.row(1)) - hazard_rate(counts.row(0)))

rate_difference(subjects)
```

**Code:**

```python
rate_difference(subjects.where('Age', '0-34'))
```

**Code:**

```python
rate_difference(subjects.where('Age', '65+'))
```

**Code:**

```python
def test(t):
    observed = rate_difference(t)
    repetitions = 200

    stats = make_array()
    for i in np.arange(repetitions):
        simulated_results = t.select('Died').sample().column('Died')
        simulated_outcomes = t.with_column('Died', simulated_results)
        simulated_stat = rate_difference(simulated_outcomes)
        stats = np.append(stats, simulated_stat)

    # Find the empirical P-value:
    p = np.count_nonzero(stats >= observed) / repetitions
    
    print('Observed absolute difference in hazard rates:', observed)
    print('P-value:', p)

#test(subjects)
```

**Code:**

```python
for age in subjects.group('Age').column('Age'):
    print('Ages', age)
    test(subjects.where('Age', age))
```
