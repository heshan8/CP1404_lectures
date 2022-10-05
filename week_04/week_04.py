names = ["Bob", "Andy", "Josh", "Mary", "Jack", "John"]
number = int(input(f"Enter number up to {len(names)}: "))
while number != 0:
    try:
        print(names[number - 1])
    except IndexError:
        print("Invalid number")
    number = int(input(f"Enter number up to {len(names)}: "))









