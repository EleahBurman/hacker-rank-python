# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.

# Example


# The original message was SOSSOS. Two of the message's characters were changed in transit.

# Function Description

# Complete the marsExploration function in the editor below.

# marsExploration has the following parameter(s):

# string s: the string as received on Earth
# Returns

# int: the number of letters changed during transmission
# Input Format

# There is one line of input: a single string, .

# Constraints

#  will contain only uppercase English letters, ascii[A-Z].
# Explanation

# Sample 0

#  = SOSSPSSQSSOR, and signal length . Sami sent  SOS messages (i.e.: ).

# Expected signal: SOSSOSSOSSOS
# Recieved signal: SOSSPSSQSSOR

# We print the number of changed letters, which is .

# Sample 1

#  = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

# Expected Signal: SOSSOS
# Received Signal: SOSSOT

# We print the number of changed letters, which is .




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here
    number_of_letters=len(s)
    
    if(number_of_letters<1 or number_of_letters>99):
        print("Too many letters")
    else:
        #if a letter is changed from the original SOS message add one to the integer we print
        
        #if you divide by 3 that's how many SOS's you have
        
        #divide the number of letters by 3 and then see which letter is off from SOS - compare there and then add to variable that i set up for number
        number_of_sos=number_of_letters/3
        sos_string="SOS"*int(number_of_sos)
        # print(sos_string, "What is this giving us")
        position=0
        changed_letters=0
        for letter in sos_string:
            print(letter, "first comparison")
            print (s[position], "second comparison")
            #print("print of position: ", position)
            if s[position]!= letter: 
                changed_letters=changed_letters+1   
            
            position=position+1
                  
                
            # if s[position]!= letter:
            #     changed_letters=changed_letters+1

        
    return changed_letters
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()