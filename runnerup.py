# Given n scores, store them in a list, and find the score of the runner up
# First line contains n
# Second line contains an array A[] of n integers each separated by a space
# Constraints: 2 <= n <= 10, -100 <= A[i] <= 100
# Sample input: 2 3 6 6 5 --- output is 5

# Input as a string
input_str = "2 3 6 6 5"

# Split the input string into a list of strings
raw_input = input_str.split()

# Convert the elements of the list to integers
n = int(raw_input[0])
arr = list(map(int, raw_input[1:]))

# Constraints: 2 <= n <= 10, -100 <= A[i] <= 100
if n < 2 or n > 10:
    print("n is out of range")
for i in arr:
    if i < -100 or i > 100:
        print("Array value is out of range")

# Logic to find the runner-up score
arr.sort(reverse=True)
runner_up_score = None

for score in arr:
    if score < max(arr):
        runner_up_score = score
        break

print("Runner-up score:", runner_up_score)
