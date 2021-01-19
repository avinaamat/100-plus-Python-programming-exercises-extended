# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
#
import zlib

my_str = 'hello world!hello world!hello world!hello world!'
print(my_str)
# In Python 3 zlib.compress() accepts only DataType <bytes>
my_str_compressed = zlib.compress(bytes(my_str, 'utf-8'))
print(my_str_compressed)
print(zlib.decompress(my_str_compressed).decode())
