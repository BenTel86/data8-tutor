---
title: "Chapter 5: Sequences"
book: "Computational and Inferential Thinking (Data 8 textbook)"
chapter: 5
semester: sp26
sections:
  - "5.1 Arrays"
  - "5.2 Ranges"
  - "5.3 More on Arrays"
sources:
  - textbooks/sp26/chapters/05/Sequences.ipynb
  - textbooks/sp26/chapters/05/1/Arrays.ipynb
  - textbooks/sp26/chapters/05/2/Ranges.ipynb
  - textbooks/sp26/chapters/05/3/More_on_Arrays.ipynb
---

# Chapter 5: Sequences

```python
from datascience import *
path_data = '../../assets/data/'
```

Values can be grouped together into collections, which allows programmers to organize those values and refer to all of them with a single name. By grouping values together, we can write code that performs a computation on many pieces of data at once.

Calling the function `make_array` on several values places them into an *array*, which is a kind of sequential collection. Below, we collect four different temperatures into an array called `highs`. These are the [estimated average daily high temperatures](http://berkeleyearth.lbl.gov/regions/global-land) over all land on Earth (in degrees Celsius) for the decades surrounding 1850, 1900, 1950, and 2000, respectively, expressed as deviations from the average absolute high temperature between 1951 and 1980, which was 14.48 degrees.

```python
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, baseline_high - 0.093,
                   baseline_high + 0.105, baseline_high + 0.684)
highs
```

*Output:*

```text
array([13.6  , 14.387, 14.585, 15.164])
```

Collections allow us to pass multiple values into a function using a single name. For instance, the `sum` function computes the sum of all values in a collection, and the `len` function computes its length. (That's the number of values we put in it.) Using them together, we can compute the average of a collection.

```python
sum(highs)/len(highs)
```

*Output:*

```text
14.434000000000001
```

The complete chart of daily high and low temperatures appears below. 

**Mean of Daily High Temperature**

![Plot titled "Global Land" and annotated "Berkeley Earth Surface Temperature." On the x-axis years are labeled from 1820 to 2000. On the y-axis the High Temperature (degrees Celsius). A dark blue line shows the 12-month moving average and a red line shows the 10-year moving average with a 95% uncertainty range. The blue line bounces above and below the red line but tends to follow it. The lines were lowest at the beginning of the data, around 13.5 to 14.5 degrees before 1940. From about 1970, the lines tend upward, increasing from about 14.5 degrees to almost 15.5 degrees.](images/global-land-TMAX-Trend.png)

**Mean of Daily Low Temperature**

![Plot titled "Global Land" and annotated "Berkeley Earth Surface Temperature." On the x-axis years are labeled from 1820 to 2000. On the y-axis the High Temperature (degrees Celsius). A dark blue line shows the 12-month moving average and a red line shows the 10-year moving average with a 95% uncertainty range. The lines show variability, but stay below 3 degrees until about 1940. More recent data post-1970 has an upward trend ending around 4 degrees.](images/global-land-TMIN-Trend.png)

## 5.1 Arrays

```python
from datascience import *
path_data = '../../../assets/data/'
```

While there are many kinds of collections in Python, we will work primarily with arrays in this class. We've already seen that the `make_array` function can be used to create arrays of numbers.

Arrays can also contain strings or other types of values, but a single array can only contain a single kind of data. (It usually doesn't make sense to group together unlike data anyway.)  For example:

```python
english_parts_of_speech = make_array("noun", "pronoun", "verb", "adverb", "adjective", "conjunction", "preposition", "interjection")
english_parts_of_speech
```

*Output:*

```text
array(['noun', 'pronoun', 'verb', 'adverb', 'adjective', 'conjunction',
       'preposition', 'interjection'], dtype='<U12')
```

Returning to the temperature data, we create arrays of average daily [high temperatures](http://berkeleyearth.lbl.gov/auto/Regional/TMAX/Text/global-land-TMAX-Trend.txt) for the decades surrounding 1850, 1900, 1950, and 2000.

```python
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, 
                   baseline_high - 0.093,
                   baseline_high + 0.105, 
                   baseline_high + 0.684)
highs
```

*Output:*

```text
array([13.6  , 14.387, 14.585, 15.164])
```

Arrays can be used in arithmetic expressions to compute over their contents. When an array is combined with a single number, that number is combined with each element of the array. Therefore, we can convert all of these temperatures to Fahrenheit by writing the familiar conversion formula.

```python
(9/5) * highs + 32
```

*Output:*

```text
array([56.48  , 57.8966, 58.253 , 59.2952])
```

![Visual representation of array arithmetic. (9/5) times the array highs (13.6, 14.387, 14.585, 15.164) plus 32 equals (9/5) times 13.6 + 32 in the first slot of the resulting array, followed by (9/5) times 14.387 plus 32 in the second slot of the array, and so on. Finally on the right hand side of the image, an array is shown with the final answers (56.48, 57.8966, 58.253, 59.2952).](images/array_arithmetic.png)

Arrays also have *methods*, which are functions that operate on the array values. The `mean` of a collection of numbers is its average value: the sum divided by the length. Each pair of parentheses in the examples below is part of a call expression; it's calling a function with no arguments to perform a computation on the array called `highs`.

```python
highs.size
```

*Output:*

```text
4
```

```python
highs.sum()
```

*Output:*

```text
57.736000000000004
```

```python
highs.mean()
```

*Output:*

```text
14.434000000000001
```

### Functions on Arrays
The `numpy` package, abbreviated `np` in programs, provides Python programmers with convenient and powerful functions for creating and manipulating arrays.

```python
import numpy as np
```

For example, the `diff` function computes the difference between each adjacent pair of elements in an array. The first element of the `diff` is the second element minus the first.

```python
np.diff(highs)
```

*Output:*

```text
array([0.787, 0.198, 0.579])
```

The [full Numpy reference](http://docs.scipy.org/doc/numpy/reference/) lists these functions exhaustively, but only a small subset are used commonly for data processing applications. These are grouped into different packages within `np`. Learning this vocabulary is an important part of learning the Python language, so refer back to this list often as you work through examples and problems.

However, you **don't need to memorize these**.  Use this as a reference.

Each of these functions takes an array as an argument and returns a single value.

| **Function**       | Description                                                          |
|--------------------|----------------------------------------------------------------------|
| `np.prod`          | Multiply all elements together                                       |
| `np.sum`           | Add all elements together                                            |
| `np.all`           | Test whether all elements are true values (non-zero numbers are true)|
| `np.any`           | Test whether any elements are true values (non-zero numbers are true)|
| `np.count_nonzero` | Count the number of non-zero elements                                |

Each of these functions takes an array as an argument and returns an array of values.

| **Function**       | Description                                                          |
|--------------------|----------------------------------------------------------------------|
| `np.diff`          | Difference between adjacent elements                                 |
| `np.round`         | Round each number to the nearest integer (whole number)              |
| `np.cumprod`       | A cumulative product: for each element, multiply all elements so far |
| `np.cumsum`        | A cumulative sum: for each element, add all elements so far          |
| `np.exp`           | Exponentiate each element                                            |
| `np.log`           | Take the natural logarithm of each element                           |
| `np.sqrt`          | Take the square root of each element                                 |
| `np.sort`          | Sort the elements                                                    |

Each of these functions takes an array of strings and returns an array.

| **Function**        | **Description**                                              |
|---------------------|--------------------------------------------------------------|
| `np.char.lower`     | Lowercase each element                                       |
| `np.char.upper`     | Uppercase each element                                       |
| `np.char.strip`     | Remove spaces at the beginning or end of each element        |
| `np.char.isalpha`   | Whether each element is only letters (no numbers or symbols) |
| `np.char.isnumeric` | Whether each element is only numeric (no letters)  

Each of these functions takes both an array of strings and a *search string*; each returns an array.

| **Function**         | **Description**                                                                  |
|----------------------|----------------------------------------------------------------------------------|
| `np.char.count`      | Count the number of times a search string appears among the elements of an array |
| `np.char.find`       | The position within each element that a search string is found first             |
| `np.char.rfind`      | The position within each element that a search string is found last              |
| `np.char.startswith` | Whether each element starts with the search string

## 5.2 Ranges

A *range* is an array of numbers in increasing or decreasing order, each separated by a regular interval. 
Ranges are useful in a surprisingly large number of situations, so it's worthwhile to learn about them.

Ranges are defined  using the `np.arange` function, which takes either one, two, or three arguments: a start, and end, and a 'step'.

If you pass one argument to `np.arange`, this becomes the `end` value, with `start=0`, `step=1` assumed.  Two arguments give the `start` and `end` with `step=1` assumed.  Three arguments give the `start`, `end` and `step` explicitly.

A range always includes its `start` value, but does not include its `end` value.  It counts up by `step`, and it stops before it gets to the `end`.

    np.arange(end): An array starting with 0 of increasing consecutive integers, stopping before end.

```python
import numpy as np
path_data = '../../../assets/data/'
```

```python
np.arange(5)
```

*Output:*

```text
array([0, 1, 2, 3, 4])
```

Notice how the array starts at 0 and goes only up to 4, not to the end value of 5.

np.arange(start, end): An array of consecutive increasing integers from start, stopping before end.

```python
np.arange(3, 9)
```

*Output:*

```text
array([3, 4, 5, 6, 7, 8])
```

np.arange(start, end, step): A range with a difference of step between each pair of consecutive values, starting from start and stopping before end.

```python
np.arange(3, 30, 5)
```

*Output:*

```text
array([ 3,  8, 13, 18, 23, 28])
```

This array starts at 3, then takes a step of 5 to get to 8, then another step of 5 to get to 13, and so on.

When you specify a step, the start, end, and step can all be either positive or negative and may be whole numbers or fractions.

```python
np.arange(1.5, -2, -0.5)
```

*Output:*

```text
array([ 1.5,  1. ,  0.5,  0. , -0.5, -1. , -1.5])
```

### Example: Leibniz's formula for $\pi$

The great German mathematician and philosopher [Gottfried Wilhelm Leibniz](https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz) 
(1646 - 1716) discovered a wonderful formula for $\pi$ as an infinite sum of simple fractions. The formula is

$$\pi = 4 \cdot \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \dots\right)$$

Though some math is needed to establish this, we can use arrays to convince ourselves that the formula works. Let's calculate the first 5000 terms of Leibniz's infinite sum and see if it is close to $\pi$.

$$4 \cdot \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \frac{1}{11} + \dots - \frac{1}{9999} \right)$$

We will calculate this finite sum by adding all the positive terms first and then subtracting the sum of all the negative terms [[1]](#footnotes):

$$4 \cdot \left( \left(1 + \frac{1}{5} + \frac{1}{9} + \dots + \frac{1}{9997} \right) - \left(\frac{1}{3} + \frac{1}{7} + \frac{1}{11} + \dots + \frac{1}{9999} \right) \right)$$

The positive terms in the sum have 1, 5, 9, and so on in the denominators. The array `by_four_to_20` contains these numbers up to 17:

```python
by_four_to_20 = np.arange(1, 20, 4)
by_four_to_20
```

*Output:*

```text
array([ 1,  5,  9, 13, 17])
```

To get an accurate approximation to $\pi$, we'll use the much longer array `positive_term_denominators`.

```python
positive_term_denominators = np.arange(1, 10000, 4)
positive_term_denominators
```

*Output:*

```text
array([   1,    5,    9, ..., 9989, 9993, 9997])
```

The positive terms we actually want to add together are just 1 over these denominators:

```python
positive_terms = 1 / positive_term_denominators
```

The negative terms have 3, 7, 11, and so on on in their denominators. This array is just 2 added to `positive_term_denominators`.

```python
negative_terms = 1 / (positive_term_denominators + 2)
```

The overall sum is

```python
4 * ( sum(positive_terms) - sum(negative_terms) )
```

*Output:*

```text
3.1413926535917955
```

This is very close to $\pi = 3.14159\dots$. Leibniz's formula is looking good!

(footnotes)=
### Footnotes
[1] Surprisingly, when we add  *infinitely* many positive and negative fractions, the order can matter! But our approximation to $\pi$ uses only a large finite number of fractions, so it's okay to add the terms in any convenient order.

## 5.3 More on Arrays

It's often necessary to compute something that involves data from more than one array. If two arrays are of the same size, Python makes it easy to do calculations involving both arrays.

For our first example, we return once more to the temperature data.  This time, we create arrays of average daily [high](http://berkeleyearth.lbl.gov/auto/Regional/TMAX/Text/global-land-TMAX-Trend.txt) and [low](http://berkeleyearth.lbl.gov/auto/Regional/TMIN/Text/global-land-TMIN-Trend.txt) temperatures for the decades surrounding 1850, 1900, 1950, and 2000.

```python
from datascience import *
import numpy as np
path_data = '../../../assets/data/'
```

```python
baseline_high = 14.48
highs = make_array(baseline_high - 0.880, 
                   baseline_high - 0.093,
                   baseline_high + 0.105, 
                   baseline_high + 0.684)
highs
```

*Output:*

```text
array([13.6  , 14.387, 14.585, 15.164])
```

```python
baseline_low = 3.00
lows = make_array(baseline_low - 0.872, baseline_low - 0.629,
                  baseline_low - 0.126, baseline_low + 0.728)
lows
```

*Output:*

```text
array([2.128, 2.371, 2.874, 3.728])
```

Suppose we'd like to compute the average daily *range* of temperatures for each decade.  That is, we want to subtract the average daily high in the 1850s from the average daily low in the 1850s, and the same for each other decade.

We could write this laboriously using `.item`:

```python
make_array(
    highs.item(0) - lows.item(0),
    highs.item(1) - lows.item(1),
    highs.item(2) - lows.item(2),
    highs.item(3) - lows.item(3)
)
```

*Output:*

```text
array([11.472, 12.016, 11.711, 11.436])
```

As when we converted an array of temperatures from Celsius to Fahrenheit, Python provides a much cleaner way to write this:

```python
highs - lows
```

*Output:*

```text
array([11.472, 12.016, 11.711, 11.436])
```

![Illustration of array subtraction. The highs array is shown on the left followed by a subtraction sign and then the lows array. The arrays are aligned so the numbers in the first position of the array are next to each other, same for the second, third, and fourth positions. Following that is an equal sign and an array representation with the first entry of lows subtracted from the first entry of highs, and the same for the second, third, and fourth entries. Following that is another equal sign with an array showing the result of the subtraction in each entry of the array.](images/array_subtraction.png)

What we've seen in these examples are special cases of a general feature of arrays.

### Elementwise arithmetic on pairs of numerical arrays
If an arithmetic operator acts on two arrays of the same size, then the operation is performed on each corresponding pair of elements in the two arrays. The final result is an array. 

For example, if `array1` and `array2` have the same number of elements, then the value of `array1 * array2` is an array. Its first element is the first element of `array1` times the first element of `array2`, its second element is the second element of `array1` times the second element of `array2`, and so on.

### Example: Wallis' Formula for $\pi$ ###
The number $\pi$ is important in many different areas of math. Centuries before computers were invented, mathematicians worked on finding simple ways to approximate the numerical value of $\pi$. We have already seen Leibniz's formula for $\pi$. About half a century before Leibniz, the English mathematician [John Wallis](https://en.wikipedia.org/wiki/John_Wallis) (1616-1703) also expressed $\pi$ in terms of simple fractions, as an infinite product.

$$
\pi = 2 \cdot \left( \frac{2}{1}\cdot\frac{2}{3}\cdot\frac{4}{3}\cdot\frac{4}{5}\cdot\frac{6}{5}\cdot\frac{6}{7}\dots \right)
$$

This is a product of "even/odd" fractions. Let's use arrays to multiply a million of them, and see if the product is close to $\pi$.

Remember that multiplication can done in any order [[1]](#footnotes), so we can readjust our calculation to:

$$\pi \approx 2 \cdot \left( \frac{2}{1} \cdot \frac{4}{3} \cdot \frac{6}{5} \cdots \frac{1,000,000}{999999} \right) \cdot \left( \frac{2}{3} \cdot \frac{4}{5} \cdot \frac{6}{7} \cdots \frac{1,000,000}{1,000,001} \right)$$

We're now ready to do the calculation. We start by creating an array of even numbers 2, 4, 6, and so on upto 1,000,000. Then we create two lists of odd numbers: 1, 3, 5, 7, ... upto 999,999, and 3, 5, 7, ... upto 1,000,001.

```python
even = np.arange(2, 1000001, 2)
one_below_even = even - 1
one_above_even = even + 1
```

Remember that `np.prod` multiplies all the elements of an array together. Now we can calculate Wallis' product, to a good approximation.

```python
2 * np.prod(even/one_below_even) * np.prod(even/one_above_even)
```

*Output:*

```text
3.1415910827951143
```

That's $\pi$ correct to five decimal places.  Wallis clearly came up with a great formula.

(footnotes)=
### Footnotes
[1] As we saw in the example about Leibniz's formula, when we add  *infinitely* many fractions, the order can matter. The same is true with multiplying fractions, as we are doing here. But our approximation to $\pi$ uses only a large finite number of fractions, so it's okay to multiply the terms in any convenient order.
