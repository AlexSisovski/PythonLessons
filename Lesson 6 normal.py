
class People:
    def __init__(self, name):
        self.name = name

    def get_name_people(self):
        print(self.name)

class Student(People):
    def __init__(self, name, mother, father, class_room):
        People.__init__(self, name)
        Class_room.__init__(self, class_room)
        self.mother = mother
        self.father = father
    def get_mather_father(self):
        print("Ученик: {}, родители: {}, {}".format(self.name, self.mother, self.father))

class Teacher(People):
    def __init__(self, name, subject):
        People.__init__(self, name)
        self.subject = subject

class Subject:
    def __init__(self, subject):
        self.subject = subject

class Class_room:
    def __init__(self, class_room):
        self.class_room = Class_room

##student1 = Student("Сергей Петров", "Татьяна Петрова", "Михаил Петров", "4A")
##teacher1 = Teacher("Иванов", "Математика")
students = [Student("Сергей Петров", "Татьяна Петрова", "Михаил Петров", "4A"),
            Student("Иван Петров", "Татьяна Петрова", "Михаил Петров", "3A"),
            Student("Сергей Петров", "Татьяна Петрова", "Михаил Петров", "2A"),
            ]


