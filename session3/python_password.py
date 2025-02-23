#Create a prog that asks the user for a password and keeps asking until the correct password "python123" is entered.
n="python123"
a=str(input("generate a password:"))
while a!=n:
    a=str(input("generate a password:"))
print(n)
