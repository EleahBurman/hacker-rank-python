# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

# Example

# The string contains all letters in the English alphabet, so return pangram.

# Function Description

# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

# pangrams has the following parameter(s):

# string s: a string to test
# Returns

# string: either pangram or not pangram
# Input Format

# A single line with string .

# Constraints


# Each character of , 

# Sample Input

# Sample Input 0

# We promptly judged antique ivory buckles for the next prize

# Sample Output 0

# pangram

# Sample Explanation 0

# All of the letters of the alphabet are present in the string.

# Sample Input 1

# We promptly judged antique ivory buckles for the prize

# Sample Output 1

# not pangram

# Sample Explanation 0

# The string lacks an x.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    #26 letters in alphabet
    # count how many different letters are in s -- if 26 then pangram if not then not pangram
    #remove spaces in s
    # Remove spaces in s and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Set to store unique alphabet letters
    unique_letters = set()
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is an alphabet letter
        if char.isalpha():
            unique_letters.add(char)
    
    # Check if all 26 letters are present
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()