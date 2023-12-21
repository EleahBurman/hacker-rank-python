n=101

#constraints n is greater or equal to 1 and less than or equal to 100
if (n < 1 or n > 100):
    print("N is out of range")
# if n is odd print Weird
elif (n % 2 != 0):
    print("Weird")
# if n is even and in the inclusion of range of 2 to 5 print not weird
elif (n % 2 == 0 and n>=2 and n<=5):
    print("Not Weird")
# if n is even and in the inclusion of range of 6 to 20 print weird
elif (n % 2 == 0 and n>=6 and n<=20):
    print("Weird")
# if n is even and greater than 20 print not weird
elif(n%2 == 0 and n>20):
    print("Not Weird")
#constraints n is greater or equal to 1 and less than or equal to 100