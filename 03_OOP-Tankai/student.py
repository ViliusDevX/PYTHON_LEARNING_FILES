class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name,surname):
        for student in self.students:
            if (student.name == name) and (student.surname == surname):
                self.students.remove(student)

    def get_average_grade(self):
        average_grade_of_all = 0
        for student in self.students:
            average_grade_of_one = student.get_grades_average()
            average_grade_of_all += average_grade_of_one
        average_grade_of_all /= len(self.students)
        return average_grade_of_all

    def get_expelled_students(self):
        low_grade_students = []
        for student in self.students:
            if student.is_expelled():
                low_grade_students.append(student)
        return low_grade_students


class Student:
    def __init__(self, name, surname):
        self.grades = []
        self.name = name
        self.surname = surname

    def get_grades_average(self):
        average_grade = 0
        for grade in self.grades:
            average_grade += grade
        average_grade /= len(self.grades)
        return average_grade

    def add_grade(self, grade):
        self.grades.append(grade)

    def is_expelled(self):
        if self.get_grades_average() < 4:
            print("true")
            return True
        else:
            print("false")
            return False


student = Student("petras", "petraitis")
student.add_grade(6)
student.add_grade(1)
student.add_grade(1)
shule = School()
shule.add_student(student)
expelled = shule.get_expelled_students()
exit()