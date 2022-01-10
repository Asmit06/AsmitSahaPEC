#Question1
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
average=(a+b+c)/3 #calculating average
print("The average is ",average)
print()
print("-------------------------------------------------------------------------")
print()

#Question2
g_income=int(input("Enter gross income :"))
n_dependants=int(input("Enter number of dependants :"))
t_income=g_income-(n_dependants*3000)-10000 #calculating taxable income
tax_payable=t_income*0.2 #tax 
print("Income Tax Payable :",tax_payable)
print()
print("-------------------------------------------------------------------------")
print()



#Question3
Student=[]#empty list to store student details
s_id=int(input("Enter student ID:"))
Student.append(s_id)#student id added to Student
s_name=input("Enter student name:")
Student.append(s_name)#student name added to Student
s_gender=input("Enter gender (F/M/U):")
Student.append(s_gender)#student gender added to Student
s_cname=input("Enter course name:")
Student.append(s_cname)#course name added to Student
s_cgpa=float(input("Enter CGPA:"))
Student.append(s_cgpa)#CGPA added to Student
print(Student)
print()
print("-------------------------------------------------------------------------")
print()




#Question4
L=[]
m1=int(input("Enter marks of student"))
m2=int(input("Enter marks of student"))
m3=int(input("Enter marks of student"))
m4=int(input("Enter marks of student"))
m5=int(input("Enter marks of student"))
L.extend([m1,m2,m3,m4,m5])       #adding data to the list L
for i in range(5):                #bubble sort 
    for j in range(0,5-i-1):
        if L[j]>L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
print("The sorted array is :",L)
print()
print("-------------------------------------------------------------------------")
print()




#Question5
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_copy=color.copy()
#part a
color.remove("Black")#removes black
print(color)
#part b
color_copy[3:5]=["Purple"]#replaces black and pink with purple
print(color_copy)
print()
print("-------------------------------------------------------------------------")





