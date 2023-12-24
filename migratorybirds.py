# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# Example

# There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

# Function Description

# Complete the migratoryBirds function in the editor below.

# migratoryBirds has the following parameter(s):

# int arr[n]: the types of birds sighted
# Returns

# int: the lowest type id of the most frequently sighted birds
# Input Format

# The first line contains an integer, , the size of .
# The second line describes  as  space-separated integers, each a type number of the bird sighted.

# Constraints

# It is guaranteed that each type is , , , , or .

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # list to store the count of each bird type
    bird_count = [0] * 6  # Assuming bird types are represented by integers from 1 to 5

    # calculate count of each type
    for bird in arr:
        bird_count[bird] += 1

    # find the bird type with the maximum count
    max_count = max(bird_count)

    # find the smallest bird type with the maximum count
    for bird_type in range(1, 6):
        if bird_count[bird_type] == max_count:
            return bird_type
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
