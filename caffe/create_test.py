import os

filename='test.txt'
if os.path.exists(filename):
	os.remove(filename)

for filename in os.listdir(os.getcwd()):
	with open('test.txt', 'a') as f:
		f.write(filename+' 0\n')
