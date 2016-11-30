from __future__ import division
import numpy as np
import cv2
from binary_search_edge import search_v_edge
from binary_search_edge import search_h_edge
from edge_detect import edge_detect
import math

#the blacklight Panel has around 1600*900 pixels in photo if well positioned
#requires the photos in similiar pattern (photo size, distance, panel size)

black=60 #set grey scale under 60 as black

def angle_detect(img):
    up,down,left,right=edge_detect(img)
    up=up[0]
    down=down[0]
    left=left[1]
    right=right[1]
    center=[]
    center.append(img.shape[0]/2)
    center.append(img.shape[1]/2)

    left1=search_v_edge(center[1],0,0.8*up+0.2*down,img)
    left2=search_v_edge(center[1],0,0.2*up+0.8*down,img)

    return math.atan((left1-left2)/(0.6*up-0.6*down))
