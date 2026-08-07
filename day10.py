'''
#task -->write a python program to calculate the innings of a batman and count the boundaries,total score using for loop 
runs = [4, 6, 1, 0, 2, 4, 0, 6]

total = 0
fours = 0
sixes = 0
dots = 0

for i in runs:
    total += i

    if i == 4:
        fours += 1
    elif i == 6:
        sixes += 1
    elif i == 0:
        dots += 1

print("Total Score:", total)
print("Number of Fours:", fours)
print("Number of Sixes:", sixes)
print("Dot Balls:", dots)
'''
'''
#Task 2 --> ATM
pin = input ("enter the number: ")
max_attempts = 5
current_attempt = 0
while current_attempt <=max_attempts:
    entered_pin = input("enter the atm pin ")
    if entered_pin == pin:
        print("logic sucessful")
        break
    else:
        print(" entered is wrong....try again carefully")
        current_attempt +=1
else:
    print("account locked, try after 24 hours")
    '''


correct_pin = "1234"

for i in range(3):
    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Wrong PIN")

else:
    print("ATM Card Blocked")








































