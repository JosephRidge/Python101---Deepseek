
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