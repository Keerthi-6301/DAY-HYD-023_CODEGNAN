'''products = list(map(int,input().split(',')))
total= 0
for i in products:
    total+= i

print(total)
'''
'''
password = input("Enter password: ")

upper = lower = digit = special = 0

for ch in password:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special Characters:", special)+
'''
'''
email = input().split()
for mail in email:
    print(mail.split("@")[1])
'''

for i in range(1,6):
    movie = input("Enter movie name:")
    print(i, ".",movie)









