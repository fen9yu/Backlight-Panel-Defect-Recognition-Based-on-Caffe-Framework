from __future__ import division
import numpy as np
import cv2
from binary_search_edge import search_v_edge
from binary_search_edge import search_h_edge

#the blacklight Panel has around 1600*900 pixels in photo if well positioned
#requires the photos in similiar pattern (photo size, distance, panel size)

black=60 #set grey scale under 60 as black

def edge_detect(img):
    center=[]
    center.append(img.shape[0]/2)
    center.append(img.shape[1]/2)
    upper=0
    bottom=img.shape[0]
    left=0
    right=img.shape[1]

    if img.item(center[0],center[1])<=black:
        if img.item(center[0],center[1]/2)>black:
            bottom=center[1]
            center[1]/=2
        else:
            top=center[1]
            center[1]=(center[1]+bottom)/2

    upper=search_h_edge(center[0],upper,center[1],img)
    bottom=search_h_edge(center[0],bottom,center[1],img)
    left=search_v_edge(center[1],left,center[0],img)
    right=search_v_edge(center[1],right,center[0],img)
    return (upper,center[1]),(bottom,center[1]),(center[0],left),(center[0],right)


#grey= img.item(img.shape[0]/2,img.shape[1]/2)
#black=img.item(img.shape[0]/2,img.shape[1]-600)
#print(grey)
#print(black)
#print(img.shape)
#for i in range(500,600):
#    print(str(2560-i)+": "+str(img.item(img.shape[0]/2,img.shape[1]-i)))