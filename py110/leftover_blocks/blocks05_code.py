# Code

"""
Based on all of your notes and analysis so far, implement a working
solution in Python. Your solution should pass all of the test cases
provided.
"""

def calculate_leftover_blocks(total_blocks):
    building_blocks = []
    layer = 0
    while sum(building_blocks) < total_blocks:
        layer += 1
        building_blocks.append(layer**2)
        if sum(building_blocks) > total_blocks:
            building_blocks.pop()
            break

    return total_blocks - sum(building_blocks)


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
