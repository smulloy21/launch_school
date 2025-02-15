# What would be the output of the below code? Try to answer without running the code.

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# We get an error, because you cannot add to a fozenset, they are immutable.
# AttributeError: 'frozenset' object has no attribute 'add'
