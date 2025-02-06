# Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and "
# prepended to the front of the string referenced by famous_words.

print(f'Four score and {famous_words}')
print('Four score and {famous_words}'.format(famous_words=famous_words))
