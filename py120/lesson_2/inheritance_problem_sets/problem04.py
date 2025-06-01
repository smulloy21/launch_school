# What is the method resolution order and why is it important?

# The method resolution order (MRO) is the order in which Python traverses
# the class hierarchy to look for methods. It is important because if you
# want to make sure your objects behave as expected, so you want make sure
# your overrides, if any, are in the right place, or conversely that you
# are not overriding methods where you do not want to be.
