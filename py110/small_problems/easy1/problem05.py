# Write a function that takes a string consisting of zero or more
# space-separated words and returns a dictionary that shows the number
# of words of different sizes.

# Words consist of any sequence of non-space characters.

'''
P
input: a string of zero or more space-separated words
output: a dictionary that shows the number of words of different sizes
rules:
    explicit:
        - there may be zero words in the string
    implicit:
        - punctuation should be included as characters in a word

E

D

A
- initialize an empty dict
- split the input string into a list of words
- for each word, if its length is in the dictionary, increase the count, otherwise
add a count of 1
return the dictionary
'''

def word_sizes(string):
    count = {}

    for word in string.split():
        length = len(word)
        if count.get(length):
            count[length] += 1
        else:
            count[length] = 1

    return count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
