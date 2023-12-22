# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    new_string=[]
    a=0
    if (len(s)<0 or len(s)>1000):
        print("length of string is out of range")
    else:
        for letter in s:
            if letter.isupper():
                new_letter=letter.lower()
                new_string.append(new_letter)
            elif letter.islower():
                new_letter=letter.upper()
                new_string.append(new_letter)
            else:
                new_letter=letter
                new_string.append(new_letter)
    return (''.join(new_string))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)