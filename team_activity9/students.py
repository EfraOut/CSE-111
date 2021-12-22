import csv

def read_dict(filename, key_column_index):
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary


def main():
    I_NUMBER = 0
    STUDENT_NAME = 1
    students = read_dict('students.csv', I_NUMBER)
    student = input('Please enter an I-Number: ')
    student = student.replace('-', '')
    # Cheking if the input has more or less digits that it should
    if len(student) < 9:
        print('Invalid I-Number: too few digits')
    elif len(student) > 9:
        print('Invalid I-Number: too many digits')

    # Getting the name if it exist on the dictionary
    if student in students:
        print(students[student][STUDENT_NAME])
    else:
        print('No such student')


if __name__ == '__main__':
    main()