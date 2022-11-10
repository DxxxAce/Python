from math import sqrt

__name__ = "utils"
__doc__ = "Requests an input from the user, converts it to a number and displays the output of the process_item function"
__all__ = ["is_prime"]

def is_prime(n: int) -> bool:
    if n <= 1 or n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def process_item(x: int) -> int:
    if x < 2:
        return 2
    elif x % 2 == 0:
        x += 1
    else:
        x += 2
    while not is_prime(x):
        x += 2
    return x

x = int(input("Please enter an unsigned integer: "))
print("The least prime number greater than", x, "is", process_item(x))
