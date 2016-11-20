import numpy as np
import addnoise
import random
import cv2
import os
import re
import sys

sys.setrecursionlimit(1000000)

def sub_sort(array,low,high):
    key = img[array[low][0],array[low][1]]
    while low < high:
        while low < high and img[array[high][0],array[high][1]] >= key:
            high -= 1
        while low < high and img[array[high][0],array[high][1]] < key:
            img[array[low][0],array[low][1]] = img[array[high][0],array[high][1]]
            low += 1
            img[array[high][0],array[high][1]] = img[array[low][0],array[low][1]]
    img[array[low][0],array[low][1]] = key
    return low

def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


k=3
image="images_a1-1001_5_30_2_2.bmp"
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
quick_sort(pixel,0,len(pixel)-1)
for i in pixel[0:len(pixel)/10]:
	img[i[0],i[1]]=temp
	addnoise.pointnoise(i[0],i[1],img,k)
cv2.imwrite("temp.bmp",img)