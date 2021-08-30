test_cases=int(input())
for i in range(0,test_cases):
	n=int(input())
	p = input()
	strList=p.split(" ")
	for i in range(len(strList)):
		strList[i] = int(strList[i])
	list = strList

	checker = False
	for i in range(1,n):
		if(i+1 < n):
			if(list[i]>list[i-1] and list[i]>list[i+1]):
				print("YES")
				print(f"{i} {i+1} {i+2}")
				checker = True
				break
			else:
				pass
		
	if(not checker):
		print("NO")

