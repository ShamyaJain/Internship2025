#Palindrome Check:
#Implement a Python program to check whether a given number is a palindrome (e.g., 121, 1331) using a while loop.
num=int(input("enter the number"))
temp=0
rev=0
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp%S10
    if rev!=num:
        print(" not palindrome")
    else:
        print(" not palindrome")
            
