---
title: "Chapter 4: Data Types"
book: "Computational and Inferential Thinking (Data 8 textbook)"
chapter: 4
semester: sp26
sections:
  - "4.1 Numbers"
  - "4.2 Strings"
  - "4.3 Comparisons"
sources:
  - textbooks/sp26/chapters/04/Data_Types.ipynb
  - textbooks/sp26/chapters/04/1/Numbers.ipynb
  - textbooks/sp26/chapters/04/2/Strings.ipynb
  - textbooks/sp26/chapters/04/2/1/String_Methods.ipynb
  - textbooks/sp26/chapters/04/3/Comparison.ipynb
---

# Chapter 4: Data Types

Every value has a type, and the built-in `type` function returns the type of the result of any expression.

One type we have encountered already is a built-in function. Python indicates that the type is a `builtin_function_or_method`; the distinction between a *function* and a *method* is not important at this stage.

```python
type(abs)
```

*Output:*

```text
builtin_function_or_method
```

This chapter will explore many useful types of data.

## 4.1 Numbers

Computers are designed to perform numerical calculations, but there are some important details about working with numbers that every programmer working with quantitative data should know. Python (like most other programming languages) distinguishes between two different types of numbers:

* Integers are called `int` values in the Python language. They can only represent whole numbers (negative, zero, or positive) that don't have a fractional component
* Real numbers are called `float` values (or *floating point values*) in the Python language. They can represent whole or fractional numbers but have some limitations.

The type of a number is evident from the way it is displayed: `int` values have no decimal point and `float` values always have a decimal point.

```python
# Some int values
2
```

*Output:*

```text
2
```

```python
1 + 3
```

*Output:*

```text
4
```

```python
-1234567890000000000
```

*Output:*

```text
-1234567890000000000
```

```python
# Some float values
1.2
```

*Output:*

```text
1.2
```

```python
3.0
```

*Output:*

```text
3.0
```

When a `float` value is combined with an `int` value using some arithmetic operator, then the result is always a `float` value. In most cases, two integers combine to form another integer, but any number (`int` or `float`) divided by another will be a `float` value. Very large or very small `float` values are displayed using scientific notation.

```python
1.5 + 2
```

*Output:*

```text
3.5
```

```python
3 / 1
```

*Output:*

```text
3.0
```

```python
-12345678900000000000.0
```

*Output:*

```text
-1.23456789e+19
```

The `type` function can be used to find the type of any number.

```python
type(3)
```

*Output:*

```text
int
```

```python
type(3 / 1)
```

*Output:*

```text
float
```

The `type` of an expression is the type of its final value. So, the `type` function will never indicate that the type of an expression is a name, because names are always evaluated to their assigned values.

```python
x = 3
type(x) # The type of x is an int, not a name
```

*Output:*

```text
int
```

```python
type(x + 2.5)
```

*Output:*

```text
float
```

### More About Float Values

Float values are very flexible, but they do have limits. 

1. A `float` can represent extremely large and extremely small numbers. There are limits, but you will rarely encounter them.
2. A `float` only represents 15 or 16 significant digits for any number; the remaining precision is lost. This limited precision is enough for the vast majority of applications.
3. After combining `float` values with arithmetic, the last few digits may be incorrect. Small rounding errors are often confusing when first encountered.

The first limit can be observed in two ways. If the result of a computation is a very large number, then it is represented as infinite. If the result is a very small number, then it is represented as zero.

```python
2e306 * 10
```

*Output:*

```text
2e+307
```

```python
2e306 * 100
```

*Output:*

```text
inf
```

```python
2e-322 / 10
```

*Output:*

```text
2e-323
```

```python
2e-322 / 100
```

*Output:*

```text
0.0
```

The second limit can be observed by an expression that involves numbers with more than 15 significant digits. These extra digits are discarded before any arithmetic is carried out.

```python
0.6666666666666666 - 0.6666666666666666123456789
```

*Output:*

```text
0.0
```

The third limit can be observed when taking the difference between two expressions that should be equivalent. For example, the expression `2 ** 0.5` computes the square root of 2, but squaring this value does not exactly recover 2.

```python
2 ** 0.5
```

*Output:*

```text
1.4142135623730951
```

```python
(2 ** 0.5) * (2 ** 0.5)
```

*Output:*

```text
2.0000000000000004
```

```python
(2 ** 0.5) * (2 ** 0.5) - 2
```

*Output:*

```text
4.440892098500626e-16
```

