# Discussion 10 Data C8 Spring 2026

## Page 1

## The Central Limit Theorem

Discussion 10

Data C8: Foundations of Data Science UC Berkeley, Spring 2026

![Text introduction to the Central Limit Theorem: large random samples with replacement have sample means that are roughly normal and centered at the population mean. It gives the spread formula as population standard deviation divided by the square root of sample size.](images/disc10-sol_page001_vector001.png)

So far in the course, you have used the bootstrap to estimate different population parameters, such as the median or mean. You are now capable of building empirical distributions for these sample statistics. An empirical distribution for a sample statistic is usually obtained by repeatedly resampling and calculating the statistic for those resamples (bootstrapping).

Now we will introduce the Central Limit Theorem (CLT), which tells us more about the distribution of the sample mean. If you draw a large random sample with replacement from a population, then, regardless of the distribution of the population, the probability distribution for that sample’s mean is roughly normal, and centered at the population mean.

#### Furthermore, the standard deviation (spread) of the distribution of sample means can be described as

standard deviation of sample means = population standard deviation √sample size

Note, the standard deviation of the sample means is not the standard deviation of the sample. It is the spread of the distribution of all sample means obtain, not of a single sample.

### 1. Sample Means

Note that in this question, the empirical distribution of the sample mean is made up from the means of samples drawn from the population (not from resamples from a single sample).

Assume that you have a certain population of interest whose histogram is below.

![Right-skewed blue histogram of a population on x-values about 1-7. The y-axis is Percent per unit; bar heights decline from roughly 0.41 in the first bin to near zero in the last.](images/disc10-sol_page001_image001.png)

- Cyrus takes many large random samples with replacement from the population, with the goal of generating an empirical

distribution of the sample mean. What shape do you expect this distribution to have? Which value will it be centered around?

By the Central Limit Theorem, the distribution will be normal (bell curve), centered around the population mean.

- Why are we able to use the CLT to reason about the empirical distribution of the sample mean’s shape if the population data

is skewed?

We are able to use the CLT, as we are drawing large random samples, with replacement, and the statistic is sum or mean. If these conditions are applied, the CLT can be used regardless of the population’s distribution.

- Suppose that Cyrus creates two empirical distributions of sample means, with different sample sizes. Which distribution

corresponds to a larger sample size? Why?

## Page 2

![Two side-by-side, roughly normal histograms of sample means, both centered near 2.0 with axes Sample Means and Percent per unit. The left distribution is wider, spanning about 1.3-2.7, while the right is narrower, about 1.6-2.4.](images/disc10-sol_page002_image001.png)

The distribution to the right corresponds to a larger sample size compared to the one to the left. We know this based on the spread of the two distributions. The larger the sample size you use, the less variable the distribution of the sample mean becomes.

You can see that increasing the sample size increases the denominator in calculating the SD of sample means, which decreases the standard deviation.

- Based solely on the information in the histogram, what is an estimate for the standard deviation of the sample mean on the

left? How did you determine this?

Approximately 0.3.

This is because the point of inflection on a normal distribution reflects 1 standard deviation away from the mean. Looking at the histogram, we can see that the inflection points occur at around 1.7 and 2.3, with the mean of the histogram being 2.0.

- Suppose you were told that the distribution on the right was generated based on a sample size of 100 and has a standard

deviation of 0.2. How big of a sample size would you need if you wanted the standard deviation of the distribution of sample means to be 10 times smaller?

First, find the Population SD.

0.2 = population SD √

100

√

⟹population SD = 0.2 ⋅

100 = 2

Then, calculate the new sample size needed.

0.2 10 = 2 √new sample size

⟹0.2 ⋅√new sample size = 2 ⋅10

⟹√new sample size = 100

new sample size = 10000

To divide the SD of the sample means by a factor of 10, we need to multiply the sample size by 102, which is 100. To skip the calculations, reference the square root law! (14.5.4 in textbook)

Data C8 Spring 2026 Discussion 10 | 2

## Page 3

### 2. Want to Go to Main Stacks?

UC Berkeley students love studying in Main Stacks! You are working with Lena on constructing a confidence interval for the mean number of hours students spend in Main Stacks each year. To do this, you take a random sample of 400 UC Berkeley students and record how many hours each student spent studying in Main Stacks over the past year. Then, you compute the mean number of hours for your sample; it is 170 hours. You also calculate the standard deviation of your sample to be 10 hours.

- Lena claims that the distribution of all possible sample means is normal with an SD of 0.5 hours. Use this information to

construct an approximate 68% confidence interval for the mean hours spent studying in Main Stacks for all UC Berkeley students.

