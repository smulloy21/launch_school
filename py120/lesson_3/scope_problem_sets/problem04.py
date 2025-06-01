# Create an instance of the Dog class from your answer to Problem 2. Set its
# breed directly from outside the class, then print the resulting breed.

class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed


lucky = Dog('Golden Retriever')
lucky._breed = 'Lab'
print(lucky.get_breed()) # Lab
