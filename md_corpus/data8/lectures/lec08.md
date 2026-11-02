---
title: "lec08"
lecture: lec08
course: data8
semester: sp26
source: lectures/data8/sp26/lec08/lec08.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
import warnings
warnings.filterwarnings("ignore")

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
plots.rcParams["patch.force_edgecolor"] = True
```

### Use counts and bar charts for categorical distributions

**Code:**

```python
nba_2020 = Table.read_table('nba_salaries.csv').where('season', 2020)
nba_2020.show(6)
```

**Code:**

```python
nba_2020.group('position').barh('position', 'count')
```

**Code:**

```python
nba_2020.where('salary', are.above(2e7)).group('position').barh('position', 'count')
```

Exercise: Show the **percentage** of each players in each position instead of the count

**Code:**

```python
counts = nba_2020.group('position')
percentages = counts.with_column('percentage', 100 * counts.column('count') /  sum(counts.column('count')))
percentages.barh('position', 'percentage')
```

### Use binning for numerical distributions

**Code:**

```python
# Data from https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/
top_movies = Table.read_table('top_movies_2026.csv')
top_movies.show(4)
```

**Code:**

```python
top_movies.set_format([1, 2, 3], CurrencyFormatter).show(4)
```

**Code:**

```python
top_movies.scatter(2, 3)
```

**Code:**

```python
top_movies.sort(3, descending=True).show(5)
```

#### **Task**: Visualize the distribution of movie ages

**Code:**

```python
ages = 2026 - top_movies.column('Year')
ages
```

**Code:**

```python
top_movies = top_movies.with_column('Age', ages)
top_movies
```

**Code:**

```python
top_movies.select('Title', 'Age').show(6)
```

**Code:**

```python
min(ages), max(ages)
```

- If you want to make equally sized bins, `np.arange()` is a great tool to help you.

**Code:**

```python
np.arange(0, max(ages)+10, 10)
```

**Code:**

```python
top_movies.hist('Age', bins = np.arange(0, max(ages)+10, 10), unit = 'Year')
```

- Otherwise, you can pick your own bins. These are just bins that we picked out.

**Code:**

```python
my_bins = make_array(0, 5, 10, 15, 25, 60)
```

**Code:**

```python
binned_data = top_movies.bin('Age', bins = my_bins)
binned_data
```

**Note:** The last "bin" does not include any observations!!

### Introducing the histogram and the area principle

**Code:**

```python
top_movies.hist('Age', bins = my_bins, unit = 'Year')
```

#### **Discussion Question**: Compare the bins $[0, 5)$ and $[15, 25)$. 

- Which one has more movies?
- Which one is more crowded?

### Challenge tasks

#### **Task**: Find the height of the $[15,25)$ bin in the histogram above.

$$\text{height} = \frac{\text{percent}}{\text{width}}$$

Add a column containing what percent of movies are in each bin (the **area** of each bin)

**Code:**

```python
binned_data = binned_data.with_column('Percent', 100*binned_data.column('Age count')/top_movies.num_rows)
```

**Code:**

```python
binned_data.show()
```

**Code:**

```python
percent = binned_data.where('bin', 15).column('Percent').item(0)
```

**Code:**

```python
width = 25-15
height = percent / width
```

**Code:**

```python
height
```

#### **Task**: Find the heights of the (rest of the) bins.

$$\text{height} = \frac{\text{percent}}{\text{width}}$$

Remember that the last row in the table does not represent a bin!

**Code:**

```python
height_table = binned_data.take(np.arange(binned_data.num_rows - 1))
height_table
```

Remember `np.diff`?

**Code:**

```python
bin_widths = np.diff(binned_data.column('bin'))
```

**Code:**

```python
bin_widths
```

**Code:**

```python
height_table = height_table.with_column('Width', bin_widths)
height_table
```

**Code:**

```python
height_table = height_table.with_column('Height',
                                        height_table.column('Percent')/height_table.column('Width'))
```

**Code:**

```python
height_table
```

To check our work one last time, let's see if the numbers in the last column match the heights of the histogram:

**Code:**

```python
top_movies.hist('Age', bins = my_bins, unit = 'Year')
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

### `top_movies_2026.csv`

200 rows, 5 columns.

| Column | Type |
| --- | --- |
| `Title` | str |
| `Worldwide Lifetime Gross` | int |
| `Domestic Lifetime Gross` | int |
| `Foreign Lifetime Gross` | int |
| `Year` | int |
