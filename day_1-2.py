#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def quartiles(arr):
  # Write your code here
  left, right, middle = [], [], []  # initialize section arrays
  n = len(arr)
  arr.sort() # sort input array
  
  # if array has single element
  if n == 1:
    q1, q2, q3 = arr[0], arr[0], arr[0]
    return q1, q2, q3
  
  # if array has even number of elements
  elif n != 1 and n % 2 == 0:
    for i in range(int(n/2)):
      left.append(arr[i])
      right.append(arr[int(n/2) + i])
    middle.append(arr[int(n/2) - 1])
    middle.append(arr[int(n/2)])
    
    # even left/right array
    if len(left) % 2 == 0:
      q1 = (left[int(len(left)/2)-1]\
    +left[int(len(left)/2)])/2
      q2 = (middle[0]+middle[1])/2
      q3 = (right[int(len(right)/2)-1]\
    +right[int(len(right)/2)])/2
    
    # odd left/right array 
    else:
      q1 = left[int(len(left)/2)]
      q2 = (middle[0]+middle[1])/2
      q3 = right[int(len(right)/2)]

    return q1, q2, q3

  # if array has odd number of elements
  else:
    for i in range(int(n/2)):
      left.append(arr[i])
      right.append(arr[int(n/2) + 1 + i])
    middle.append(arr[int(n/2)])
    
    # even left/right array
    if len(left) % 2 == 0:
      q1 = (left[int(len(left)/2)-1]\
    +left[int(len(left)/2)])/2
      q2 = middle[0]
      q3 = (right[int(len(right)/2)-1]\
    +right[int(len(right)/2)])/2
    
    # odd left/right array
    else:
      q1 = left[int(len(left)/2)]
      q2 = middle[0]
      q3 = right[int(len(right)/2)]
    
    return q1, q2, q3

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    
    arr = []
    for num, freq in zip(values, freqs):
        for i in range(freq):
            arr.append(num)
    arr.sort()  # sort the array
    
    q1, _, q3 = quartiles(arr)
    IQR = q3-q1
    print("%.1f" % IQR)
    
    return "%.1f" % IQR
            

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
