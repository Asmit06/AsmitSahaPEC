#question 1
str1="Python is a case sensitive language"
#part a
str1_len=len(str1)
print("Length of input string is :",str1_len) #length of string
#part b
str_rev=str1[::-1] #reverses the string
print("Reverse of input string is :",str_rev) 
#part c
str_cop=str1[10:26] #slices the string
print(str_cop) 
#part d
str3=str1.replace("a case sensitive","object oriented") #replaces "a case sensitive" with "object orieted"
print(str3)
#part e
str1_index=str1.index("a") #gives first occurence of "a" 
print(str1_index)
#part f
str1_white=str1.strip() #removes whitespace from string
print(str1_white)
print()
print("----------------------------------------------------------------------------------------")
print()
print()

#Question 2
name=input("Enter name:")
sid=input("Enter SID:")
dept=input("Enter Department Name:")
cgpa=float(input("Enter CGPA:"))
print("Hey,",name,"Here! \nMy SID is",sid," \nI am from",dept,"department and my CGPA is",cgpa) #\n is used to move pointer to new line when printing
print()
print("----------------------------------------------------------------------------------------")
print()
print()

#Question 3
a=56
b=10
print("a&b :",a&b)#bitwise AND
print("a|b :",a|b)#bitwise OR
print("a^b :",a^b)#bitwise XOR
print("a<<2 :",a<<2)#bitwise left shift 2 bits
print("b<<2 :",b<<2)#bitwise left shift 2 bits
print("a>>2 :",a>>2)#bitwise right shift 2 bits
print("b>>4 :",b>>4)#bitwise right shift 4 bits
print()
print("----------------------------------------------------------------------------------------")
print()
print()

#Question 4
a1=int(input("Enter a number :"))
b1=int(input("Enter a number :"))
c1=int(input("Enter a number :"))
if a1>b1:# checks if a1 is greater than b1
    if a1>c1:# checks if a1 is greater than c1
        print(a1,"is greatest")
    else:
        print(c1,"is greatest")
else:
    if b1>c1:# checks if b1 is greater than c1
        print(b1,"is greatest")
    else:
        print(c1,"is greatest")
print()
print("----------------------------------------------------------------------------------------")
print()
print()

#Question 5
org_str=input("Enter the string: ")
flag=org_str.find("name")#searches for index of "name" and returns -1 if not found
if flag==-1:
    print("No")
else:
    print("Yes")
print()
print("----------------------------------------------------------------------------------------")
print()
print()

#Question 6
s1=int(input("Enter length of one side of triangle:"))
s2=int(input("Enter length of one side of triangle:"))
s3=int(input("Enter length of one side of triangle:"))
if s1+s2>s3 and s2+s3>s1 and s3+s1>s2: #checks if triangle is valid or not
    print("Yes")
else:
    print("No")
print()
print("----------------------------------------------------------------------------------------")
print()
print()
