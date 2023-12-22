def fact(n)
    res-1
    for i in range(1,n+1):
        res*=i
    return res
  def nPr(n,r):
      return fact (n)/fact(n-r)
    n=int(input("Enter the n value:  ")
    r=int(input("Enter the r value:  ")
    print("The nPr value is:  ",nPr(n,r))