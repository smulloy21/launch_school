# Without running the following code, can you determine what the following
# code will do? Explain why you will get those results.


import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

# it will print 'You will ' and then a random one of the list returned by `choices`
