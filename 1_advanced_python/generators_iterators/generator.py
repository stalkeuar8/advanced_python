class Iter:
    def __init__(self, n):
        self.n = n
        self.current = -1


    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
        return self.current

    def __previous__(self):
        if self.current == 0:
            raise StopIteration("You got start point")
        self.current -= 1
        return self.current

try:
    itr = Iter(5)
    print(itr.__next__())
    print(itr.__next__())
    print(itr.__previous__())
    print(itr.__previous__())
except StopIteration as e:
    print(e)



my_list = [i for i in range(1, 11)]

for i in range(1, 11):
    print(i)

print("\n--------inside----\n")

iterable_obj = iter(my_list)
print(type(my_list))
print(type(iterable_obj))
ny_typ = (1, 2, 3, 4)
print(type(ny_typ))
print(type(iter(ny_typ)))
print(type([i for i in range(1, 11)]))

def gen(n):
    for i in range(n):
        yield n

print(type(gen))
print(id(gen))
print(type(gen(5)))
print(id(gen(5)))

while True:
    try:
        next_item = iterable_obj.__next__()
        print(next_item)
    except StopIteration:
        break


