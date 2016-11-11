import numpy as np
import addnoise
import random
import cv2
import os
import re
k=3
image="images_a1-1001_5_30_2_2.bmp"
img=cv2.imread(image,0)
nonblack=[]
black=[]
for i in range(len(img)):
	for j in range(len(img[i])):
		if img[i][j]>40:
			nonblack.append(img[i][j])
		else:
			black.append([i,j])
temp=sum(nonblack)/len(nonblack)
for i in black:
	img[i[0],i[1]]=temp
	addnoise.pointnoise(i[0],i[1],img,k)
cv2.imwrite("temp.bmp",img)
