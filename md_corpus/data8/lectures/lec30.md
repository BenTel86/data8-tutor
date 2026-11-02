---
title: "lec30"
lecture: lec30
course: data8
semester: sp26
source: lectures/data8/sp26/lec30/lec30.ipynb
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

**Code:**

```python
# Some functions for plotting. You don't have to understand how any
# of the functions in this cell work, since they use things we 
# haven't learned about in Data 8.

def resize_window(lim=3.5):
    plots.xlim(-lim, lim)
    plots.ylim(-lim, lim)
    
def draw_line(slope=0, intercept=0, x=make_array(-4, 4), color='r'):
    y = x*slope + intercept
    plots.plot(x, y, color=color)
    
def draw_vertical_line(x_position, color='black'):
    x = make_array(x_position, x_position)
    y = make_array(-4, 4)
    plots.plot(x, y, color=color)
    
def make_correlated_data(r):
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r*x + (np.sqrt(1-r**2))*z
    return x, y

def r_table(r):
    """
    Generate a table of 1000 x,y data points in standard units
    whose correlation is approximately equal to r
    """
    np.random.seed(8)
    x, y = make_correlated_data(r)
    return Table().with_columns('x', x, 'y', y)
```

**Code:**

```python
def demographics_errors(slope, intercept):
    # Use four convenient points from the original data
    sample = [[14.7, 33995], [19.1, 61454], [50.7, 71183], [59.5, 105918]]
    demographics.scatter('College%', 'Median Income', alpha=0.5)
    xlims = make_array(5, 75)
    # Plot a line with the slope and intercept you specified:
    plots.plot(xlims, slope * xlims + intercept, lw=4)
    # Plot red lines from each of the four points to the line
    for x, y in sample:
        plots.plot([x, x], [y, slope * x + intercept], color='r', lw=4)
```

**Code:**

```python
def show_demographics_rmse(slope, intercept):
    demographics_errors(slope, intercept)
    x = demographics.column('College%')
    y = demographics.column('Median Income')
    prediction = slope * x + intercept
    mse = np.mean((y - prediction) ** 2)
    print("Root mean squared error:", round(mse ** 0.5, 2))
```

**Code:**

```python
def fitted_values(t, x, y):
    """Return an array of the regressions estimates at all the x values"""
    a = slope(t, x, y)
    b = intercept(t, x, y)
    return a*t.column(x) + b
```

## Slope & Intercept

**Code:**

```python
def standard_units(x):
    """Converts an array x to standard units"""
    return (x - np.mean(x)) / np.std(x)

def correlation(t, x, y):
    x_su = standard_units(t.column(x))
    y_su = standard_units(t.column(y))
    return np.mean(x_su * y_su)
```

**Code:**

```python
def slope(t, x, y):
    """Computes the slope of the regression line"""
    r = correlation(t, x, y)
    y_sd = np.std(t.column(y))
    x_sd = np.std(t.column(x))
    return r * y_sd / x_sd

def intercept(t, x, y):
    """Computes the intercept of the regression line"""
    x_mean = np.mean(t.column(x))
    y_mean = np.mean(t.column(y))
    return y_mean - slope(t, x, y)*x_mean
```

### Error in Estimation

**Code:**

```python
demographics = Table.read_table('district_demographics2016.csv')
demographics.show(5)
```

**Code:**

```python
demographics = demographics.drop(
    'State', 'District', 'Percent voting for Clinton')
demographics.show(5)
```

**Code:**

```python
demographics.scatter('College%', 'Median Income')
```

**Code:**

```python
college = demographics.column('College%')
income = demographics.column('Median Income')
print("     College% average", np.average(college), 'and SD', np.std(college))
print("Median Income average", np.average(income), 'and SD', np.std(income))
print("Correlation", correlation(demographics, 'College%', 'Median Income'))
```

**Code:**

```python
regression_slope = slope(demographics, 'College%', 'Median Income')
regression_intercept = intercept(demographics, 'College%', 'Median Income')
regression_slope, regression_intercept
```

**Code:**

```python
predicted = fitted_values(demographics, 'College%', 'Median Income')
demographics = demographics.with_column(
    'Linear Prediction', predicted)
demographics.scatter('College%')
```

**Code:**

```python
actual = demographics.column('Median Income')
errors = actual - predicted
```

**Code:**

```python
demographics.with_column('Error', errors)
```

**Code:**

