from math import sqrt

# 1.
def fibonacci(n: int):
    if (n <= 0):
        return []
    if (n == 1):
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib

# print(fibonacci(9))


# 2.
def is_prime(n: int):
    if (n <= 1 or n % 2 == 0):
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

def prime_numbers(ls: list):
    return [x for x in ls if is_prime(x)]

# print (prime_numbers([1, 3, 65, 9, 7, 238, 107]))


# 3.
def list_ops(a: list, b: list):
    intersect = [x for x in a if x in b]
    reunion = [x for x in a] +  [x for x in b if x not in a]
    difference1 = [x for x in a if x not in b]
    difference2 = [x for x in b if x not in a]
    return intersect, reunion, difference1, difference2

# print(list_ops([2, 7, 61, 25, 13], [19, 7, 13, 8, 10, 32]))


# 4.
def compose(notes: list, moves: list, start: int):
    if not (len(notes) and len(moves) and start >= 0):
        return []
    song = [notes[start]]
    size = len(notes)
    for x in moves:
        start = (start + x) % size
        song.append(notes[start])
    return song

# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# 5.
def matrix_replace(m):
    return [[0 if i > j else m[i][j] for j in range(len(m[0]))] for i in range(len(m))]

# print(matrix_replace([[1, 4, 5, 12],
#                       [-5, 8, 9, 0],
#                       [-6, 7, 11, 19],
#                       [4, 12, 1, 6]]))


# 6.
def filter_by_count(x: int, *lists):
    full = []
    for list in lists:
        full += list
    return [el for i, el in enumerate(full) if full.count(el) == x and i == full.index(el)]

# print(filter_by_count(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))


# 7.
def palindromes(ls):
    lsp = list(filter(lambda element: str(element) == str(element)[::-1], ls))
    return (len(lsp), max(lsp))

# print(palindromes([12321, 65, 234, 565, 7601067, 124, 1]))


# 8.
def div_chars(strings: list, x = 1, flag = True):
    res = []
    for string in strings:
        res.append([c for i, c in enumerate(string) if ord(c) % x != flag and i == string.index(c)])
    return res

# print(div_chars(["test", "hello", "lab002"], 2, False))


# 9.
def spectators(heights: list):
    res = []
    for col in range(0, len(heights[0])):
        max_height = heights[0][col]
        for row in range(1, len(heights)):
            if heights[row][col] <= max_height:
                res.append((row, col))
            else:
                max_height = heights[row][col]
    return res

# print(spectators([[1, 2, 3, 2, 1, 1],
#                   [2, 4, 4, 3, 7, 2],
#                   [5, 5, 2, 5, 6, 4],
#                   [6, 6, 7, 6, 7, 5]]))


# 10.
def zip_lists(*lists):
    max_size = len(max(lists, key = len))
    for ls in lists:
        while len(ls) < max_size:
            ls += [None]
    return list(zip(*lists))

# print(zip_lists([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"]))


# 11.
def sort_tuples(tuples: list):
    return sorted(tuples, key = lambda t: t[1][2])

# print(sort_tuples([('abc', 'bcd'), ('abc', 'zza')]))


# 12.
def group_by_rhyme(words: list):
    groups = []
    for i in range (len(words)):
        rhyme = list(filter(lambda word: word[-2:] == words[i][-2:], words))
        if rhyme not in groups:
            groups.append(rhyme)
    return groups

# print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
