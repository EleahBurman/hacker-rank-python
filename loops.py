# for all non-negative integers i<n print n**2
n=3
#constraints n>=1 and n<=20
if (n<1 or n>20):
    print("n is out of range")
#list all non negative integers that are less than n=3 is [0,1,2]
for i in range(n):
    print((pow(i,2)))
#print square of each number