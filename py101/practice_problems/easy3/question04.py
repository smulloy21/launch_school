# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # [{"first": 42}, {"second": "value2"}, 3, 4, 5]

# the copy is a shallow copy, so if a nested mutable object is mutated,
# it affects both lists
