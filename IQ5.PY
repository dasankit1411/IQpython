#Write a Python program that takes a text file as input and returns the number of words of a given text file.
def read(filename):
	count=0
	with open(filename) as f:
		data=f.read()
		content=data.split()
		print (content)
	for word in content:
		count=count+1
	print(count)
read('E:/demo.txt')