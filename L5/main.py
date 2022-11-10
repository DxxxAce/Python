import numpy as np
# import app

# 2.
def sum(*args: int, **kwargs: int) -> int:
    return np.sum([x for x in kwargs.values()])

l_sum = lambda *args, **kwargs: sum(*args, **kwargs)

# print(l_sum(1, 2, c = 3, d = 4))


# 3.
def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u']

def vowels(string: str) -> list:
    string = string.lower()
    found = []
    found += [c for c in string if is_vowel(c)]
    return found

l_vowels = lambda string: vowels(string)

def filter_vowels(string: str) -> list:
    string = string.lower()
    return [x for x in filter(lambda c: is_vowel(c), string)]

# print(filter_vowels("Programming in Python is fun"))


# 4.
def validate_dict(d: dict) -> bool:
    if len(d) < 2:
        return False
    for el in d.keys():
        if type(el) == str and len(el) >= 3:
            return True
    return False

def dict_arguments(*args: any, **kwargs: any) -> list:
    dicts = []
    dicts += [d for d in args if type(d) == dict and validate_dict(d)]
    dicts += [d for d in kwargs.values() if type(d) == dict and validate_dict(d)]
    return dicts

# print(dict_arguments({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3},
#                      [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
#                      dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#                      test={1: 1, 'test': True}))


# 5.
def numbers(l: list) -> list:
    return [x for x in filter(lambda el: type(el) in [int, float, complex], l)]

# print(numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))


# 6.
def even_odd_pairs(l: list) -> list:
    evens = [x for x in l if x % 2 == 0]
    odds = [y for y in l if y % 2 == 1]
    return [t for t in zip(evens, odds)]

# print(even_odd_pairs([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))


# 7.
def fibonacci(n: int) -> list:
    if (n <= 0):
        return []
    if (n == 1):
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

def sum_digits(x: int) -> int:
    return sum(map(int, str(x)))

def process(**kwargs) -> list:
    fib = fibonacci(1000)
    if "filters" in kwargs.keys():
        for f in kwargs["filters"]:
            fib = [x for x in filter(f, fib)]
    if "limit" in kwargs.keys():
        fib = fib[:kwargs["limit"]]
    if "offset" in kwargs.keys():
        fib = fib[kwargs["offset"]:]
    return fib

print(process(filters = [lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
              limit = 2, offset = 2))


# 9.
def generate_dicts(pairs: list) -> list:
    return [{"sum": np.sum(pair), "prod": np.prod(pair), "pow": pair[0] ** pair[1]} for pair in pairs]

# print(generate_dicts(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))