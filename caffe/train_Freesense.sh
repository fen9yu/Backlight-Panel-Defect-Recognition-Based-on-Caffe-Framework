#!/bin/bash
set -e

./build/tools/caffe train --solver=freesense_solver.prototxt $@
