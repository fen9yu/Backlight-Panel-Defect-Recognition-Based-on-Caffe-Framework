import numpy as np
import random
import cv2
import os
import re
k=9
image="images_a1-1001_5_30_2_2.bmp"
img=cv2.imread(image,0)
def pointnoise(i,j,img,k):
	if random.uniform(0,3)>2 and img[i][j]<=255-k:
		img[i][j]+=int(random.uniform(0,k))
	elif random.uniform(0,3)<1 and img[i][j]>=k:
		img[i][j]-=int(random.uniform(0,k))
def imgnoise(img,k):
	for i in range(len(img)):
		for j in range(len(img)):
			pointnoise(i,j,img,k)
imgnoise(img,k)
cv2.imwrite("temp.bmp",img)
