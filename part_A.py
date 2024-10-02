#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:53:24 2024

@author: alexsolheim
"""

"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt

# Compute standard deviation using for loops

def std_loops(x):
    
    # Compute the mean using for loops
    
    N = 0
    total_sum = 0
    for num in x:
        total_sum = total_sum + num
        N = N + 1
    mean = total_sum / N
    
    # Compute the mean of squares using for loops
    
    sum_of_squares = 0
    for num in x:
        sum_of_squares = sum_of_squares + num ** 2
    mean_of_squares = sum_of_squares / N
    
    # Compute the variance
    
    variance = mean_of_squares - mean ** 2
    
    # Compute the standard deviation
    
    standard_deviation = sqrt(variance)
    
    return standard_deviation

# Compute standard deviation using the built-in functions sum() and len()

def std_builtin(x):
    
    # Compute the mean
    
    mean = sum(x) / len(x)
    
    # Compute the mean of squares
    
    mean_of_squares = sum([num ** 2 for num in x]) / len(x)

    # Compute the variance

    variance = mean_of_squares - mean ** 2
    
    # Compute the standard deviation
    
    standard_deviation = sqrt(variance)
    
    return standard_deviation

# Compute standard deviation using numpy
    
import numpy as np

num_lst = [1, 2, 3, 4, 5]

print(f'Standard deviation using for loops: {std_loops(num_lst)}')

print(f'Standard deviation using built-in fuctions: {std_builtin(num_lst)}')

print(f'Standard deviation using numpy: {np.std(num_lst)}')
    