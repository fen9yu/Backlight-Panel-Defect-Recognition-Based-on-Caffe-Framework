#!/bin/bash
rm -rf img_train_lmdb
~/caffe/caffe/build/tools/convert_imageset --shuffle \
--resize_height=18 --resize_width=18 \
~/feng/Img/ ~/feng/Img/result.txt img_train_lmdb 
#./train/ is picture dir;
#train/test_10_25.txt is picture namelist for train_set
#img_train_lmdb is the train_Set_lmdb's name
echo "train convert done"

rm -rf img_test_lmdb
~/caffe/caffe/build/tools/convert_imageset --shuffle \
--resize_height=18 --resize_width=18 \
~/feng/test/ ~/feng/test/result.txt img_test_lmdb
echo "test convert done"