We know that the distribution is approximately normal and hence we know that roughly 68% of the area under the normal curve (or 68% of the data) is contained within 1 SD of the mean. Therefore, our confidence interval range will be

[170 −1 ⋅0.5, 170 + 1 ⋅0.5] = [169.5 hours, 170.5 hours]

- If Lena had not told you what the SD of the distribution of sample means was, could you estimate it from the data in the

sample? If yes, how? If no, why not?

We know that the sample size is 400 and that the standard deviation of our sample was 10 hours. Recall the equation for the SD of sample means is

standard deviation of sample means = population standard deviation √sample size

We can substitute the sample SD (10 hours) in place of the population SD in this formula (assuming the sample is represen­ tative of the population) and calculate the value!

standard deviation of sample means = 10 hours √

400 = 10 hours

20 = 0.5 hours

![Text note contrasting sample-mean distributions from direct population sampling with bootstrap distributions from one representative sample. It explains that the former centers on the population mean, the latter on the sample mean, and the Central Limit Theorem applies in both cases.](images/disc10-sol_page003_vector001.png)

A helpful note. In Question 1, our large samples drawn with replacement were obtained directly from the population. As a result, our empirical distribution of the sample mean was centered around the population mean.

In contrast, in Question 2, we only have access to a single sample. As a result, we use the sample’s mean and standard deviation in place of the population’s mean and standard deviation, given the assumption that it is a representative sample.

If you bootstrap (resample) from a representative sample and obtain the empirical distribution of the sample means, it will be roughly centered around the original sample’s mean, not the population mean. However, it is helpful to note that as the sample size gets larger, your original sample’s mean will likely get closer and closer to the population mean, by the law of large numbers.

In both situations – whether resampling directly from the population or bootstrapping from a single representative sample - the Central Limit Theorem applies as long as its conditions are met.

Data C8 Spring 2026 Discussion 10 | 3

## Page 4

### 3. CLT with TLC

You are a super fan of the girl group TLC and are interested in estimating the average amount of plays their songs have online. You generate an 80% confidence interval for this parameter to be [700000, 1200000] based on a random sample of 50 songs. Are each of the following statements true or false? Give a brief explanation for each question.

Note: Generally, 𝑛≥30 is considered the minimum sample size for CLT to take effect!

#### (a) The value of our population parameter changes depending on our sampling process.

True False

False. Our population parameter is fixed. It depends on an entire population that we know to be true. On the other hand, the sample statistic is dependent on what our sample looks like, which can vary. This is what allows us to describe probabilities regarding a confidence interval before we generate them but not after. (see part (d))

- The empirical distribution of any statistic we choose will be roughly normal based on the Central Limit Theorem, but it

requires our population to have a normal distribution to begin with.

True False

False. The Central Limit Theorem states that the probability distribution of the sum, average, or proportions of a large random sample drawn with replacement will be roughly normal, regardless of the distribution of the population from which the sample is drawn.

- If we calculate a 95% confidence interval using the same sample and resamples, the interval will be narrower than the original

confidence interval because we are more certain of our results.

True False

False. Using a 95% confidence level would result in a wider interval than an 80% confidence level. In fact, the 95% confidence interval will envelop the original 80% confidence interval. The “increased confidence” comes from having a wider interval, though we are less certain of actual value of the parameter.

- Using the same process to generate another 80% confidence interval, there is an 80% chance that the next confidence interval

you generate will contain the true average number of plays for TLC songs.

True False

True. Before we create the confidence interval, there is an 80% chance that the confidence interval we create next will contain the true population parameter. Confidence refers to the probability associated with our process of generating confidence intervals, not the probability associated with a single well-defined interval.

- There is an 80% chance that a confidence interval we generated contains the true average number of plays for TLC songs.

True False

False. Once we have calculated a confidence interval, it is fixed - it either contains the parameter or it does not. There is no chance involved.

#### (f) 80% of TLC’s songs have between 700,000 and 1,200,000 plays.

True False

False. Our confidence interval is estimating the average number of plays but makes absolutely NO claim about what percentage of songs have between 700,000 and 1,200,000 plays. A 𝑛% confidence interval contains 𝑛% of the statistics you simulated, but it does not suggest that 𝑛% of the population is in that interval!

#### (g) The original sample mean you obtained was approximately 950,000 plays.

True False

Data C8 Spring 2026 Discussion 10 | 4

## Page 5

True. If we sample repeatedly from the original sample to construct the confidence interval, the Central Limit Theorem tells us that the distribution of sample means will be roughly normal and that it will be centered around the sample mean.

Data C8 Spring 2026 Discussion 10 | 5
