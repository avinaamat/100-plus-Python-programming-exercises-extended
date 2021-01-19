# Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
#
class Person:
    gender = 'Unknown'

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self):
        self.gender = 'Male'


class Female(Person):
    def __init__(self):
        self.gender = 'Female'

p1=Person()
p2=Male()
p3=Female()
print(p1.getGender())
print(p2.getGender())
print(p3.getGender())