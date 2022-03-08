#Question 1
from tkinter import *
from tkinter import messagebox
#from tkinter.tix import *
win = Tk()
def calculation():#function to calculate GST rate and total tax.
    global origCost, netPrice, gst, diff    # Defining global variables 
    if len(en1.get()) == 0 or len(en2.get()) == 0: # If nothing is entered, prompt an error window.
        messagebox.showerror("Error", "Error! : No value has been entered in Original Cost or Net Price.")
    else:
        try: # Creating an exception if any error occurs.
            origCost = float(en1.get())
            netPrice = float(en2.get())
            diff = netPrice - origCost
            gst = (diff * 100) / origCost     # Calculating GST.
        except Exception as e:         # Prompting an error message if any error occurs.
            messagebox.showerror("Error", "Error! : " + str(exp))
        if origCost>netPrice:
            messagebox.showerror("Error", "Error! : GST rate cannot be negative.")
        else:
            lb3.config(text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on Net Price : ₹{1:.2f}".format(gst,diff))
            lb3.place(x=200,y=200)

#PopUp Title
win.title("Question 1")

# Geometry.
win.geometry('500x400')
win.minsize(450, 370)
win.maxsize(700, 450)
#Header
head=Label(win, text="GST TAX CALCULATOR", bd=5, font=('Aerial',22,'underline'), bg='black', fg='white')
head.pack(fill=X)

#Main Design
lb1 = Label(win, text="Original Cost :", font="Arial 12")                                                                
"""lb1.grid(row=0, column=0, pady=10)"""
lb1.place(x=10,y=50)
en1=Entry(win)
en1.place(x=150,y=50)
lb2 = Label(win, text="Net Price :", font="Arial 12")
lb2.place(x=10,y=100)
en2=Entry(win)
en2.place(x=150,y=100)
bt1 = Button(win, text="Calculate", command=calculation, cursor='hand2', font="Arial 12")  
bt1.place(x=75,y=150)
lb3 = Label(win, bg='grey', fg='white', font="Arial 12", bd=7)  
win.mainloop()



# Question 2
from tkinter import *
from tkinter import messagebox
from tkinter.tix import *
import calendar

def calendar_():#Defining a function to Create a separate window to display the calendar
    global year #Defining a global variable.
    if len(en1.get()) == 0:
        messagebox.showerror("Error", "Error! : No value has been entered for year.")
    elif int(en1.get()) <= 0:
        messagebox.showerror("Error", "Error! :  Year cannot be negative or 0.")
    else:# Creating an exception if invalid integer is entered by the user.
        try:
            year = int(en1.get())#Getting value from entry box 1.
        except Exception as e:
            messagebox.showerror("Error", str(e))
        cal = calendar.calendar(year)# Using calendar library to print the Calendar.
        top1 = Toplevel(win2)# Creating a different window to print Calendar
        top1.title(f"{year} Calendar")# Title and icon.
        # Geometry.
        top1.geometry('640x620')
        top1.minsize(640, 630)
        top1.maxsize(640, 630)
        # Content.
        txt1 = Text(top1, relief=RIDGE, borderwidth=2, width=100, height=100) # Text box 1.
        txt1.pack(padx=20, pady=10)
        txt1.insert('end', cal)# Inserting calendar string in Text box 1.
        top1.mainloop()
win2 = Tk()
win2.title("Question 2")
# Geometry
win2.geometry('400x300')
win2.minsize(350, 250)
win2.maxsize(500, 400)
# Heading
Heading = Label(win2, text="Calendar Application", bd=5, font='Aerial 22 underline', bg='black', fg='white')
Heading.pack(pady=10, ipadx=10)
# Creating a frame
f1 = Frame(win2, bd=20)
f1.pack()
# Content
lb1 = Label(f1, text="Enter year :")                                                                   
lb1.pack(pady=5)
en1 = Entry(f1)                                                                                        
en1.pack(pady=5)
bt1 = Button(f1, text="Show Calendar", command=calendar_, cursor='hand2')                               
bt1.pack(pady=5)
win2.mainloop()


#Qurstion 3
from tkinter import *

win3 = Tk() # This is to create a basic window
win3.geometry("312x324")  # this is for the size of the window 
win3.resizable(0, 0)  # this is to prevent from resizing the window
win3.title("Calculator")

def click(item):# This Function continuously updates the input field whenever you enter a number
    global expression
    expression = expression + str(item)
    input_text.set(expression)
def clears(): #used to clear the input field
    global expression 
    expression = "" 
    input_text.set("")
def equal():#This method calculates the expression  present in input field
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
 
input_text = StringVar()#It is used to get the instance of input field
 
# creating a frame for the input field
input_frame = Frame(win3, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
 
# create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win3, width=312, height=272.5, bg="grey")
btns_frame.pack()

#Creating Buttons 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clears())
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("/"))
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(7))
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(8)) 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(9))
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("*"))
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(4))
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(5))
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(6))
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("-"))
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(1))
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(2))
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(3))
add = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("+"))
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(0))
dot = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click("."))
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal())

#gridding
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
four.grid(row = 2, column = 0, padx = 1, pady = 1)
five.grid(row = 2, column = 1, padx = 1, pady = 1)
six.grid(row = 2, column = 2, padx = 1, pady = 1)
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
one.grid(row = 3, column = 0, padx = 1, pady = 1)
two.grid(row = 3, column = 1, padx = 1, pady = 1)
three.grid(row = 3, column = 2, padx = 1, pady = 1)
add.grid(row = 3, column = 3, padx = 1, pady = 1)
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
dot.grid(row = 4, column = 2, padx = 1, pady = 1)
equals.grid(row = 4, column = 3, padx = 1, pady = 1)

win3.mainloop()

#Queston 4
def partition(arr, ini, fin):
    i = (ini-1)         # Index of smaller element and indicates the right position of pivot found so far
    pivot = arr[fin]     # Element to be placed at right position (pivot)
    for j in range(ini, fin):
        if arr[j] <= pivot: # If current element is smaller than or equal to pivot
            i = i+1# increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[fin] = arr[fin], arr[i+1]
    return (i+1)

def quickSort(arr, ini, fin):# Function to do Quick sort
    if len(arr) == 1:
        return arr
    if ini < fin:
        pi = partition(arr, ini, fin)
        quickSort(arr, ini, pi-1)        # Separately sort elements before partition
        quickSort(arr, pi+1,fin)       #  and after partition

ars = input("Enter marks seperated by spaces :")
arr=ars.split()
for i in range(len(arr)):
    arr[i]=int(arr[i])
n = len(arr)
quickSort(arr, 0, n-1)
print("Array Sorted by QuickSort Algorithm :",arr)
print()
print()



#question 5
ars = input("Enter numbers seperated by spaces :")
arr5=ars.split()
for i in range(len(arr5)):
    arr5[i]=int(arr5[i])
#part a
arr5.sort()#sorts the list
print("Sorted List : ",arr5)
#part b
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2 
        if arr[mid] < x:# If x is greater, ignore left half
            low = mid + 1
        elif arr[mid] > x:# If x is smaller, ignore right half
            high = mid - 1
        else:# means x is present at mid
            return mid
    return -1# If we reach here, then the element was not present
x = int(input("Enter number to search : "))
result = binary_search(arr5, x)# Function call
if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in array")
#part c
print("Number of occurrences of element",x,"is:",arr5.count(x))#counts number of occurences of x








