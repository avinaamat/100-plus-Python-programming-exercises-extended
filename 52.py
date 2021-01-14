# Define a custom exception class which takes a string message as attribute.
#
class Exc(Exception):
    def __init__(self, message):
        self.message = message


if(1):
    raise Exc('agsadnjasfahj')
