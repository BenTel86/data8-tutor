# Tutoring 09 Data C8 Spring 2026

## Page 1

## Correlation & Regression

Tutoring 09

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. Correlation

Association Refers to any relationship between two variables. It does not have to be linear. For instance, in the plots below, all of them show an association, but only the first graph demonstrates a linear association.

![Three unlabeled-axis scatterplot sketches comparing relationship shapes: a roughly straight increasing linear pattern, a nonlinear upward-curving pattern, and a nonlinear inverted-U pattern.](images/tut09_page001_image001.png)

Correlation Denotes a linear association between two variables. The correlation coefficient 𝑟, is a number between −1 and 1 that measures the strength and direction of the linear relationship between two variables.

- Strength: how clustered the scatter plot is around a straight line. If the plot is highly clustered, the absolute value of 𝑟is closer to 1. - Direction: if 𝑦 tends to increase as 𝑥 increases, 𝑟 is positive. If 𝑦 tends to decrease as 𝑥 increases, 𝑟 is negative.

Formula for 𝑟 - The average of the product of 𝑥 and 𝑦 when both variables are measured in standard units. - 𝑟 is a number without units because it is computed with standard units, which also has no units. - Remember, standard units allow us to quantify the relationship between two variables on different units and scales. - 𝑟 is unaffected by switching the axes. This is because it is the average of products of standard units; 𝑥⋅𝑦= 𝑦⋅𝑥. More intuitively, since correlation is a measure of spread around a line, switching the axes won’t change the spread around the line.

Practice Problems The following table, taters, depicts the number of tater tots a person has eaten, along with a number that quantifies their satisfaction, which is a number that goes from 0 to 10.

![Two-column table with headers 'Tater Tots Consumed' and 'Satisfaction.' Six row pairs are (10, 8), (3, 4), (8, 6), (5, 5), (16, 9), and (1, 3).](images/tut09_page001_vector001.png)

#### Tater Tots Consumed Satisfaction

10 8

3 4

8 6

5 5

16 9

1 3

(...94 rows omitted)

## Page 2

- First, complete the function su that takes in an array of numbers and outputs the array in standard units. Then, calculate the

#### correlation coefficient between Tater Tots Consumed and Satisfaction and assign it to r.

def su(array):

return ____________________________________________

consumed_su = __________________________________________

satisfaction_su = __________________________________________

r = __________________________________________

- Suppose that we find the correlation coefficient, 𝑟, to be equal to 0.743. What can you conclude about the association between

the number of tater tots consumed and a person’s satisfaction?

#### (c) A high value of 𝑟 shows that a change in 𝑥 causes a change in 𝑦.

True

False

#### (d) If we switch the axes of a plot, the correlation coefficient will not change.

True

False

#### (e) Answer the following questions about the plots below.

![Six scatterplots labeled a-f on axes from roughly -4 to 4: a moderate negative, b near-perfect positive, c moderate positive, d strong positive, e strong negative, and f perfect positive linear association.](images/tut09_page002_image001.png)

- Order the scatter plots above from least correlated to most correlated (in terms of the absolute value of 𝑟).

(Least) _________________________________________________________________________________________ (Most)

#### ii. Which plots show positive correlation? Which show negative correlation?

Positive: ________________________________________ Negative: ________________________________________

Data C8 Spring 2026 Tutoring 09 | 2

## Page 3

### 2. Regression

![Reference panel for correlation and regression: y = slope*x + intercept; in standard units, y = r*x. In original units, slope = r*SD(y)/SD(x), and intercept = average(y) - slope*average(x).](images/tut09_page003_vector001.png)

Correlation Coefficient The equation for the regression line can be calculated using 𝑟. Recall that the equation of a line is

𝑦= slope ⋅𝑥+ intercept

Standard Units Visually, the shape/pattern of the scatter plot and the regression line look the same whether 𝑥 and 𝑦 are in standard units or their original units.

#### Regression line [standard units]

𝑦= 𝑟⋅𝑥

#### Regression line when [original units]

Calculate the correlation coefficient, 𝑟. Then calculate the slope and intercept given by these formulae.

slope = 𝑟⋅ SD of 𝑦

SD of 𝑥 intercept = average of 𝑦−slope ⋅average of 𝑥

Practice Problems The top100 table contains the 100 most streamed songs on Spotify in 2023. The energy column represents the song’s perceived energy level as a percentage, and the danceability column represents (as a percentage) how suitable the song is for dancing.

![Scatterplot of energy on the x-axis (about 20 to 95) versus danceability on the y-axis (about 30 to 92). Points are widely dispersed but show a weak overall positive association, with most observations clustered between energy 45 to 90 and danceability 55 to 85.](images/tut09_page003_image001.png)

Here are some statistics regarding the two columns: - The energy column has: - a mean of 64 - a standard deviation of 16. - The danceability column has: - a mean of 66 - a standard deviation of 14.5. - The correlation between energy and danceability is 0.3.

- Write an equation for the regression line of the data in the top100 table, with the intention of predicting an unseen

#### danceability percentage given an observed energy percentage. Feel free to use a calculator!

- Using the regression line, what would we predict the danceability to be for a song that had an energy of 90?

- Suppose that we also calculate our regression line in standard units. Would it be appropriate to use this regression line to

#### predict a danceabillity for which our observed energy (in standard units) is −2? Explain.

Data C8 Spring 2026 Tutoring 09 | 3

## Page 4

### 3. Root Mean Squared Errors (RMSE)

Root Mean Squared Error (RMSE) RMSE is the square root (R) of the mean (M) of the squared errors (SE). We take the square root of the MSE (mean squared error) such that the RMSE is comparable and of the same units as the original data.

Let 𝑒𝑖 be the residuals and 𝑛 be the number of points in the dataset.

RMSE = √𝑒2

1 + 𝑒2 2 + … + 𝑒2𝑛 𝑛

![Regression-error diagram on axes about -4 to 8 horizontally and -6 to 6 vertically. Blue points lie around an orange rising proposed line; red vertical segments show residuals, and translucent red squares visualize each squared error.](images/tut09_page004_image001.png)

#### Practice Problems

- Write a function that takes in an array of observed values, an array of predictions, and returns the RMSE. You may assume

that the two arrays have the same length.

def rmse(observed, predicted):

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

- In the calculation of root mean squared error, why is it important for us to square the residuals before taking the mean?

#### (c) While both valid, why do we tend to use and look at the RMSE over the MSE (mean squared error)?

Data C8 Spring 2026 Tutoring 09 | 4
