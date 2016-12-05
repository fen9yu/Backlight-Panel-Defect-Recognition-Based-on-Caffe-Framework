from __future__ import division
import cv2
import re
import numpy as np
from edge_detect import edge_detect
from angle_detect import angle_detect
import math
import shutil
import os

side=64
RED=[0,0,255]


with open('defects.txt','r') as f:
	for line in f.readlines():
		#find the coordinate of the defect
		m=re.match(r'(.*?)(a.*?)_(\d+)_(\d+)',line)
		#if it is the first time a defect appear on the picture, make a copy of the picture and rotate it, remove black
		if not os.path.isfile(m.group(2)+'marked.bmp'):
			shutil.copy(m.group(2)+'.bmp',m.group(2)+'marked.bmp')
			orgin=cv2.imread(m.group(2)+'marked.bmp',0)
			ang=angle_detect(orgin)
			#rotate the picture so that the backlight panel is put straight
			rows,cols=orgin.shape
			M0 = cv2.getRotationMatrix2D((cols/2,rows/2),-ang*180/math.pi,1)
			orgin = cv2.warpAffine(orgin,M0,(cols,rows))

			#detect the border of the backlight panel in the rotated picture
			up,down,left,right=edge_detect(orgin)
			#select the region of backlight panel in the picture
			orgin=orgin[int(round(up[0])):int(round(down[0])),int(round(left[1])):int(round(right[1]))]
			orgin=cv2.cvtColor(orgin,cv2.COLOR_GRAY2BGR)
		else:
			orgin=cv2.imread(m.group(2)+'marked.bmp',1)
		#get the defect part
		defect=orgin[side*int(m.group(3))+1:side*(int(m.group(3))+1)-1,side*int(m.group(4))+1:side*(int(m.group(4))+1)-1]
		#add border to the defect part
		defect=cv2.copyMakeBorder(defect,1,1,1,1,cv2.BORDER_CONSTANT,value=RED)
		#put the defect part with border back into the picture
		orgin[side*int(m.group(3)):side*(int(m.group(3))+1),side*int(m.group(4)):side*(int(m.group(4))+1)]=defect

		cv2.imwrite(m.group(2)+'marked.bmp',orgin)