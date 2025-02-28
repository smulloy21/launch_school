# A developer is trying to remove duplicates from a list. They use a
# set for deduplication, but the order of elements is lost. How can we
# preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
seen = set()
unique_data = [num for num in data if not (num in seen or seen.add(num))]
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
