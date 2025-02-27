# Modify the function from the previous exercise so it ignores
# non-alphabetic characters when determining whether it should
# uppercase or lowercase each letter. The non-alphabetic characters
# should still be included in the return value; they just don't count
# when toggling the desired case.


'''
P
input: a string
output: the string, with caps toggled on and off for every alpha character

E

D

A
- set a variable upper to True
- for each isalpha() character, append its uppercase if upper is True, else its lowercase to the output string
- toggle the variable upper to its opposite value
- return the output string
'''


def staggered_case(string):
    output = ''
    upper = True
    for char in string:
        if char.isalpha():
            output += char.upper() if upper else char.lower()
            upper = not upper
        else:
            output += char
    return output


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
