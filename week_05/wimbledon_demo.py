"""Wimbledon Men's Winners"""

in_file = open('wimbledon.txt')
lines = [line.strip() for line in in_file.readlines()]
# print(lines)

winners = set(lines)  # turn into a set and assigned variable
print(winners)
print(len(winners))

in_file.close()
