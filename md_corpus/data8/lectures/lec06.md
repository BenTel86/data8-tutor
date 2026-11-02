---
title: "lec06"
lecture: lec06
course: data8
semester: sp26
source: lectures/data8/sp26/lec06/lec06.ipynb
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

## NBA Salaries

**Code:**

```python
nba = Table.read_table('nba_salaries.csv').where('season', 2020).drop('rank', 'season')
nba.show(3)
```

**Code:**

```python
nba.where('position', 'C').show(2)
```

**Code:**

```python
nba.where('position', are.equal_to('C')).show(2)
```

**Code:**

```python
nba.where('position', are.not_equal_to('C')).show(2)
```

**Code:**

```python
nba.where('salary', are.between(3e6, 5e6)).show(2)
```

**Code:**

```python
nba.where('salary', are.between(3e6, 5e6)).num_rows / nba.num_rows
```

## Census ##

**Code:**

```python
full = Table.read_table('nc-est2019-agesex-res.csv')
full.show(5)
```

**Code:**

```python
partial = full.select('SEX', 'AGE', 'POPESTIMATE2014', 'POPESTIMATE2019')
partial.show(5)
```

**Code:**

```python
us_pop = partial.relabeled(2, '2014').relabeled(3, '2019')
us_pop.show(5)
```

**Code:**

```python
us_pop.where('AGE', are.above_or_equal_to(100)).sort('AGE')
```

## 2019 Sex Ratios ##

**Code:**

```python
us_pop_2019 = us_pop.drop('2014')
us_pop_2019.show(3)
```

**Code:**

```python
all_ages = us_pop_2019.where('AGE', are.equal_to(999))
all_ages
```

**Code:**

```python
infants = us_pop_2019.where('AGE', are.equal_to(0))
infants
```

**Code:**

```python
females_all_rows = us_pop_2019.where('SEX', are.equal_to(2))
females = females_all_rows.where('AGE', are.not_equal_to(999))
females.show(3)
```

**Code:**

```python
males_all_rows = us_pop_2019.where('SEX', are.equal_to(1))
males = males_all_rows.where('AGE', are.not_equal_to(999))
males.show(3)
```

**Code:**

```python
f_to_m_ratios = females.column(2) / males.column(2)

ratios = Table().with_columns(
    'Age', females.column('AGE'),
    'F:M Ratio', f_to_m_ratios
)

ratios
```

**Code:**

```python
ratios.sort('Age', descending=True)
```

## Line Plot

**Code:**

```python
ratios.plot('Age', 'F:M Ratio')
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `nba_salaries.csv`

9,456 rows, 6 columns.

| Column | Type |
| --- | --- |
| `rank` | int |
| `name` | str |
| `position` | str |
| `team` | str |
| `salary` | int |
| `season` | int |

### `nc-est2019-agesex-res.csv`

306 rows, 14 columns.

| Column | Type |
| --- | --- |
| `SEX` | int |
| `AGE` | int |
| `CENSUS2010POP` | int |
| `ESTIMATESBASE2010` | int |
| `POPESTIMATE2010` | int |
| `POPESTIMATE2011` | int |
| `POPESTIMATE2012` | int |
| `POPESTIMATE2013` | int |
| `POPESTIMATE2014` | int |
| `POPESTIMATE2015` | int |
| `POPESTIMATE2016` | int |
| `POPESTIMATE2017` | int |
| `POPESTIMATE2018` | int |
| `POPESTIMATE2019` | int |
