'''correct_code = "6301"

while True:
    code = input("Enter secret code: ")

    if code == correct_code:
        print("Correct")
        break
    else:
        print("Wrong")
 '''
'''
# fixed OTP for testing
otp = 1234
attempts = 0
while attempts < 7:
    if int(input("Enter OTP: ")) == otp:
        print("Verified")
        break
    attempts += 1
    print(f"Wrong. {7-attempts} left")
else:
    print("Blocked")
    '''
'''
food = input()
count = 0
while food!="Exit":
    count+=1
    food = input()
print("Total number of items ordered",count)
'''
secret = "python"
current = 0
max_attempts = 3
while current < max_attempts:
    a = input()
    if (a == secret):
        print("access again")
        break
    else:
        remaining = max_attempts-current
        print(f"wrong guess & you have only")
        current+=1
else:
    print("chance over")
              
    
