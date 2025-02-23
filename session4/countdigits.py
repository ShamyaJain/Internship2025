#Count Digits:
#Write a program to count the number of digits in a given positive integer using a while loop.

num=int(input("enter the number"))
count_2=0
temp=num
while temp>0:
    temp//=10
    count_2+=1
print(count_2)
