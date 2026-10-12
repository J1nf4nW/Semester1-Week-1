# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}
keys = []
values = []
for c, r in rivers.items():
    print(c,r)
# loop through the dict extracting key and value
while rivers:
    c, r = rivers.popitem() 
    keys.append(c)
    values.append(r)
print(keys)
print(values)


# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session