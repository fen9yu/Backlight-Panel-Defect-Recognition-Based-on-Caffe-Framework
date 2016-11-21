#!/bin/bash

caffe train \
-solver freesense_solver_11_21.prototxt \
-snapshot examples/mnist/lenet_iter_5000.solverstate

# snapshot is the state where you want to resume from~