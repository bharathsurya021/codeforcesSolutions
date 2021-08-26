def compare_string(str1,str2):
    if (str1==str2):
    	print(0)
    elif(str1<str2):
        print(-1)
    else:
        print(1)

x = input()
y= input()
string1 = x.lower()
string2 = y.lower()
compare_string(string1,string2)