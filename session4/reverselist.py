#Reverse a List:
#Implement a Python program to reverse a list using a while loop (without using the reverse() method).
num_list=[]
while True:
    data=input("enter the data:")
    choice=input("do you have more(yes/no)")
    if choice=="no":
        break
print(data[::-1])
num_list.append(data)
