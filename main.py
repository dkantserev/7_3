n = list(map(int,input().split()))
s=set()

for i in n:
	if i in s:
		print(f'YES {i}')
	s.add(i)
	print(f'NO {i}')
