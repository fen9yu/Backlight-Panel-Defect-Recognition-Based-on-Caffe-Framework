import numpy as np
import random
import cv2
import os
import re

def pointnoise(i,j,img,k):
	if random.uniform(0,3)>2 and img[i][j]<=255-k:
		img[i][j]+=int(random.uniform(0,k))
	elif random.uniform(0,3)<1 and img[i][j]>=k:
		img[i][j]-=int(random.uniform(0,k))
def imgnoise(img,k):
	for i in range(len(img)):
		for j in range(len(img)):
			pointnoise(i,j,img,k)

