python cut_img.py
cd caffe
cd ../../_a1-1001.bmp
python ../backlight/caffe/create_test.py
cd ../backlight/caffe
chmod +x test_create_lmdb.sh
./test_create_lmdb.sh &> rubbish
chmod +x test_Freesense.sh
./test_Freesense.sh > testresult 2>rubbish
python classify.py
rm testresult
rm rubbish