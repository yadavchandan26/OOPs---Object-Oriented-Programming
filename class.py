# Object Oriented Programming
class student:
    name='rahul'
    age=18

s1=student()
print(s1.name)
print(s1.age)

# class with __init__ method
# __init__ method is used to inialize object to class's attributes

class college_student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


s1=college_student('rahul',19)
s2=college_student()