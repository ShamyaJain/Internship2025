#Create a program that takes a user's age as input and prints:
#"Child" if age < 12
#"Teenager" if age is between 13 and 19
#"Adult" if age is 20 or above.

age=int(input("enter the age:"))
if age<12:
    print("it is child")
if 13<age<19:
    print("it is a teenager")
if age>=20:
    print("it is adult")
