import os
import sys
import json
import re
import random
import copy
import math
import collections

import numpy as np
import scipy.stats
import scipy.spatial

def perform_t_test(points1, points2, two_sided=True):
    n1 = float(len(points1))
    n2 = float(len(points2))
    x1_bar = float(np.mean(points1))
    x2_bar = float(np.mean(points2))
    s1_2 = float(np.var(points1))
    s2_2 = float(np.var(points2))
    s = math.sqrt(s1_2 / n1 + s2_2 / n2)
    t = (x1_bar - x2_bar) / s
    df_numerator = pow(s1_2 / n1 + s2_2 / n2, 2.0)
    df_denominator = pow(s1_2 / n1, 2.0) / (n1 - 1.0) + pow(s2_2 / n2, 2.0) / (n2 - 1.0)
    df = df_numerator / df_denominator
    
    probability = scipy.stats.t.cdf(t, df)
    if two_sided:
        if probability > 0.5:
            p_value = 1.0 - probability
        else:
            p_value = probability
        probability = 1.0 - 2 * p_value
    
    p_value = 1.0 - probability
    return p_value

def calculate_confidence_interval(points, confidence_threshold=0.95):
    n = float(len(points))
    v = n - 1.0
    x_bar = np.mean(points)
    s = math.sqrt(np.var(points))
    A = scipy.stats.t.ppf(confidence_threshold, v)
    lower_bound = x_bar - A * s / math.sqrt(n)
    upper_bound = x_bar + A * s / math.sqrt(n)
    return (lower_bound, upper_bound)
