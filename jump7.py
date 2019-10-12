for i in range(101):
	if i % 7 == 0 or i // 10 == 7 or int(str(i)[-1]) == 7 :
		continue
	print(i)
