def word(str):
	lowercase_count =0
	uppercase_count=0

	for x in str:
		if x.islower():
			lowercase_count +=1
		else:
			uppercase_count +=1
	if uppercase_count>lowercase_count:
		print(str.upper())
	else:
		print(str.lower())
string = input()
word(string)