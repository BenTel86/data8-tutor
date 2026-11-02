---
title: "lec04"
lecture: lec04
course: data8
semester: sp26
source: lectures/data8/sp26/lec04/lec04.ipynb
language: python
---

**Code:**

```python
from datascience import *
import numpy as np
```

## Tables ##

A table is given a name (such as `nba`) in our programming environment so that we can perform operations on the whole table.

**Code:**

```python
# From https://github.com/erikgregorywebb/datasets/blob/master/nba-salaries.csv
nba = Table.read_table('nba_salaries.csv')
nba
```

*Output:*

| rank | name | position | team | salary | season |
| --- | --- | --- | --- | --- | --- |
| 1 | Shaquille O'Neal | C | Los Angeles Lakers | 17142000 | 2000 |
| 2 | Kevin Garnett | PF | Minnesota Timberwolves | 16806000 | 2000 |
| 3 | Alonzo Mourning | C | Miami Heat | 15004000 | 2000 |
| 4 | Juwan Howard | PF | Washington Wizards | 15000000 | 2000 |
| 5 | Scottie Pippen | SF | Portland Trail Blazers | 14795000 | 2000 |
| 6 | Karl Malone | PF | Utah Jazz | 14000000 | 2000 |
| 7 | Larry Johnson | F | New York Knicks | 11910000 | 2000 |
| 8 | Gary Payton | PG | Seattle SuperSonics | 11020000 | 2000 |
| 9 | Rasheed Wallace | PF | Portland Trail Blazers | 10800000 | 2000 |
| 10 | Shawn Kemp | C | Cleveland Cavaliers | 10780000 | 2000 |

Manipulating the table creates a new table, but doesn't change/lose the original.

**Code:**

```python
nba.select('name')
```

*Output:*

| name |
| --- |
| Shaquille O'Neal |
| Kevin Garnett |
| Alonzo Mourning |
| Juwan Howard |
| Scottie Pippen |
| Karl Malone |
| Larry Johnson |
| Gary Payton |
| Rasheed Wallace |
| Shawn Kemp |

**Code:**

```python
nba.drop('rank', 'position').sort('name')
```

*Output:*

| name | team | salary | season |
| --- | --- | --- | --- |
| A.C. Green | Miami Heat | 2250000 | 2001 |
| A.J. Guyton | Chicago Bulls | 316000 | 2001 |
| A.J. Guyton | Chicago Bulls | 465000 | 2002 |
| A.J. Price | Indiana Pacers | 457588 | 2010 |
| A.J. Price | Indiana Pacers | 762195 | 2011 |
| A.J. Price | Indiana Pacers | 854389 | 2012 |
| A.J. Price | Washington Wizards | 854389 | 2013 |
| A.J. Price | Phoenix Suns | 53838 | 2015 |
| AJ Hammons | Dallas Mavericks | 650000 | 2017 |
| AJ Hammons | Miami Heat | 1312611 | 2018 |

**Code:**

```python
nba.sort('name')
```

*Output:*

| rank | name | position | team | salary | season |
| --- | --- | --- | --- | --- | --- |
| 180 | A.C. Green | F | Miami Heat | 2250000 | 2001 |
| 355 | A.J. Guyton | G | Chicago Bulls | 316000 | 2001 |
| 384 | A.J. Guyton | G | Chicago Bulls | 465000 | 2002 |
| 441 | A.J. Price | PG | Indiana Pacers | 457588 | 2010 |
| 444 | A.J. Price | PG | Indiana Pacers | 762195 | 2011 |
| 414 | A.J. Price | PG | Indiana Pacers | 854389 | 2012 |
| 445 | A.J. Price | PG | Washington Wizards | 854389 | 2013 |
| 522 | A.J. Price | PG | Phoenix Suns | 53838 | 2015 |
| 477 | AJ Hammons | C | Dallas Mavericks | 650000 | 2017 |
| 418 | AJ Hammons | C | Miami Heat | 1312611 | 2018 |

**Code:**

```python
'nba'
```

