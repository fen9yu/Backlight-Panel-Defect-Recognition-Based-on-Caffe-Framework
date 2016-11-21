#!/bin/bash
set -e



~/caffe/caffe/build/tools/caffe test -model=Freesense_tt_1121.prototxt -weights=snapshot_201611211542_21_trans_iter_218000.caffemodel $@
