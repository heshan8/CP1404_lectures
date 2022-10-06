# names = ["Bob", "Andy", "Josh", "Mary", "Jack", "John"]
# number = int(input(f"Enter number up to {len(names)}: "))
# while number != 0:
#     try:
#         print(names[number - 1])
#     except IndexError:
#         print(f"Number must be less than {len(names) + 1}")
#     number = int(input(f"Enter number up to {len(names)}: "))
# print("Quit")

# from operator import itemgetter
#
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# new_score_pair = input("Enter name and score: ").split()
# score_pairs.append(new_score_pair)
# score_pairs[3][1] = int(new_score_pair[1])  # converting new_score_pair score to an int
# score_pairs.sort(key=itemgetter(1), reverse=True)  # sorting by second index and reversing the order
# print(score_pairs)

text = "This is a sentence".split()
long_words = [word for word in text if len(word) > 3]
print(long_words)

