#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function

  mean = sum(arr)/len(arr) # calculate the mean
  
  # error from the mean squared
  err = []
  for num in arr:
    err.append((mean-num)**2)

  # std calculation
  std = math.sqrt(sum(err)/len(arr))
  print("%.1f" % std)
  
  return "%.1f" % std
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
