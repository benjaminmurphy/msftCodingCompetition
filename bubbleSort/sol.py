#!/usr/bin/python3

def bs(a):
	out = 0
	for start in range(1,len(a)):
		for curr in range(1, len(a)):
			if a[curr] < a[curr-1]:
				out += 1
				temp = a[curr]
				a[curr] = a[curr-1]
				a[curr-1] = temp
	return out

f = open('PracticeInput.txt')
for line in f:
	a = [int(val) for val in line.split()]
	print(bs(a))
	print(' '.join([str(val) for val in a]))
