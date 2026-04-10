
output = ""
output = userName

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

#  oop

print("=================================================")
print(output)
print("=================================================")

