#! /usr/bin/env python3

from msgBox import *

border_msg("     Adult BMI Calculator     ")

w = float(input("Your weight in kg: "))
h = float(input("Your height in cm: "))

def BMI(weight, height):
    a = ((weight/height/height)*10000)
    b = "{:.1f}".format(a)
    print("\nYour BMI value: "+b)
    return b

bmi = float(BMI(w, h))
if bmi < 18.5:
    print_msg_box(msg='\n~ UNDERWEIGHT ~\n', indent=10, title='BMI Category:')

elif bmi >= 18.5 and bmi <= 24.9:
    print_msg_box(msg='\n~ NORMAL WEIGHT ~\n', indent=10, title='BMI Category:')

elif bmi >= 25 and bmi <= 29.9:
    print_msg_box(msg='\n~ OVERWEIGHT ~\n', indent=10, title='BMI Category:')

else:
    print_msg_box(msg='\n~ OBERSITY ~\n', indent=10, title='BMI Category:')
