# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
#
while True:
    x=input()
    if not x:
        break
    if x=="yes" or x=="YES" or x=="Yes":
        print("Yes")
    else:
        print('No')
