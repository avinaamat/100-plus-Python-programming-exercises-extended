# ou are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification.
#
# If the following string is given as input to the program:
#
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Then, the output of the program should be:
#
# 3
# 2 1 1
from collections import OrderedDict
leng=int(input('enter length: '))
my_dict=OrderedDict()
for i in range(leng):
    word=input('enter word: ')
    if word in my_dict:
        my_dict[word]+=1
    else:
        my_dict[word]=1

print(len(my_dict))
for k,v in my_dict.items():
    print(v, end=' ')