#!/usr/bin/python3
f = open('PracticeInput.txt')


def convert(val, base):
	convert = { '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'a':int('a',36), 'b':int('b',36), 'c':int('c',36), 'd':int('d',36), 'e':int('e',36), 'f':int('f',36), 'g':int('g',36), 'h':int('h',36), 'i':int('i',36), 'j':int('j',36), 'k':int('k',36), 'l':int('l',36), 'm':int('m',36), 'n':int('n',36), 'o':int('o',36), 'p':int('p',36), 'q':int('q',36), 'r':int('r',36), 's':int('s',36), 't':int('t',36), 'u':int('u',36), 'v':int('v',36), 'w':int('w',36), 'x':int('x',36), 'y':int('y',36), 'z':int('z',36) }
	out = 0
	for c in val[::-1]:
		print(c)
		out += int(convert[str(c)])
		out *= base 
	out /= base
	return str(out)


for line in f:
	a = line.split(',')
	val = convert(a[0],int(a[1]))
	val = convert(val, int(a[2]))

