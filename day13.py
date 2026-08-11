'''
#Text case convertor
text = input("Enter a sentence: ")

methods = ["upper", "lower", "title", "capitalize", "swapcase"]

for method in methods:
    if method == "upper":
        print("Upper:", text.upper())
    elif method == "lower":
        print("Lower:", text.lower())
    elif method == "title":
        print("Title:", text.title())
    elif method == "capitalize":
        print("Capitalize:", text.capitalize())
    elif method == "swapcase":
        print("Swapcase:", text.swapcase())
'''
'''
while True:
    user_name = input("Enter username: ")

    if user_name == "quit":
        break

    if user_name.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Contains other characters")

    if user_name[0].isalpha():
        print("Starts with a letter")
    else:
        print("Does not start with a letter")

    if user_name.isidentifier():
        print("Valid Python identifier")
    else:
        print("Invalid Python identifier")

    if user_name.isascii():
        print("Contains ASCII characters")
    else:
        print("Contains non-ASCII characters")
'''
'''
# 3. Student Report

print("STUDENT REPORT".center(30))

for count in range(3):
    student_name = input("Name: ")
    student_marks = int(input("Marks: "))

    if student_marks >= 80:
        student_grade = "A"
    elif student_marks >= 60:
        student_grade = "B"
    elif student_marks >= 40:
        student_grade = "C"
    else:
        student_grade = "Fail"

    print(f"{student_name.ljust(10)} {str(student_marks).rjust(5)} {student_grade.rjust(5)}")



'''
# 4. Character and Text Analyzer

input_text = input("Enter text: ")

letter_count = 0
digit_count = 0
space_count = 0
printable_count = 0

for character in input_text:
    if character.isalpha():
        letter_count = letter_count + 1

    if character.isdigit():
        digit_count = digit_count + 1

    if character.isspace():
        space_count = space_count + 1

    if character.isprintable():
        printable_count = printable_count + 1

print("Letters:", letter_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Printable:", printable_count)
print("Lowercase:", input_text.islower())
print("Uppercase:", input_text.isupper())
print("Title:", input_text.istitle())




















        
