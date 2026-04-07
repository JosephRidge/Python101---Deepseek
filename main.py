"""
Prior running any python program, you must run inside an isolated "space":
    - Container => Docker, Kuberntes, customized one
    - virtual environment **=> python virtual env

Python is an OOP language
Python embraces type inferencing

VARIABLE: 
- this stores a reference of somthing stored in memory: 

TYPES:
- global(accessed evrywhere around the app.) 
- local(scoped to a particular section)

PARTS:
- variable Name
- assignment operator
- value being stored


"""

userName = "John Doe" # global variable 
output = ""
output = userName


"""
DATA TYPES: 
- Computers Distinguish different data types in different ways/ manners

TYPES:
- Numbers (Integers, Floating, Complex)
    - Integer: (number that spans from 0 to -ve infinity and 0 to +ve infinity, 
    but not an decimal placed number). class name => int()
    - Floating: (decimal placed numbers). Class name => float()
    - Complex numbers: ( square-root of 2) 

- Texts (strings):
    - is an array of characters and is immutable(constant) in nature

- Arrays:
    - a collection of items, the items are reffreed to as elements
    - counting starts from 0

"""

numOne = 10 # integer
numTwo = 20.7 # float
numThree = complex(2) # parsing an integer into a complex number 

output = type(numOne) # variable reassigment
output = type(numTwo) # variable reassigment
output = type(numThree) # variable reassigment
output= numThree

summation = numOne + numTwo
output = int(summation) # we parse the summation into an integer

#  texts
firstName = "John Doe"
output = firstName
numThree = str(numThree) # parsing into a string
output = type(firstName)
output = type(numThree)

output = firstName[5] # accessing elmeents in a array using index

"""
array[start:stop]
array[start:stop:step]
"""
citeName = "Wikipedia"
output = firstName[1:6] # slicing
output = firstName[5:]
output = citeName[3:7]
output = citeName[1:8:2] # slicing with a step
output = citeName[1:8]

# citeName[0] = 'P' # this returns an exeception as strings are immutable

# string functions
output = citeName.upper()
output = citeName.lower()

# concatenation & interpolation
firstName = "John"

lastName = "Doe"
output = firstName + " " + lastName  
output = "My full names are:"+ " " + firstName + " " + lastName
output = f"My full names are: {firstName} {lastName}"

citeName = "RickNMorty"
output = citeName[-1]
output = citeName[0]

# arrays

fruits = ["apples","mangoes", "bananas", 100, 123, 456] # differing datatypes is not adviced
fruits[-1] ="pineapples"  # reassinging the value of an elment at position -1
fruits[-2]="tomatoe"
fruits[-3]="watermelons"
fruits.append("kiwi")
output = type(fruits)
output = len(fruits) # checks the size of the array
citeName = "eMobilis "
output = len(citeName)

## Boolean => True or False
areLightsOn = True 
isLeftFanOn = False

# dictionary: key-value
student = {
    "name":"John Doe",
    "age":100,
    "course":"Software Engineering", 
    "year":2026,
    0:"zero"
}

# Operator  => comparison operator, boolean operator
"""
Operator: what to subject it to
TYPES: 
    - arithmetic operator: +,-,/,%,//,**
    - assignment operators: +=, =, -=, *=, /=
    - comparison operators: >,<, >=,<=, ==
    - boolean operators: and, or, not
Operand: thing
"""

numOne = 10 
numTwo  = 15

#  arithemtic operations
output =  numOne + numTwo # addition
output =  numOne - numTwo # subraction
output =  numOne * numTwo # multiplication
output =  numOne ** numTwo # power
output =  numOne / numTwo # division
output =  numOne // numTwo # floor - truncates 
output = numOne % numTwo # modulus - returns the remainer

#  assignment operators
output = 10
output +=10 # output = output +10
output -=1
output *=10
output /=5
output **=6

# comparison operators: returns predicate=> returns true or false
output = 10>1
output = 10<1
output = 10>10
output = 10>=10
output = 10<=10
output = 10==10
output= False
output = not output 
output =  not 10==10


# control flows
"""
Control Flows: 
Help us make decisions in code
- if..else
- if..elif..else
- match 
"""

color = "blue"
size = 20
height = 30.57
isComplete = False

#  if..else
if color.upper() == "Blue".upper():
    output = "BLUE"
else:
    output = "not blue!"

height = 30.57

# if..elif..else
if height > 40.1:
    output = "TALL"
elif height >31.51 and height < 40.12:
    output = "MEDIUM"
else:
    output ="SHORT"

#  match case => switch case
x= 11
match x:
    case 10:
        output = "It's 10"
    case 20:
        output = "It's 20"
    case _:
        output = "It's neither 10 nor 20"
#  ternary operator:
x=11
output  = "ten" if x ==10 else "not ten" # ternary operator, do not nest them
output = 10
"""
Functions: 
- sequence of statments that perform a particular task or objective

TYPES:
- Paramterized
- Non-Parameterized
- lambda (anonymous functions)

"""
#  defined a function - non-parameterized 
def greetings():
    print("good afternoon!")

#  call a function
# greetings()
def turnLightsOff():
    isColorBlue = False # local variable => it can only be accessed inside turnLightsOff
    print("Turning lights OFF!!")

output = 10 # global variable
# output = isColorBlue  # this will return an exception since it is locally defined

# parametrized function
def studentGreetings(name): 
    print(f"Welcome to Class {name}!")

studentGreetings("John Doe")
studentGreetings("Jane Doe")

x = lambda y: y + 1 # lambda function
userName = lambda name: name.upper()

output = x(19)
output = userName("Shanize")

output = student["name"]
output = student["age"]

#  loops:


print("=================================================")
print(output)
print("=================================================")

