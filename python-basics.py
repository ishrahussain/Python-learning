
#python is case sensitive language
print("Hello World!!")


name="ISHRA HUSSAIN"
roll_no=74543 #underscor can be used in varaiables names
print("PIAIC Artificial Intelligence Batch 3")
print("Name: ", name)
print("Roll No: ", roll_no)
age=23

print("Age is ", age)

marks=85
#it will recocgnize integers so we can use them for calculations
print("Marks: ", marks+5)
print(marks+age)

gpa=1+1

print("Multiple prints: ", gpa ,marks/2, age*2) #print multiple things seperated by comma

gpa+=1 #it is same as gpa=gpa+1
print(marks%gpa, gpa)
gpa*=1.29
print("GPA is:", gpa)

cost=1+3*4  #python works according to DMAS rule but we can also use parathesis
cost1=1+(3*4)
print("Same ", cost, cost1)

first_name="Ishra"
last_name="Hussain"
full_name=first_name+ " " + last_name #plus is used only for concatinating strings
print("My full name is ", full_name)

if name == "ISHRA":
    print("My name is Ishra") #pressing tab is necessary for indenting
    
    
if 2*4==8:
    print("It is correct")
    print("Full Marks")

if gpa!=4: #not equal to
    print("You are not topper")

if gpa<=3:
    print("Work hard")
    
pet="Pupoo"

if pet=="Ponny":
    print("pet name is ponny")
else:
    print("My pet name is Pupoo :)")
    
if pet=="Ponny" :
    print("My pet is rabbit")
elif pet=="Pupoo":
    print("My pet is a cat")
    
if pet=="Pupoo" and gpa>3:
    print("Its all good")

if name=="ISHRA" or gpa==4:
    print("Welcome")    
    
if (name=="ISHRA" or gpa==4) and pet=="Pupoo":
    print("This is my home")
    

if pet=="Pupoo":
    if name=="ISHRA":
        print("This is nested loop")
    elif gpa==4:
        print("This is also nested loop")
    else:
        print("Leave it")
else:
    print("Leave it")

#so this is how we can comment using hashes
    
'''  i ca write here too
this is another way
of commenting multiple lines
wow thats good
and there too'''
#List is defined as:
books=["physics", "chemistry", "biology", "maths", "english", "urdu"] #start adress is 0 i.e. books[0]=physics
print("I want to study " + books[3])

#array can also have multiple types of variables
random_stuff=["toy", "computer", 45, "pakistan"]
print( "The number is ", random_stuff[2] )

books.append("Islamiyat") #to add more elements to list
print("Appended book: ", books[6])

random_stuff.append(1947)

books=books+ ["AI", "GIT"]

books.insert(3, "Electronic Devices")   #add it to defined place and other elements move to next position

books[8]="Artificial Intelligence" #to update value we do this

print("Books:", books)

students=[] #can also add empty list and update later on


old_books=books[4:8]    #for picking slices of list,the number after colon is index of element after the last elemtn of slice, hence is not picked
print("Old Books ", old_books)

some_books=books[:5]    #picks from start 0 index
print("Some Books ", some_books)

last_books=books[5:]    #picks from defuined index to the last element
print("Picked books", last_books)
#chapter 17 completed

del old_books[0]    #to delete element at index 0, python adjusts indexes
print("Some old books deleted:", old_books)

del some_books[2]   #2 deleted others index adjusted
print(some_books)

some_books.remove("chemistry")      #delete using its value
print("Removed some books", some_books)


removed_books=books.pop(8)  #,=move mentioned element to this variable, it is not list it is just a string variable
removed_books_list=[] #create a emmpty list
removed_books_list.append(removed_books)    #append to add more elements to the list
removed_books=books.pop(2)
removed_books_list.append(removed_books)

#can also add elements directly to another list like this:
removed_books_list.insert(0, books.pop(1))

#to pop last element of list dont mention position
removed_books_list.insert(0,books.pop())    
print("Popped books", removed_books_list)
print("Books now: ", books)

#tuples: list whose elements are fixed and cant be changed
#tuple brackets are round brackets
cities=("Lahore", "Islamabad", "Karachi", "Peshawar", "Quetta")
print("My city is ", cities[1])