Because each operation creates a new table, multiple operations can be applied.

**Code:**

```python
nba.where('position', 'PG')
```

*Output:*

| rank | name | position | team | salary | season |
| --- | --- | --- | --- | --- | --- |
| 8 | Gary Payton | PG | Seattle SuperSonics | 11020000 | 2000 |
| 11 | Damon Stoudamire | PG | Portland Trail Blazers | 10125000 | 2000 |
| 20 | Stephon Marbury | PG | New Jersey Nets | 9000000 | 2000 |
| 24 | Nick Van Exel | PG | Denver Nuggets | 8354000 | 2000 |
| 26 | Terrell Brandon | PG | Minnesota Timberwolves | 7400000 | 2000 |
| 34 | Jason Kidd | PG | Phoenix Suns | 6858000 | 2000 |
| 35 | Kenny Anderson | PG | Boston Celtics | 6680000 | 2000 |
| 39 | Steve Nash | PG | Dallas Mavericks | 5500000 | 2000 |
| 55 | Charlie Ward | PG | New York Knicks | 4540000 | 2000 |
| 61 | Darrel Armstrong | PG | Orlando Magic | 4125000 | 2000 |

**Code:**

```python
nba.where('name', "Shaquille O'Neal")
```

*Output:*

| rank | name | position | team | salary | season |
| --- | --- | --- | --- | --- | --- |
| 1 | Shaquille O'Neal | C | Los Angeles Lakers | 17142000 | 2000 |
| 2 | Shaquille O'Neal | C | Los Angeles Lakers | 19285000 | 2001 |
| 2 | Shaquille O'Neal | C | Los Angeles Lakers | 21428000 | 2002 |
| 2 | Shaquille O'Neal | C | Los Angeles Lakers | 23571000 | 2003 |
| 2 | Shaquille O'Neal | C | Los Angeles Lakers | 26571000 | 2004 |
| 1 | Shaquille O'Neal | C | Miami Heat | 29464000 | 2005 |
| 1 | Shaquille O'Neal | C | Miami Heat | 20000000 | 2006 |
| 2 | Shaquille O'Neal | C | Miami Heat | 20000000 | 2007 |
| 2 | Shaquille O'Neal | C | Phoenix Suns | 21000000 | 2008 |
| 5 | Shaquille O'Neal | C | Phoenix Suns | 21000000 | 2009 |

The result of applying operations is a table, which can also be given a name (e.g., `point_guards`) in our programming environment.

**Code:**

```python
point_guards = nba.where('position', 'PG').drop('rank', 'position')
point_guards
```

*Output:*

| name | team | salary | season |
| --- | --- | --- | --- |
| Gary Payton | Seattle SuperSonics | 11020000 | 2000 |
| Damon Stoudamire | Portland Trail Blazers | 10125000 | 2000 |
| Stephon Marbury | New Jersey Nets | 9000000 | 2000 |
| Nick Van Exel | Denver Nuggets | 8354000 | 2000 |
| Terrell Brandon | Minnesota Timberwolves | 7400000 | 2000 |
| Jason Kidd | Phoenix Suns | 6858000 | 2000 |
| Kenny Anderson | Boston Celtics | 6680000 | 2000 |
| Steve Nash | Dallas Mavericks | 5500000 | 2000 |
| Charlie Ward | New York Knicks | 4540000 | 2000 |
| Darrel Armstrong | Orlando Magic | 4125000 | 2000 |

**Code:**

```python
point_guards.where('season', 2020).sort('name').sort('team')
```

*Output:*

| name | team | salary | season |
| --- | --- | --- | --- |
| Brandon Goodwin | Atlanta Hawks | 522738 | 2020 |
| Trae Young | Atlanta Hawks | 6273000 | 2020 |
| Brad Wanamaker | Boston Celtics | 1445697 | 2020 |
| Carsen Edwards | Boston Celtics | 1228026 | 2020 |
| Kemba Walker | Boston Celtics | 32742000 | 2020 |
| Marcus Smart | Boston Celtics | 12553571 | 2020 |
| Kyrie Irving | Brooklyn Nets | 31742000 | 2020 |
| Spencer Dinwiddie | Brooklyn Nets | 10605600 | 2020 |
| Devonte' Graham | Charlotte Hornets | 1416852 | 2020 |
| Terry Rozier | Charlotte Hornets | 19894737 | 2020 |

