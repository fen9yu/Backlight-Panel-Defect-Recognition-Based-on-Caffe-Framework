#!/bin/bash
rm -rf img_train_lmdb
~/caffe/caffe/build/tools/convert_imageset --shuffle \
--resize_height=64 --resize_width=64 \
~/train/ ~/train/result.txt img_train_lmdb 
#./train/ is picture dir;
#train/test_10_25.txt is picture namelist for train_set
#img_train_lmdb is the train_Set_lmdb's name
echo "train convert done"

rm -rf img_test_lmdb
~/caffe/caffe/build/tools/convert_imageset --shuffle \
--resize_height=64 --resize_width=64 \
~/test/ ~/test/test.txt img_test_lmdb
echo "test convert done"
