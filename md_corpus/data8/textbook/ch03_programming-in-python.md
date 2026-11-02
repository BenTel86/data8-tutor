---
title: "Chapter 3: Programming in Python"
book: "Computational and Inferential Thinking (Data 8 textbook)"
chapter: 3
semester: sp26
sections:
  - "3.1 Expressions"
  - "3.2 Names"
  - "3.3 Call Expressions"
  - "3.4 Introduction to Tables"
sources:
  - textbooks/sp26/chapters/03/programming-in-python.md
  - textbooks/sp26/chapters/03/1/Expressions.ipynb
  - textbooks/sp26/chapters/03/2/Names.ipynb
  - textbooks/sp26/chapters/03/2/1/Growth.ipynb
  - textbooks/sp26/chapters/03/3/Calls.ipynb
  - textbooks/sp26/chapters/03/4/Introduction_to_Tables.ipynb
---

# Chapter 3: Programming in Python

Programming can dramatically improve our ability to collect and analyze information
about the world, which in turn can lead to discoveries through the kind of careful
reasoning demonstrated in the previous section. In data science, the purpose of
writing a program is to instruct a computer to carry out the steps of an analysis.
Computers cannot study the world on their own. People must describe precisely what
steps the computer should take in order to collect and analyze data, and those steps
are expressed through programs.

## 3.1 Expressions