**Code:**

```python
nba
```

Sorting can be performed in descending order as well.

**Code:**

```python
point_guards.where('season', 2020).sort('salary').show(10)
```

*Output:*

| name | team | salary | season |
| --- | --- | --- | --- |
| Ky Bowman | Golden State Warriors | 350189 | 2020 |
| Reggie Jackson | LA Clippers | 512721 | 2020 |
| Brandon Goodwin | Atlanta Hawks | 522738 | 2020 |
| Chris Clemons | Houston Rockets | 563347 | 2020 |
| Justin Robinson | Washington Wizards | 898310 | 2020 |
| Jalen Lecque | Phoenix Suns | 898310 | 2020 |
| Gary Payton II | Washington Wizards | 1052909 | 2020 |
| Carsen Edwards | Boston Celtics | 1228026 | 2020 |
| Devonte' Graham | Charlotte Hornets | 1416852 | 2020 |
| Jevon Carter | Phoenix Suns | 1416852 | 2020 |

**Code:**

```python
point_guards.where('season', 2020).sort('salary', descending=True).show(10)
```

*Output:*

| name | team | salary | season |
| --- | --- | --- | --- |
| Stephen Curry | Golden State Warriors | 40231758 | 2020 |
| Chris Paul | Oklahoma City Thunder | 38506482 | 2020 |
| Russell Westbrook | Houston Rockets | 38506482 | 2020 |
| John Wall | Washington Wizards | 38199000 | 2020 |
| Kyle Lowry | Toronto Raptors | 34996296 | 2020 |
| Kemba Walker | Boston Celtics | 32742000 | 2020 |
| Mike Conley | Utah Jazz | 32511624 | 2020 |
| Kyrie Irving | Brooklyn Nets | 31742000 | 2020 |
| Damian Lillard | Portland Trail Blazers | 29802321 | 2020 |
| Malcolm Brogdon | Indiana Pacers | 20000000 | 2020 |

## Numbers ##

**Code:**

```python
30
```

*Output:*

```text
30
```

**Code:**

```python
10 * 3    # int
```

*Output:*

```text
30
```

**Code:**

```python
10 / 3    # float
```

*Output:*

```text
3.3333333333333335
```

**Code:**

```python
10 / 2
```

*Output:*

```text
5.0
```

**Code:**

```python
10 ** 3
```

*Output:*

```text
1000
```

**Code:**

```python
10 ** 0.5
```

*Output:*

```text
3.1622776601683795
```

**Code:**

```python
1234567 ** 89
```

*Output:*

```text
139574185988226216352411677967079384654819840770263154148901015711434587555916221871855053939370772085656915237689603767083349991793713346471091572628494106076146419389211087459209170823939332677859093756734470172351895079430772488109105692648444480028380122417140932569432824316430008740958025053716735421344729410520681559715479472541631321425013768978692403188995380725532383634472359562908542469547971146457062422356845701571795811721146126639734809904577967012608961528997012178537266420111446716001493476975934877110973383995456863730247
```

**Code:**

```python
10 / 3
```

*Output:*

```text
3.3333333333333335
```

**Code:**

```python
75892745.215489247589274985712
```

*Output:*

```text
75892745.21548925
```

**Code:**

```python
75892745.215489247589274985712 - 75892745.21548925
```

*Output:*

```text
0.0
```

**Code:**

```python
(13 ** 0.5) ** 2
```

*Output:*

```text
12.999999999999998
```

**Code:**

```python
3.605551275463989 * 3.605551275463989
```

*Output:*

```text
12.999999999999998
```

**Code:**

```python
int(10 / 5)
```

*Output:*

```text
2
```

**Code:**

```python
int(10 / 4)
```

