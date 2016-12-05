import numpy as np
import cv2
import os
import re

side=64 #the length of side for cutting images

#get all the files/directory in the current directory
files=os.listdir("./")
for image in files:
	if re.match('^\S*-[0-9]*.bmp',image)==None or re.match('^_\S*',image)!=None or os.path.exists('./_'+image):
		continue
	seg=[]
	img = cv2.imread(image,0)

	#find the angle of the backlight panel with respect to the border of the picture
	ang=angle_detect(img)
	#rotate the picture so that the backlight panel is put straight
	rows,cols=img.shape
	M0 = cv2.getRotationMatrix2D((cols/2,rows/2),-ang*180/math.pi,1)
	img = cv2.warpAffine(img,M0,(cols,rows))

	#detect the border of the backlight panel in the rotated picture
	up,down,left,right=edge_detect(img)
	#select the region of backlight panel in the picture
	img=img[int(round(up[0])):int(round(down[0])),int(round(left[1])):int(round(right[1]))]

	#transformation matrix
	tm=np.array([[math.cos(ang),math.sin(ang),(1-math.cos(ang))*cols/2-math.sin(ang)*rows/2],[-math.sin(ang),math.cos(ang),math.sin(ang)*cols/2+(1-math.cos(ang))*rows/2],[0,0,1]])
	#coordinate of the defects after rotation
	defectrot=[]
	#calculate the coordinate of the defects after rotation
	for i in range(len(defect)):
		df=np.array([[defect[i][0]],[defect[i][1]],[1]])
		prod=np.dot(tm,df)
		tempdefect=[prod[1][0],prod[0][0]]
		#calculate the coordinate of the defects after selecting the region of backlight panel
		defectrot.append([int(round(tempdefect[1]))-int(round(up[0])),int(round(tempdefect[0])-int(round(left[1])))])
	defect=defectrot

	#make a directory for each image and go into the directory
	#os.mkdir('_'+image)
	#os.chdir("./_"+image)
	remain_v=img.shape[0]
	remain_h=img.shape[1]
	i=0
	j=0

	while remain_v > side:
		seg.append([])
		while remain_h > side:
			seg[i].append(img[side*i:side*(i+1),side*j:side*(j+1)])
			imgname=image.split('.')[0]+'_'+str(i)+'_'+str(j)+'.bmp'
			remain_h-=side
			'''if cv2.mean(seg[i][j])[0] < 3.9:
				j+=1
				continue'''
			cv2.imwrite(imgname,seg[i][j])
			j+=1

		seg[i].append(img[side*i:side*(i+1),img.shape[1]-side:img.shape[1]])
		imgname=image.split('.')[0]+'_'+str(i)+'_'+str(j)+'.bmp'
		remain_h-=side
		'''if cv2.mean(seg[i][j])[0] < 3.9:
			j+=1
			continue'''
		cv2.imwrite(imgname,seg[i][j])
		remain_v-=side
		remain_h=img.shape[1]
		j=0
		i+=1
	seg.append([])
	while remain_h > side:
		seg[i].append(img[img.shape[0]-side:img.shape[0],side*j:side*(j+1)])
		imgname=image.split('.')[0]+'_'+str(i)+'_'+str(j)+'.bmp'
		remain_h-=side
		'''if cv2.mean(seg[i][j])[0] < 3.9:
			j+=1
			continue'''
		cv2.imwrite(imgname,seg[i][j])
		j+=1

	seg[i].append(img[img.shape[0]-side:img.shape[0],img.shape[1]-side:img.shape[1]])
	imgname=image.split('.')[0]+'_'+str(i)+'_'+str(j)+'.bmp'
	remain_h-=side
	'''if cv2.mean(seg[i][j])[0] < 3.9:
		j+=1
		continue'''
	cv2.imwrite(imgname,seg[i][j])
	remain_v-=side
	remain_h=img.shape[1]
	#os.chdir("..")
