class Foo:
    pass

foo = Foo()

print(f'I am a {type(foo).__name__} object.')
print(f'I am a {foo.__class__.__name__} object.')
