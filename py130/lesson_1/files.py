file = open('example.txt', 'r')
content = file.read()
file.close()

print(repr(content))
# 'Running dog\nSleeping cat\nSwimming fish\nSinging bird\n'
