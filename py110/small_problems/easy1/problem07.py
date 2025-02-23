# Given a string of words separated by spaces, write a function that
# swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that
# the string will always contain at least one word. You may also assume
# that each string contains nothing but words and spaces, and that
# there are no leading, trailing, or repeated spaces.


'''
P
input: a string of words separated by spaces
output: a string of words separated by spaces, with each first and last letter swapped
rules:
    explicit:
        - the returned string should contain all the same words, just modified
        - don't need to worry about an empty string or non alpha and space characters
        - don't need to worry about leading, trailing or repeated spaces
    implicit:
        - all cases should remain the same

E
swap('Abcde') == "ebcdA"

D
A
- split the string into a list of words
- for each word in the string, modify so the word is its last letter,
the middle of the word, then its first letter
- return the joined string of the new words
'''

def swap(string):
    words = string.split()

    for idx, word in enumerate(words):
        if len(word) > 1:
            words[idx] = word[-1] + word[1:-1] + word[0]

    return ' '.join(words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
