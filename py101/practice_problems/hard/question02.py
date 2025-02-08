# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list) # [1, 2]
print(dictionary) # {'first': [1, 2]}

# Try to answer without running the code or looking at the solution.

# line 5 does indeed mutate the list that dictionary references

# We can initialize num_list with a reference to a copy of the original list:

dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# We can use list slicing which returns a new list:

dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)
