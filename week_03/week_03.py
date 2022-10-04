# infile = open("demo.txt", "r")
# lines = infile.readlines()
# for line in lines:
#     if line.startswith("#"):
#         print(line.strip())
#


# name = input("file: ")
# with open("test.txt", "w") as out_file:
#     print(name, file=out_file)


with open("test.txt", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(",")
        guitar = parts[0]
        year = parts[1]
        price = (parts[2]).strip("\\n")
        print(f"{guitar} is made in {year} and costs ${price}")
