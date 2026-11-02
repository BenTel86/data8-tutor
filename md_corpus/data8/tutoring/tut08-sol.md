# Tutoring 08 Data C8 Spring 2026

## Page 1

## The Normal Distribution

Tutoring 08

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

### 1. The Normal Distribution

![Standard normal density curve with horizontal axis z from -4 to 4 and vertical axis phi(z) from 0 to 0.4. The bell curve peaks at z = 0, and blue points mark symmetric locations near z = -1.1 and 1.1 at density 0.19.](images/tut08-sol_page001_image001.png)

This is a normal distribution curve, with a few important properties: - The total area under the curve is 100% - The curve is symmetric about the mean. The mean and median are equal - The points of inflection of the curve are at ±1 standard deviations away from the mean

A standard normal distribution curve has mean 0 and standard deviation 1.

#### Chebyshev and Normal Bounds

The left table uses Chebyshev’s inequality to calculate the proportion of values that fall within 𝑘 SDs of the mean. Chebyshev’s bound works for all distributions, which is why it is a weaker bound, since it does not assume any properties of the underlying distribution.

The right shows more specific bounds for the normal distribution. It provides much more information than the Chebyshev bounds, since it assumes knowledge of the underlying distribution.

#### Range Proportion in Range [Chebyshev]

#### Range Proportion in Range [Normal]

mean ± 1 SDs ≥1 −1 (0%)

mean ± 1 SDs ≈68%

mean ± 2 SDs ≥1 − 1

4 (75%)

mean ± 2 SDs ≈95%

mean ± 3 SDs ≥1 − 1

9 (88.8%)

mean ± 3 SDs ≈99.7%

mean ± 4 SDs ≥1 − 1

16 (93.75%)

mean ± 4 SDs ≈99.99%

#### Practice Problems

#### (a) Discuss what it means for the Chebyshev bound for mean ± 1 SDs to be greater than or equal to 0.

The bound is so weak it tells us no information!

- Suppose vehicle speeds on a highway are normally distributed with mean 90 mph and SD 10 mph. Using the table above,

what is the approximate probability that a randomly chosen car is going more than 100 mph?

## Page 2

![Normal density curve titled 'Normal Curve with Mean=90 and SD=10,' with x-values about 60 to 120 and density up to 0.04. The curve peaks at 90; the right-tail area from x = 100 onward is shaded yellow.](images/tut08-sol_page002_image001.png)

We know that: - The normal distribution is symmetric about 90 (its mean). - The total area under the curve is 100%. - About 68% of the data is within 1 SD of the mean.

Using these facts we know that 50% of the data is below 90, and 34% (half of 68%) is between the mean and 1 SD above the mean. Thus, the region not highlighted adds up to 84% (50% below 90 and 34% between 90 and 100), and so the highlighted region must be 100% - 84% = 16% or 0.16.

Data C8 Spring 2026 Tutoring 08 | 2

## Page 3

### 2. The Central Limit Theorem

