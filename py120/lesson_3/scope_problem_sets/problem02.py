class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed


lucky = Dog('Golden Retriever')
lady = Dog('Poodle')
print(lucky.get_breed())
print(lady.get_breed())
