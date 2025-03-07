# Write a function that takes a string as an argument and returns that
# string with every occurrence of a "number word" -- 'zero', 'one',
# 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' --
# converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.


'''
P
input: a string of one or more words
output: the string, with any 'number words' converted to integers (e.g. 'five' => '5')

E

D

A
- create a map of all number word digits to string digits
- split the input string into a list of words
- for each word in the list, if the word is in the number word dict, replace it with its digit value
- concatenate the string back to a space-separated sentence
'''

map = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

def word_to_digit(message):
    word_list = message.split()
    for idx, word in enumerate(word_list):
        if word in map:
            word_list[idx] = map[word]
    return ' '.join(word_list)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
