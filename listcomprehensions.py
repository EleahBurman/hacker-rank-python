#given 3 integers x,y,z representing dimentions of cuboid along with integer n
#print list of all possible coordinates given by (i,j,k) on 3d grid where sum of i+j+k does not equal n
#0<=i<=x;0<=j<=y;0<=k<=z
#constrains print list in lexicographic increasing order
#print an array of all elements that do not sum to n
x=1
y=1
z=1
n=2

arr1=[]
arr2=[]
arr3=[]

for i in range(0,x+1):
    arr1.append(i)

for i in range(0,y+1):
    arr2.append(i)

for i in range(0,z+1):
    arr3.append(i)

#print(arr1)
#print(arr2)
#print(arr3)

#list comprehension
new_list=[]
for p in arr1:
    for q in arr2:
        for r in arr3:
            new_list.append((p,q,r))

#print (new_list)

#using value of n
final_list=[]

for(r,s,t) in new_list:
    if((r+s+t) !=n):
        final_list.append((r,s,t))
    
print ("Here is the final list:", final_list)



