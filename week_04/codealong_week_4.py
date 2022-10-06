"""
numbers = [10, 0, -3, 50, -32, 64, 99, 200]
data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
words = "CP1404 is a very good subject and I am HAPPY".split()

NUMBERS

numbers
    [10, 0, -3, 50, -32, 64, 99, 200]
[number for number in numbers]
    [10, 0, -3, 50, -32, 64, 99, 200]
[number *2 for number in numbers]
    [20, 0, -6, 100, -64, 128, 198, 400]
[number /2 for number in numbers]
    [5.0, 0.0, -1.5, 25.0, -16.0, 32.0, 49.5, 100.0]
[number / 2 for number in numbers]
    [5.0, 0.0, -1.5, 25.0, -16.0, 32.0, 49.5, 100.0]
[number // 2 for number in numbers]
    [5, 0, -2, 25, -16, 32, 49, 100]
[int(number // 2) for number in numbers]
    [5, 0, -2, 25, -16, 32, 49, 100]
[number **2 for number in numbers]
    [100, 0, 9, 2500, 1024, 4096, 9801, 40000]
[1 for number in numbers]
    [1, 1, 1, 1, 1, 1, 1, 1]
[print(number) for number in numbers]
    10
    0
    -3
    50
    -32
    64
    99
    200
    [None, None, None, None, None, None, None, None]
[number for number in numbers]
    [10, 0, -3, 50, -32, 64, 99, 200]
[number for number in numbers if number > 50]
    [64, 99, 200]
[number for number in numbers if number < 0]
    [-3, -32]
[1 / number for number in numbers if number > 0]
    [0.1, 0.02, 0.015625, 0.010101010101010102, 0.005]
[(1 , number) for number in numbers]
    [(1, 10), (1, 0), (1, -3), (1, 50), (1, -32), (1, 64), (1, 99), (1, 200)]



WORDS

words
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words]
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words if len(word) > 4]
    ['CP1404', 'subject', 'HAPPY']
[word for word in words if len(word) > 5]
    ['CP1404', 'subject']
[len(word) for word in words]
    [6, 2, 1, 4, 4, 7, 3, 1, 2, 5]
max(len(word) for word in words)
    7
(len(word) for word in words)
    <generator object <genexpr> at 0x00000227EF4EE880>
max(len(word) for word in words if len(word) < 5)
    4
[word[0] for word in words]
    ['C', 'i', 'a', 'v', 'g', 's', 'a', 'I', 'a', 'H']
[word.upper for word in words]
    [<built-in method upper of str object at 0x00000227EF2E21B0>, <built-in method upper of str object at 0x00000227EF3BCEF0>, <built-in method upper of str object at 0x00000227EC0075B0>, <built-in method upper of str object at 0x00000227EF3062F0>, <built-in method upper of str object at 0x00000227EF305670>, <built-in method upper of str object at 0x00000227EF5A7770>, <built-in method upper of str object at 0x00000227EF5A7230>, <built-in method upper of str object at 0x00000227EBFFC9B0>, <built-in method upper of str object at 0x00000227EF5A7370>, <built-in method upper of str object at 0x00000227EF5A7470>]

[word.upper() for word in words]
    ['CP1404', 'IS', 'A', 'VERY', 'GOOD', 'SUBJECT', 'AND', 'I', 'AM', 'HAPPY']
[word for word in words if word.upper()]
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words if word.isupper()]
    ['CP1404', 'I', 'HAPPY']
words[0]
    'CP1404'
words[0][0]
    'C'
[word[0] for word in words if word == "a" or "e" or "i" or "o" or "u"]
    ['C', 'i', 'a', 'v', 'g', 's', 'a', 'I', 'a', 'H']
[word for word in words if word == "a" or "e" or "i" or "o" or "u"]
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words[0][0] if word == "a" or "e" or "i" or "o" or "u"]
    ['C']
[word for word in words if word[0] == "a" or "e" or "i" or "o" or "u"]
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words if word[0] in "aeiou"]
    ['is', 'a', 'and', 'am']
[word for word in words if word[0] in "aeiou" or "AEIOU"]
    ['CP1404', 'is', 'a', 'very', 'good', 'subject', 'and', 'I', 'am', 'HAPPY']
[word for word in words if word[0] in "aeiouAEIOU"]
    ['is', 'a', 'and', 'I', 'am']

[word for word in words if word[0].upper() in "aeiou"]
    []
[word for word in words if word[0].lower() in "aeiou"]
    ['is', 'a', 'and', 'I', 'am']


DATA

data
    [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
[data for data in data]
    [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
[pair for pair in data]
    [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
[tuple(pair) for pair in data]
    [('Derek', 7), ('Carrie', 8), ('Bob', 6), ('Aaron', 9)]
[f"{pair}" for pair in data]
    ["['Derek', 7]", "['Carrie', 8]", "['Bob', 6]", "['Aaron', 9]"]
[f"{pair[0][0]}" for pair in data]
    ['D', 'C', 'B', 'A']
[f"{pair[0]}" for pair in data]
    ['Derek', 'Carrie', 'Bob', 'Aaron']
[f"{pair[0]} {pair[1]}" for pair in data]
    ['Derek 7', 'Carrie 8', 'Bob 6', 'Aaron 9']
[pair[1] for pair in data]
    [7, 8, 6, 9]
max(([pair[1] for pair in data]))
    9
max((pair[1] for pair in data))
    9
[pair[1] for pair in data]
    [7, 8, 6, 9]
[pair[0] for pair in data]
    ['Derek', 'Carrie', 'Bob', 'Aaron']

[pair[0]for pair in data  if pair[1] > 7  ]
    ['Carrie', 'Aaron']
[sorted(pair[0]) for pair in data  if pair[1] > 7]
    [['C', 'a', 'e', 'i', 'r', 'r'], ['A', 'a', 'n', 'o', 'r']]

sorted([pair[0] for pair in data  if pair[1] > 7])
    ['Aaron', 'Carrie']
"""



