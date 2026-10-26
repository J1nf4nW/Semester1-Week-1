
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
    Takes an input of a list of numbers and takes the length of the list and also stores the accumulated sum of the list to calculate for the mean value of the list by doing sum/length of list
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 