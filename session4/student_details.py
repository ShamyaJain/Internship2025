
student_list=[]
n=int(input("how many students"))
for i in range(n):
    name=input("enetr name:")
    age=int(input("enter age:"))
    course=input("enter course:")
    student=[name,age,course]
    student_list.append(student)
print("student list are",student_list)
   
