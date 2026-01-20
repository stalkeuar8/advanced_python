











class Countdown:
    def __init__(self, start_from):
        self.start_from = start_from
        self.current = self.start_from

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.start_from:
            self.current -= 1
            return self.start_from
        if not self.current <= 0:
            self.current -= 1
            return self.current
        else:
            raise StopIteration


class EvenNums:
    def __init__(self, n):
        self.n = n
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current == self.n:
            self.current += 1
            return self.current**2
        else:
            raise StopIteration














def number_divisible_by(n, divisor):
    for i in range(1, n+1):
        if not i%divisor:
            yield i


def repeat_string(s, n):
    for _ in range(n):
        yield s


def zip_lists(list1, list2):
    list1_itr = iter(list1)
    list2_itr = iter(list2)
    for i in range(len(list1)):
        yield next(list1_itr), next(list2_itr)

def power_of_two(n):
    for i in range(n):
        yield 2**i




def count_up_to(n):
    for i in range(1, n+1):
        yield i

# for num in count_up_to(10):
#     print(num)

def even_numbers(n):
    for i in range(1, n+1):
        if not i%2:
            yield i

# print(list(even_numbers(10)))

def squares(n):
    for i in range(1, n+1):
        yield i**2

# print(list(squares(6)))

def countdown(n):
    for i in range(n, 0, -1):
        yield i

# for num in countdown(10):
#     print(num)






class FibonacciGenerator:
    def __init__(self, n=None):
        if n is None:
            self.is_endless = True
        else:
            self.n = n
            self.is_endless = False
        self.current = -1
        self.currents_list = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_endless:
            pass
        else:
            if self.current < self.n:
                pass
            else:
                raise StopIteration

        if self.current == -1 or self.current == 0:
            self.current += 1
        else:
            self.current = self.currents_list[0] + self.currents_list[1]
            if not self.is_endless and self.current > self.n:
                self.current = self.currents_list[0]
                raise StopIteration
        self.currents_list.insert(0, self.current)
        return self.current

def fibo_gen(n):
    a = 0
    b = 1
    for i in range(n):
        current = a
        yield current
        a, b = b, a + b

print(list(fibo_gen(10)))

# try:
#     fibo_gen = FibonacciGenerator()
#     fibo_iter = iter(fibo_gen)
#     for n in fibo_gen:
#         print(n)
# except StopIteration as e:
#     print(e)