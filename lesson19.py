class Student:
    def __init__(self, name: str, *grades: int | float):
        self.name = name
        self.__grades = list(grades)


    def add_grade(self, grade: int | float):
        if type(grade) not in (int, float):
            raise ValueError
        
        self.__grades.append(grade)
        print(f"Оцінку додано до студента{self.name}")


    def get_average(self):
        return sum(self.__grades) / len(self.__grades)
    
    def get_grades(self):
        return self.__grades.copy()
    
    def __str__(self):
        return (f"{self.name} - {self.get_average()}")
    
    def __gt__(self, other):
        if type(other) is not Student:
            raise ValueError

        return self.get_average() > other.get_average()

class VipStudent(Student):
    def __init__(self, name: str, *grades: int | float):
        new_grades = map(lambda grades: grades + 1, grades)

        super().__init__(name, *new_grades)
        
    def vip_method(self):
        pass




class StudentGroup:
    def __init__(self, name: str):
        self.name = name
        self.student: list[Student] = []


    def add_spudednts(self, *students: Student):
        for st in students:
            if type(st) is not Student:
                raise ValueError
            
            if st in self.student:
                print(f"Студент {st.name} у списку")
                continue

            self.student.append(st)

    def get_best_student(self):
        # return max(self.student, key=lambda student: student.get_average())
        return max(self.student)
    



qwerty = VipStudent("Qwerty", 12, 12, 12, 12)


bob = Student("Bob", 10, 5, 4, 12)
john = Student("John", 10, 8, 4, 12)
alise = Student("Alise", 10, 5, 10, 12)

print(bob.get_average())
print(john.get_average())
print(alise.get_average())

group = StudentGroup("PV511")

group.add_spudednts(bob, john, alise)

print(group.get_best_student())

print(qwerty.get_average())

