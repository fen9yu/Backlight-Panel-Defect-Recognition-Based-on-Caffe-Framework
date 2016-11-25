import shutil

with open('result.txt', 'r') as f:
	for line in f.readlines():
		image=line[:-3]
		shutil.copy(image,r'../RemoveblackImg/')