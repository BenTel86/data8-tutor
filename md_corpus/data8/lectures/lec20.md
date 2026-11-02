---
title: "Simulation"
lecture: lec20
course: data8
semester: sp26
source: lectures/data8/sp26/lec20/lec20.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

import warnings
warnings.simplefilter("ignore")
```

## Discussion Question: Super Soda

**Code:**

```python
def simulate_one_count(sample_size):
    return np.count_nonzero(np.random.choice(['H', 'T'], sample_size) == 'H')
simulate_one_count(200)
```

**Code:**

```python
num_simulations = 10000
counts = make_array()
for i in np.arange(num_simulations):
    counts = np.append(counts, simulate_one_count(200))
```

**Code:**

```python
trials = Table().with_column('Number of Heads', counts)
trials.hist(right_end=91)
plots.ylim(-0.001, 0.055)
plots.scatter(91, 0, color='red', s=40, zorder=3)
plots.title('Prediction Under the Null');
```

**Code:**

```python
np.count_nonzero(counts <= 91)/len(counts)
```

Conclusion:

## Changing the number of simulations

**Code:**

```python
# Keeping the data fixed, we can re-run the test with a new simulation under the null
def run_test(num_simulations, sample_size):
    counts = make_array()
    for i in np.arange(num_simulations):
        counts = np.append(counts, simulate_one_count(sample_size))
    return counts

counts = run_test(10000, 200)
np.count_nonzero(counts <= 91)/len(counts)
```

**Code:**

```python
# Let's repeat that 50 times for each number of simulations
tests = Table(['simulations', 'p-value for 91'])
for num_sims in [100, 1000, 10000]:
    for k in np.arange(50):
        counts = run_test(num_sims, 200)
        tests = tests.with_row([
            num_sims, 
            np.count_nonzero(counts <= 91)/len(counts),
        ])
tests.show(3)
```

**Code:**

```python
# For larger numbers of simulations, p-values are more consistent
tests.hist(1, group='simulations')
```

## Changing the size of the taste test

**Code:**

```python
# Suppose that the true proportion of people who prefer Super Soda is 45%
true_proportion = 0.45
true_distribution = make_array(true_proportion, 1 - true_proportion)
true_distribution
```

**Code:**

```python
# Taste tests with 200 people will give varioius numbers of people who prefer Super Soda
sample_size = 200
sample_proportions(sample_size, true_distribution) * sample_size
```

**Code:**

```python
# If you run a taste test for 200 people, what might you conclude?
def run_experiment(num_simulations, sample_size, true_proportion):
    # Collect data
    true_distribution = make_array(true_proportion, 1 - true_proportion)
    taste_test_results = sample_proportions(sample_size, true_distribution) * sample_size
    observed_stat_from_this_sample = taste_test_results.item(0)
    
    # Conduct hypothesis test
    counts = run_test(num_simulations, sample_size)
    p_value = np.count_nonzero(counts <= observed_stat_from_this_sample) / len(counts)
    return p_value

run_experiment(10000, 200, 0.45)
```

**Code:**

```python
# Let's imagine running our taste test over and over again to see how often we reject the null
true_proportion = 0.45
sample_size = 200
p_values = make_array()
for k in np.arange(100):
    p_value = run_experiment(1000, sample_size, true_proportion)
    p_values = np.append(p_values, p_value)
Table().with_column('P-value', p_values).hist(0, bins=20)
print('Percent of p-values at or below 0.05:', 100 * np.count_nonzero(p_values <= 0.05) / len(p_values))
```

# Simulation

10 tickets are selected at random with replacement from a basket that contains 30% green tickets, 20% blue tickets, and 50% red tickets. 
What's the chance that 5 or more of those 10 tickets are blue?

**Code:**

```python
sample_proportions(10, [.3, .2, .5]).item(1) * 10
```

**Code:**

```python
blue_counts = make_array()
for i in np.arange(10000):
    c = sample_proportions(10, [.3, .2, .5]).item(1) * 10
    blue_counts = np.append(blue_counts, c)
np.count_nonzero(blue_counts >= 5) / len(blue_counts)
```
