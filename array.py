#prog to sum of even no and odd seperatly...
from array import*

a=array('i',[])

n=int(input("Enter the limit:"))
print("Enter the array element one by one:")
even=0
odd=0
for i in range(n):
    x=int(input())
    a.append(x)
    
for i in a:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Sum of even no:",even)
print("Sum of odd",odd)