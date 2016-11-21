echo 'Cutting image...'
python cut_img.py
cd caffe
cd ../../_a1-1001.bmp
echo 'Creating test.txt...'
python ../backlight/caffe/create_test.py
cd ../backlight/caffe
chmod +x test_create_lmdb.sh
echo 'Creating img_test_lmdb...'
./test_create_lmdb.sh &> rubbish
chmod +x test_Freesense.sh
echo 'Testing...'
./test_Freesense.sh > testresult 2>rubbish
echo 'Classifying the whole image...'
echo '-----------------------------------------'
python classify.py
echo '-----------------------------------------'
echo 'Cleaning...'
rm testresult
rm rubbish