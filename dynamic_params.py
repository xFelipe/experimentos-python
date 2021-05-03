from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def __repr__(self):
        return f'<name: {self.name}, grades: {self.grades}>'

    def take_exam(self, grade):
        self.grades.append(grade)


s1 = Student('s1')
s2 = Student('s2')

s1.take_exam(2)
print(s1)
print(s2)
