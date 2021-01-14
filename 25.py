# Define a class, which have a class parameter and have a same instance parameter.
class MyClass:
    x='me'
    def __init__(self, x=None):
        self.x=x


print(MyClass.x)
s=MyClass('asdfgg')
print(s.x)
print(MyClass.x)

