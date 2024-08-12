class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()


    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()


    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()


    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Первый', 'Студент', 'М')
student2 = Student('Второй', 'Студент', 'Ж')

lecturer1 = Lecturer('Первый', 'Преподаватель')
lecturer2 = Lecturer('Второй', 'Преподаватель')

# Пример установки оценок
student1.grades = {'Python': [9, 8, 10], 'Math': [7, 8]}
student2.grades = {'Python': [6, 7, 5], 'Math': [8, 9]}
lecturer1.grades = {'Python': [10, 10, 9], 'Math': [9, 8]}
lecturer2.grades = {'Python': [7, 8, 7], 'Math': [6, 7]}

# Сравнение студентов
print(student1 > student2)  # True или False в зависимости от оценок

# Сравнение лекторов
print(lecturer1 < lecturer2)  # True или False в зависимости от оценок

