from __future__ import division
import numpy as np
import cv2

black=60 #set grey scale under 60 as black

def search_v_edge(center,side,y,img):
    while(abs(center-side)>1):
        if img.item(int(round(y)),int(round((center+side)/2)))>black:
            center=(center+side)/2
        else:
            side=(center+side)/2
    return center

def search_h_edge(center,side,x,img):
    while(abs(center-side)>1):
        if img.item(int(round((center+side)/2)),int(round(x)))>black:
            center=(center+side)/2

        else:
            side=(center+side)/2
    return center