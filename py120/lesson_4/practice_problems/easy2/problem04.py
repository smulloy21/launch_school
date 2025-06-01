# Suppose we have this code:

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Without running the above code, what would each snippet do were you to run
# it?

# Snippet 1
hello = Hello()
hello.hi() # Hello
# Snippet 2
hello = Hello()
hello.bye() # AttributeError
# Snippet 3
hello = Hello()
hello.greet() # TypeError Missing argument 'message'
# Snippet 4
hello = Hello()
hello.greet('Goodbye') # Goodbye
# Snippet 5
Hello.hi() # TypeError missing argument 'self'
# ^ When we invoke instance methods as class methods, no instance is passed in
# as self.
