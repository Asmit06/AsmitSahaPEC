#Question1
str=input("Enter a string: ")
ar=str.split()#splits the string by storing words in a list
if len(ar)==1:
    print("No of occurences of each character :",len(ar[0]))#prints no of characters in the string
else:
    print("No of occurences of each word :",len(ar))#prints no of words in the string
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()


#Question 2
day=int(input("Enter day"))
month=int(input("Enter month"))
year=int(input("Enter year"))
def leap(lpy):    #function to check if leap year or not
    if lpy%100==0:
        if lpy%400==0:
            return True
        else:
            return False
    else:
        if lpy%4==0:
            return True
        else:
            return False
flag=0#variable to keep track if the data input is valid or not
if day>31 or day<0 or month<0 or month>12:
    flag=1
if month==2:#check if month is february 
    if day==28:
        if leap(year)==True:
            day=29#in leap years february has 29 days 
        else:
            day=1
            month=3
    elif day==29:
        if leap(year)==True:
            day=1
            month=3
        else:
            flag=1
    else:
        day=day+1
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:#months with 31 days
    if day==31:
        month+=1
        day=1
    else:
        day+=1
elif month==12:#checks if month is december 
    if day==31:#updates year if last day of december
        day=1
        month=1
        year+=1
    else:
        day+=1
else:#for months with 30 days
    if day==31:
        flag=1
    if day==30:
        month+=1
        day=1
    else:
        day=day+1
if flag==0:#if flag is zero then the date entered by user is correct
    print("Next date is : ",day,"/",month,"/",year)
else:
    print("Incorrect Input")
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()


#Question3
arr=[]
s=input("Enter integers seperated by spaces:")
s_arr=s.split()
for i in s_arr:
    arr.append(int(i))
a=[]
for i in arr:
    a1=[]
    b=i*i
    a1.append(i)#appends original integer to list
    a1.append(b)#appends squared integer to list
    a.append(tuple(a1))#type changes list to tuple then appends to list
print(a)
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()   



#Question4
grade=int(input("Enter grade: "))
perf=["Outstanding","Excellent","Very Good","Good","Average","Below Average","Poor"]
lett=["A+","A","B+","B","C+","C","D"]
if grade>=4 and grade<=10:
    grade=10-grade#changes the grade so that it can be used to search in the list
    print("Your grade is '"+lett[grade]+"' and '"+perf[grade]+"'")
else:
    print("Out of Range")
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()



#Question5
ini=65
n=int(input("Enter the no of lines: "))
for i in range(0,n):
    if i==0:
        s=''#no space in first line
    else:
        s=" "*(i)#used to add space in the particular line
    fin=ini+(n*2)-1-(2*i)
    for j in range(ini,fin):
        s=s+chr(j)#concatenates spaces and letters
    print(s)
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()



#Question 6
choice="Y"
dict1={}
while True:#loop programmed to exit only if N/n is entered and to input data only if Y/y is entered 
    if choice.upper()=="Y":
        sid=int(input("Input SID : "))
        name=input("Enter Name : ")
        dict1[sid]=name
    elif choice.upper()=="N":
        break
    else:
        print("Invalid input please enter again")
    choice=input("Do you wish to continue (Y/N) : ")
    
sidc=list(dict1.keys())#list of sid
namec=list(dict1.values())#list of names
#Part a
print("---------------------------DETAILS OF STUDENTS-----------------------")
print("SID                                 NAME")
for i6 in range(0,len(dict1)):
    print(sidc[i6],"                                 ",namec[i6])#prints details of students
#Part b
dicb={}
namecopy=list(namec)
namecopy.sort()
sidcopy=[]
for z in namecopy:
    sidcopy.append(sidc[namec.index(z)])#enters the sid in a new list according to the sorted name list
for ic in range(len(namecopy)):
    dicb[sidcopy[ic]]=namecopy[ic]#creates new dictionary which is sorted by name
print("Sorted by Name")
print(dicb)
#Part c
dicc={}
sidcop=list(sidc)
sidcop.sort()
namecop=[]
for h in sidcop:
    namecop.append(namec[sidc.index(h)])#enters the name in a new list according to the sorted sid list
for ic in range(len(namecop)):
    dicc[sidcop[ic]]=namecop[ic]#creates new dictionary which is sorted by sid
print("Sorted by SID")
print(dicc)
#Part d
sidenter=int(input("Enter sid to search : "))
print(dict1[sidenter])#prints the name after searching in dictionary
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()




#Question 7
n=int(input("Enter number of terms : "))
first=0
second=1
fibo=[]
if n>1:
    fibo.append(first)#appends 0 if no of terms >1
if n>2:
    fibo.append(second)#appends 0 if no of terms >2
if n>=3:
    for fib in range(2,n):
        fibcop=first+second#adds prev 2 digits
        fibo.append(fibcop)
        first=second#changes value of first digit with next digit
        second=fibcop#changes value of second digit with sum of prev 2 digits
print(fibo)
sum7=0
for i7 in fibo:
    sum7+=i7#finds sum of n fibonacci terms
average=(sum7)/len(fibo)#finds average of sum of n fibonacci terms
print("The average is:",average)
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()




#Question 8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
#part a
print("Part a")
print(set1^set2)#set of all elements that are in Set1 and Set2 but not both (symmetric difference)
#part b
print("Part b")
print((set1^set2)^set3)#set of all elements that are in only one of the three sets Set1, Set2 and Set3.
#part c
print("Part c")
l1=list(set1)
l2=list(set2)
l3=list(set3)
l4=l1+l2+l3#list containing all the elements in the sets
arr8=[]#set of elements that are exactly two of the sets Set1, Set2 and Set3.
for i8 in range(0,len(l4)):
    flag=1
    if l4[i8] in arr8:#if element already present in the list it is ignored
        continue
    else:
        for j8 in range(i8+1,len(l4)):
            if l4[i8]==l4[j8]:
                flag=flag+1
        if flag==2:#if there is 2 intances of an element in the list
            arr8.append(l4[i8])
print(set(arr8))#converts new list to set    
#part d
print("Part d")
set4={1,2,3,4,5,6,7,8,9,10}
print(set4-set1)#new set of all integers in the range 1 to 10 that are not in Set1.
#part e
print("Part e")
print(set4-(set1|set2|set3))#set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print()
print()












    

