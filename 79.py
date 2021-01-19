# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
#
from itertools import product as pd
subject = ["I", "You"]
verbs = ["Play", "Love"]
object = ["Hockey", "Football"]
sol=pd(subject, verbs, object)
for i in sol:
    print(i[0] + ' ' + i[1] + ' '+i[2])