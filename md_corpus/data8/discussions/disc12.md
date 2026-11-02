# Discussion 12 Data C8 Spring 2026

## Page 1

## Residuals

Discussion 12

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

In data science, we can use linear regression in order to make predictions. When making predictions, it is also important to assess the accuracy of our predictions. To do so, we can examine the error between our actual data and the predictions; these errors are called residuals.

An example can be found below in the graph of miles per gallon (mpg) compared to the acceleration of a car. The left scatter plot shows the original data with a regression line fitted to it, and the right plot shows the corresponding residuals.

![Two plots against acceleration: mpg decreases from about 45 to 20 along a fitted line as acceleration rises from about 6 to 20, while the residual plot shows points scattered around zero without a strong pattern.](images/disc12_page001_image001.png)

Key facts: - residual = actual value of 𝑦−predicted value of 𝑦 - When we perform linear regression with an intercept, the sum of the residuals will always be equal to 0. - In a well-fitted linear regression, the residual plot shows no pattern, and the residuals sum to 0. - When a residual plot shows a pattern, there may be a non-linear relation between the variables. - If the residual plot shows uneven variation about the horizontal line at 0, the regression estimates are not equally accurate across the range of the predictor variable. This is known as heteroscedasticity.

### 1. Visual Diagnostic

Displayed below are three residual plots. For which of the following residual plots is using linear regression a reasonable idea, and why? What might the original graphs have looked like?

![Three residual plots versus x. Plot 1 forms a pronounced upside-down parabola, Plot 2 is an even random band around zero, and Plot 3 fans outward as x increases.](images/disc12_page001_image002.png)

## Page 2

### 2. Fight for California!

At a Cal football game the Mic Men, who are spirit leaders, claimed that our opponent’s ability to score was linearly affected by the student section’s noise level. Noah thinks they are wrong. Instead, he believes there is no linear relationship between student section noise and opponents’ scores. A friend gives Noah a table called noise which contains the following information:

- Opponent (string): Cal’s opponent for the game. - Loudness (int): Each row represents the maximum noise in decibels produced by the Student Section when Cal is on defense during a single home football game. - Points (int): The number of points scored by the opposing team.

A sample of the table with data from the 2024 season is below:

![Table with columns Opponent, Loudness, and Points. Seven rows range from Auburn at 55 loudness and 14 points to Stanford at 120 and 21; Miami FL has the most points, 39, at loudness 85.](images/disc12_page002_vector001.png)

#### Opponent Loudness Points

UC Davis 65 13

Auburn 55 14

San Diego St 75 10

Miami FL 85 39

Pittsburgh 70 17

Stanford 120 21

NC State 100 24

- Noah thinks that there is no correlation between Loudness and Points and that the Mic Men’s claim is wrong. How can Noah

test his hypothesis?

#### Null Hypothesis:

#### Alternative Hypothesis:

#### Testing Method:

- Noah decides to write a function which produces one bootstrapped estimate of the correlation between Loudness and Points.

Define the one_relationship function below which takes in the following arguments:

- tbl (Table): a table that contains a sample and has the same columns as noise.
- x_col (string): the column name for the 𝑥 variable.
- y_col (string): the column name for the 𝑦 variable.

The function should return one bootstrapped estimate of the correlation coefficient 𝑟. You can assume that you have access to the function correlation(x, y), which returns the correlation between arrays 𝑥 and 𝑦.

def one_relationship(tbl, x_col, y_col):

bootstrap = ______________________________________________

x_values = ______________________________________________

y_values = ______________________________________________

return ______________________________________________

Data C8 Spring 2026 Discussion 12 | 2

## Page 3

- Noah decides to generate a 70% confidence interval for the true correlation between Loudness and Points using 1000 bootstrap

resamples. Fill in the following code to generate the interval.

______________________________________________________

for i in ______________________________________________________:

______________________________________________________

______________________________________________________

lower_bound = ______________________________________________________

upper_bound = ______________________________________________________

ci = make_array(lower_bound, upper_bound)

- Noah enjoys chaos so he decides to swap the x_col and y_col arguments each time he makes a call to one_relationship

inside his for loop. Will this impact his interval?

Yes

No

- After running the above code Noah gets an interval of [−0.75, −0.14]. Therefore, we _______________________________

the null hypothesis using a p-value cutoff of _______________________________.

- Regardless, Cal Athletics wants you to generate a line of best fit for your data. Should you use the method of least squares

(i.e., minimizing RMSE) or the regression equations? Is there a difference between the two?

Regression Equations

Least Squares

No Difference

Data C8 Spring 2026 Discussion 12 | 3

## Page 4

### 3. Rogue Residuals

Each of the following plots is a residual plot from an attempted linear regression of a variable 𝑦 on a variable 𝑥. For each one, indicate whether the regression line seems to be a good fit, a bad fit, or if it is invalid for a well-fit regression.

#### (a) Residual Plot 1

#### (b) Residual Plot 2

![Residual plot with x from -20 to 20 and residual from about -0.2 to 1.0. Points form a roughly patternless horizontal cloud centered near 0.4.](images/disc12_page004_image001.png)

![Residual plot with x from -6 to 6 and residual from -4 to 4. Points trace a U-shaped pattern, with positive residuals at both ends and mostly negative residuals near the center.](images/disc12_page004_image002.png)

The regression seems to fit the data well.

The regression seems to fit the data well.

#### The regression does not seem to fit well.

#### The regression does not seem to fit well.

The residual plot is invalid.

The residual plot is invalid.

#### (c) Residual Plot 3

#### (d) Residual Plot 4

![Residual plot with x from 190 to 230 and residual from about -3 to 3. Points are scattered in a fairly uniform horizontal band around zero with no clear trend.](images/disc12_page004_image003.png)

![Residual plot with x from -20 to 20 and residual from -4 to 4. Residuals rise strongly from mostly negative on the left to mostly positive on the right.](images/disc12_page004_image004.png)

The regression seems to fit the data well.

The regression seems to fit the data well.

#### The regression does not seem to fit well.

#### The regression does not seem to fit well.

The residual plot is invalid.

The residual plot is invalid.

Data C8 Spring 2026 Discussion 12 | 4
