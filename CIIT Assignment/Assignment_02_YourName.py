#Assignment Task: Student Scholarship Eligibility Checker
#Create a Python program that checks whether a student is eligible for 
# a scholarship based on their examination marks.


from unicodedata import name


print("-------Scholarship Eligibility Checker-------")

name = input("Enter your Full name: ")
marks = int(input("Enter your marks: "))
print("" \
"" \
"")




print("------Student Result-----")
print("Name: ", name)
print("Marks: ", marks)
print("Result: ", end="")

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 80:
    print("Full Scholarship")
elif marks >= 70:
    print("Partial Scholarship")
elif marks >= 40:
    print("Passed - No Scholarship")
else:
    print("Failed - No Scholarship")