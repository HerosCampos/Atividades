class Student:
    def __init__(self, new_name, new_grades):
        # Properties
        self.name = new_name
        self.grades = new_grades

    # Method
    def average(self):
        return sum(self.grades) / len(self.grades) 


#student_one = Student("Rolf Smith", [70, 88, 90, 99])
#print(student_one.name)
#print(student_one.average())


# Inheritance
class WorkingStudent(Student):
    def __init__(self, new_name, new_grades, salary):
        super().__init__(new_name, new_grades)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 40


rolf = WorkingStudent('Rolf', [50, 99, 80, 75], 15.50)
print(rolf.average(), rolf.grades, rolf.salary, rolf.name)
rolf.grades.append(100)
print(rolf.average(), rolf.grades, rolf.salary, rolf.name)
print(rolf.weekly_salary())

################################################################################


#class Garage:
#    def __init__(self):
#        self.cars = []
#
#    # We que do for loops once we have __len__ and __getitem__ methods implemented
#    def __len__(self):
#        return len(self.cars)
#
#    def __getitem__(self, i):
#        return self.cars[i]
#
#    def __repr__(self):
#        return f"<Garage {self.cars}>"    

#    def __str__(self):
#        return f"Garage with {len(self)} cars."


#ford = Garage()
#ford.cars.append("Ford")
#ford.cars.append("Fusion")
#print(ford)
#print(len(ford))
#for car in ford:
#    print(car)




