# text = """CP1403
# CP2404
# CP1404
# CP2404
# CP1403
# CP1403
# CP5633
# CP1404
# CP1404
# CP1403
# CP5633
# CP2404
# CP1403
# CP1404
# CP5633
# CP2404
# CP1403
# CP1404
# CP5632
# CP5633
# CP5641
# CP5632
# CP5633
# CP5641
# CP5632
# CP5633
# CP5641
# CP5632
# CP5633
# CP5641
# """
#
# print(", ".join(set(text.split())))
# # using a set to remove duplicates and join to remove commas and print a string.

my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}

print(f"{'difference':<21}: ", my_subjects - your_subjects)  # Subjects that i do but you dont
print(f"{'difference':<21}: ", your_subjects - my_subjects)  # subjects that you do but, I don't (above reversed)
print(f"{'union':<21}: ", my_subjects | your_subjects)  # all our subjects excluding (duplicates)
print(f"{'intersection':<21}: ", my_subjects & your_subjects)  # shared subjects (only the subjects done together)
print(f"{'symmetric_difference':<21}: ", my_subjects ^ your_subjects)  # Non shared (subjects not done together)
