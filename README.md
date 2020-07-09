# Python T-Test and Confidence Interval Estimation

A simple Python implementation of standard statistical t-test and confidence interval estimation.

## Usage

This module exports two public functions:

```
perform_t_test(points1, points2)
calculate_confidence_interval(points, confidence_threshold)
```

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

Return Value: This function returns a single float that indicates the calculated p-value.

### Function: calculate_confidence_interval

```
calculate_confidence_interval(points, confidence_threshold)
```

This function calculates and returns the confidence interval on a dataset using the given confidence threshold.

Arguments:

| Name | Type | Description | Optional? | Default <br/> Value |
| ---- | ---- | ----------- | --------- | ------------------- |
| `points` | `[float]` | The dataset on which to calculate the interval, represented as a list of floats. | False | N/A |
| `confidence_threshold` | `float` | The confidence threshold to be used in the confidence interval calculation. | True | `0.95` |

Return Value: This function returns a list of two floats containing the bounds of the interval, wrapped in a tuple: `(lower_bound, upper_bound)`.

## Setup

There's not much to it; just include the ttest.py file in your project, make sure you've installed the dependencies listed below, and use away!

### Dependancies

This module relies on 2 relatively standard Python libraries:

  1. [Numpy](numpy.org)
  2. [SciPy](www.scipy.org)
  
## Example Usage

An implementation of the module on two randomly generated sample datasets has been given below:

```
import random
from ttest import *

# Creating sample data:
random.seed(1234) # Setting a random seed to ensure consistent results across runs of this sample
points1 = random.sample(range(10, 30), 10)
points2 = random.sample(range(15, 35), 10)

confidence_threshold = 0.95

t_test_result = perform_t_test(points1, points2)
confidence_interval = calculate_confidence_interval(points1, confidence_threshold)

print("T-Test for the sample data: ", t_test_result)
print("Calculated confidence interval: ", confidence_interval)
```
This sample will produce the following results:

```
T-Test for the sample data: 0.0011817174369730399
Calculated confidence interval: (14.167038919376605, 20.432961080623397)
```
