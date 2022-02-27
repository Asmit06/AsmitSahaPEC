#question 1
def hanoi(n,A,C,B):
    if n==0:
        return
    hanoi(n-1,A,B,C)
    print(n,"      ",A,"       ",C)#swaps the disk n from initial pos to final pos
    hanoi(n-1,B,C,A)
print("Rod Positions:       A        B        C")
print("Disk No     Original Position       Final Position")
hanoi(3,"A","C","B")
print("----------------------------------------------------------------------------------------------------------------------------------")
print()
print()

#question 2
def fact(n):#function to return factorial 
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact
fin=[]

def pascal(n):#function to return the pascal pattern
    if n==0:
        return fin.append("1")
    else:
        pascal(n-1)
        new=""
        for j in range(0,n):
            new=new+str((fact(n)//(fact(j)*fact(n-j))))+" "#pascals triangle values are nCr
        new+="1"#concatenating 1 to end of each line
        
        fin.append(new)
    return fin
n=int(input("Enter the number of lines"))
arr=(pascal(n-1))#0 is used in the code thus n-1 is passed
flag=n-1

for i in range(n):
    print((" "*flag),end="")#prints the triangle in the pattern
    flag=flag-1
    print(arr[i])
print("----------------------------------------------------------------------------------------------------------------------------------")
print()
print()

#question 3
n1=int(input("Enter a number :"))
n2=int(input("Enter a number :"))
quotientremainder=(divmod(n1,n2))#calling divmod function to get quotient and remainder
result1=quotientremainder
rb=[]
rb.append(n1)
rb.append(n2)
rb=rb+list(result1)
print("Quotient and remainder :",quotientremainder)
#Part a
print("PART A")
print("Is the function callable?",callable(divmod))#checks if function is callable or not
#part b
print("PART B")
if 0 in rb:#checks if any of the value's are zero
    print("All all values non zero?",False)
else:
    print("All all values non zero?",True)
#part c
print("PART C")
cop=list(rb)+[4,5,6]#adds the list to original list of values
result=[]
for i3 in cop:
    if i3>4:
        result.append(i3)#adds values greater than 4 into a new list
print("Numbers greater than 4",result)
#part d
print("PART D")
result_set=set(result)#converts list to set
print("After conversion to set:",result_set)
#part e
print("PART E")
result_fset=frozenset(result_set)#makes the set unmutable
print("The immutable set:",result_fset)
#part f
print("PART F")
print("Maximum value in the set :",max(result_fset))#returns maximum value in the set
print()
print("Hash of max value :",hash(max(result_fset)))#returns hash value of the max value
print("----------------------------------------------------------------------------------------------------------------------------------")
print()
print()

#question 4
class Student:
    def __init__(self,name,rno):#assigns parameter values to the object
        self.name=name
        self.rno=rno  
        print("Student Name:",name,"           Roll No:",rno)
        
    def __del__(self):#destructor to delete object
        print("Student details deleted")
name4=input("Enter student name :")
rno4=int(input("Enter student roll number :"))
s1=Student(name4,rno4)
del s1#deletes the object s1
#print(s1)    error is shown saying "s1" not defined
print("----------------------------------------------------------------------------------------------------------------------------------")
print()
print()


#question 5
class Employee:
    def __init__(self,emp,name,sal):#constructor to assign values to object
        self.emp=emp
        self.name=name
        self.sal=sal
    def display(self):#function to display object
        print("Employee :",self.emp,"    Name :",self.name,"    Employee :",self.sal)
    def __del__(self):#destructor to delete objects
        print("Destructor called. Employee details of ",self.name,"deleted")
               
p1=Employee(1,"Mehak",40000)
p2=Employee(2,"Ashok",50000)
p3=Employee(3,"Viren",60000)
p1.display()
p2.display()
p3.display()
print()
print()
#part a
print("PART A")
p1.sal=70000#updates the salary of object p1
print("After updation   ")
p1.display()
#part b
print("PART B")
del p3#deletes the object p3
print("----------------------------------------------------------------------------------------------------------------------------------")
print()
print()


#question 6
g_word=input("Enter George's word :")
b_word=input("Enter Barbie's word :")
def anagrams(s):#function that returns an array consisting of various permutations of the passed value
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):#Slice the first character off the string.
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])#Place the first character in all possible locations within the anagrams formed from the “rest” of the original string.
    return ans
arr=anagrams(g_word)
if b_word in arr:#checks if word is present in the array consisting of all its permutations
    print("Friendship is Real")
else:
    print("Friendship is Fake")
print("----------------------------------------------------------------------------------------------------------------------------------")
