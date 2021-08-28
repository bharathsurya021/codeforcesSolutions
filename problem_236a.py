def find_gender(str):
	distinct_string = ""
	for x in str:
		if x not in distinct_string:
			distinct_string = distinct_string+x
	if len(distinct_string)%2 !=0:
		print("IGNORE HIM!")
	else:
		print("CHAT WITH HER!")


string = input()
find_gender(string)
