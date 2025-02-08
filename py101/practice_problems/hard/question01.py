# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Try to answer without running the code or looking at the solution.

# I think this will raise a syntax error

# In actuality, no error is raised, the function merely returns None
