# Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Compute and display the total age of the family's male members. Try
# working out the answer two ways: first with an ordinary loop, then
# with a comprehension.

# The result should be 444.

total_male_age = 0
for data in munsters.values():
    if data['gender'] == 'male':
        total_male_age += data['age']
print(total_male_age) # 444

total_male_age = sum([data['age'] for data in munsters.values()
                      if data['gender'] == 'male'])
print(total_male_age) # 444
