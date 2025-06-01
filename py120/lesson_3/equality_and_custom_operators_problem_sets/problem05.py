class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    # def __add__(self, other):
    #     if ((isinstance(self.value, int) or self.value.isnumeric())
    #        and (isinstance(other, int) or other.isnumeric())):
    #         return Silly(int(self.value) + int(other))
    #     else:
    #         return Silly(str(self.value) + str(other))

    def __add__(self, other):
        try:
            int(self.value)
            int(other)
        except ValueError:
            return Silly(str(self.value) + str(other))
        else:
            return Silly(int(self.value) + int(other))


print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Sillyß('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)
