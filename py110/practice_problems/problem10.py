# Create a function that takes a string of digits as an argument and returns
# the number of even-numbered substrings that can be formed. For example, in
# the case of '1432', the even-numbered substrings are '14', '1432', '4',
# '432', '32', and '2', for a total of 6 substrings.

# If a substring occurs more than once, you should count each occurrence as a
# separate substring.

"""
P
input: a string of digits
output: the number of even substrings that can be formed from the input
rules:
- do no rearrange the digits
- if the same substring occurs more than once, include each as a separate substring

E
'1432' =>
1
14      +1
143
1432    +1
4       +1
43
432     +1
3
32      +1
2       +1

D

A
initialize `count` to 0
- for i in range(0, len(string) + 1)
-- for j in range(i + 1, len(string) + 1)
--- number  = int(string[i:j])
--- if number is even,
---- increment count
return count

"""

def even_substrings(string):
    count = 0
    for i in range(0, len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            number = int(string[i:j])
            if number % 2 == 0:
                count += 1

    return count

# Examples
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
# The above tests should each print True.
