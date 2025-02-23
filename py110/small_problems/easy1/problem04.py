# Write a function that takes a list of numbers and returns a list with
# the same number of elements, but with each element's value being the
# running total from the original list.

'''
P
input: a list of integers
output: a list of integers, the 'running total' of the sum so far
rules:
    explicit:
        - the integers in the output list should be the running total
        from the original list
        -
    implicit:
        - an empty list should return an empty list
        - the input list contains variable amount of integers
        - the input list contains only valid integers

E

D/A
- initialize an empty list
- iterate over the input list and
    - for each number, append the sum of it and the last item in the new list to the new list
- return the new list
'''


def running_total(nums):
    sums = []
    for num in nums:
        sums.append(num + sums[-1] if len(sums) > 0 else num)
    return sums


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
