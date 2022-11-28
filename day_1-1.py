#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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
      q1 = int((left[int(len(left)/2)-1]\
    +left[int(len(left)/2)])/2)
      q2 = int((middle[0]+middle[1])/2)
      q3 = int((right[int(len(right)/2)-1]\
    +right[int(len(right)/2)])/2)
    
    # odd left/right array 
    else:
      q1 = left[int(len(left)/2)]
      q2 = int((middle[0]+middle[1])/2)
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
      q1 = int((left[int(len(left)/2)-1]\
    +left[int(len(left)/2)])/2)
      q2 = middle[0]
      q3 = int((right[int(len(right)/2)-1]\
    +right[int(len(right)/2)])/2)
    
    # odd left/right array
    else:
      q1 = left[int(len(left)/2)]
      q2 = middle[0]
      q3 = right[int(len(right)/2)]
    
    return q1, q2, q3

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))
    
    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
