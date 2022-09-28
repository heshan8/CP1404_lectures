def main():
    infile = open("DEMO.md")
    text = infile.readlines()
    infile.close()
    print(f"{text[0]}{text[1]}")


main()
