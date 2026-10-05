# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#"tomato" as it in both sets
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#as there are 5 types of item all together across both sets
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
print(fruit.add("banana"))
# Remove an item from vegetables
print(fruit.discard("leek"))
# Find and display symmetric difference of the two sets
both_difference = fruit.symmetric_difference(vegetables)
print(both_difference)