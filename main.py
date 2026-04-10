
output = ""
output = userName

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

#  oop

print("=================================================")
print(output)
print("=================================================")

