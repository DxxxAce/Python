# 1. Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)

def lists_to_sets(a: list, b: list):
    sa = set(a)
    sb = set(b)
    return [sa & sb, sa | sb, sa - sb, sb - sa]

# print(lists_to_sets([14, 9, 'set', 25, 8], ['set', 137, 25, 'list', 0]))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys
# are the characters in the character string and the values are the number of occurrences of that
# character in the given text.

def count_occurences(string: str):
    count = dict()
    for c in string:
        if c not in count:
            count[c] = string.count(c)
    return count

# print(count_occurences("Ana are mere multe"))


# 3. Compare two dictionaries without using the operator "==" returning True or False. Attention, dictionaries
# must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.

def comp_dictionaries(a, b):
    if type(a) != type(b):
        return False
    enumerables = [list, tuple, set, dict]
    if type(a) in enumerables:
        if len(a) != len(b):
            return False
        pairs = zip(a, b)
        for (x, y) in pairs:
            if not comp_dictionaries(x, y):
                return False
        if type(a) == dict:
            pairs = zip(a.values(), b.values())
            for (x, y) in pairs:
                if not comp_dictionaries(x, y):
                    return False
    return a == b

# print(comp_dictionaries({"A":1, "B":2, "C":{1:"misu", 2:"gicu"}, "D":6},
#                         {"A":1, "B":2, "C":{1:"misu", 2:"fanel"}, "D":7}))


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value
# elements given as name-parameters. Build and return a string that represents the corresponding XML element.

def build_xml_element(tag: str, content: str, **props):
    result = '<' + tag
    for prop, value in props.items():
        result += ' ' + prop + '=\"' + value + '\"'
    result += '>' + content + '<\\' + tag + '>'
    return result

# print(build_xml_element ("a", "Hello there", href = "http://python.org", _class = "my-link", id = "someid"))


# 5. The validate_dict function that receives as a parameter a set of tuples (that represents validation rules
# for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows:
# (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle"
# is inside the value (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.

def validate_dict(s: set, d: dict):
    for rule in s:
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        sufix = rule[3]
        if not (key in d.keys()
                and d[key].startswith(prefix)
                and middle in d[key][1:-1]
                and d[key].endswith(sufix)):
            return False
    return True

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(validate_dict(s, d))


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# a representing the number of unique elements in the list, and b representing the number
# of duplicate elements in the list (use sets to achieve this objective).

def uniques_and_duplicates(ls: list):
    s = set(ls)
    return (len(s), len(ls) - len(s))

# print(uniques_and_duplicates([1, 2, 3, 1, 'u', 6, 3, 'u', 5, 1, 9]))


# 7. Write a function that receives a variable number of sets and returns a dictionary
# with the following operations from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets, and op is the
# applied operator: |, &, -.

def set_ops(*sets):
    d = dict()
    for i, s1 in enumerate(sets):
        for j, s2 in enumerate(sets[i + 1:]):
            d[f"{s1} | {s2}"] = s1 | s2
            d[f"{s1} & {s2}"] = s1 & s2
            d[f"{s1} - {s2}"] = s1 - s2
            d[f"{s2} - {s1}"] = s2 - s1
    return d

# print(set_ops({1,2}, {2, 3}, {1,3,7}))


# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains
# a string key "start". Starting with the value of this key you must obtain a list of objects by iterating
# over mapping in the following way: the value of the current key is the key for the next value, until you
# find a loop (a key that was visited before). The function must return the list of objects obtained as
# previously described.

def loop(mapping: dict):
    key = mapping['start']
    res = list()
    while key not in res:
        res += key
        key = mapping[key]
    return res

# print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments and will return the number of positional arguments whose values can be found among keyword arguments values.

def my_function(*args, **kwargs):
    count = 0
    for arg in args:
        count += 1 if arg in kwargs.values() else 0
    return count

# print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
