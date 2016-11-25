import numpy as np
import addnoise
import random
import cv2
import os
import re
import sys

sys.setrecursionlimit(1000000)

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and img[array[high][0],array[high][1]] >= img[key[0],key[1]]:
            high -= 1
        while low < high and img[array[high][0],array[high][1]] < img[key[0],key[1]]:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


k=3
image="9.bmp"
img=cv2.imread(image,0)
nonblack=[]
black=[]
pixel=[]
for i in range(len(img)):
	for j in range(len(img[i])):
		if img[i][j]>40:
			nonblack.append(img[i][j])
		else:
			black.append([i,j])
		pixel.append([i,j]);
temp=sum(nonblack)/len(nonblack)
for i in black:
	img[i[0],i[1]]=temp
	addnoise.pointnoise(i[0],i[1],img,k)
if len(black)!=0:
	quick_sort(pixel,0,len(pixel)-1)
	s=0
	for i in pixel[len(pixel)/10:]:
		s+=img[i[0],i[1]]
	temp2=s/len(pixel[len(pixel)/10:])
	for i in pixel[0:len(pixel)/10]:
		img[i[0],i[1]]=temp2
		addnoise.pointnoise(i[0],i[1],img,k)
cv2.imwrite("temp.bmp",img)