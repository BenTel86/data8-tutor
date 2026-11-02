---
title: "lec28"
lecture: lec28
course: data8
semester: sp26
source: lectures/data8/sp26/lec28/lec28.ipynb
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

**Code:**

```python
def r_scatter(r):
    plots.figure(figsize=(5,5))
    "Generate a scatter plot with a correlation approximately r"
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r*x + (np.sqrt(1-r**2))*z
    plots.scatter(x, y, color='darkblue', s=20)
    plots.xlim(-4, 4)
    plots.ylim(-4, 4)
```

## Prediction

**Code:**

```python
# Note: Child heights are the **adult** heights of children in a family
families = Table.read_table('family_heights.csv')
parent_avgs = (families.column('father') + families.column('mother'))/2
heights = Table().with_columns(
    'Parent Average', parent_avgs,
    'Child', families.column('child'),
)
heights
```

**Code:**

```python
heights.scatter('Parent Average', 'Child')
```

**Code:**

```python
nearby = heights.where('Parent Average', are.between(67.5, 68.5))
nearby_mean = np.average(nearby.column('Child'))
nearby_mean
```

**Code:**

```python
heights.scatter('Parent Average', 'Child')
plots.plot([67.5, 67.5], [50, 85], color='red', lw=2)
plots.plot([68.5, 68.5], [50, 85], color='red', lw=2)
plots.scatter(68, nearby_mean, color='red', s=50);
```

**Code:**

```python
def predict_child(h):
    """Predict the height of a child whose parents have a parent average height of p_avg.
    
    The prediction is the average height of the children whose parent average height is
    in the range p_avg plus or minus 0.5.
    """
    nearby = heights.where('Parent Average', are.between(h - 1/2, h + 1/2))
    return np.average(nearby.column('Child'))
```

**Code:**

```python
heights_with_predictions = heights.with_columns(
    'Prediction', heights.apply(predict_child, 'Parent Average'))
```

**Code:**

```python
heights_with_predictions.scatter('Parent Average')
```

## Association

**Code:**

```python
hybrid = Table.read_table('hybrid.csv')
```

**Code:**

```python
hybrid.group('year').barh('year')
```

**Code:**

```python
hybrid.sort('msrp', descending=True)
```

**Code:**

```python
hybrid.scatter('mpg', 'msrp')
```

**Code:**

```python
hybrid.scatter('acceleration', 'msrp')
```

**Code:**

```python
suv = hybrid.where('class', 'SUV')
suv.num_rows
```

**Code:**

```python
suv.scatter('acceleration', 'msrp')
```

**Code:**

```python
suv.scatter('mpg', 'msrp')
```

**Code:**

```python
def standard_units(x):
    "Convert any array of numbers to standard units."
    return (x - np.average(x)) / np.std(x)
```

**Code:**

```python
Table().with_columns(
    'mpg (standard units)',  standard_units(suv.column('mpg')), 
    'msrp (standard units)', standard_units(suv.column('msrp'))
).scatter(0, 1)
plots.xlim(-3, 3)
plots.ylim(-3, 3);
```

**Code:**

```python
suv.scatter('acceleration', 'msrp')
```

**Code:**

```python
Table().with_columns(
    'acceleration (standard units)', standard_units(suv.column('acceleration')), 
    'msrp (standard units)',         standard_units(suv.column('msrp'))
).scatter(0, 1)
plots.xlim(-3, 3)
plots.ylim(-3, 3);
```

## Correlation

**Code:**

```python
r_scatter(-1)
```

**Code:**

```python
x = np.arange(1, 7, 1)
y = make_array(2, 3, 1, 5, 2, 7)
t = Table().with_columns(
        'x', x,
        'y', y
    )
t
```

**Code:**

```python
t.scatter('x', 'y', s=30, color='red')
```

**Code:**

```python
t = t.with_columns(
        'x (standard units)', standard_units(x),
        'y (standard units)', standard_units(y)
    )
t
```

**Code:**

```python
t.scatter(2, 3, s=30, color='red')
```

**Code:**

```python
t = t.with_columns(
    'product of standard units', t.column(2) * t.column(3))
t
```

**Code:**

```python
# r is the average of the products of the standard units

r = np.average(t.column(2) * t.column(3))
r
```

**Code:**

```python
def correlation(t, x, y):
    """t is a table; x and y are column labels"""
    x_in_standard_units = standard_units(t.column(x))
    y_in_standard_units = standard_units(t.column(y))
    return np.average(x_in_standard_units * y_in_standard_units)
```

**Code:**

```python
correlation(t, 'x', 'y')
```

**Code:**

```python
suv.scatter('mpg', 'msrp')
```

**Code:**

```python
correlation(suv, 'mpg', 'msrp')
```

**Code:**

```python
suv.scatter('acceleration', 'msrp')
```

**Code:**

```python
correlation(suv, 'acceleration', 'msrp')
```

### Switching Axes

**Code:**

```python
correlation(t, 'x', 'y')
```

**Code:**

```python
t.scatter('x', 'y', s=30, color='red')
```

**Code:**

```python
t.scatter('y', 'x', s=30, color='red')
```

**Code:**

```python
correlation(t, 'y', 'x')
```

### Nonlinearity

**Code:**

```python
new_x = np.arange(-4, 4.1, 0.5)
nonlinear = Table().with_columns(
        'x', new_x,
        'y', new_x**2
    )
nonlinear.scatter('x', 'y', s=30, color='r')
```

**Code:**

```python
correlation(nonlinear, 'x', 'y')
```

### Outliers

**Code:**

```python
line = Table().with_columns(
        'x', make_array(1, 2, 3, 4),
        'y', make_array(1, 2, 3, 4)
    )
line.scatter('x', 'y', s=30, color='r')
```

**Code:**

```python
correlation(line, 'x', 'y')
```

**Code:**

```python
outlier = Table().with_columns(
        'x', make_array(1, 2, 3, 4, 5),
        'y', make_array(1, 2, 3, 4, 0)
    )
outlier.scatter('x', 'y', s=30, color='r')
```

**Code:**

```python
correlation(outlier, 'x', 'y')
```

### Ecological Correlations

**Code:**

```python
sat2014 = Table.read_table('sat2014.csv').sort('State')
sat2014
```

**Code:**

```python
sat2014.scatter('Critical Reading', 'Math')
```

**Code:**

```python
correlation(sat2014, 'Critical Reading', 'Math')
```

**Code:**

```python
def rate_code(x):
    if x <= 25:
        return 'low'
    elif x <= 50:
        return 'low-moderate'
    elif x <= 75:
        return 'moderate_high'
    else:
        return 'high'
```

**Code:**

```python
rate_codes = sat2014.apply(rate_code, 'Participation Rate')
```

**Code:**

```python
sat2014 = sat2014.with_columns('Rate Code', rate_codes)
sat2014
```

**Code:**

```python
sat2014.scatter('Critical Reading', 'Math', group='Rate Code')
```

**Code:**

```python
sat2014.where('Rate Code', 'low').show()
```

**Code:**

```python
sat2014.where('Rate Code', 'high').show()
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `family_heights.csv`

934 rows, 7 columns.

| Column | Type |
| --- | --- |
| `family` | str |
| `father` | float |
| `mother` | float |
| `child` | float |
| `children` | int |
| `order` | int |
| `m/f` | str |

### `hybrid.csv`

153 rows, 6 columns.

| Column | Type |
| --- | --- |
| `vehicle` | str |
| `year` | int |
| `msrp` | float |
| `acceleration` | float |
| `mpg` | float |
| `class` | str |

### `sat2014.csv`

51 rows, 6 columns.

| Column | Type |
| --- | --- |
| `State` | str |
| `Participation Rate` | float |
| `Critical Reading` | int |
| `Math` | int |
| `Writing` | int |
| `Combined` | int |
