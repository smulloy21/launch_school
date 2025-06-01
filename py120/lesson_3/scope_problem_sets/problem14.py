class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# Without running this code, what will happen if you were to run it? Why?

# it will raise an AttributeError because var_a is never initialized for an instance
# of class B - B's __init__ class overwrites A's, which is where it would have been
# initialized
