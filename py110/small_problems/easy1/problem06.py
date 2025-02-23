# Modify the word_sizes function from the previous exercise to exclude
# non-letters when determining word size. For instance, the word size
# of "it's" is 3, not 4.

'''
P
input: a string of zero or more space separated words
output: a dictionary with the count of different word lengths in the string
rules:
    - same as before, but now ignore non-alphanumeric characters
E
D
A
- initialize a dictionary of word length counts
- convert the string into a list of words, with only alphanumeric characters
- for each word in the list, add its length to the dictionary if not present,
then increase its count by 1
- return the dictionary of word length counts
'''

def word_sizes(string):
    counts = {}
    string = ''.join(char for char in string
                     if char.isalnum() or char.isspace())
    for word in string.split():
        length = len(word)
        if length not in counts:
            counts[length] = 0
        counts[length] += 1

    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
