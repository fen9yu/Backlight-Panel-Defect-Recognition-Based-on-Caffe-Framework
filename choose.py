import random
file=open("train.txt")
rate=5
defect=[]
perfect=[]
for i in file.readlines():
	if i[-2]=="1":
		defect.append(i)
	else:
		perfect.append(i)
for i in range(rate*len(defect),len(perfect)):
	k=int(random.uniform(0,i))
	if k<rate*len(defect):
		perfect[i],perfect[k]=perfect[k],perfect[i]
file.close()
outputfile=open("result.txt","w+")
for i in defect:
	outputfile.write(i)
for i in perfect[:rate*len(defect)]:
	outputfile.write(i)