```python
demographics.with_column('Error', errors).hist('Error')
```

**Code:**

```python
np.mean(errors)
```

**Code:**

```python
np.mean(errors ** 2) ** 0.5
```

**Code:**

```python
demographics_errors(regression_slope, regression_intercept)
```

**Code:**

```python
demographics_errors(regression_slope, regression_intercept - 30000)
```

**Code:**

```python
# takes any slope, any intercept

demographics_errors(1350, 19000)
```

**Code:**

```python
demographics_errors(-1000, 75000)
```

### Root Mean Square Error ###

**Code:**

```python
show_demographics_rmse(-1000, 75000)
```

**Code:**

```python
show_demographics_rmse(1350, 19000)
```

**Code:**

```python
show_demographics_rmse(regression_slope, regression_intercept)
```

### Numerical Optimization ###

**Code:**

```python
x = np.arange(1, 3, 0.1)
y = (x-2)**2 + 3
Table().with_columns('x', x, 'y', y).plot('x')
```

**Code:**

```python
def f(x):
    return ((x-2)**2) + 3
```

**Code:**

```python
minimize(f)
```

**Code:**

```python
f(minimize(f))
```

**Code:**

```python
x = np.arange(-1.5, 1.5, 0.05)
y2 = 2 * np.sin(x*np.pi) + x ** 3 + x ** 4 
Table().with_columns('x', x, 'y', y2).plot('x')
```

**Code:**

```python
def complicated_function(x):
    return 2 * np.sin(x*np.pi) + x ** 3 + x ** 4
```

**Code:**

```python
minimize(complicated_function)
```

### Minimizing RMSE ###

**Code:**

```python
def demographics_rmse(any_slope, any_intercept):
    x = demographics.column('College%')
    y = demographics.column('Median Income')
    estimate = any_slope*x + any_intercept
    return (np.mean((y - estimate) ** 2)) ** 0.5
```

**Code:**

```python
demographics_rmse(1500, 20000)
```

**Code:**

```python
demographics_rmse(1350, 19000)
```

**Code:**

```python
demographics_rmse(-1000, 75000)
```

**Code:**

```python
minimize(demographics_rmse)
```

**Code:**

```python
make_array(regression_slope, regression_intercept)
```

### Nonlinear Regression ###

**Code:**

```python
shotput = Table.read_table('shotput.csv')
shotput
```

**Code:**

```python
shotput.scatter('Weight Lifted')
```

**Code:**

```python
def shotput_linear_rmse(any_slope, any_intercept):
    x = shotput.column('Weight Lifted')
    y = shotput.column('Shot Put Distance')
    estimate = any_slope*x + any_intercept
    return np.mean((y - estimate) ** 2) ** 0.5
```

**Code:**

```python
best_line = minimize(shotput_linear_rmse)
best_line
```

**Code:**

```python
weights = shotput.column(0)
```

**Code:**

```python
linear_fit = best_line.item(0)*weights + best_line.item(1)

shotput.with_column(
    'Best Line', linear_fit
).scatter(0)
```

**Quadratic Function**

$$
f(x) ~=~ ax^2 + bx + c
$$
for constants $a$, $b$, and $c$.

**Code:**

```python
def shotput_quadratic_rmse(a, b, c):
    x = shotput.column('Weight Lifted')
    y = shotput.column('Shot Put Distance')
    estimate = a*(x**2) + b*x + c
    return np.mean((y - estimate) ** 2) ** 0.5
```

**Code:**

```python
best_quad = minimize(shotput_quadratic_rmse)
best_quad
```

**Code:**

```python
# x = weight lifted = 100 kg
# Then predicted shot put distance:

(-0.00104)*(100**2) + 0.2827*100 - 1.5318
```

**Code:**

```python
quad_fit = best_quad.item(0)*(weights**2) + best_quad.item(1)*weights + best_quad.item(2)
```

**Code:**

```python
shotput.with_column('Best Quadratic Curve', quad_fit).scatter(0)
```

**Code:**

```python
shotput_linear_rmse(best_line.item(0), best_line.item(1))
```

**Code:**

```python
shotput_quadratic_rmse(best_quad.item(0), best_quad.item(1), best_quad.item(2))
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

### `shotput.csv`

28 rows, 2 columns.

| Column | Type |
| --- | --- |
| `Weight Lifted` | float |
| `Shot Put Distance` | float |
