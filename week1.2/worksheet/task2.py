# Worksheet 1.2: Task 2 Solution
# Prompts the user to input a sequence of float values
# Reads these values into a list, using code that we have provided
# Finds the minimum, maximum, mean and median of these values
# Prints each statistic on a separate line
import sys
def read_numbers():
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

def mean():
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    print(f"Mean = {mean}")

def median():
    n = len(numbers)
    numbers.sort()

    if n % 2 == 0:
        med1 = numbers[n // 2]
        med2 = numbers[n // 2 - 1]
        median = (med1 + med2) / 2
    else:
        median = numbers[n // 2]

    print(f"Median = {median}")

def minimum():
    minimum = min(numbers)
    print(f"Minimum = {minimum}")

def maximum():
    maximum = max(numbers)
    print(f"Maximum = {maximum}")

try:
    numbers = read_numbers()
    numbers.sort()
    if len(numbers) != 0:
        minimum()
        maximum()
        mean()
        median()
    else:
        sys.exit("Error: no numbers provided")
except:
    sys.exit("Please check your values are either float or integer values in the list")