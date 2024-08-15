class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
              lecturer.grades.setdefault(course, []).append(grade)
            else:
              print('Недопустимая оценка')
           
  def average_grade(self):
      total_grades = 0
      count = 0
      for grades in self.grades.values():
          total_grades += sum(grades)
          count += len(grades)
      return total_grades / count if count > 0 else 0

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
      
  def __eq__(self, other):
    if isinstance(other, Student):
        return self.average_grade() == other.average_grade()

  def __str__(self):
      return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за домашние задания: {round(self.average_grade(), 1)}\n'
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
              f'Завершенные курсы: {", ".join(self.finished_courses)}')


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
      
  def __eq__(self, other):
    if isinstance(other, Lecturer):
        return self.average_grade() == other.average_grade()

  def __str__(self):
      return (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за лекции: {round(self.average_grade(), 1)}')


class Reviewer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        student.grades.setdefault(course, []).append(grade)
      else:
          return 'Недопустимая оценка'
          
  def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}'


# Создание экземпляров классов
student1 = Student("Первый", "Студент", "М")
student1.courses_in_progress = ["Python"]
student1.finished_courses = ["Математика"]

student2 = Student("Второй", "Студент", "Ж")
student2.courses_in_progress = ["Python"]
student2.finished_courses = ["Физика"]

lecturer1 = Lecturer("Первый", "Преподаватель")
lecturer1.courses_attached = ["Python"]

lecturer2 = Lecturer("Второй", "Преподаватель")
lecturer2.courses_attached = ["Python"]

reviewer1 = Reviewer("Певый", "Проверяющий")
reviewer1.courses_attached = ["Python"]

reviewer2 = Reviewer("Второй", "Проверяющий")
reviewer2.courses_attached = ["Python"]

# Оценка лектора
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Python", 8)
student2.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Python", 7)

# Оценка студента
reviewer1.rate_hw(student1, "Python", 9)
reviewer2.rate_hw(student2, "Python", 10)

# Вывод информации о студентах и лекторах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

# сравнение студентов по средней оценке за домашние задания
print(student1.average_grade(), student2.average_grade())
print(student1 > student2)
print(student1 == student2)
print(student1 < student2)

# сравнение лекторов по средней оценке за лекции
print(lecturer1.average_grade(), lecturer2.average_grade())
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 < lecturer2)

# Функция для подсчета средней оценки за домашние задания по всем студентам
def average_student_grade(students, course):
  total_grades = 0
  count = 0
  for student in students:
      if course in student.grades:
          total_grades += sum(student.grades[course])
          count += len(student.grades[course])
  return round(total_grades / count, 1) if count > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов
def average_lecturer_grade(lecturers, course):
  total_grades = 0
  count = 0
  for lecturer in lecturers:
      if course in lecturer.grades:
          total_grades += sum(lecturer.grades[course])
          count += len(lecturer.grades[course])
  return round(total_grades / count, 1) if count > 0 else 0

# Пример использования функций
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("Средняя оценка студентов по курсу Python:", average_student_grade(students_list, "Python"))
print("Средняя оценка лекторов по курсу Python:", average_lecturer_grade(lecturers_list, "Python"))
