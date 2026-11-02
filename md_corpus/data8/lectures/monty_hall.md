---
title: "3 Door (Classic) Version"
lecture: lec31
variant: monty_hall
course: data8
semester: sp26
source: lectures/data8/sp26/lec31/monty_hall.ipynb
language: python
---

**Code:**

```python
from datascience import *
%matplotlib inline

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np
import warnings
```

# 3 Door (Classic) Version

**Code:**

```python
three_door_prizes = ['car', 'goat 1', 'goat 2']
def hide(prizes):
    prize_table = Table().with_column('Prize', prizes)
    return (prize_table.sample(with_replacement=False)
                       .with_column('Door', np.arange(1, len(prizes) + 1))
                       .select('Door', 'Prize'))
    
hide(three_door_prizes)
```

*Output:*

| Door | Prize |
| --- | --- |
| 1 | goat 2 |
| 2 | goat 1 |
| 3 | car |

**Code:**

```python
def pick(t):
    """Return the door number of a randomly selected row of a doors table."""
    return np.random.choice(t.column('Door'))

def monty_hall():
    doors = hide(three_door_prizes)
    contestant_initial_choice = pick(doors)
    remaining = doors.where('Door', are.not_equal_to(contestant_initial_choice))
    revealed = pick(remaining.where('Prize', are.containing('goat')))
    remaining = remaining.where('Door', are.not_equal_to(revealed))
    contestant_final_choice = pick(remaining)
    what_happened = Table().with_columns(
        'Door', [contestant_initial_choice, revealed, contestant_final_choice],
        'Status', ['Picked first', 'Revealed', 'Final choice'])
    return doors.join('Door', what_happened, 'Door')

monty_hall()
```

*Output:*

| Door | Prize | Status |
| --- | --- | --- |
| 1 | goat 1 | Final choice |
| 2 | goat 2 | Revealed |
| 3 | car | Picked first |

**Code:**

```python
def won_the_car(result_table):
    return result_table.where('Status', 'Final choice').column('Prize').item(0) == 'car'

won_the_car(monty_hall())
```

*Output:*

```text
False
```

**Code:**

```python
trials = 10000
cars = 0
for i in np.arange(trials):
    if won_the_car(monty_hall()):
        cars = cars + 1
print(100 * cars / trials, 'percent cars')
```

*Output (stdout):*

```text
66.13 percent cars
```

# 4 Door Version from Spring 2026 Midterm

**Code:**

```python
four_door_prizes = ['car', 'goat 1', 'goat 2', 'goat 3']
hide(four_door_prizes)
```

*Output:*

| Door | Prize |
| --- | --- |
| 1 | goat 1 |
| 2 | goat 2 |
| 3 | car |
| 4 | goat 3 |

**Code:**

```python
def monty_hall_4(lock):
    doors = hide(four_door_prizes)
    contestant_initial_choice = pick(doors)
    remaining = doors.where('Door', are.not_equal_to(contestant_initial_choice))
    
    if lock:
        locked = pick(remaining)
        remaining = remaining.where('Door', are.not_equal_to(locked))
    else:
        locked = None

    revealed = pick(remaining.where('Prize', are.containing('goat')))
    remaining = remaining.where('Door', are.not_equal_to(revealed))
    contestant_final_choice = pick(remaining)
    
    if lock:
        ignored = None
    else:
        remaining = remaining.where('Door', are.not_equal_to(contestant_final_choice))
        ignored = pick(remaining)
    
    what_happened = Table().with_columns(
        'Door', [contestant_initial_choice, revealed, contestant_final_choice, 
                 locked, ignored],
        'Status', ['Picked first', 'Revealed', 'Final choice',
                   'Locked', 'Ignored'])
    return doors.join('Door', what_happened, 'Door')

print('With Lock')
monty_hall_4(True).show()
print('Without Lock')
monty_hall_4(False).show()
```

*Output (stdout):*

```text
With Lock
```

*Output:*

| Door | Prize | Status |
| --- | --- | --- |
| 1 | car | Locked |
| 2 | goat 2 | Picked first |
| 3 | goat 3 | Revealed |
| 4 | goat 1 | Final choice |

*Output (stdout):*

```text
Without Lock
```

*Output:*

| Door | Prize | Status |
| --- | --- | --- |
| 1 | goat 3 | Picked first |
| 2 | goat 2 | Revealed |
| 3 | goat 1 | Ignored |
| 4 | car | Final choice |

**Code:**

```python
trials = 10000
lock = True

for lock in [True, False]:
    cars = 0
    for i in np.arange(trials):
        if won_the_car(monty_hall_4(lock)):
            cars = cars + 1
    print('With lock equal to', lock, 'win percentage is', 100 * cars / trials)
```

*Output (stdout):*

```text
With lock equal to True win percentage is 50.26
With lock equal to False win percentage is 37.79
```
