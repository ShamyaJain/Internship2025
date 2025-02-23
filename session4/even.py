#Create a Python program to remove all even numbers from a given list
list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<=len(list)-1:
    if i%2==0:
        i+=1
        print(list)
