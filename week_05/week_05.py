from operator import itemgetter


# thing = 8
# if isinstance(thing, str):
#     print("Yes it is")
# else:
#     print("no its not")
#
# def run_tests():
#     names = ["bill", "Jane", "Sven", "steven"]
#     ages = [21, 34, 56, 0]
#     print(find_oldest(names, ages))
#
#
# def find_oldest(names, ages):
#     # return names[ages.index(max(ages))] # <- List expression way
#
#     oldest_age = -1
#     oldest_index = -1
#     for i, age in enumerate(ages):    # <<<<---- Longer way
#         if age > oldest_age:
#             oldest_age = age
#             oldest_index = i
#     return names[oldest_index]
#
# run_tests()

"""================================================================================================================="""


name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}

get_name = input("Enter name: ")
get_age = int(input("Enter age: "))
name_to_age[get_name] = get_age
max_length = max(len(name) for name in list(name_to_age))
for name, age in name_to_age.items():
    print(f"{name:{max_length}} - {age:3} ")

# week_4 duplicate here for some reason
# score_pair = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
# new_score_pair = input("Enter name and score: ").split()
# score_pairs.append(new_score_pair)
# score_pairs[3][1] = int(new_score_pair[1])  # converting new_score_pair score to an int
# score_pairs.sort(key=itemgetter(1), reverse=True)  # sorting by second index and reversing the order
# print(score_pairs)




































