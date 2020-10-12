from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(1, height + 1):
    # first half
    print(" " * (height - (i)), end="")
    print("#" * (i), end="")

    print("  ", end="")

    # second half
    print("#" * (i))