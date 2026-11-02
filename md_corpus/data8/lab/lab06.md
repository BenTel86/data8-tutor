---
title: "Lab 6: Examining the Therapeutic Touch"
assignment: lab06
semester: sp26
source: semester_assignments/sp26/lab/lab06/autograder/lab06.ipynb
version: solution (autograder) with student scaffolds
student_source: semester_assignments/sp26/lab/lab06/student/lab06.ipynb
total_points: 1
language: python
---

![Data 8 Logo](lab06_assets/data8logo.png)

# Lab 6: Examining the Therapeutic Touch

Welcome to Lab 6! This assignment involves using statistical modeling, hypothesis testing, and simulation to analyze data and draw conclusions

**Recommended Reading**:

* [Assessing a Model](https://inferentialthinking.com/chapters/11/1/Assessing_a_Model.html)
* [Empirical Distribution of a Statistic](https://inferentialthinking.com/chapters/10/3/Empirical_Distribution_of_a_Statistic.html)
* [Random Sampling in Python](https://inferentialthinking.com/chapters/10/4/Random_Sampling_in_Python.html)
* [Python Reference](https://www.data8.org/su26/reference/)

**Getting help on lab**: Whenever you feel stuck or need some further clarification, find a GSI or tutor, and they'll be happy to help!

As a reminder, here are the policies for getting full credit if you are in regular lab (Lab is worth 20% of your final grade):
- 80% of lab credit will be attendance-based. To receive attendance credit for lab, you must attend the full discussion portion (first hour) at which point the GSI will take attendance. 
- The remaining 20% of credit will be awarded for submitting the programming-based assignment to Pensive by the deadline (5pm on Friday) with all test cases passing.

If you are in self-service lab, 100% of credit will be awarded for submitting the programming-based assignment to Pensive by the deadline (5pm on Friday) with all test cases passing.

**Submission**: Once you’re finished, run all cells besides the last one, select File > Save Notebook, and then execute the final cell. The result will contain a zip file that you can use to submit on Pensive.

Let's begin by setting up the tests and imports by running the cell below.

After such an extensive introduction to programming for data science, we are finally moving into the section of the course where we can apply our new skills to answer real questions.  

In this lab, we'll use testing techniques that were introduced in lecture to test the idea of the therapeutic touch, the idea that some practitioner can feel and massage your human energy field.

**Code:**

```python
# Run this cell, but please don't change it.
 
# These lines import the Numpy and Datascience modules.
import numpy as np
from datascience import *
def sample_proportions(sample_size, probabilities):
    return np.random.multinomial(sample_size, probabilities) / sample_size

# These lines do some fancy plotting magic
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
from matplotlib import patches
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
```

---
## 1. What is the Therapeutic Touch

The Therapeutic Touch (TT) is the idea that everyone can feel the Human Energy Field (HEF) around individuals.  Those who practice TT have described different people's HEFs as "warm as Jell-O" and "tactile as taffy." 

TT was a popular technique used throughout the 20th century that was touted as a great way to bring balance to a person's health. Certain practitioners claim they have the ability to feel the HEF and can massage it in order to promote health and relaxation in individuals.

### Emily Rosa

[Emily Rosa](https://en.wikipedia.org/wiki/Emily_Rosa) was a 4th grade student who was very familiar with the world of TT, thanks to her parents, who were both medical practitioners and skeptics of TT.

For her 4th grade science fair project, Emily decided to test whether or not TT practitioners could truly interact with a person's HEF. She later went on to publish her work in TT, becoming the youngest person to have a research paper published in a peer reviewed medical journal.

### Emily's Experiment

Emily's experiment was clean, simple, and effective. Due to her parents' occupations in the medical field, she had wide access to people who claimed to be TT practitioners. 

Emily recruited 21 Therapeutic Touch (TT) practitioners to participate in her science experiment. She would take a TT practitioner and ask them to extend their hands through a screen (which they can't see through). Emily would be on the other side and would flip a fair coin. Depending on how the coin landed, she would put out either her left hand or her right hand. The TT practitioner would then have to answer which hand Emily put out. If a practitioner could truly interact with a person's HEF, it would be expected that they answered correctly.

Overall, through 210 samples, the practitioner picked the correct hand 44% of the time. 

Emily's main goal here was to test whether or not the TT practitioners' guesses were random, like the flip of a coin. In most medical experiments, this is the norm. **We want to test whether or not the treatment has an effect, *not* whether or not the treatment actually works.**

We will now begin to formulate this experiment in terms of the terminology we learned in this course.

---

**Question 1.1**: Describe Emily’s [model](https://inferentialthinking.com/chapters/11/1/Assessing_a_Model.html) for how likely the TT practitioners are to choose the correct hand. What alternative model is her model meant to discredit?

If you are able, check in with fellow peers, the discussion forum, or your lab TA/tutors, to come to a conclusion.

**SOLUTION:** Emily’s model is that the TT practitioners have a 50% chance of choosing the correct hand, like flipping a fair coin. She is trying to debunk the alternative model that the TT practitioners have some chance other than 50% of choosing the correct hand.

--- 

**Question 1.2:** Remember that the practitioner got the correct answer 44% (0.44) of the time. According to Emily's model, on average, what proportion of times do we expect the practitioner to guess the correct hand? Make sure your answer is a number between 0 and 1.

**Student scaffold:**

```python
expected_proportion_correct = ...
expected_proportion_correct
```

**Solution:**

```python
expected_proportion_correct = 0.5 # SOLUTION
expected_proportion_correct
```

*Output:*

```text
0.5
```

**Test — `q1_2`**

```python
>>> 0 <= expected_proportion_correct <= 1
True

>>> from lab06_check import correctness_check_1_2
>>> correctness_check_1_2(expected_proportion_correct)
True
```

The goal now is to see if our deviation from this expected proportion of correct answers is due to something other than chance. 

--- 

**Question 1.3:** We usually use a statistic to help determine which model the evidence points towards. What is a statistic that we can use to compare outcomes under Emily’s model to what was observed? Assign `valid_stat` to an array of integer(s) representing test statistics that Emily can use: 

1. The difference between the expected percent correct and the actual percent correct
2. The absolute difference between the expected percent correct and the actual percent correct
3. The sum of the expected percent correct and the actual percent correct

**NOTE:** Make sure to use `make_array` to create your array of integer(s)!

> *Hint*: What should the domain (possible x values) be for the distribution of our test statistics?

**Student scaffold:**

```python
valid_stat = ...
valid_stat
```

**Solution:**

```python
valid_stat = make_array(2) # SOLUTION
valid_stat
```

*Output:*

```text
array([2])
```

**Test — `q1_3`**

```python
>>> type(valid_stat) == np.ndarray
True

>>> from lab06_check import correctness_check_1_3
>>> correctness_check_1_3(valid_stat)
True
```

--- 

**Question 1.4:** Why is the statistic from Question 1.3 the appropriate choice for comparing outcomes in Emily's experiment? How does it relate to the models you defined in Question 1.1? 

If you are able, check in with fellow peers, the discussion forum, or your lab TA/Tutors.

**SOLUTION:** We want to take the absolute difference between the expected percent correct and actual perfect correct because we are interested in exploring whether or not the treatment has an effect, not whether or not the treatment actually works. This is because the alternate model states that practioners are not answering randomly, but not whether their accuracy is better or worse than if they were guessing at random.

--- 

**Question 1.5:** Define the function `statistic` which takes in an expected proportion and an actual proportion, and returns the value of the statistic chosen in Question 1.3. Assume that the argument takes in proportions, but  return your answer as a percentage. 

*Hint:* Remember we are asking for a **percentage**, not a proportion.

**Student scaffold:**

```python
def statistic(expected_prop, actual_prop):
    ...
```

**Solution:**

```python
def statistic(expected_prop, actual_prop):
    return abs(expected_prop - actual_prop) * 100 # SOLUTION
```

**Test — `q1_5`**

```python
>>> int(round(statistic(0.5, 0.5) + statistic(0.4, 0.1), 1))
30

>>> int(statistic(0.4, 0.1) - statistic(0.1, 0.4))
0
```

--- 

**Question 1.6:** Use your newly defined function to calculate the observed statistic from Emily's experiment.

**Student scaffold:**

```python
observed_statistic = ...
observed_statistic
```

**Solution:**

```python
observed_statistic = statistic(expected_proportion_correct, .44) # SOLUTION
observed_statistic
```

*Output:*

```text
6.0
```

**Test — `q1_6`**

```python
>>> from lab06_check import correctness_check_1_6
>>> correctness_check_1_6(observed_statistic)
True
```

**Is this observed statistic consistent with what we expect to see under Emily’s model?**

In order to answer this question, we must simulate the experiment as though Emily's model was correct, and calculate our statistic for every simulation.

### `sample_proportions`

`sample_proportions` can be used to randomly sample from multiple categories when you know the proportion of data points that are expected to fall in each category. `sample_proportions` takes two arguments: the sample size and an array of proportions corresponding to each category in the population (should sum to 1).

*Note:* A detailed comparison of the three main sampling methods used in Data 8 can be found on this [Sampling Notes Document](https://drive.google.com/file/d/16fIxluoOgr-BfKq_YdUFd3z3zEmwtsRk/view)

Consider flipping a fair coin, where the two outcomes (coin lands heads and coin lands tails) occur with an equal chance. We expect that half of all coin flips will land heads, and half of all coin flips will land tails.

Run the following cell to see the simulation of 10 flips of a fair coin. Let the first item of `coin_proportions` be the proportion of heads and the second item of `coin_proportions` be the proportion of tails.

*Observe what happens when you run this cell multiple times—the proportion of coin flips that land heads and tails appears to change, as you are simulating flipping 10 coins each time!*

**Code:**

```python
coin_proportions = make_array(0.5, 0.5) 
ten_flips = sample_proportions(10, coin_proportions)
ten_flips
```

*Output:*

```text
array([ 0.8,  0.2])
```

`sample_proportions` returns an array that is the same length as the proportion array that is passed through. It contains the proportion of each category that appears in the sample. 

In our example, the first item of `ten_flips` is the simulated proportion of heads and the second item of `ten_flips` is the simulated proportion of tails.

**Code:**

```python
simulated_proportion_heads = ten_flips.item(0)
simulated_proportion_tails = ten_flips.item(1)

print("In our simulation, " + str(simulated_proportion_heads) + " of flips were heads and " \
      + str(simulated_proportion_tails) + " of flips were tails.")
```

*Output (stdout):*

```text
In our simulation, 0.8 of flips were heads and 0.2 of flips were tails.
```

---

**Question 1.7:** To begin simulating, we should start by creating a representation of Emily's model to use for our simulation. This will be an array with two items in it. The first item should be the proportion of times a TT practitioner picks the correct hand, assuming that Emily’s model was correct. The second item should be the proportion of times, under the same assumption, that the TT practitioner picks the incorrect hand. Assign `model_proportions` to this array. 

After this, we can simulate 210 hand choices, as Emily evaluated in real life, and find a single statistic to summarize this instance of the simulation. Use the `sample_proportions` function and **assign the simulated proportion of correct hand choices to** `simulation_proportion_correct`. Lastly, use your `statistic` function to assign `one_statistic`  to the value of the statistic for this one simulation.

*Hint:* `sample_proportions` usage can be found on the [Python Reference](https://www.data8.org/su26/reference/).

*Note:* Once you are done, you can observe how `one_statistic` randomly changes by commenting out `np.random.seed(16)`. Just make sure to uncomment it before running the grader check.

**Student scaffold:**

```python
# This saves the random state of our code so that we can 
# generate the same numbers each time we run the code.
# Please do not change this line. 
np.random.seed(16)

model_proportions = ...
simulation_proportion_correct = ...
one_statistic = ...
one_statistic
```

**Solution:**

```python
# This saves the random state of our code so that we can 
# generate the same numbers each time we run the code.
# Please do not change this line. 
np.random.seed(16)

model_proportions = make_array(.5,.5) #SOLUTION
simulation_proportion_correct = sample_proportions(210, model_proportions).item(0) #SOLUTION
one_statistic = statistic(expected_proportion_correct, simulation_proportion_correct) #SOLUTION
one_statistic
```

*Output:*

```text
0.9523809523809545
```

**Test — `q1_7`**

```python
>>> len(model_proportions) % 2 == 0
True

>>> len(np.unique(model_proportions))
1

>>> sum(model_proportions) == 1
True

>>> type(simulation_proportion_correct) == float
True

>>> round(simulation_proportion_correct, 2)
0.49

>>> round(one_statistic, 2) - 0.95 < 0.05
True
```

---

**Question 1.8:** Let's now see what the distribution of statistics is actually like under Emily's model. 

Define the function `simulation_and_statistic` to take in the `model_proportions` array and the expected proportion of times a TT practitioner would guess a hand correctly under Emily's model. The function should simulate Emily running through the experiment 210 times and return the statistic of this one simulation.

*Hint:* This should follow the same pattern as the code you did in the previous problem.

**Student scaffold:**

```python
def simulation_and_statistic(model_proportions, expected_proportion_correct):
    '''Simulates 210 TT hand choices under Emily’s model. 
    Returns one statistic from the simulation.'''
    ...
```

**Solution:**

```python
def simulation_and_statistic(model_proportions, expected_proportion_correct):
    '''Simulates 210 TT hand choices under Emily’s model. 
    Returns one statistic from the simulation.'''
    # BEGIN SOLUTION
    simulated_proportion = sample_proportions(210, model_proportions).item(0)
    simulated_statistic = statistic(expected_proportion_correct, simulated_proportion)
    return simulated_statistic
    # END SOLUTION
```

Using this function, assign `simulated_statistics` to an array of 1000 statistics that you calculated under the assumption that Emily's model was true.

**Student scaffold:**

```python
num_repetitions = 1000

simulated_statistics = ...

for ... in ...:
    ...
```

**Solution:**

```python
num_repetitions = 1000

simulated_statistics = make_array() # SOLUTION
# BEGIN SOLUTION NO PROMPT
for i in np.arange(num_repetitions):
    a_statistic = simulation_and_statistic(model_proportions, expected_proportion_correct)
    simulated_statistics = np.append(simulated_statistics, a_statistic)
# END SOLUTION

""" # BEGIN PROMPT
for ... in ...:
    ...
"""; # END PROMPT
```

**Test — `q1_8` (1 point)**

```python
>>> len(simulated_statistics) == 1000
True

>>> np.all(simulated_statistics <= 30)
True

>>> np.all(simulated_statistics >= 0)
True

>>> 0 <= simulation_and_statistic(model_proportions, expected_proportion_correct) <= 25
True
```

Let's view the distribution of the simulated statistics under Emily's model, and visually compare where the observed statistic lies relative to the simulated statistics.

**Code:**

```python
t = Table().with_column('Simulated Statistics', simulated_statistics)
t.hist()
plt.scatter(observed_statistic, 0, color='red', s=100, zorder=2);
```

![Plot output from cell 38 — see preceding code](lab06_assets/cell038_out0.png)

We can make a visual argument as to whether we believe the observed statistic is consistent with Emily’s model. Here, since larger values of the test statistic suggest the alternative model (where the chance of guessing the correct hand is something other than 50%), we can formalize our analysis by finding what proportion of simulated statistics were as large or larger than our observed test statistic (the area at or to the right of the observed test statistic). If this area is small enough, we’ll declare that the observed data are inconsistent with our simulated model. Here is the [link](https://inferentialthinking.com/chapters/11/1/Assessing_a_Model.html#comparing-the-prediction-and-the-data) to the section in the textbook.

--- 

**Question 1.9:** Calculate the proportion of simulated statistics in Question 1.8 greater than or equal to the observed statistic. 

*Hint:* `np.count_nonzero` usage can be found [here](https://inferentialthinking.com/chapters/09/Randomness.html).

**Student scaffold:**

```python
proportion_greater_or_equal = ...
proportion_greater_or_equal
```

**Solution:**

```python
proportion_greater_or_equal = np.count_nonzero(simulated_statistics>=observed_statistic)/len(simulated_statistics) # SOLUTION
proportion_greater_or_equal
```

*Output:*

```text
0.089
```

**Test — `q1_9`**

```python
>>> 0 <= proportion_greater_or_equal <= 1
True

>>> proportion_greater_or_equal * 1000 == np.count_nonzero(simulated_statistics >= observed_statistic)
True
```

By convention, we often compare the proportion we just calculated to 0.05. If the proportion of simulated statistics greater than or equal to the observed statistic is sufficiently small (less than or equal to 0.05), then this is evidence **against** Emily's model. Conceptually, you may think of this as the case where less than 5% of simulated values are as far or farther away from what we had expected. This would mean that seeing a result **as extreme as our observed value** would be very **unlikely** under Emily’s model, given how rarely that occurred in our simulations.

This should help you make your own conclusions about Emily Rosa's experiment. 

Therapeutic touch fell out of use after this experiment, which was eventually accepted into one of the premier medical journals. TT practitioners hit back and accused Emily and her family of tampering with the results, while some claimed that Emily's bad spiritual mood towards therapeutic touch made it difficult to read her HEF. Whatever it may be, Emily's experiment is a classic example about how anyone, with the right resources, can test anything they want!

---

**Question 1.10:** Now, take some time to reflect on the questions below and then, discuss with your peers or take a look at the discussions on the Ed post for this lab.

1. Is the data more consistent with Emily' model (practitioners were randomly guessing)?
2. What does this mean in terms of Emily's experiment? Do the TT practitioners' answers follow an even chance model or is there something else at play? 

Did you talk to your peers or look at the discussion forum? (True/False)

**Student scaffold:**

```python
peer_talk = ...
peer_talk
```

**Solution:**

```python
peer_talk = True # SOLUTION
peer_talk
```

*Output:*

```text
True
```

**Test — `q1_10`**

```python
>>> peer_talk == True
True
```

---

You're done with lab!

**Important submission information:**
- **Run all the tests** and verify that they all pass
- **Save** from the **File** menu
- **Run the final cell to generate the zip file**
- **Click the link to download the zip file**
- Then, go to [Pensive](https://www.pensieve.co/) and submit the zip file to the corresponding assignment. The name of this assignment is "Lab XX Autograder", where XX is the lab number -- 01, 02, 03, etc.

- If you finish early in Regular Lab, **ask one of the staff members to check you off**.

**It is your responsibility to make sure your work is saved before running the last cell.**

---

To double-check your work, the cell below will rerun all of the autograder tests.

## Submission

Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**