The final result above is `0.0000000000000004440892098500626`, a number that is very close to zero. The correct answer to this arithmetic expression is 0, but a small error in the final significant digit appears very different in scientific notation. This behavior appears in almost all programming languages because it is the result of the standard way that arithmetic is carried out on computers. 

Although `float` values are not always exact, they are certainly reliable and work the same way across all different kinds of computers and programming languages.

## 4.2 Strings

Much of the world's data is text, and a piece of text represented in a computer is called a *string*. A string can represent a word, a sentence, or even the contents of every book in a library. Since text can include numbers (like this: 5) or truth values (True), a string can also describe those things.

The meaning of an expression depends both upon its structure and the types of values that are being combined. So, for instance, adding two strings together produces another string. This expression is still an addition expression, but it is combining a different type of value.

```python
"data" + "science"
```

*Output:*

```text
'datascience'
```

Addition is completely literal; it combines these two strings together without regard for their contents. It doesn't add a space because these are different words; that's up to the programmer (you) to specify.

```python
"data" + " " + "science"
```

*Output:*

```text
'data science'
```

Single and double quotes can both be used to create strings: `'hi'` and `"hi"` are identical expressions. Double quotes are often preferred because they allow you to include apostrophes inside of strings.

```python
"This won't work with a single-quoted string!"
```

*Output:*

```text
"This won't work with a single-quoted string!"
```

Why not? Try it out.

The `str` function returns a string representation of any value. Using this function, strings can be constructed that have embedded values.

```python
"That's " + str(1 + 1) + ' ' + str(True)
```

*Output:*

```text
"That's 2 True"
```

### 4.2.1 String Methods

From an existing string, related strings can be constructed using string methods, which are functions that operate on strings. These methods are called by placing a dot after the string, then calling the function.

For example, the following method generates an uppercased version of a string.

```python
"loud".upper()
```

*Output:*

```text
'LOUD'
```

Perhaps the most important method is `replace`, which replaces all instances of a substring within the string. The `replace` method takes two arguments, the text to be replaced and its replacement.

```python
'hitchhiker'.replace('hi', 'ma')
```

*Output:*

```text
'matchmaker'
```

String methods can also be invoked using variable names, as long as those names are bound to strings. So, for instance, the following two-step process generates the word "degrade" starting from "train" by first creating "ingrain" and then applying a second replacement.

```python
s = "train"
t = s.replace('t', 'ing')
u = t.replace('in', 'de')
u
```

*Output:*

```text
'degrade'
```

Note that the line `t = s.replace('t', 'ing')` doesn't change the string `s`, which is still "train".  The method call `s.replace('t', 'ing')` just has a value, which is the string "ingrain".

```python
s
```

*Output:*

```text
'train'
```

This is the first time we've seen methods, but methods are not unique to strings.  As we will see shortly, other types of objects can have them.

## 4.3 Comparisons

Boolean values most often arise from comparison operators. Python includes a variety of operators that compare values. For example, `3` is larger than `1 + 1`.

```python
3 > 1 + 1
```

*Output:*

```text
True
```

The value `True` indicates that the comparison is valid; Python has confirmed this simple fact about the relationship between `3` and `1+1`. The full set of common comparison operators are listed below.

| Comparison         | Operator | True example | False Example |
|--------------------|----------|--------------|---------------|
| Less than          | <        | 2 < 3        | 2 < 2         |
| Greater than       | >        | 3>2          | 3>3           |
| Less than or equal | <=       | 2 <= 2       | 3 <= 2        |
| Greater or equal   | >=       | 3 >= 3       | 2 >= 3        |
| Equal              | ==       | 3 == 3       | 3 == 2        |
| Not equal          | !=       | 3 != 2       | 2 != 2        |

An expression can contain multiple comparisons, and they all must hold in order for the whole expression to be `True`. For example, we can express that `1+1` is between `1` and `3` using the following expression.

```python
1 < 1 + 1 < 3
```

*Output:*

```text
True
```

The average of two numbers is always between the smaller number and the larger number. We express this relationship for the numbers `x` and `y` below. You can try different values of `x` and `y` to confirm this relationship.

```python
x = 12
y = 5
min(x, y) <= (x+y)/2 <= max(x, y)
```

*Output:*

```text
True
```

Strings can also be compared, and their order is alphabetical. A shorter string is less than a longer string that begins with the shorter string.

```python
"Dog" > "Catastrophe" > "Cat"
```

*Output:*

```text
True
```
