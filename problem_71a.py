def abbrev(str):
    x=len(str)-1
    k=len(str[1:x])
    print("{}{}{}".format(str[0],k,str[-1]))

n=int(input())
for i in range(0,n):
    input_string = input()
    length_of_string = len(input_string)
    if length_of_string>10:
        abbrev(input_string)
    else:
        print(input_string)