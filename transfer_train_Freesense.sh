#!/bin/bash
set -e

#Fine Tune Syntax

./build/tools/caffe train -solver freesense_solver_11_07.prototxt -weights snapshot_11_07_c3ip1_iter_3000.caffemodel

#First parameter: tools directory
#Second parameter: "train"
#Third parameter: -solver definition(*.prototxt)
#Fourth ~ : weights definition(*.model)