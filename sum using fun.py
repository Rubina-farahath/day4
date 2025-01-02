def add(y):
    x=20
    c=x+y
    return c
sum=add(20)
print(sum)
print("--------------------------------")
def disp():
    def show():
        print("show function")
    print("display function:")
    show()
disp()