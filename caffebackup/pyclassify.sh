#!/bin/bash
#
python python/classify_liang.py --model_def Freesense_tt_1107_deploy.prototxt --pretrained_model snapshot_201611192034_09_trans_iter_232000.caffemodel --center_only $1  foo
