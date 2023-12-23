# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

# Example

# . We're working with 32 bits, so:



# Return .

# Function Description

# Complete the flippingBits function in the editor below.

# flippingBits has the following parameter(s):

# int n: an integer
# Returns

# int: the unsigned decimal integer result
# Input Format

# The first line of the input contains , the number of queries.
# Each of the next  lines contain an integer, , to process.

# Constraints



def flippingBits(n):
    # Use the bitwise NOT operator to flip all the bits
    flipped_result = ~n
    
    # Use the bitwise AND operator to ensure that the result is a 32-bit unsigned integer
    result = flipped_result & 0xFFFFFFFF
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()