#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    #initialize total
    max_total = 0
    #initialize n to half the length since its a square of 2n and 2*(0.5)=1
    n = int(len(matrix)/2)
    #itirate over each quadrant
    for i in range(n):
        for j in range(n):
            # For each element in the top-left quadrant, the code calculates the maximum of the corresponding elements in the other three quadrants (top-right, bottom-left, and bottom-right). It uses (2*n-1) to access elements in the other quadrants.
            max_s = max(matrix[i][j], matrix[i][(2*n-1)-j], matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j])
            # The maximum value found in each quadrant (max_s) is added to the max_total variable.
            max_total += max_s
    
    return max_total
  
if __name__ == '__main__':