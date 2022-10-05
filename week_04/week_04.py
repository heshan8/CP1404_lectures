names = ["Bob", "Andy", "Josh", "Mary", "Jack", "John"]
number = int(input(f"Enter number up to {len(names)}: "))
try:
    print(names[number - 1])
except IndexError:
    print("Invalid number")










