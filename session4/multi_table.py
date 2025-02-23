#multiplication Table:
#Create a Python program to print the multiplication table of any given number using a while loop.

a=int(input("enter the numbeR:"))
n=1
while n<10:
    multi=a*n
    n+=1
    multi=a*n
    print(a,"*",n,"=",multi)
