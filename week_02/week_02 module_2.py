# Do this now #1
# # import random
# # length = int(input("Enter Length: "))
# # while length > 0:
# #     width = random.randint(1, length)
# #     area = length * width
# #     print(f"Area of {length} x {width} is {area}")
# #     length = int(input("Enter Length: "))
#
# Do this now #2
#
# # def print_grid(number_of_rows, number_of_columns):
# #     print(f"{'*' * number_of_columns}\n" * number_of_rows)
# #
# #
# # print_grid(3, 7)
#
# """Do this now #3"""

import random

menu = """ - (G) get valid (non empty name)
 - (P) print greeting with lines
 - (S) print secret name (random variation)
 - (Q) Quit """


def main():
    name = ""
    print(menu)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid Choice: ")
        print(menu)
        choice = input(">").upper()
    print("Good Bye!")


def get_valid_name():
    name = input("Enter name: ")
    while name == "":
        print("Invalid name")
        name = input("Enter name: ")
    return name


def print_line(length):
    print("-" * length)


def print_greeting(name):
    length = len(name)
    print_line(length)
    print(name)
    print_line(length)


def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


main()

# do this now 4

# 1. determine_subject_grade
# 2. convert_currency
# 3. print_report
# 4. calculate_average
# 5. calculate_even_number
# 6. get_age
