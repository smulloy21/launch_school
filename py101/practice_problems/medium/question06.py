# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) # 34

# 34. The mess_with_it function does not mutate the global variable answer.
