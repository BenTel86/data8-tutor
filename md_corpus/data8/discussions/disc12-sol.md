# Discussion 12 Data C8 Spring 2026

## Page 1

## Residuals

Discussion 12

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

In data science, we can use linear regression in order to make predictions. When making predictions, it is also important to assess the accuracy of our predictions. To do so, we can examine the error between our actual data and the predictions; these errors are called residuals.

An example can be found below in the graph of miles per gallon (mpg) compared to the acceleration of a car. The left scatter plot shows the original data with a regression line fitted to it, and the right plot shows the corresponding residuals.

![Two plots against acceleration: mpg decreases from about 45 to 20 along a fitted line as acceleration rises from about 6 to 20, while the residual plot shows points scattered around zero without a strong pattern.](images/disc12-sol_page001_image001.png)

Key facts: - residual = actual value of 𝑦−predicted value of 𝑦 - When we perform linear regression with an intercept, the sum of the residuals will always be equal to 0. - In a well-fitted linear regression, the residual plot shows no pattern, and the residuals sum to 0. - When a residual plot shows a pattern, there may be a non-linear relation between the variables. - If the residual plot shows uneven variation about the horizontal line at 0, the regression estimates are not equally accurate across the range of the predictor variable. This is known as heteroscedasticity.

### 1. Visual Diagnostic

Displayed below are three residual plots. For which of the following residual plots is using linear regression a reasonable idea, and why? What might the original graphs have looked like?

![Three residual plots versus x. Plot 1 forms a pronounced upside-down parabola, Plot 2 is an even random band around zero, and Plot 3 fans outward as x increases.](images/disc12-sol_page001_image002.png)

## Page 2

Plot 1 exhibits a clearly non-linear pattern which tells us that using linear regression is inappropriate.

Plot 2 is the best residual plot to use linear regression for, since the residuals have the pattern of a formless cloud. Plot 2 satisfies the two things that we are looking for: - The sum of the residuals add up to zero - There is no observable trend or pattern in the residuals.

Using linear regression for Plot 3 is a mixed bag, as the data still seems to follow a linear pattern but the residual plot is heteroscedastic, meaning the residuals are more spread out for different values of 𝑥. One consequence of heteroscedasticity is that our predictions will be less accurate, and although there are ways of combating heteroscedasticity, directly applying linear regression to the sample would not be appropriate.

Here are the original graphs:

![Three scatterplots with yellow linear predictions: Plot 1 has a curved arch the nearly flat line misses, Plot 2 follows a strong decreasing linear trend well, and Plot 3 decreases but has increasing spread.](images/disc12-sol_page002_image001.png)

Data C8 Spring 2026 Discussion 12 | 2

## Page 3

### 2. Fight for California!

At a Cal football game the Mic Men, who are spirit leaders, claimed that our opponent’s ability to score was linearly affected by the student section’s noise level. Noah thinks they are wrong. Instead, he believes there is no linear relationship between student section noise and opponents’ scores. A friend gives Noah a table called noise which contains the following information:

- Opponent (string): Cal’s opponent for the game. - Loudness (int): Each row represents the maximum noise in decibels produced by the Student Section when Cal is on defense during a single home football game. - Points (int): The number of points scored by the opposing team.

A sample of the table with data from the 2024 season is below:

![Table with columns Opponent, Loudness, and Points. Seven rows range from Auburn at 55 loudness and 14 points to Stanford at 120 and 21; Miami FL has the most points, 39, at loudness 85.](images/disc12-sol_page003_vector001.png)

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

Null Hypothesis: There is no linear association between Loudness and Points. The true correlation is 0. The non-zero correlation observed in the sample is simply due to chance.

Alternative Hypothesis: There is a linear association between Loudness and Points. The true correlation is non-zero (there is some linear relationship between the two variables). The non-zero correlation observed in the sample is not simply due to chance.

Testing Method: We are essentially trying to estimate the true value of 𝑟. Therefore, we can bootstrap the sample repeatedly, generate a confidence interval for 𝑟, and check to see if zero is included in the confidence interval.

- Noah decides to write a function which produces one bootstrapped estimate of the correlation between Loudness and Points.

Define the one_relationship function below which takes in the following arguments:

- tbl (Table): a table that contains a sample and has the same columns as noise.
- x_col (string): the column name for the 𝑥 variable.
- y_col (string): the column name for the 𝑦 variable.

The function should return one bootstrapped estimate of the correlation coefficient 𝑟. You can assume that you have access to the function correlation(x, y), which returns the correlation between arrays 𝑥 and 𝑦.

