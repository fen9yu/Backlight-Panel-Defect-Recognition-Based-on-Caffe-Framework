import numpy as np
import cv2
import os
import re

side=18 #the length of side for cutting images

#get all the files/directory in the current directory
files=os.listdir("./")
for image in files:
	if re.match('^\S*-[0-9]*.bmp',image)==None or re.match('^_\S*',image)!=None or os.path.exists('./_'+image):
		continue
	seg=[]
	img = cv2.imread(image,0)
	os.mkdir('_'+image)
	os.chdir("./_"+image)
	remain_v=img.shape[0]
	remain_h=img.shape[1]
	i=0
	j=0

	while remain_v >= side:
		seg.append([])
		while remain_h >= side:
			seg[i].append(img[side*i:side*(i+1),side*j:side*(j+1)])
			imgname=image.split('.')[0]+'_'+str(i)+'_'+str(j)+'.bmp'
			remain_h-=side
			if cv2.mean(seg[i][j])[0] < 3.9:
				j+=1
				continue
			cv2.imwrite(imgname,seg[i][j])
			j+=1
		remain_v-=side
		remain_h=img.shape[1]
		j=0
		i+=1
	os.chdir("..")
