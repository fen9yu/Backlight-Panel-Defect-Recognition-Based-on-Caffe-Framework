from __future__ import division
import numpy as np
import cv2

black=60 #set grey scale under 60 as black

def search_v_edge(center,side,y,img):
    while(abs(center-side)>1):
        if img.item(round(y),round((center+side)/2))>black:
            center=(center+side)/2
        else:
            side=(center+side)/2
    return center

def search_h_edge(center,side,x,img):
    while(abs(center-side)>1):
        if img.item(round((center+side)/2),round(x))>black:
            center=(center+side)/2

        else:
            side=(center+side)/2
    return center