*Output:*

```text
2
```

**Code:**

```python
float(3)
```

*Output:*

```text
3.0
```

**Code:**

```python
6 / 4
```

*Output:*

```text
1.5
```

**Code:**

```python
6 / 4000
```

*Output:*

```text
0.0015
```

**Code:**

```python
6 / 400000000000000000000000000000000000000000000000000000000
```

*Output:*

```text
1.5e-56
```

**Code:**

```python
400000000000000000000000000000000000000000000000000000000 * 1.5e-56
```

*Output:*

```text
6.0
```

**Code:**

```python
1.5e-56
```

*Output:*

```text
1.5e-56
```

**Code:**

```python
x = 5
```

**Code:**

```python
x
```

*Output:*

```text
5
```

**Code:**

```python
x + 1
```

*Output:*

```text
6
```

**Code:**

```python
2x
```

*Error:*

```text
  Cell In[64], line 1
    2x
    ^
SyntaxError: invalid decimal literal
```

**Code:**

```python
2 * x
```

*Output:*

```text
10
```

## Strings ##

**Code:**

```python
'Flavor'
```

*Output:*

```text
'Flavor'
```

**Code:**

```python
flavor = 2
```

**Code:**

```python
flavor
```

*Output:*

```text
2
```

**Code:**

```python
# The line below causes a name error
# Flavor
```

**Code:**

```python
"Flavor"
```

*Output:*

```text
'Flavor'
```

**Code:**

```python
'Don't always use single quotes'
```

*Error:*

```text
  Cell In[72], line 1
    'Don't always use single quotes'
                                   ^
SyntaxError: unterminated string literal (detected at line 1)
```

**Code:**

```python
"Don't always use single quotes"
```

*Output:*

```text
"Don't always use single quotes"
```

**Code:**

```python
'straw' 'berry' # concatenation
```

*Output:*

```text
'strawberry'
```

**Code:**

```python
'straw' + 'berry' # concatenation
```

*Output:*

```text
'strawberry'
```

**Code:**

```python
'Chris' + 'Paul' # spaces aren't added for you
```

*Output:*

```text
'ChrisPaul'
```

**Code:**

```python
'Chris' + ' ' + 'Paul'
```

*Output:*

```text
'Chris Paul'
```

**Code:**

```python
x = 'straw'
y = 'berry'
x + y
```

*Output:*

```text
'strawberry'
```

**Code:**

```python
x y
```

*Error:*

```text
  Cell In[80], line 1
    x y
      ^
SyntaxError: invalid syntax
```

**Code:**

```python
'ha' * 100
```

*Output:*

```text
'hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha'
```

**Code:**

```python
'lo' * 5.5
```

*Error:*

```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[82], line 1
----> 1 'lo' * 5.5

TypeError: can't multiply sequence by non-int of type 'float'
```

**Code:**

```python
'ha' + 10
```

*Error:*

```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[83], line 1
----> 1 'ha' + 10

TypeError: can only concatenate str (not "int") to str
```

**Code:**

```python
'ha' + str(10)
```

*Output:*

```text
'ha10'
```

**Code:**

```python
'ha' + '10'
```

*Output:*

```text
'ha10'
```

**Code:**

```python
'3' + 5
```

*Error:*

```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[87], line 1
----> 1 '3' + 5

TypeError: can only concatenate str (not "int") to str
```

**Code:**

```python
int('3') + 5
```

*Output:*

```text
8
```

**Code:**

```python
int('3.0')
```

*Error:*

```text
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[90], line 1
----> 1 int('3.0')

ValueError: invalid literal for int() with base 10: '3.0'
```

**Code:**

```python
'3.0'
```

*Output:*

```text
'3.0'
```

**Code:**

```python
float('3.0')
```

*Output:*

```text
3.0
```

**Code:**

```python
int(3.0)
```

*Output:*

```text
3
```

**Code:**

```python
int(float('3.0'))
```

*Output:*

```text
3
```

**Code:**

```python
3
```

*Output:*

```text
3
```

**Code:**

