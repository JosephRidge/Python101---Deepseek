
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

# tuples => immutable list of items, defined inside ()
colors = ("blue", "green", "red")