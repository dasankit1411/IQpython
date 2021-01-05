#read file line by line and stored in a list
def readfile(fname):
	l=[]
	with open(fname) as f:
		line=f.read().splitlines()
		l.append(line)
		print(l)

readfile('E:/demo.txt')