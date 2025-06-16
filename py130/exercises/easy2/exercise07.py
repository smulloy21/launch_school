# Unpack values from a tuple of four elements, but only keep the first and
# last values.

data = (100, 200, 300, 400)
first, *_, last = data

print(first, last) # 100 400
print(_) # [200, 300]
