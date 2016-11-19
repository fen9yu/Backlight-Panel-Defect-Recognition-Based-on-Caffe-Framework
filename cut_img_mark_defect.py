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
				imgname=date+'_'+image.split('.')[0]+'_'+str(i)+'_'+str(j)+'+'+str(offset)
				remain_h-=side
				if cv2.mean(seg[i][j])[0] < 3.9:
					j+=1
					continue
				
				#mark defect for cut images 0/1
				flag=0
				rows,cols=seg[i][j].shape
				for point in defect:
					if point[0]>i*side+offset and point[0]<(i+1)*side+offset and point[1]>j*side+offset and point[1]<(j+1)*side+offset:
						if point[0]>i*side+offset+margin and point[0]<(i+1)*side+offset-margin and point[1]>j*side+offset+margin and point[1]<(j+1)*side+offset-margin:
							M1 = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
							M2 = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
							M3 = cv2.getRotationMatrix2D((cols/2,rows/2),270,1)
							dst0f1=cv2.flip(seg[i][j],0)
							dst0f2=cv2.flip(seg[i][j],1)
							dst1 = cv2.warpAffine(seg[i][j],M1,(cols,rows))
							dst1f1=cv2.flip(dst1,0)
							dst1f2=cv2.flip(dst1,1)
							dst2 = cv2.warpAffine(seg[i][j],M2,(cols,rows))
							dst2f1=cv2.flip(dst2,0)
							dst2f2=cv2.flip(dst2,1)
							dst3 = cv2.warpAffine(seg[i][j],M3,(cols,rows))
							dst3f1=cv2.flip(dst3,0)
							dst3f2=cv2.flip(dst3,1)
							imgname='1_'+imgname
							imgname1=imgname+'_0_0'+'.bmp'
							imgname1flip1=imgname+'_0_1'+'.bmp'
							imgname1flip2=imgname+'_0_2'+'.bmp'
							imgname2=imgname+'_90_0'+'.bmp'
							imgname2flip1=imgname+'_90_1'+'.bmp'
							imgname2flip2=imgname+'_90_2'+'.bmp'
							imgname3=imgname+'_180_0'+'.bmp'
							imgname3flip1=imgname+'_180_1'+'.bmp'
							imgname3flip2=imgname+'_180_2'+'.bmp'
							imgname4=imgname+'_270_0'+'.bmp'
							imgname4flip1=imgname+'_270_1'+'.bmp'
							imgname4flip2=imgname+'_270_2'+'.bmp'
							f.write(imgname1+' '+str(1)+'\n')
							f.write(imgname1flip1+' '+str(1)+'\n')
							f.write(imgname1flip2+' '+str(1)+'\n')
							f.write(imgname2+' '+str(1)+'\n')
							f.write(imgname2flip1+' '+str(1)+'\n')
							f.write(imgname2flip2+' '+str(1)+'\n')
							f.write(imgname3+' '+str(1)+'\n')
							f.write(imgname3flip1+' '+str(1)+'\n')
							f.write(imgname3flip2+' '+str(1)+'\n')
							f.write(imgname4+' '+str(1)+'\n')
							f.write(imgname4flip1+' '+str(1)+'\n')
							f.write(imgname4flip2+' '+str(1)+'\n')
							os.chdir(os.path.split(os.getcwd())[0])
							cv2.imwrite(imgname1,seg[i][j])
							cv2.imwrite(imgname1flip1,dst0f1)
							cv2.imwrite(imgname1flip2,dst0f2)
							cv2.imwrite(imgname2,dst1)
							cv2.imwrite(imgname2flip1,dst1f1)
							cv2.imwrite(imgname2flip2,dst1f2)
							cv2.imwrite(imgname3,dst2)
							cv2.imwrite(imgname3flip1,dst2f1)
							cv2.imwrite(imgname3flip2,dst2f2)
							cv2.imwrite(imgname4,dst3)
							cv2.imwrite(imgname4flip1,dst3f1)
							cv2.imwrite(imgname4flip2,dst3f2)
							os.chdir(origpath)
						flag=1
						break
					elif point[0]>i*side+offset-margin and point[0]<(i+1)*side+offset+margin and point[1]>j*side+offset-margin and point[1]<(j+1)*side+offset+margin:
						flag=-1
				if flag == 0:
					imgname='0_'+imgname+'.bmp'
					f.write(imgname+' '+str(0)+'\n')
					os.chdir(os.path.split(os.getcwd())[0])
					cv2.imwrite(imgname,seg[i][j])
					os.chdir(origpath)
				j+=1
			remain_v-=side
			remain_h=img.shape[1]
			j=0
			i+=1
