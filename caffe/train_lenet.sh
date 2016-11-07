#!/bin/bash
set -e

~/caffe/caffe/build/tools/caffe train --solver=examples/images/freesense/freesense_solver.prototxt $@
