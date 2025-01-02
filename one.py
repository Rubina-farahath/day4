def display(n):
    print("I 'm the function one")
    n()
def one():
    print(" i am first nested fun:")
def two():
    print("i am second nested function:")
display(one)
display(two)