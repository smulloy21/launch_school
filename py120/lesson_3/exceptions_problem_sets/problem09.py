numbers = [1, 2, 3, 4, 5]

def LBYL(lst):
    if len(lst) < 6:
        return None
    return lst[5]

def AFNP(lst):
    try:
        return lst[5]
    except IndexError:
        return None

print(LBYL(numbers))
print(AFNP(numbers))
