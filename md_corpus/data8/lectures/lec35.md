---
title: "Evaluation & Inference"
lecture: lec35
course: data8
semester: sp26
source: lectures/data8/sp26/lec35/lec35.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
import matplotlib

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

import warnings
warnings.simplefilter("ignore")
```

## Review of the Steps ##

- `distance(pt1, pt2)`: Returns the distance between the arrays `pt1` and `pt2`
- `row_distance(row1, row2)`: Returns the distance between the rows `row1` and `row2`
- `distances(training, example)`: Returns a table that is `training` with an additional column `'Distance'` that contains the distance between `example` and each row of `training`
- `closest(training, example, k)`: Returns a table of the rows corresponding to the k smallest distances 
- `majority_class(topk)`: Returns the majority class in the `'Class'` column
- `classify(training, example, k)`: Returns the predicted class of `example` based on a `k` nearest neighbors classifier using the historical sample `training`

**Code:**

```python
def distance(pt1, pt2):
    """Return the distance between two points, represented as arrays"""
    return np.sqrt(sum((pt1 - pt2)**2))

def row_distance(row1, row2):
    """Return the distance between two numerical rows of a table"""
    return distance(np.array(row1), np.array(row2))

def distances(training, example):
    """
    Compute distance between example and every row in training.
    Return training augmented with Distance column
    """
    distances = make_array()
    attributes_only = training.drop('Class')
    
    for row in attributes_only.rows:
        distances = np.append(distances, row_distance(row, example))
            
    return training.with_column('Distance_to_ex', distances)

def closest(training, example, k):
    """
    Return a table of the k closest neighbors to example
    """
    return distances(training, example).sort('Distance_to_ex').take(np.arange(k))

def majority_class(topk):
    """
    Return the class with the highest count
    """
    return topk.group('Class').sort('count', descending=True).column(0).item(0)

def classify(training, example, k):
    """
    Return the majority class among the 
    k nearest neighbors of example
    """
    return majority_class(closest(training, example, k))

def evaluate_accuracy(training, test, k):
    """Return the proportion of correctly classified examples 
    in the test set"""
    test_attributes = test.drop('Class')
    num_correct = 0
    for i in np.arange(test.num_rows):
        c = classify(training, test_attributes.row(i), k)
        num_correct = num_correct + (c == test.column('Class').item(i))
    return num_correct / test.num_rows
```

# Evaluation & Inference

**Code:**

```python
def classify_all(training, test, k):
    """Classify each row of the test table and add a column of the results."""
    test_attributes = test.drop('Class')
    guesses = make_array()
    for i in np.arange(test.num_rows):
        c = classify(training, test_attributes.row(i), k)
        guesses = np.append(guesses, c)
    return test.with_column("Prediction", guesses)
```

**Code:**

```python
patients = Table.read_table('breast-cancer.csv').drop('ID')
shuffled = patients.sample(with_replacement=False) # Randomly permute the rows
training_set = shuffled.take(np.arange(342))
test_set  = shuffled.take(np.arange(342, 683))
test_result = classify_all(training_set, test_set, 3)
test_result.show(3)
```

**Code:**

```python
# A confusion matrix

test_result.pivot('Prediction', 'Class')
```

**Code:**

```python
def get_accuracy(t, prediction_label='Prediction'):
    """Return the accuracy on a test table with Class and Prediction columns."""
    return sum(t.column('Class') == t.column(prediction_label)) / t.num_rows
    
get_accuracy(test_result)
```

**Code:**

```python
# A confidence interval for the accuracy of this classifier 
# on the population from which the data were sampled

accuracies = make_array()
for i in np.arange(1000):
    resample = test_result.sample()
    accuracies = np.append(accuracies, get_accuracy(resample))
left = percentile(2.5, accuracies)
right = percentile(97.5, accuracies)

make_array(left, right)
```

**Code:**

```python
evaluate_accuracy(training_set, test_set, 3)
```

**Code:**

```python
evaluate_accuracy(training_set, test_set, 7)
```

**Code:**

```python
with_3 = classify_all(training_set, test_set, 3)
with_7 = classify_all(training_set, test_set, 7)
with_3_and_7 = (with_3.relabeled('Prediction', 'Prediction A')
                      .with_column('Prediction B', with_7.column('Prediction')))
with_3_and_7.show(3)
```

**Code:**

```python
# How often do the classifiers disagree on the test set?

with_3_and_7.pivot('Prediction A', 'Prediction B')
```

**Code:**

```python
get_accuracy(with_3_and_7, 'Prediction A')
```

**Code:**

```python
get_accuracy(with_3_and_7, 'Prediction B')
```

**Code:**

```python
# A confidence interval for the difference in accuracies of two
# classifiers on the population from which the data were sampled

acc_diffs = make_array()
for i in np.arange(1000):
    resample = with_3_and_7.sample()
    diff = get_accuracy(resample, 'Prediction A') - get_accuracy(resample, 'Prediction B')
    acc_diffs = np.append(acc_diffs, diff)
left = percentile(2.5, acc_diffs)
right = percentile(97.5, acc_diffs)

make_array(left, right)
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `breast-cancer.csv`

683 rows, 11 columns.

| Column | Type |
| --- | --- |
| `ID` | int |
| `Clump Thickness` | int |
| `Uniformity of Cell Size` | int |
| `Uniformity of Cell Shape` | int |
| `Marginal Adhesion` | int |
| `Single Epithelial Cell Size` | int |
| `Bare Nuclei` | int |
| `Bland Chromatin` | int |
| `Normal Nucleoli` | int |
| `Mitoses` | int |
| `Class` | int |
