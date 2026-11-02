---
title: "lec17_live"
lecture: lec17
variant: live
course: data8
semester: sp26
source: lectures/data8/sp26/lec17/lec17_live.ipynb
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

## The GSI's Defense ##

**Code:**

```python
scores = Table.read_table('scores_by_section.csv')
scores.show(5)
```

*Output:*

| Section | Midterm |
| --- | --- |
| 1 | 22 |
| 2 | 12 |
| 2 | 23 |
| 2 | 14 |
| 1 | 20 |

### Visual Representation

**Code:**

```python
avg_t.hist(bins = 20)
plots.plot([five_percent_point, five_percent_point], [0, 0.35], color='gold', lw=2)
plots.title('Area to the left of the gold line: 5%');
plots.scatter(observed_average, -0.01, color='red', s=120);
```

---

## Datasets

Datasets this notebook loads with `Table.read_table`. Column names are exact, including spaces and capitalization. Only the schema is recorded here — the data itself is not in this document, so any question about its values must be answered by running code, not by reasoning over the rows shown elsewhere in this file.

### `scores_by_section.csv`

359 rows, 2 columns.

| Column | Type |
| --- | --- |
| `Section` | int |
| `Midterm` | int |
