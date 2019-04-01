from datetime import datetime, timedelta
from hashlib import sha256

class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.age = self.calculate_age()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def calculate_age(self):
        diff = (datetime.now() - datetime(self.year, 1, 1, 1, 1))
        return diff.days // 365

    def __str__(self):
        return self.full_name() + " " + str(self.age)

    def __repr__(self):
        return str(self)


def get_average_age(people):
    return sum([person.age for person in people]) / len(people)


class Student:

    # the person parameter must be a Person object
    def __init__(self, person, password):
        """
        bonus(use sha256 hashing)
        """
        self.person = person
        self.password = password
        self.projects = []

    # use the full_name method for Person
    def get_name(self):
        return self.person.full_name()

    def check_password(self, password):
        return self.password == password

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        self.projects.append(project)


#person = Person("fn", "ln", 1989)
#print(person.age)
#print(person)

#people = [Person("John", "Smith", 1985), Person("Mary", "Smith", 1970)]
#print(get_average_age(people))

person = Person("fn", "ln", 1989)
student = Student(person, "asd")
print(student.get_name())