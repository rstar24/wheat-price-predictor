# anonymous functions 
# it is one of the cool features 
# of python
def create_adder(x):
    def adder(y):
        return x+y
    return adder

f = (lambda x : x > 2) (3)
print(f)
ff=(lambda x,y : x**2 + y**2 )(2,1)
print(ff)



add_10 = create_adder(10)
print(add_10)
print(add_10(3))


list(map(add_10,[1,2,3]))
list1 = list(map(max,[1,2,3,4],[5,6,7,8]))

for i in list1:
    print(list1[1])

dict1 = {x : x**2 for x in range(1,6)}
print(dict1)

list2 = list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))

for i in range(len(list2)):
    print(list2[i])