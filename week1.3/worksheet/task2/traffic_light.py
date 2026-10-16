"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jinfan Wang
"""
states = { "red":4, "red_amber":3, "green":5, "amber":3 }
systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
maxtime += 1
state = "red"
while systime < maxtime:
    if state == "red":
        for i in range(states[state]):
            if systime >= maxtime:
                break
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "red_amber"
    elif state == "red_amber":
        for i in range(states[state]):
            if systime >= maxtime:
                break
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "green"
    elif state == "green":
        for i in range(states[state]):
            if systime >= maxtime:
                break
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "amber"
    elif state == "amber":
        for i in range(states[state]):
            if systime >= maxtime:
                break           
            print(f"Time {systime:03} State {state}")
            systime += 1
        state = "red"
    else:
        print("Please enter a valid integer runtime for the program")
        break
    
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14