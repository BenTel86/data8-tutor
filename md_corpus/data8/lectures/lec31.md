---
title: "Residuals"
lecture: lec31
course: data8
semester: sp26
source: lectures/data8/sp26/lec31/lec31.ipynb
language: python
---

**Code:**

```python
# HIDDEN
from datascience import *
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
```

## Regression-Related Functions

**Code:**

```python
def standard_units(arr):
    """ Converts an array to standard units """
    return (arr - np.average(arr))/np.std(arr)

def correlation(t, x, y):
    """ Computes correlation: t is a table, and x and y are column names """
    x_standard = standard_units(t.column(x))
    y_standard = standard_units(t.column(y))
    return np.average(x_standard * y_standard)

def slope(t, x, y):
    """ Computes the slope of the regression line, like correlation above """
    r = correlation(t, x, y)
    y_sd = np.std(t.column(y))
    x_sd = np.std(t.column(x))
    return r * y_sd / x_sd

def intercept(t, x, y):
    """ Computes the intercept of the regression line, like slope above """
    x_mean = np.mean(t.column(x))
    y_mean = np.mean(t.column(y))
    return y_mean - slope(t, x, y)*x_mean

def fitted_values(t, x, y):
    """Return an array of the regression estimates (predictions) at all the x values"""
    a = slope(t, x, y)
    b = intercept(t, x, y)
    return a*t.column(x) + b
```

**Code:**

```python
demographics = Table.read_table('district_demographics2016.csv')
demographics.sample(6).show()
```

**Linear Fit**

$\text{estimate of Median Income} = a \cdot \text{College\%} + b$

**Code:**

```python
fitted_income = demographics.select('College%', 'Median Income')
fitted_income = fitted_income.with_columns('Fitted Median Income',
    fitted_values(demographics, 'College%', 'Median Income'))
fitted_income.scatter('College%')
fitted_income.sample(5).show()
```

# Residuals

**Code:**

```python
def residuals(t, x, y):
    predictions = fitted_values(t, x, y)
    return t.column(y) - predictions
```

### Residual plots can tell us about our model fit

#### Case study 1: 2016 election demographics

**Code:**

```python
income_residuals = fitted_income.with_columns(
    'Residual', residuals(demographics, 'College%', 'Median Income')
)
income_residuals.show(5)
```

These two functions will help us plot things the rest of the way.

**Code:**

```python
def plot_fitted(t, x, y):
    fitted_label = 'Fitted ' + y
    (t.with_column(fitted_label, fitted_values(t, x, y))
      .select(x, y, fitted_label).scatter(0))

def plot_residuals(t, x, y):
    residuals_label = y + ' Residuals'
    (t.with_columns(residuals_label, residuals(t, x, y))
      .scatter(x, residuals_label))
```

______

**Code:**

```python
plot_fitted(demographics, 'College%', 'Median Income')
```

**Code:**

```python
plot_residuals(demographics, 'College%', 'Median Income')
```

#### Case study 2: dugongs

**Code:**

```python
dugong = Table.read_table('dugong.csv')
dugong.show(5)
```

**Code:**

```python
dugong.scatter('Length', 'Age')
```

**Code:**

```python
correlation(dugong, 'Length', 'Age')
```

$\text{estimate of Age} = a \cdot \text{Length} + b$

**Code:**

```python
plot_fitted(dugong, 'Length', 'Age')
```

**Code:**

```python
plot_residuals(dugong, 'Length', 'Age')
```

#### Case study 3: US women

**Code:**

```python
us_women = Table.read_table('us_women.csv')
us_women.show(5)
```

**Code:**

```python
us_women.scatter('height')
```

**Code:**

```python
correlation(us_women, 'height', 'ave weight')
```

$\text{estimate of height} = a \cdot \text{average weight} + b$

**Code:**

```python
plot_fitted(us_women, 'height', 'ave weight')
```

**Code:**

```python
plot_residuals(us_women, 'height', 'ave weight')
```

#### Case study 4: Heights

**Code:**

```python
family_heights = Table.read_table('family_heights.csv')
family_heights.where('family', '1')
```

**Code:**

```python
parents = (family_heights.column('father') + family_heights.column('mother'))/2
heights = Table().with_columns(
    'Parent Average', parents,
    'Child', family_heights.column('child')
    )
heights.show(6)
```

$\text{estimate of a child's adult height} = a \cdot \text{average parent height} + b$

**Code:**

```python
plot_fitted(heights, 'Parent Average', 'Child')
```

**Code:**

```python
plot_residuals(heights, 'Parent Average', 'Child')
```

### Mathematical Properties of Regression

The average of the residuals are zero.

**Code:**

```python
round(np.average(residuals(demographics, 'College%', 'Median Income')), 10)
```

**Code:**

```python
round(np.average(residuals(dugong, 'Length', 'Age')), 10)
```

**Code:**

```python
round(np.average(residuals(heights, 'Parent Average', 'Child')), 10)
```

______

The correlation coefficients between:

- The residuals and $x$
- The residuals and the fitted values

are both 0.

**Code:**

```python
heights = heights.with_columns(
    'Residual', residuals(heights, 'Parent Average', 'Child'),
    'Fitted Value', fitted_values(heights, 'Parent Average', 'Child')
)
```

**Code:**

```python
round(correlation(heights, 'Parent Average', 'Residual'), 10)
```

**Code:**

```python
round(correlation(heights, 'Fitted Value', 'Residual'), 10)
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `district_demographics2016.csv`

435 rows, 5 columns.

| Column | Type |
| --- | --- |
| `State` | str |
| `District` | str |
| `Median Income` | int |
| `Percent voting for Clinton` | float |
| `College%` | float |

### `dugong.csv`

27 rows, 2 columns.

| Column | Type |
| --- | --- |
| `Length` | float |
| `Age` | float |

### `us_women.csv`

15 rows, 2 columns.

| Column | Type |
| --- | --- |
| `height` | int |
| `ave weight` | int |

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
| `sex` | str |
