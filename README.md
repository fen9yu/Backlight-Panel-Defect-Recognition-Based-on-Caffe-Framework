# Backlight-Panel-Defect-Recognition-Based-on-Caffe-Framework
UM-SJTU JI VE450 capstone project

* Use cut_img&mark_defect.py to cut and mark premarked images for training.  
  * Put the images into directories by date. e.g.: 2016-9-17  
The folder should include images starting with "a" and "b" correspondingly. e.g.: a1-0001-0101.bmp and b1-0001-0101.png should be in the folder at the same time.  
  * cut_img&mark_defect.py and diffdetect.py should be placed in the parent directory of the images, in the same directory of the folders named by date. e.g.: 2016-9-17 2016-9-18 cut_img&mark_defect.py diffdetect.py  
  * In the terminal, cd to one date folder which includes images of that day, then run cut_img&mark_defect.py in the parent directory. The python script should create cut images in the parent direct directory of the images, which is same folder where the script is. A text file named train which contains the marking information will be created mean while.  
  * e.g.:  
`$ cd 2016-9-17`  
`$ python ../cut_img&mark_defect.py`  
   
   
* Use cut_img.py to cut "raw" images.  
It will create a folder for every "raw" image to put the cut images. May be the behavor will be changed later.  