Programming languages are much simpler than human languages. Nonetheless, there are some rules of grammar to learn in any language, and that is where we will begin. In this text, we will use the [Python](https://www.python.org/) programming language. Learning the grammar rules is essential, and the same rules used in the most basic programs are also central to more sophisticated programs.

Programs are made up of *expressions*, which describe to the computer how to combine pieces of data. For example, a multiplication expression consists of a `*` symbol between two numerical expressions. Expressions, such as `3 * 4`, are *evaluated* by the computer. The value (the result of *evaluation*) of the last expression in each cell, `12` in this case, is displayed below the cell.

```python
3 * 4
```

*Output:*

```text
12
```

The grammar rules of a programming language are rigid. In Python, the `*` symbol cannot appear twice in a row. The computer will not try to interpret an expression that differs from its prescribed expression structures. Instead, it will show a `SyntaxError` error. The *Syntax* of a language is its set of grammar rules, and a `SyntaxError` indicates that an expression structure doesn't match any of the rules of the language.

```python
3 * * 4
```

*Error:*

```text
  File "<ipython-input-2-012ea60b41dd>", line 1
    3 * * 4
        ^
SyntaxError: invalid syntax
```

Small changes to an expression can change its meaning entirely. Below, the space between the `*`'s has been removed. Because `**` appears between two numerical expressions, the expression is a well-formed *exponentiation* expression (the first number raised to the power of the second: 3 times 3 times 3 times 3). The symbols `*` and `**` are called *operators*, and the values they combine are called *operands*.

```python
3 ** 4
```

*Output:*

```text
81
```

**Common Operators.** Data science often involves combining numerical values, and the set of operators in a programming language are designed so that expressions can be used to express any sort of arithmetic. In Python, the following operators are essential.

| Expression Type | Operator | Example    | Value     |
|-----------------|----------|------------|-----------|
| Addition        | `+`      | `2 + 3`    | `5`       |
| Subtraction     | `-`      | `2 - 3`    | `-1`      |
| Multiplication  | `*`      | `2 * 3`    | `6`       |
| Division        | `/`      | `7 / 3`    | `2.66667` |
| Remainder       | `%`      | `7 % 3`    | `1`       |
| Exponentiation  | `**`     | `2 ** 0.5` | `1.41421` |

Python expressions obey the same familiar rules of *precedence* as in algebra: multiplication and division occur before addition and subtraction. Parentheses can be used to group together smaller expressions within a larger expression.

```python
1 + 2 * 3 * 4 * 5 / 6 ** 3 + 7 + 8 - 9 + 10
```

*Output:*

```text
17.555555555555557
```

```python
1 + 2 * (3 * 4 * 5 / 6) ** 3 + 7 + 8 - 9 + 10
```

*Output:*

```text
2017.0
```

This chapter introduces many types of expressions. Learning to program involves trying out everything you learn in combination, investigating the behavior of the computer. What happens if you divide by zero? What happens if you divide twice in a row? You don't always need to ask an expert (or the Internet); many of these details can be discovered by trying them out yourself.

## 3.2 Names

Names are given to values in Python using an *assignment* statement. In an assignment, a name is followed by `=`, which is followed by any expression. The value of the expression to the right of `=` is *assigned* to the name. Once a name has a value assigned to it, the value will be substituted for that name in future expressions.

```python
a = 10
b = 20
a + b
```

*Output:*

```text
30
```

A previously assigned name can be used in the expression to the right of `=`.

```python
quarter = 1/4
half = 2 * quarter
half
```

*Output:*

```text
0.5
```

However, only the current value of an expression is assigned to a name. If that value changes later, names that were defined in terms of that value will not change automatically.

```python
quarter = 4
half
```

*Output:*

```text
0.5
```

Names must start with a letter, but can contain both letters and numbers. A name cannot contain a space; instead, it is common to use an underscore character `_` to replace each space. Names are only as useful as you make them; it's up to the programmer to choose names that are easy to interpret. Typically, more meaningful names can be invented than `a` and `b`. For example, to describe the sales tax on a $5 purchase in Berkeley, CA, the following names clarify the meaning of the various quantities involved.

```python
purchase_price = 5
state_tax_rate = 0.075
county_tax_rate = 0.02
city_tax_rate = 0
sales_tax_rate = state_tax_rate + county_tax_rate + city_tax_rate
sales_tax = purchase_price * sales_tax_rate
sales_tax
```

*Output:*

```text
0.475
```

### 3.2.1 Example: Growth Rates

The relationship between two measurements of the same quantity taken at different times is often expressed as a *growth rate*. For example, the United States federal government [employed](http://www.bls.gov/opub/mlr/2013/article/industry-employment-and-output-projections-to-2022.htm) 2,766,000 people in 2002 and 2,814,000 people in 2012. To compute a growth rate, we must first decide which value to treat as the `initial` amount. For values over time, the earlier value is a natural choice. Then, we divide the difference between the `changed` and `initial` amount by the `initial` amount.

```python
initial = 2766000
changed = 2814000
(changed - initial) / initial
```

*Output:*

```text
0.01735357917570499
```

It is also typical to subtract one from the ratio of the two measurements, which yields the same value.

```python
(changed/initial) - 1
```

*Output:*

```text
0.017353579175704903
```

This value is the growth rate over 10 years. A useful property of growth rates is that they don't change even if the values are expressed in different units. So, for example, we can express the same relationship between thousands of people in 2002 and 2012.

```python
initial = 2766
changed = 2814
(changed/initial) - 1
```

*Output:*

```text
0.017353579175704903
```

In 10 years, the number of employees of the US Federal Government has increased by only 1.74%. In that time, the total expenditures of the US Federal Government increased from \$2.37 trillion to \$3.38 trillion in 2012.

```python
initial = 2.37
changed = 3.38
(changed/initial) - 1
```

*Output:*

```text
0.4261603375527425
```

A 42.6% increase in the federal budget is much larger than the 1.74% increase in federal employees. In fact, the number of federal employees has grown much more slowly than the population of the United States, which increased 9.21% in the same time period from 287.6 million people in 2002 to 314.1 million in 2012.

```python
initial = 287.6
changed = 314.1
(changed/initial) - 1
```

*Output:*

```text
0.09214186369958277
```

A growth rate can be negative, representing a decrease in some value. For example, the number of manufacturing jobs in the US decreased from 15.3 million in 2002 to 11.9 million in 2012, a -22.2% growth rate.

```python
initial = 15.3
changed = 11.9
(changed/initial) - 1
```

*Output:*

```text
-0.2222222222222222
```

An annual growth rate is a growth rate of some quantity over a single year. An annual growth rate of 0.035, accumulated each year for 10 years, gives a much larger ten-year growth rate of 0.41 (or 41%).

```python
1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 * 1.035 - 1
```

*Output:*

```text
0.410598760621121
```

This same computation can be expressed using names and exponents.

```python
annual_growth_rate = 0.035
ten_year_growth_rate = (1 + annual_growth_rate) ** 10 - 1
ten_year_growth_rate
```

*Output:*

```text
0.410598760621121
```

Likewise, a ten-year growth rate can be used to compute an equivalent annual growth rate. Below, `t` is the number of years that have passed between measurements. The following computes the annual growth rate of federal expenditures over the last 10 years.

```python
initial = 2.37
changed = 3.38
t = 10
(changed/initial) ** (1/t) - 1
```

*Output:*

```text
0.03613617208346853
```

The total growth over 10 years is equivalent to a 3.6% increase each year.

In summary, a growth rate `g` is used to describe the relative size of an `initial` amount and a `changed` amount after some amount of time `t`. To compute `changed`, apply the growth rate `g` repeatedly, `t` times using exponentiation.

`initial * (1 + g) ** t`

To compute `g`, raise the total growth to the power of `1/t` and subtract one.

`(changed/initial) ** (1/t) - 1`

## 3.3 Call Expressions

*Call expressions* invoke functions, which are named operations. The name of the function appears first, followed by expressions in parentheses.

```python
abs(-12)
```

*Output:*

```text
12
```

```python
round(5 - 1.3)
```

*Output:*

```text
4
```

```python
max(2, 2 + 3, 4)
```

*Output:*

```text
5
```

In this last example, the `max` function is *called* on three *arguments*: 2, 5, and 4. The value of each expression within parentheses is passed to the function, and the function *returns* the final value of the full call expression. The `max` function can take any number of arguments and returns the maximum.

A few functions are available by default, such as `abs` and `round`, but most functions that are built into the Python language are stored in a collection of functions called a *module*. An *import statement* is used to provide access to a module, such as `math` or `operator`.

```python
import math
import operator
math.sqrt(operator.add(4, 5))
```

*Output:*

```text
3.0
```

An equivalent expression could be expressed using the `+` and `**` operators instead.

```python
(4 + 5) ** 0.5
```

*Output:*

```text
3.0
```

Operators and call expressions can be used together in an expression. The *percent difference* between two values is used to compare values for which neither one is obviously `initial` or `changed`. For example, in 2014 Florida farms produced 2.72 billion eggs while Iowa farms produced 16.25 billion eggs (http://quickstats.nass.usda.gov/). The percent difference is 100 times the absolute value of the difference between the values, divided by their average. In this case, the difference is larger than the average, and so the percent difference is greater than 100.

```python
florida = 2.72
iowa = 16.25
100*abs(florida-iowa)/((florida+iowa)/2)
```

*Output:*

```text
142.6462836056932
```

Learning how different functions behave is an important part of learning a programming language. A Jupyter notebook can assist in remembering the names and effects of different functions. When editing a code cell, press the *tab* key after typing the beginning of a name to bring up a list of ways to complete that name. For example, press *tab* after `math.` to see all of the functions available in the `math` module. Typing will narrow down the list of options. To learn more about a function, place a `?` after its name. For example, typing `math.log?` will bring up a description of the `log` function in the `math` module.

```python
math.log?
```

log(x[, base])

    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.

The square brackets in the example call indicate that an argument is optional. That is, `log` can be called with either one or two arguments.

```python
math.log(16, 2)
```

*Output:*

```text
4.0
```

```python
math.log(16)/math.log(2)
```

*Output:*

```text
4.0
```

The list of [Python's built-in functions](https://docs.python.org/3/library/functions.html) is quite long and includes many functions that are never needed in data science applications. The list of [mathematical functions in the `math` module](https://docs.python.org/3/library/math.html) is similarly long. This text will introduce the most important functions in context, rather than expecting the reader to memorize or understand these lists.

## 3.4 Introduction to Tables

```python
from datascience import *
path_data = '../../../assets/data/'
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

cones = Table.read_table(path_data + 'cones.csv')
nba = Table.read_table(path_data + 'nba_salaries.csv').relabeled(3, 'SALARY')
movies = Table.read_table(path_data + 'movies_by_year.csv')
```

We can now apply Python to analyze data. We will work with data stored in Table structures.

Tables are a fundamental way of representing data sets. A table can be viewed in two ways:
* a sequence of named columns that each describe a single attribute of all entries in a data set, or
* a sequence of rows that each contain all information about a single individual in a data set.

We will study tables in great detail in the next several chapters. For now, we will just introduce a few methods without going into technical details. 

The table `cones` has been imported for us; later we will see how, but here we will just work with it. First, let's take a look at it.

```python
cones
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| strawberry | pink | 3.55 |
| chocolate | light brown | 4.75 |
| chocolate | dark brown | 5.25 |
| strawberry | pink | 5.25 |
| chocolate | dark brown | 5.25 |
| bubblegum | pink | 4.75 |

The table has six rows. Each row corresponds to one ice cream cone. The ice cream cones are the *individuals*.

Each cone has three attributes: flavor, color, and price. Each column contains the data on one of these attributes, and so all the entries of any single column are of the same kind. Each column has a label. We will refer to columns by their labels.

A table method is just like a function, but it must operate on a table. So the call looks like

`name_of_table.method(arguments)`

For example, if you want to see just the first two rows of a table, you can use the table method `show`.

```python
cones.show(2)
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| strawberry | pink | 3.55 |
| chocolate | light brown | 4.75 |

You can replace 2 by any number of rows. If you ask for more than six, you will only get six, because `cones` only has six rows.

### Choosing Sets of Columns
The method `select` creates a new table consisting of only the specified columns.

```python
cones.select('Flavor')
```

*Output:*

| Flavor |
| --- |
| strawberry |
| chocolate |
| chocolate |
| strawberry |
| chocolate |
| bubblegum |

This leaves the original table unchanged.

```python
cones
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| strawberry | pink | 3.55 |
| chocolate | light brown | 4.75 |
| chocolate | dark brown | 5.25 |
| strawberry | pink | 5.25 |
| chocolate | dark brown | 5.25 |
| bubblegum | pink | 4.75 |

You can select more than one column, by separating the column labels by commas.

```python
cones.select('Flavor', 'Price')
```

*Output:*

| Flavor | Price |
| --- | --- |
| strawberry | 3.55 |
| chocolate | 4.75 |
| chocolate | 5.25 |
| strawberry | 5.25 |
| chocolate | 5.25 |
| bubblegum | 4.75 |

You can also *drop* columns you don't want. The table above can be created by dropping the `Color` column.

```python
cones.drop('Color')
```

*Output:*

| Flavor | Price |
| --- | --- |
| strawberry | 3.55 |
| chocolate | 4.75 |
| chocolate | 5.25 |
| strawberry | 5.25 |
| chocolate | 5.25 |
| bubblegum | 4.75 |

You can name this new table and look at it again by just typing its name.

```python
no_colors = cones.drop('Color')

no_colors
```

*Output:*

| Flavor | Price |
| --- | --- |
| strawberry | 3.55 |
| chocolate | 4.75 |
| chocolate | 5.25 |
| strawberry | 5.25 |
| chocolate | 5.25 |
| bubblegum | 4.75 |

Like `select`, the `drop` method creates a smaller table and leaves the original table unchanged. In order to explore your data, you can create any number of smaller tables by using choosing or dropping columns. It will do no harm to your original data table.

### Sorting Rows

The `sort` method creates a new table by arranging the rows of the original table in ascending order of the values in the specified column. Here the `cones` table has been sorted in ascending order of the price of the cones.

```python
cones.sort('Price')
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| strawberry | pink | 3.55 |
| chocolate | light brown | 4.75 |
| bubblegum | pink | 4.75 |
| chocolate | dark brown | 5.25 |
| strawberry | pink | 5.25 |
| chocolate | dark brown | 5.25 |

To sort in descending order, you can use an *optional* argument to `sort`. As the name implies, optional arguments don't have to be used, but they can be used if you want to change the default behavior of a method. 

By default, `sort` sorts in increasing order of the values in the specified column. To sort in decreasing order, use the optional argument `descending=True`.

```python
cones.sort('Price', descending=True)
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| chocolate | dark brown | 5.25 |
| strawberry | pink | 5.25 |
| chocolate | dark brown | 5.25 |
| bubblegum | pink | 4.75 |
| chocolate | light brown | 4.75 |
| strawberry | pink | 3.55 |

Like `select` and `drop`, the `sort` method leaves the original table unchanged.

### Selecting Rows that Satisfy a Condition
The `where` method creates a new table consisting only of the rows that satisfy a given condition. In this section we will work with a very simple condition, which is that the value in a specified column must be equal to a value that we also specify. Thus the `where` method has two arguments.

The code in the cell below creates a table consisting only of the rows corresponding to chocolate cones.

```python
cones.where('Flavor', 'chocolate')
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |
| chocolate | light brown | 4.75 |
| chocolate | dark brown | 5.25 |
| chocolate | dark brown | 5.25 |

The arguments, separated by a comma, are the label of the column and the value we are looking for in that column. The `where` method can also be used when the condition that the rows must satisfy is more complicated. In those situations the call will be a little more complicated as well.

It is important to provide the value exactly. For example, if we specify `Chocolate` instead of `chocolate`, then `where` correctly finds no rows where the flavor is `Chocolate`.

```python
cones.where('Flavor', 'Chocolate')
```

*Output:*

| Flavor | Color | Price |
| --- | --- | --- |

Like all the other table methods in this section, `where` leaves the original table unchanged.

### Example: Salaries in the NBA

"The NBA is the highest paying professional sports league in the world," [reported CNN](http://edition.cnn.com/2015/12/04/sport/gallery/highest-paid-nba-players/) in March 2016. The table `nba` contains the [salaries of all National Basketball Association players](https://www.statcrunch.com/app/index.php?dataid=1843341) in 2015-2016.

Each row represents one player. The columns are:

| **Column Label**   | Description                                         |
|--------------------|-----------------------------------------------------|
| `PLAYER`           | Player's name                                       |
| `POSITION`         | Player's position on team                           |
| `TEAM`             | Team name                                           |
|`SALARY`    | Player's salary in 2015-2016, in millions of dollars|
 
The code for the positions is PG (Point Guard), SG (Shooting Guard), PF (Power Forward), SF (Small Forward), and C (Center). But what follows doesn't involve details about how basketball is played.

The first row shows that Paul Millsap, Power Forward for the Atlanta Hawks, had a salary of almost $\$18.7$ million in 2015-2016.

```python
nba
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Paul Millsap | PF | Atlanta Hawks | 18.6717 |
| Al Horford | C | Atlanta Hawks | 12 |
| Tiago Splitter | C | Atlanta Hawks | 9.75625 |
| Jeff Teague | PG | Atlanta Hawks | 8 |
| Kyle Korver | SG | Atlanta Hawks | 5.74648 |
| Thabo Sefolosha | SF | Atlanta Hawks | 4 |
| Mike Scott | PF | Atlanta Hawks | 3.33333 |
| Kent Bazemore | SF | Atlanta Hawks | 2 |
| Dennis Schroder | PG | Atlanta Hawks | 1.7634 |
| Tim Hardaway Jr. | SG | Atlanta Hawks | 1.30452 |

Fans of Stephen Curry can find his row by using `where`.

```python
nba.where('PLAYER', 'Stephen Curry')
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Stephen Curry | PG | Golden State Warriors | 11.3708 |

We can also create a new table called `warriors` consisting of just the data for the Golden State Warriors.

```python
warriors = nba.where('TEAM', 'Golden State Warriors')
warriors
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Klay Thompson | SG | Golden State Warriors | 15.501 |
| Draymond Green | PF | Golden State Warriors | 14.2609 |
| Andrew Bogut | C | Golden State Warriors | 13.8 |
| Andre Iguodala | SF | Golden State Warriors | 11.7105 |
| Stephen Curry | PG | Golden State Warriors | 11.3708 |
| Jason Thompson | PF | Golden State Warriors | 7.00847 |
| Shaun Livingston | PG | Golden State Warriors | 5.54373 |
| Harrison Barnes | SF | Golden State Warriors | 3.8734 |
| Marreese Speights | C | Golden State Warriors | 3.815 |
| Leandro Barbosa | SG | Golden State Warriors | 2.5 |

By default, the first 10 lines of a table are displayed. You can use `show` to display more or fewer. To display the entire table, use `show` with no argument in the parentheses.

```python
warriors.show()
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Klay Thompson | SG | Golden State Warriors | 15.501 |
| Draymond Green | PF | Golden State Warriors | 14.2609 |
| Andrew Bogut | C | Golden State Warriors | 13.8 |
| Andre Iguodala | SF | Golden State Warriors | 11.7105 |
| Stephen Curry | PG | Golden State Warriors | 11.3708 |
| Jason Thompson | PF | Golden State Warriors | 7.00847 |
| Shaun Livingston | PG | Golden State Warriors | 5.54373 |
| Harrison Barnes | SF | Golden State Warriors | 3.8734 |
| Marreese Speights | C | Golden State Warriors | 3.815 |
| Leandro Barbosa | SG | Golden State Warriors | 2.5 |
| Festus Ezeli | C | Golden State Warriors | 2.00875 |
| Brandon Rush | SF | Golden State Warriors | 1.27096 |
| Kevon Looney | SF | Golden State Warriors | 1.13196 |
| Anderson Varejao | PF | Golden State Warriors | 0.289755 |

The `nba` table is sorted in alphabetical order of the team names. To see how the players were paid in 2015-2016, it is useful to sort the data by salary. Remember that by default, the sorting is in increasing order.

```python
nba.sort('SALARY')
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Thanasis Antetokounmpo | SF | New York Knicks | 0.030888 |
| Jordan McRae | SG | Phoenix Suns | 0.049709 |
| Cory Jefferson | PF | Phoenix Suns | 0.049709 |
| Elliot Williams | SG | Memphis Grizzlies | 0.055722 |
| Orlando Johnson | SG | Phoenix Suns | 0.055722 |
| Phil Pressey | PG | Phoenix Suns | 0.055722 |
| Keith Appling | PG | Orlando Magic | 0.061776 |
| Sean Kilpatrick | SG | Denver Nuggets | 0.099418 |
| Erick Green | PG | Utah Jazz | 0.099418 |
| Jeff Ayres | PF | Los Angeles Clippers | 0.111444 |

These figures are somewhat difficult to compare as some of these players changed teams during the season and received salaries from more than one team; only the salary from the last team appears in the table.  

The CNN report is about the other end of the salary scale – the players who were among the highest paid in the world. To identify these players we can sort in descending order of salary and look at the top few rows.

```python
nba.sort('SALARY', descending=True)
```

*Output:*

| PLAYER | POSITION | TEAM | SALARY |
| --- | --- | --- | --- |
| Kobe Bryant | SF | Los Angeles Lakers | 25 |
| Joe Johnson | SF | Brooklyn Nets | 24.8949 |
| LeBron James | SF | Cleveland Cavaliers | 22.9705 |
| Carmelo Anthony | SF | New York Knicks | 22.875 |
| Dwight Howard | C | Houston Rockets | 22.3594 |
| Chris Bosh | PF | Miami Heat | 22.1927 |
| Chris Paul | PG | Los Angeles Clippers | 21.4687 |
| Kevin Durant | SF | Oklahoma City Thunder | 20.1586 |
| Derrick Rose | PG | Chicago Bulls | 20.0931 |
| Dwyane Wade | SG | Miami Heat | 20 |

The late Kobe Bryant was the highest earning NBA player in 2015-2016.