```python
dot_oh = '.0'
float('3' + dot_oh)
```

*Output:*

```text
3.0
```

**Code:**

```python
float('3' + dot_oh) * 7
```

*Output:*

```text
21.0
```

## Types ##

**Code:**

```python
type(10)
```

*Output:*

```text
int
```

**Code:**

```python
a = 10
```

**Code:**

```python
a
```

*Output:*

```text
10
```

**Code:**

```python
type(a)
```

*Output:*

```text
int
```

**Code:**

```python
type(4.5)
```

*Output:*

```text
float
```

**Code:**

```python
type('abc')
```

*Output:*

```text
str
```

**Code:**

```python
type(nba)
```

*Output:*

```text
datascience.tables.Table
```

**Code:**

```python
type(Table.read_table('nba_salaries.csv'))
```

*Output:*

```text
datascience.tables.Table
```

**Code:**

```python
type(True)
```

*Output:*

```text
bool
```

**Code:**

```python
type(abs(-5))
```

*Output:*

```text
int
```

**Code:**

```python
type(abs)
```

*Output:*

```text
builtin_function_or_method
```

## Arrays ##

**Code:**

```python
first_four = make_array(1, 2, 3, 4)
```

**Code:**

```python
first_four
```

*Output:*

```text
array([1, 2, 3, 4])
```

**Code:**

```python
array([1, 2, 3, 4])
```

*Error:*

```text
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[116], line 1
----> 1 array([1, 2, 3, 4])

NameError: name 'array' is not defined
```

**Code:**

```python
from numpy import array
```

**Code:**

```python
array([1, 2, 3, 4])
```

*Output:*

```text
array([1, 2, 3, 4])
```

**Code:**

```python
first_four
```

*Output:*

```text
array([1, 2, 3, 4])
```

**Code:**

```python
first_four * 2
```

*Output:*

```text
array([2, 4, 6, 8])
```

**Code:**

```python
first_four ** 2
```

*Output:*

```text
array([ 1,  4,  9, 16])
```

**Code:**

```python
(first_four + 1) ** 2
```

*Output:*

```text
array([ 4,  9, 16, 25])
```

**Code:**

```python
first_four # array is unchanged, just like when we call show/select/drop on Table
```

*Output:*

```text
array([1, 2, 3, 4])
```

**Code:**

```python
next_four = make_array(5, 6, 7, 8)
```

**Code:**

```python
next_four
```

*Output:*

```text
array([5, 6, 7, 8])
```

**Code:**

```python
first_four + next_four
```

*Output:*

```text
array([ 6,  8, 10, 12])
```

**Code:**

```python
only_three = make_array(5, 6, 7)
```

**Code:**

```python
# This line will cause an error 
first_four + only_three
```

*Error:*

```text
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[129], line 2
      1 # This line will cause an error 
----> 2 first_four + only_three

ValueError: operands could not be broadcast together with shapes (4,) (3,)
```

**Code:**

```python
str_array = make_array('ha', 'he', 'ho')
```

**Code:**

```python
str_array
```

*Output:*

```text
array(['ha', 'he', 'ho'],
      dtype='<U2')
```

**Code:**

```python
str_array * 4
```

*Error:*

```text
---------------------------------------------------------------------------
UFuncTypeError                            Traceback (most recent call last)
Cell In[132], line 1
----> 1 str_array * 4

UFuncTypeError: ufunc 'multiply' did not contain a loop with signature matching types (dtype('<U2'), dtype('int64')) -> None
```

**Code:**

```python
next_four
```

*Output:*

```text
array([5, 6, 7, 8])
```

**Code:**

```python
next_four.item(0)
```

*Output:*

```text
5
```

**Code:**

```python
next_four.item(4)
```

*Error:*

```text
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[138], line 1
----> 1 next_four.item(4)

IndexError: index 4 is out of bounds for axis 0 with size 4
```

**Code:**

```python
sum(next_four)
```

**Code:**

```python
np.average(next_four)
```

**Code:**

```python
len(next_four)
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
