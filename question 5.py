#Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class My_class:
    my_str=''
    #def __init__(self):
    def printString(self):
        print(self.my_str.upper())
    def getString(self):
        self.my_str=input('enter string: ')

x=My_class()
x.getString()
x.print_string()