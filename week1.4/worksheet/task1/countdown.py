
def countdown(number): 
    if number > 0:
        for i in range (number+1):
            print(number)
            number -= 1
    else:
        print(f"{number} is an invalid input")
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
number = int(input("Enter a positive integer number:"))
countdown(number)