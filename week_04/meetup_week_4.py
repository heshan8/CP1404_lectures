def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)


def get_numbers():
    user_input = input("Enter numbers seperated by commas: ").split(",")
    return [float(items) for items in user_input]


def square_numbers(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2


def display_numbers(numbers):
    print("..".join([str(number) for number in sorted(numbers)]))


main()
