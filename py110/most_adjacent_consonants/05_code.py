# Code with intent

import pdb

def consonant_count(string):
    string = [char for char in string if not char.isspace()]
    max_consonant_count = 0
    adjacent_consonants = ''
    for char in string:
        if char not in 'aeiou':
            adjacent_consonants += char
            if len(adjacent_consonants) > max_consonant_count and len(adjacent_consonants) > 1:
                max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count and len(adjacent_consonants) > 1:
                max_consonant_count = len(adjacent_consonants)
            adjacent_consonants = ''

    return max_consonant_count

def sort_by_consonant_count(string_list):
    string_list.sort(key=consonant_count, reverse=True)
    return string_list


print(consonant_count('dddaa'))       # 3
print(consonant_count('ccaa'))        # 2
print(consonant_count('baa'))         # 0
print(consonant_count('aa'))          # 0
print(consonant_count('rstafgdjecc')) # 4
print(consonant_count('month'))       # 3
print(consonant_count('xxxx'))        # 4
print(consonant_count('salt pan'))    # 3


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
