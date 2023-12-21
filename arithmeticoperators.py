#first line contains the sum of two numbers
#second line contains difference of the two numbers (first - second)
# third line contains product of the two numbers
#constraints 1 <=a <=10**10 1 <=b <=10**10
a= 3
b=5


if (a<1 and a>pow(10,10)):
    print("A is out of range")
elif (b <1 and b>pow(10,10)):
    print("B is out of range")
else: 
    print(a+b)
    print(a-b)
    print(a*b)