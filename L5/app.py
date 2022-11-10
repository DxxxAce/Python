from utils import process_item

__name__ = "app"
__doc__ = "Runs in an infinite loop, waiting for inputs from the user until meeting the character \'q\', " \
          "converts the input to a number and processes it using the function process_item implented in utils.py"

x = input("Please enter an unsigned integer: ")

while x != "q":
    n = int(x)
    print("The least prime number greater than", n, "is", process_item(n))
    x = input("Please enter an unsigned integer: ")