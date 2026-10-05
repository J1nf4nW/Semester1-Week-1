# Worksheet 1.2: Task 1 Solution
import sys
try:
    mark = input("Please enter your mark:")
    mark = int(mark)
    if mark <= 100 and mark >= 70:
        print(f"{mark} is a Distinction")
    elif mark <= 100 and mark >= 40:
        print(f"{mark} is a Pass")
    elif mark <= 100 and mark >= 0:
        print(f"{mark} is a Fail")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")