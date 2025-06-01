# Define a Dog class that has a breed instance variable. Instantiate two
# objects from this class, one with the breed 'Golden Retriever' and another
# with the breed 'Poodle'. Print the breed of each dog.

class Dog:
    def __init__(self, breed):
        self.breed = breed


lucky = Dog('Golden Retriever')
lady = Dog('Poodle')
print(lucky.breed)
print(lady.breed)
