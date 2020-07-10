# Python T-Test and Confidence Interval Estimation

A simple Python implementation of standard statistical t-test and confidence interval estimation. 

For more details on how the the Student's T-Test and confidence interval estimation work behind the scenes, check out the [Student's T-Test Wikipedia article](https://en.wikipedia.org/wiki/Student%27s_t-test) and the [the Wikipedia article on confidence intervals](https://en.wikipedia.org/wiki/Confidence_interval).

## Setup

There's not much to it - just include the ttest.py file in your project, make sure you've installed the dependencies listed below, and use away!

### Dependancies

This module relies on two relatively standard Python libraries:

  1. [Numpy](numpy.org)
  2. [SciPy](www.scipy.org)

## Usage

This module exports two public functions, `perform_t_test1` and `calculate_confidence_interval`.

### Function: perform_t_test

```
perform_t_test(points1, points2)
```

This function performs a t-test on two given sets of data and returns the associated p-value.

Arguments:

| Name | Type | Description | Optional? | Default <br/> Value |
| ---- | ---- | ----------- | --------- | ------------------- |
| `points1` | `[float]` | The first dataset to be compared, represented as a list of floats. | False | N/A |
| `points2` | `[float]` | The second dataset to be compared, represented as a list of floats. | False | N/A |
| `two_sided` | `bool` | A flag indicating whether the test is to be two-tailed. | True | `True` |

Return Value: This function returns a single `float` that indicates the calculated p-value.

### Function: calculate_confidence_interval

```
calculate_confidence_interval(points, confidence_threshold)
```

This function calculates and returns the confidence interval on the provided dataset with the given confidence threshold.

Arguments:

| Name | Type | Description | Optional? | Default <br/> Value |
| ---- | ---- | ----------- | --------- | ------------------- |
| `points` | `[float]` | The dataset on which to calculate the interval, represented as a list of floats. | False | N/A |
| `confidence_threshold` | `float` | The confidence threshold to be used in the confidence interval calculation. | True | `0.95` |

Return Value: This function returns a tuple containing two floats representing the bounds of the interval: `(lower_bound, upper_bound)`.
  
## Example Usage

An implementation of the module on two randomly generated sample datasets has been given below:

```
import random
from ttest import *

# Creating sample data:
random.seed(1234) # Setting a random seed to ensure consistent results across runs of this sample
points1 = random.sample(range(10, 30), 10)
points2 = random.sample(range(15, 35), 10)

p_value = perform_t_test(points1, points2)
confidence_interval = calculate_confidence_interval(points1, 0.95)

print("T-Test for the sample data: ", p_value)
print("Calculated confidence interval: ", confidence_interval)
```
This sample will produce the following results:

```
T-Test for the sample data: 0.0011817174369730399
Calculated confidence interval: (14.167038919376605, 20.432961080623397)
```
