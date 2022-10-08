#! /usr/bin/env python3

print("\n==============================\n")
print("     Adult BMI Calculator     ")
print("           by azfar")
print("\n==============================\n\n")

w = float(input("Your weight in kg: "))
h = float(input("Your height in cm: "))

def BMI(weight, height):
    a = ((weight/height/height)*10000)
    b = "{:.1f}".format(a)
    print("\nYour BMI value: "+b)
    return b

def print_msg_box(msg, indent=1, width=None, title=None):
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝\n\n'  # lower_border
    print(box)

bmi = float(BMI(w, h))
if bmi < 18.5:
    print_msg_box(msg='\n~ UNDERWEIGHT ~\n', indent=10, title='BMI Category:')

elif bmi >= 18.5 and bmi <= 24.9:
    print_msg_box(msg='\n~ NORMAL WEIGHT ~\n', indent=10, title='BMI Category:')

elif bmi >= 25 and bmi <= 29.9:
    print_msg_box(msg='\n~ OVERWEIGHT ~\n', indent=10, title='BMI Category:')

else:
    print_msg_box(msg='\n~ OBERSITY ~\n', indent=10, title='BMI Category:')
