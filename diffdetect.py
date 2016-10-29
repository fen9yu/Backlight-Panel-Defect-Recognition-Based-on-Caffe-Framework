import cv2
import numpy as np
#---------------------Usage---------------------------
'''
imdiff(img1,img2) return the coordinate of the defect point
'''
#--------------------Example--------------------------
'''
img1=cv2.imread("b2-1002.png",0)
img2=cv2.imread("a2-1002.bmp",0)
imdiff(img1,img2)
print imdiff(img1,img2)
'''
#--------------------Result---------------------------
'''
[[384, 1950], [395, 1941]]
'''
#-----------------------------------------------------
def imdiff(img1,img2):
	return [[i+33,j+33]for i in range(img1.shape[0])for j in range(img1.shape[1]) if img1[i][j]!=img2[i][j] and img1[i+66][j+66]!=img2[i+66][j+66] and img1[i][j+66]!=img2[i][j+66] and img1[i+66][j]!=img2[i+66][j]]
