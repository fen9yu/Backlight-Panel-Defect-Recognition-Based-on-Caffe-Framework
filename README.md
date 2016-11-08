# Backlight-Panel-Defect-Recognition-Based-on-Caffe-Framework
UM-SJTU JI VE450 Capstone Project

* Use `cut_img_mark_defect.py` to cut and mark premarked images for training. You can also set an offset by using command line argument.  
  * Put the images into directories by date. e.g.: `2016-9-17`  
The folder should include images starting with "a" and "b" correspondingly. e.g.: `a1-0001-0101.bmp` and `b1-0001-0101.png` should be in the folder at the same time.  
  * `cut_img_mark_defect.py` and `diffdetect.py` should be placed in the parent directory of the images, in the same directory of the folders named by date.  
  e.g.:  
  `$ ls`  
  `2016-9-17 2016-9-18 cut_img_mark_defect.py diffdetect.py`  
  * In the terminal, cd to one date folder which includes images of that day, then run cut_img_mark_defect.py in the parent directory. The python script should create cut images in the parent direct directory of the images, which is same folder where the script is. A text file named train which contains the marking information will be created mean while.  
  * You can set an offset by using command line argument. `python cut_img_mark_defect.py <offset>`. If you do not type the offset, the default will be 0. Also, the offset should be less than the length of side.  
  * e.g.:  
  `$ cd 2016-9-17`  
  `$ python ../cut_img_mark_defect.py`  
  `$ python ../cut_img_mark_defect.py 32`
   
   
* Use `cut_img_mark_defect_only1.py` to only cut and mark defected premarked images for training, use it in the same way as `cut_img_mark_defect.py`  

	 
* Use `cut_img.py` to cut "raw" images.  
It will create a folder for every "raw" image to put the cut images. May be the behavor will be changed later.  

* Use `choose.py` to randomly choose defect and normal images by a certain rate (default==5).  
Use this script after you cut images by using `cut_img*.py` in the same folder. It will generate a `result.txt` from `train.txt`.  
	* e.g.:  
	`$ cd 2016-9-17`   
	`$python ../choose.py`