![Reference statement of the Central Limit Theorem: the sum or average of a large random sample drawn with replacement is roughly normal, regardless of the population's underlying distribution.](images/tut08-sol_page003_vector001.png)

The Central Limit Theorem (CLT) says that the distribution of the sum or average of a large random sample drawn with replacement will be roughly normal, regardless of the underlying distribution of the population from which the sample is drawn.

Practice Problems Suppose you simulate the proportion of purple-flowered plants in a sample of 200 plants (from Mendel’s 75% purple- and 25% white-flower plant population) using sample_proportions 1000 times. Then, you plotted the distribution of the proportion of purple-flowered plants from each of the 1000 trials.

#### (a) What would this distribution look like? Where would the distribution be centered?

A bell curve resembling the normal distribution, centered approximately at the expected proportion of 3/4. Notice that a proportion is basically just an average of a bunch of 0′s and 1′s!

#### (b) What would it look like if we conducted 10000 trials instead?

Compared to 2.1, this bell curve will still be centered approximately at the expected proportion of 3/4, but the empirical distribution will be “smoother” and more closely resemble a normal distribution.

- Does the initial distribution of the population have an effect on the shape of the distribution of the sample mean? If yes,

what is its effect? If no, explain why not.

No, the CLT states that regardless of the distribution of the population, the distribution of sample means will be approxi­ mately normal. How the population is distributed will have no effect on the shape.

Data C8 Spring 2026 Tutoring 08 | 3

## Page 4

### 3. Variability of the Sample Mean

![Reference panel states SD of sample means = population SD / sqrt(sample size), explaining that larger samples give less variable, more accurate estimates. It notes proportions are means of 0s and 1s and that a binary population's SD is at most 0.5.](images/tut08-sol_page004_vector001.png)

#### The SD of Sample Means

standard deviation of sample means = population standard deviation √sample size

This is the standard deviation of the means of all the possible samples that could be drawn, and measures the variability of the sample means. The smaller the SD, the more accurate the estimate. This is different from both the sample SD and the population SD.

Proportions are Means A proportion is just the average of an array of 1s and 0s (since it is the proportion of 1s in the array), which means the CLT applies to proportions. Often, we work with data where the population is binary (e.g. the proportion of “Yes” vs “No” votes). The SD of a 0-1 Population is at most 0.5 regardless of the proportion of 1s in the population.

#### Practice Problems

- Suppose we sample repeatedly from the population. If we increase the sample size, what happens to the distribution of the

sample mean? Does it become narrower or wider? Where is it centered?

The distribution of the sample mean will become narrower as the sample size increases. As the sample size increases (or decreases, for that matter), the distribution of the sample mean will stay centered at the population mean.

- If you had a sample size of 100, but wanted to increase accuracy by a factor of 4, what should the new sample size be?

In order to decrease the SD of possible sample means by a factor of 4, we would need to increase the denominator on the right hand side of the equation by a factor of 4. However, since we are taking the square root of the sample size, we must increase the sample size by a factor of 16.

SD of sample means = population SD √sample size

new SD of sample means = population SD √new sample size = 1

4 ⋅SD of sample means = 1 4 ⋅population SD √

100

⟹ 1 √new sample size = 1

4 ⋅ 1 √

100

⟹new sample size = 16 ⋅100 = 1600

- Briefly state the difference between the sample SD and the SD of sample means. Which one of these is affected by the

sample size?

The sample SD is the standard deviation of the data in a sample. For a good sample, the sample SD is expected to be fairly close to the population SD (since a good sample is representative of the population). On the other hand, the SD of sample means is the standard deviation of the distribution of all possible sample means, a distribution that describes how the sample mean can turn out when you obtain a sample and calculate its mean. The SD of sample means has a much more clearly defined relationship with the sample size as opposed to the sample SD.

- Suppose we have a sample with a mean of 40 and an SD of 10. Which one of the histograms below is more likely an empirical

distribution of the means of 10000 bootstrap resamples, each of size 100, from the sample?

Data C8 Spring 2026 Tutoring 08 | 4

## Page 5

![Two roughly bell-shaped histograms, each with counts up to about 3,000. The left distribution is centered near 40 and spans about 37 to 43; the right is also centered near 40 but is wider, spanning about 34 to 46.](images/tut08-sol_page005_image001.png)

The left one. We know that these distributions are approximately normal because they are distributions of sample means. The SD of the sample mean, based on the information given about the population, should be 10 √

100 = 1. The left one seems to have an SD of 1. Note that we do not have access to the population SD, so we use the next best thing — the sample SD — when calculating the SD of the sample mean.

- Fill in the blank: Based on the sample from the previous question, there is a ________% chance that the next resampled

mean (i.e., resample from the sample and compute the mean) lies within the range [38, 42].

Approximately 95%. We know for a normal distribution, roughly 95% of the data lies within 2 SDs of the mean. In this case, the distribution we are referring to is the distribution of all possible sample means.

- Suppose a redwood forest has trees whose average height is 200 feet with an SD of 30 feet. A random sample with replacement

of 400 trees is taken. Fill in the blank: There is roughly a 68% chance that the average height of the sample lies within the range 200 plus or minus ___________.

This is just the SD of the sample means, 30 √

400 = 30 20 or 1.5 feet. This is because 68% of the data is contained within 1 SD of the mean for a normal distribution.

Data C8 Spring 2026 Tutoring 08 | 5

## Page 6

### 4. Designing Experiments

![Reference panel on choosing sample size for a precise 95% confidence interval. It gives width of 95% CI = 4 * population SD / sqrt(sample size) and explains that the middle 95% spans two SDs on each side of the mean.](images/tut08-sol_page006_vector001.png)

Choosing the Sample Size of an Experiment When we want to estimate a population parameter (e.g., median height) we conduct the bootstrap process and obtain bootstrap estimates. If the width of our 95% confidence interval is small, it means our estimates are more precise.

Ultimately, this means that we want to limit the variability of our estimate. We know from the CLT that the variability of the sample mean is affected by the sample size! For a normal distribution, the “middle 95%” is within 2 SDs of the mean. We can use this information to create a confidence interval: the center ±2 SDs.

The width of this confidence interval is:

width of 95% CI = 4 × population SD √sample size

The term being multiplied is the SD of all the sample means– if the bounds of our 95% confidence interval are 2 SDs to the left of the mean and 2 SDs to the right, then the width is 4 SDs total!

We can use this equation above to calculate the sample size we need for an experiment.

Practice Problems Let’s say you want to poll the population of UC Berkeley students to ask whether they like pineapple on pizza. You can only take a sample, but you want to estimate the population proportion of students who like pineapple on their pizza. Let’s say you need your estimate to have a confidence interval width of at most 0.05.

- Suppose the population SD of the proportion of students who like pineapple on pizza is 0.1. What sample size do you need

#### to achieve a 95% confidence interval width of at most 0.05?

width of 95% CI = 4 ⋅ population SD √sample size ≤0.05

⟹√sample size ≥ 4 ⋅0.1

0.05

⟹√sample size ≥8

sample size = 64

- Suppose you do not know the population SD of the students who like pineapple on their pizza. Would it still be possible to

calculate the minimum sample size needed? If so, what sample size would you need to obtain a 95% confidence interval of width at most 0.05?

We can replace the population SD with the maximum SD possible in a population of 1s and 0s, which is 0.5.

Substituting in 0.5 for the population SD:

4 ⋅ 0.5 √sample size ≤0.05

⟹√sample size ≥ 2 0.05

⟹√sample size ≥40

sample size = 1600

#### Notice that the sample size we got here is significantly larger than the one in part (a).

Data C8 Spring 2026 Tutoring 08 | 6
