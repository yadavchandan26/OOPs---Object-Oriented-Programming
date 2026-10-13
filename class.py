# Object Oriented Programming
class student:
    name='rahul_chapari'
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
s2=college_student('kunal',20)

print(s1.name)
print(s1.age)

print(s2.name,s2.age)

class student_:

    def __init__(self,name,year):
        self.name=name
        self.year=year

    def introduce(self):
        print(f"My name is : {self.name}")
        print(f"I'm {self.year} year of college student.")
        print('Thank you>>')

s1=student_("ayush",2)
s2=student_("shreya",3)

s1.introduce()
s2.introduce()

class sub:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def sub(self):
        return print(f"subtraction will be {self.a-self.b}")


    