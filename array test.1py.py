#prog to search a element in the array.
from array import *
  
a=array('i',[9,6,5,4,8,5,9])

key=int(input("Enter the val to be searched :"))
flange=0
for i in a:
    if key==i:
        flange=1
        break

if flange==1:
    print("Search is sucessfull :")
else:
    print("Search is unsucessfull :")
        