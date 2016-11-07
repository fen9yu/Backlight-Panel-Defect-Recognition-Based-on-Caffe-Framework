#!/bin/bash
set -e

t=`date +%Y%m%d%H%M`
sed -i "s/\"snapshot_[0-9]*/\"snapshot_$t/" freesense_solver.prototxt
~/caffe/caffe/build/tools/caffe train --solver=freesense_solver.prototxt $@
