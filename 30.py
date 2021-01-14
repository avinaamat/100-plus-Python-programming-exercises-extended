# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.
max_len = lambda s1, s2: s1 if len(s1) >= len(s2) else s2
print(max_len('sgda', 'adfhwrjw'))
# another sol:
func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)

