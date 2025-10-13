
# 1
def get_best_students(input_file: str, output_file='files\\output.txt'):
    students = []

    with open(input_file, 'r') as read_file:
        for line in read_file:
            split = line.split()

            name = split[0]
            grades = list(map(int, split[2:]))

            if sum(grades) / len(grades) > 6:
                students.append(name)

    with open(output_file, 'w') as write_file:
        for name in students:
            print(name, file=write_file)


get_best_students('files\\input.txt')


