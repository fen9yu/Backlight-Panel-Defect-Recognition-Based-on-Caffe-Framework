import numpy as np
import cv2
import os
import re
import sys
from diffdetect import imdiff

side=64 #the length of side for cutting images
margin=3 #if defects are in the range of margin, it will not be marked neither 0 nor 1. To improve accuracy.
#the offset of the starting point
if len(sys.argv)==1:
	offset=0
elif len(sys.argv)==2:
	offset=int(sys.argv[1])
else:
	print("too much arguments")

#get all the files/directory in the current directory
files=os.listdir("./")
origpath=os.getcwd()
date=os.path.split(os.getcwd())[1]
#open a txt file which named by the directory(date recommanded), in order to write in it
with open(os.path.split(os.getcwd())[0]+'/train.txt','a') as f:
	for image in files:
		#only deal with the images start with "a" and include decfect type 10, e.g.: a12-1002.bmp
		if re.match(r'^a.*?-10.*',image)==None or os.path.exists('./_'+image):
			continue

		#remove images with more than one type of defect, which need manual process
		#you can decide whether to use it or not
		if re.match(r'.*?-.*?-.*?',image)!=None:
			continue

		seg=[]
		img = cv2.imread(image,0)

		#find the coordinate of defects
		image2 = 'b'+re.match(r'^a(\S*?).bmp',image).group(1)+'.png'
		img2 = cv2.imread(image2,0)
		defect = imdiff(img,img2)

		#make a directory for each image and go into the directory
		#os.mkdir('_'+image)
		#os.chdir("./_"+image)
		remain_v=img.shape[0]-offset
		remain_h=img.shape[1]-offset
		i=0
		j=0

		#cut the images
		while remain_v >= side:
			seg.append([])
			while remain_h >= side:
				seg[i].append(img[side*i+offset:side*(i+1)+offset,side*j+offset:side*(j+1)+offset])
				imgname=date+'_'+image.split('.')[0]+'_'+str(i)+'_'+str(j)+'+'+str(offset)+'.bmp'
				remain_h-=side
				if cv2.mean(seg[i][j])[0] < 3.9:
					j+=1
					continue
				os.chdir(os.path.split(os.getcwd())[0])
				cv2.imwrite(imgname,seg[i][j])
				os.chdir(origpath)
				#mark defect for cut images 0/1
				flag=0
				for point in defect:
					if point[0]>i*side+offset and point[0]<(i+1)*side+offset and point[1]>j*side+offset and point[1]<(j+1)*side+offset:
						if point[0]>i*side+offset+margin and point[0]<(i+1)*side+offset-margin and point[1]>j*side+offset+margin and point[1]<(j+1)*side+offset-margin:
							f.write(imgname+' '+str(1)+'\n')
						flag=1
						break
					elif point[0]>i*side+offset-margin and point[0]<(i+1)*side+offset+margin and point[1]>j*side+offset-margin and point[1]<(j+1)*side+offset+margin:
						flag=-1
				if flag == 0:
					f.write(imgname+' '+str(0)+'\n')
				j+=1
			remain_v-=side
			remain_h=img.shape[1]
			j=0
			i+=1
