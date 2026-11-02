---
title: "Classification Examples"
lecture: lec33
course: data8
semester: sp26
source: lectures/data8/sp26/lec33/lec33.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import warnings
warnings.simplefilter("ignore")
```

**Code:**

```python
def standard_units(x):
    return (x - np.mean(x))/np.std(x)
```

**Code:**

```python
def distance(point1, point2):
    """The distance between two arrays of numbers."""
    return np.sqrt(np.sum((point1 - point2)**2))

def all_distances(training, point):
    """The distance between p (an array of numbers) and the numbers in row i of attribute_table."""
    attributes = training.drop('Class')
    def distance_from_point(row):
        return distance(point, np.array(row))
    return attributes.apply(distance_from_point)

def table_with_distances(training, point):
    """A copy of the training table with the distance from each row to array p."""
    return training.with_column('Distance', all_distances(training, point))

def closest(training, point, k):
    """A table containing the k closest rows in the training table to array p."""
    with_dists = table_with_distances(training, point)
    sorted_by_distance = with_dists.sort('Distance')
    topk = sorted_by_distance.take(np.arange(k))
    return topk

def majority(topkclasses):
    """1 if the majority of the "Class" column is 1s, and 0 otherwise."""
    ones = topkclasses.where('Class', are.equal_to(1)).num_rows
    zeros = topkclasses.where('Class', are.equal_to(0)).num_rows
    if ones > zeros:
        return 1
    else:
        return 0

def classify(training, p, k):
    """Classify an example with attributes p using k-nearest neighbor classification with the given training table."""
    closestk = closest(training, p, k)
    topkclasses = closestk.select('Class')
    return majority(topkclasses)

def show_closest(point):
    """point = array([x,y]) 
    gives the coordinates of a new point
    shown in red"""
    
    HemoGl = ckd.drop('White Blood Cell Count', 'Color')
    t = closest(HemoGl, point, 1)
    x_closest = t.row(0).item(1)
    y_closest = t.row(0).item(2)
    ckd.scatter('Hemoglobin', 'Glucose', group='Color')
    plt.scatter(point.item(0), point.item(1), color='red', s=30)
    plt.plot(make_array(point.item(0), x_closest), make_array(point.item(1), y_closest), color='k', lw=2);
```

**Code:**

```python
def plot_all_points(test_grid):
    test_grid.scatter('Hemoglobin', 'Glucose', color='red', alpha=0.4, s=30)

    plt.scatter(ckd.column('Hemoglobin'), ckd.column('Glucose'), c=ckd.column('Color'), edgecolor='k')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2);
    
def classify_grid(training, test, k):
    c = make_array()
    for i in range(test.num_rows):
        # Run the classifier on the ith patient in the test set
        c = np.append(c, classify(training, make_array(test.row(i)), k))   
    return c

def plot_all_points_classified(test_grid):
    c = classify_grid(ckd.drop('White Blood Cell Count', 'Color'), test_grid, 1)
    test_grid = test_grid.with_column('Class', c).join('Class', color_table)
    test_grid.scatter('Hemoglobin', 'Glucose', group='Color', alpha=0.4, s=30)

    plt.scatter(ckd.column('Hemoglobin'), ckd.column('Glucose'), c=ckd.column('Color'), edgecolor='k')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2);
```

# Classification Examples

## Classifying Patients ##

**Code:**

```python
ckd = Table.read_table('ckd.csv').relabeled('Blood Glucose Random', 'Glucose')
ckd.show(3)
```

**Code:**

```python
ckd.group('Class')
```

**Code:**

```python
ckd.scatter('White Blood Cell Count', 'Glucose', group='Class')
```

**Code:**

```python
ckd.scatter('Hemoglobin', 'Glucose', group='Class')
```

**Code:**

```python
# we want to be able to way to predict the class of someone
# without having to plot & eye ball this graph every time.
#
# one way to do this is to put some thresholds into code

