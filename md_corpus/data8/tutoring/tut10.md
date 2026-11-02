# Tutoring 10 Data C8 Spring 2026

## Page 1

## Residuals & Regression Inference

Tutoring 10

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Regression Inference

You take a sample of Data 8 students and ask them about their daily consumption of coffee and their midterm exam scores. Assume you are given a table students with the columns cups and score. The column cups contains the daily consumption of coffee and score contains the midterm exam score for each student from the sample. You perform linear regression and find a slope of 0.13 points per cup of coffee. Katy is considering buying coffee for her discussion to increase their scores but is not sure if this will work.

- State a null and alternative hypothesis to see whether this slope was due to randomness in your sample.

#### Null Hypothesis:

#### Alternative Hypothesis:

- Write a function slope that takes in a table, tbl, and returns the slope of the least-squares line using the first column to

predict values of the second column.

def slope(tbl):

x = ________________________________________________________

y = ________________________________________________________

zx = _______________________________________________________

zy = _______________________________________________________

r = ________________________________________________________

____________________________________________________________

- Complete the code to generate 5000 bootstrap resample slopes and then calculate a 95% confidence interval for the slope.

Assume the function slope(tbl) has been implemented correctly.

slopes = ________________________

for i in ________________________:

resample_slope = ________________________________________________ ________________________________________________________________________ left_end = ________________________

right_end = ________________________

interval = make_array(left_end, right_end)

## Page 2

#### (d) Suppose you find the confidence interval [0.02, 0.24].

#### i. What do you conclude about your hypotheses at a p-value cutoff of 5%?

#### ii. What about at a p-value cutoff of 10%?

#### iii. What about at a p-value cutoff of 1%?

- Your friend who has not taken Data 8 looks at your result and asks you what the confidence interval means. Which one of

the following is a correct response?

For 95% of students, there is a relationship between coffee consumption and midterm score.

There is a 95% probability that the true slope is between 0.02 and 0.24.

There is a 95% probability that our sampling process will produce an interval that contains the true slope.

### 2. Residuals

Suppose Kimiko tries to predict the emergency response time of Superheroes from each of the following four different variables:

- Income (float): the average income in the emergency location’s neighborhood.
- Distance (float): the distance in miles from the emergency location to their headquarters.
- Crimes (float): the average weekly number of crimes reported in the emergency location’s neighborhood last year.
- Height (float): the average building height (in feet) in the emergency location’s neighborhood.

To assess her predictions from each variable, she creates the following residual plots.

#### (a) Which of the above is a valid residual plot that indicates a linear

relationship between the variable and response time?

Income Distance

![Four residual scatterplots. Income shows an inverted-U pattern peaking near $60,000; Distance is patternless; Crime has a strong downward trend; Height forms a W-like curve. Vertical axes show residuals.](images/tut10_page002_image001.png)

Crimes Height

None

#### (b) Kimiko suspects she may have made a mistake in her code when

plotting the residuals. Which of the plots above are impossible residual plots?

Income Distance

Crimes Height

None

#### (c) For which of the above plots should Kimiko try a quadratic

equation for regression?

Income Distance

Crimes Height

None

Data C8 Spring 2026 Tutoring 10 | 2
