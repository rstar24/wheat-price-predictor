# THis is a local funtion
# int python
x1 = 5

def set_x(num):
    x = num
    print(f"This is the number {x}")
    print(f"I am a global variable {x1}")

set_x(10)
# This is a global function in the python

def set_global_x(num):
    global x 
    x1 = num
    print(num)
    x1 = x1 + 1
    print(x1)

set_global_x(100)

# python has a feature called the first class function
def create_adder(x):
    def adder(y):
        print("Something from here")
        return x+y
    print("some thing from here")
    return adder

f = 15
g = 16
add1 =  create_adder(f)
fg = add1(1)
ffg = "its true " if (fg == g) else "No I am thinking different"
print(ffg)





