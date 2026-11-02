---
title: "lec05"
lecture: lec05
course: data8
semester: sp26
source: lectures/data8/sp26/lec05/lec05.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
```

## Arrays

**Code:**

```python
a = make_array(5, 6, 7, 8)
```

**Code:**

```python
a + 1
```

**Code:**

```python
a * 2
```

**Code:**

```python
a + a
```

**Code:**

```python
(a + a).item(2)
```

**Code:**

```python
sum(a)
```

**Code:**

```python
len(a)
```

**Code:**

```python
sum(a) / len(a)
```

**Code:**

```python
np.average(a)
```

## Columns of Tables are Arrays ##

**Code:**

```python
nba = Table.read_table('nba_salaries.csv').where('season', 2020)
warriors = nba.where('team', 'Golden State Warriors')
```

**Code:**

```python
warriors
```

**Code:**

```python
warriors.select('salary')
```

**Code:**

```python
warriors.column('salary')
```

What was the average salary among players on the warriors in the 2020 season?

**Code:**

```python
np.average(warriors.column('salary'))
```

**Code:**

```python
celtics = nba.where('team', 'Boston Celtics')
```

**Code:**

```python
np.average(warriors.column('salary')) - np.average(celtics.column('salary'))
```

## Ranges ##

**Code:**

```python
make_array(0, 1, 2, 3, 4, 5, 6)
```

**Code:**

```python
np.arange(7)
```

**Code:**

```python
np.arange(5, 11)
```

**Code:**

```python
np.arange(0, 20, 2)
```

**Code:**

```python
np.arange(0, 21, 2)
```

**Code:**

```python
np.arange(0, 1, 0.1)
```

### Create a table from columns

**Code:**

```python
streets = make_array('Bancroft', 'Durant', 'Channing', 'Haste')
streets
```

**Code:**

```python
Table()
```

**Code:**

```python
southside = Table().with_column('Streets', streets)
southside
```

**Code:**

```python
southside.with_column('Blocks from campus', np.arange(4))
```

**Code:**

```python
Table().with_columns(
    'Streets', streets,
    'Blocks from campus', np.arange(4)
)
```

### W.E.B. DuBois was a data scientist!

**Code:**

```python
du_bois = Table.read_table('du_bois.csv')
du_bois
```

**Code:**

```python
du_bois.column('ACTUAL AVERAGE')
```

**Code:**

```python
du_bois.column('FOOD')
```

**Code:**

```python
du_bois.column('ACTUAL AVERAGE') * du_bois.column('FOOD')
```

**Code:**

```python
food_dollars = du_bois.column('ACTUAL AVERAGE') * du_bois.column('FOOD')
du_bois.with_columns('Food $', food_dollars)
```

**Code:**

```python
du_bois
```

**Code:**

```python
du_bois = du_bois.with_columns('Food $', food_dollars)
du_bois
```

**Code:**

```python
du_bois.select('CLASS', 'ACTUAL AVERAGE', 'FOOD', 'Food $')
```

**Code:**

```python
du_bois.labels
```

**Code:**

```python
du_bois.num_rows
```

**Code:**

```python
du_bois.num_columns
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

### `du_bois.csv`

7 rows, 8 columns.

| Column | Type |
| --- | --- |
| `CLASS` | str |
| `ACTUAL AVERAGE` | float |
| `RENT` | float |
| `FOOD` | float |
| `CLOTHES` | float |
| `TAXES` | float |
| `OTHER` | float |
| `STATUS` | str |
