#!/bin/bash
set -e

~/caffe/caffe/build/tools/caffe train --solver=freesense_solver.prototxt $@