def one_relationship(tbl, x_col, y_col):

bootstrap = ______________________________________________

Data C8 Spring 2026 Discussion 12 | 3

## Page 4

x_values = ______________________________________________

y_values = ______________________________________________

return ______________________________________________

def one_relationship(tbl, x_col, y_col): bootstrap = tbl.sample() x_values = bootstrap.column(x_col) y_values = bootstrap.column(y_col) return correlation(x_values, y_values)

#### Data C8 Spring 2026 Discussion 12 | 4

## Page 5

- Noah decides to generate a 70% confidence interval for the true correlation between Loudness and Points using 1000 bootstrap

resamples. Fill in the following code to generate the interval.

______________________________________________________

for i in ______________________________________________________:

______________________________________________________

______________________________________________________

lower_bound = ______________________________________________________

upper_bound = ______________________________________________________

ci = make_array(lower_bound, upper_bound)

correlations = make_array()

for i in np.arange(1000): bootstrapped_corr = one_relationship(noise, "Loudness", "Points") correlations = np.append(correlations, bootstrapped_corr)

lower_bound = percentile(15, correlations) upper_bound = percentile(85, correlations) ci = make_array(lower_bound, upper_bound)

- Noah enjoys chaos so he decides to swap the x_col and y_col arguments each time he makes a call to one_relationship

inside his for loop. Will this impact his interval?

Yes

No

Correlation does not change if you change which variable is on each axis. Therefore, Noah can swap the axes and the interval will still be generated correctly, although it will likely be a little different since the process is random!

- After running the above code Noah gets an interval of [−0.75, −0.14]. Therefore, we _______________________________

the null hypothesis using a p-value cutoff of _______________________________.

We reject the null hypothesis because 0 is outside of the confidence interval for the true correlation. Since the interval is a 70% confidence interval, we are using a p-value cutoff of 30%.

- Regardless, Cal Athletics wants you to generate a line of best fit for your data. Should you use the method of least squares

(i.e., minimizing RMSE) or the regression equations? Is there a difference between the two?

Regression Equations

Least Squares

No Difference

It does not matter which method you use; they both result in the same line. This also means that the regression equations give you the unique line that minimizes the RMSE!

Data C8 Spring 2026 Discussion 12 | 5

## Page 6

### 3. Rogue Residuals

Each of the following plots is a residual plot from an attempted linear regression of a variable 𝑦 on a variable 𝑥. For each one, indicate whether the regression line seems to be a good fit, a bad fit, or if it is invalid for a well-fit regression.

#### (a) Residual Plot 1

#### (b) Residual Plot 2

![Residual plot with x from -20 to 20 and residual from about -0.2 to 1.0. Points form a roughly patternless horizontal cloud centered near 0.4.](images/disc12-sol_page006_image001.png)

![Residual plot with x from -6 to 6 and residual from -4 to 4. Points trace a U-shaped pattern, with positive residuals at both ends and mostly negative residuals near the center.](images/disc12-sol_page006_image002.png)

The regression seems to fit the data well.

The regression seems to fit the data well.

#### The regression does not seem to fit well.

#### The regression does not seem to fit well.

The residual plot is invalid.

The residual plot is invalid.

Invalid residual plot, since the sum of residuals is not equal to 0. Though this is an invalid residual plot, as in it would never exist with a well-fit regression, it is still appropriate to conclude the underlying data is appropriate for regres­ sion.

Parabolic shape in the residual plot, therefore linear regres­ sion is not appropriate. Regression therefore does not fit the data well.

#### (c) Residual Plot 3

#### (d) Residual Plot 4

![Residual plot with x from 190 to 230 and residual from about -3 to 3. Points are scattered in a fairly uniform horizontal band around zero with no clear trend.](images/disc12-sol_page006_image003.png)

![Residual plot with x from -20 to 20 and residual from -4 to 4. Residuals rise strongly from mostly negative on the left to mostly positive on the right.](images/disc12-sol_page006_image004.png)

The regression seems to fit the data well.

The regression seems to fit the data well.

#### The regression does not seem to fit well.

#### The regression does not seem to fit well.

The residual plot is invalid.

The residual plot is invalid.

No visible pattern in the residual plot and the residuals seem to sum to 0, so the regression fits well.

The regression line tends to overestimate for 𝑥< −10 and underestimate for 𝑥> 10. We can change the slope to produce a better regression line, which shouldn’t be possible because the regression line minimizes RMSE! This is an invalid residual plot, but the underlying relationship is still linear, as we see a linear trend in the residuals.

Data C8 Spring 2026 Discussion 12 | 6
