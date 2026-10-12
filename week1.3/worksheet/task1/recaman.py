# Worksheet 1.3: Task 1
L = int(input("Length of sequence: ")) # this should be your only input

sequence = [0]
#let ak-1 be called preceding

for k in range(1, L):
    preceding = sequence[-1]
    ak = preceding - k

    if ak > 0 and ak not in sequence:
        sequence.append(ak)
    else:
        sequence.append(preceding + k)
print(sequence)
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

# ak = (ak-1) – k     if   (ak-1) – k > 0 , and this number is not already in the sequence 
#ak = (ak-1) + k     otherwise 

# You may wish to use further output for testing purposes while you develop your code

#[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence