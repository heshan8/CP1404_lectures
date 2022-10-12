"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_subject_details(data)
    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject_code = input("What subject code: ")
    print(f"{subject_to_data[subject_code][0]} teaches {subject_code}")



def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def convert_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data


def print_subject_details(data):
    for subject_details in data:
        print(f" {subject_details[0]:1} is taught by {subject_details[1]:12} and has {subject_details[2]:3} students")


main()