max_glucose_for_0 = ckd.where('Class',are.equal_to(0)).column('Glucose').max()
min_hemoglobin_for_0 = ckd.where('Class',are.equal_to(0)).column('Hemoglobin').min()
```

**Code:**

```python
def classify_manually(hemoglobin, glucose):
    if hemoglobin < min_hemoglobin_for_0 or glucose > max_glucose_for_0:
        return 1
    else:
        return 0
```

**Code:**

```python
# Let's try our classifier!
classify_manually(15, 100)
```

**Code:**

```python
classify_manually(10, 300)
```

## Classifying Banknotes ##

**Code:**

```python
banknotes = Table.read_table('banknote.csv')
banknotes
```

**Code:**

```python
banknotes.group('Class')
```

**Code:**

```python
banknotes.scatter('WaveletVar', 'WaveletCurt', group='Class')
```

**Code:**

```python
banknotes.scatter('WaveletSkew', 'Entropy', group='Class')
```

**Code:**

```python
from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_banknotes(angle):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(banknotes.column('WaveletSkew'), 
               banknotes.column('WaveletVar'), 
               banknotes.column('WaveletCurt'), 
               c=banknotes.column('Class'),
               cmap='viridis',
               s=50)
    ax.view_init(elev=30, azim=angle)
    
# Create the interactive sliders
interact(plot_banknotes, 
         angle=IntSlider(min=0, max=360, step=5, value=45));
```

## Nearest Neighbor Classifer

**Code:**

```python
# convert features into standard units
ckd = Table().with_columns(
    'Hemoglobin', standard_units(ckd.column('Hemoglobin')),
    'Glucose', standard_units(ckd.column('Glucose')),
    'White Blood Cell Count', standard_units(ckd.column('White Blood Cell Count')),
    'Class', ckd.column('Class')
)
```

**Code:**

```python
color_table = Table().with_columns(
    'Class', make_array(0, 1),
    'Color', make_array('darkblue', 'gold')
)
ckd = ckd.join('Class', color_table)
```

**Code:**

```python
ckd.scatter('Hemoglobin', 'Glucose', group='Color')
```

**Code:**

```python
alice = make_array(0, 1.5)
show_closest(alice)
```

## Decision Boundary

**Code:**

```python
alice = make_array(0, 0)
show_closest(alice)
```

**Code:**

```python
# Create a grid of all points
x_array = make_array()
y_array = make_array()
for x in np.arange(-2, 2.1, 0.1):
    for y in np.arange(-2, 2.1, 0.1):
        x_array = np.append(x_array, x)
        y_array = np.append(y_array, y)

test_grid = Table().with_columns(
    'Hemoglobin', x_array,
    'Glucose', y_array
)
```

**Code:**

```python
plot_all_points(test_grid)
```

**Code:**

```python
plot_all_points_classified(test_grid)
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `ckd.csv`

158 rows, 25 columns.

| Column | Type |
| --- | --- |
| `Age` | int |
| `Blood Pressure` | int |
| `Specific Gravity` | float |
| `Albumin` | int |
| `Sugar` | int |
| `Red Blood Cells` | str |
| `Pus Cell` | str |
| `Pus Cell clumps` | str |
| `Bacteria` | str |
| `Blood Glucose Random` | int |
| `Blood Urea` | int |
| `Serum Creatinine` | float |
| `Sodium` | int |
| `Potassium` | float |
| `Hemoglobin` | float |
| `Packed Cell Volume` | int |
| `White Blood Cell Count` | int |
| `Red Blood Cell Count` | float |
| `Hypertension` | str |
| `Diabetes Mellitus` | str |
| `Coronary Artery Disease` | str |
| `Appetite` | str |
| `Pedal Edema` | str |
| `Anemia` | str |
| `Class` | int |

### `banknote.csv`

1,372 rows, 5 columns.

| Column | Type |
| --- | --- |
| `WaveletVar` | float |
| `WaveletSkew` | float |
| `WaveletCurt` | float |
| `Entropy` | float |
| `Class` | int |
