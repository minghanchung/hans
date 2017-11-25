password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	p = input('Enter password:')
	if p == password:
		print('登入成功')
		break
	else:
		print('wrong number! only', i, 'times')