monsters = [["Mike", 340, "blue"], ["James", 14, "Green"], ["Randall", 24, "purple"]]
thing = [monster for monster in monsters if monster[1] > 16]
print(thing)
