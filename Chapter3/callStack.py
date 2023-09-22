# Example of how the call stack works in python

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye")
    bye()

def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("ok bye!")

greet("Goku")