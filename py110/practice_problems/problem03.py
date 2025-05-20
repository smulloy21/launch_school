# Create a function that takes a string argument and returns a copy of the
# string with every second character in every third word converted to
# uppercase. Other characters should remain the same.

"""
P
input: a string
output: a copy of that string with every second character in every thrid word converted to uppercase
rules:
- other characters should remain the same case as in the original

E

D

A
- split the sentence into a list of words
- for every third word in the list, replace the element in the list with the weird_word version (HELPER)

- HELPER weird_word takes a word and converts every 2nd character to uppercase

"""

def to_weird_case(sentence):
    return ' '.join([weird_word(word) if (idx + 1) % 3 == 0 else word for idx, word in enumerate(sentence.split())])

def weird_word(word):
    return ''.join([char.upper() if (idx + 1) % 2 == 0 else char for idx, char in enumerate(word)])


# Examples
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
# The above tests should each print True.
