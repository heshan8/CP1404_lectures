# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# for person, score in data:
#     print(f"{person} - {score}")
from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelleyoh', 9]]
# name_to_number = {pair[0]: pair[1] for pair in data}


name_to_number = {'Bob': 612, 'Xavier': 80, 'Chantanelleyoh': 9, 'Derek': 7}
print(name_to_number)
max_length = max(len(key) for key in name_to_number)
for name, number in name_to_number.items():
    print(f"{name:{max_length}} = {number: 4}")

# max_length = max(len(pair[0]) for pair in data)
# print(max_length)
# for pair in sorted(data, key=itemgetter(1), reverse=True):
#     print(f"{pair[0]:{max_length}} - {pair[1]}")


"""Questions comparing dicts, lists, sets when when they're used"""
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1