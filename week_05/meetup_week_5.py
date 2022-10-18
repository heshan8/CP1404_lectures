from operator import itemgetter
# iterating and printing a list
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
for person, score in data:
    print(f"{person} - {score}")

"""================================================================================================================="""

# using list comprehensions (returns sorted)
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelleyoh', 9]]
name_to_number = {pair[0]: pair[1] for pair in data}
print(f"{name_to_number}")

# using for loop and using max and len for nicer output (clear)
name_to_number = {'Bob': 612, 'Xavier': 80, 'Chantanelleyoh': 9, 'Derek': 7}
print(name_to_number)
max_length = max(len(key) for key in name_to_number)
for name, number in name_to_number.items():
    print(f"{name:{max_length}} = {number: 4}")

# using item getter
max_length = max(len(pair[0]) for pair in data)
print(max_length)
for pair in sorted(data, key=itemgetter(1), reverse=True): # item getter gets the element out of the (list/tuple/set)
    print(f"{pair[0]:{max_length}} - {pair[1]}")

"""Questions comparing dicts, lists, sets when they're used"""
word_to_count = {'hi': 3}
for word in word_to_count:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
print(word_to_count)