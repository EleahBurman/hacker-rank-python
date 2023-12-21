#print all integers between 1 and n, should read 12345
#constraints 1<=n<=150
def print_function(n):
    if(n<1 or n>150):
        print("n is out of range")
    else:
        for i in range(1, n+1):
            print(i, end="")

print_function(5)