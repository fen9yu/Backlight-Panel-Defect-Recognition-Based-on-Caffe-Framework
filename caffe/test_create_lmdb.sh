#!/bin/bash

rm -rf img_test_lmdb
~/caffe/caffe/build/tools/convert_imageset --shuffle \
--resize_height=18 --resize_width=18 \
~/dr3/_a1-1001.bmp/ ~/dr3/_a1-1001.bmp/test.txt img_test_lmdb
echo "test convert done"
