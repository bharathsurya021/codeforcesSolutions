string =input()
x= string.split("+")
x.sort()
y=""
for i in x:
    y = y+i+"+"
print(y[:-1])