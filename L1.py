import math
import re


# 1.
def greatestCommonDivisor():
    numbers = input("Please enter some numbers:\n")
    arr = []

    for x in numbers.split(" "):
        arr.append(int(x))

    if len(arr) == 0:
        return "undefined"
    elif len(arr) == 1:
        return arr[0]
    else:
        div = math.gcd(arr[0], arr[1])

        for i in range(2, len(arr)):
            div = math.gcd(div, arr[i])

        return div


# print(greatestCommonDivisor())

# 2.
def isVowel(c):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    if c in vowels:
        return True

    return False


def countVowels(string):
    count = 0

    for c in string:
        if isVowel(c):
            count += 1

    return count


# print(countVowels("asdsEupqoRni"))

# 3.
def countOccurences(substring, string):
    return string.count(substring)


# print(countOccurences("Mihnea", "Mihnea si cu Mihnea au mers acasa la Mihnea sa il manance pe Mihnea"))

# 4.
def camelToUnderscore(string):
    if len(string) == 0:
        return ""

    string = string[0].lower() + string[1:]

    for i in range(1, len(string)):
        if string[i].isupper():
            string = string[:i] + '_' + string[i].lower() + string[i + 1:]

    return string


# print(camelToUnderscore("UpperCamelCaseToLowerCaseWithUnderscores"))

# 5.
def spiralOrder(matrix):
    if len(matrix) == 0:
        return ""

    result = ""
    size = len(matrix)
    visited = [[0 for i in range(size)] for j in range(size)]
    rowShift = [0, 1, 0, -1]
    colShift = [1, 0, -1, 0]
    row = 0
    col = 0
    shift = 0

    for i in range(size * size):
        result += matrix[row][col]
        visited[row][col] = True
        currentRow = row + rowShift[shift]
        currentCol = col + colShift[shift]

        if 0 <= currentRow and currentRow < size and 0 <= currentCol and currentCol < size and not (
        visited[currentRow][currentCol]):
            row = currentRow
            col = currentCol
        else:
            shift = (shift + 1) % 4
            row += rowShift[shift]
            col += colShift[shift]

    return result


# m = [['f', 'i', 'r', 's'],
#      ['n', '_', 'l', 't'],
#      ['o', 'b', 'a', '_'],
#      ['h', 't', 'y', 'p']]
#
# print(spiralOrder(m))

# 6.
def validatePalindrome(n):
    string = str(n)
    return string == string[::-1]


# print(validatePalindrome(18781))

# 7.
def firstNumber(string):
    match = re.search(r'\d+', string)

    if match:
        return match.group()

    return "none"


# print(firstNumber("asdwadsa123sads54dazd90dasd"))
# print(firstNumber("sfasfmhajfkasnfbajbfa"))

# 8.
def countPositiveBits(n):
    bits = bin(n)
    print(bits)
    return bits.count('1')


# print(countPositiveBits(24))

# 9.
def mostFrequentLetter(string):
    auxString = string.lower()
    frequency = {}

    for c in auxString:
        if c >= 'a' and c <= 'z':
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1

    return max(frequency, key=frequency.get())


# print(mostFrequentLetter("An apple is not a tomato!"))

# 10.
def countWords(string):
    return string.count(' ') + 1

# print(countWords("I have Python exam"))
