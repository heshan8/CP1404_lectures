"""
demo
"""

# monthly_cost = float(input("Monthly cost of Streaming service: "))
# yearly_cost = monthly_cost * 12
# print(f"Yearly cost is ${yearly_cost:.2f}")

# gross_pay = float(input("Gross pay:"))
# tax_rate = float(input("Tax rate:"))
# tax_amount = gross_pay * tax_rate
# net_pay = gross_pay - tax_amount
# print(f"Your net pay is ${net_pay}")


# age = int(input("Enter Age:"))
# if age < 5:
#     category = "Baby"
# elif age < 18:
#     category = "Child"
# elif age < 26:
#     category = "Young adult"
# elif age < 66:
#     category = "Adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")

# secret = 8
# guess = int(input("Guess the secret number between 1-10:"))
# while guess != secret:
#     print("Try again!:")
#     guess = int(input("? "))
# print("nice one")

# age = int(input("Enter Age:"))
# while age < 0 or age > 120:  # while the input is bad
#     print("Please enter a valid age")
#     age = int(input("Enter Age:"))
# if age < 5:
#     category = "Baby"
# elif age < 18:
#     category = "Child"
# elif age < 26:
#     category = "Young adult"
# elif age < 66:
#     category = "Adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")

# name = ""
# name = str(input("Enter name:"))
# while name == "":  # while the input is bad
#     print("Please enter a name")
#     name = str(input("Enter name:"))
# print(f"Hello {name}")

# total = 0
# age_count = int(input("How many ages to enter: "))
# for ages in range(age_count):
#     age = int(input("Enter age:"))
#     total = total + age
# average = total / age_count
# print(f"Age total is {total} and age average is {average:.0f}")

# total_age = 0
# number_of_ages = 0
# age = int(input("Age: "))
# while age > 0:  # while input is bad (age is higher than 0)
#     total_age = total_age + age
#     number_of_ages = + 1
#     age = int(input("Age: "))
# average = total_age / number_of_ages
# print(f"Age total is {number_of_ages} and age average is {average:.0f}")

total = 0
number_of_ages = 0
age = int(input("Age: "))
while age > 0:  # while input is bad (age is higher than 0)
    total = total + age
    number_of_ages += 1
    age = int(input("Age: "))
average = total / number_of_ages
print(f"Age total is {number_of_ages} and age average is {average:.0f}")
