def generator():
    for num in range(1, 6):
        yield num

for num in generator():
    print(num)
# 1
# 2
# 3
# 4
# 5
