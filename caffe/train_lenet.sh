#!/bin/bash
set -e

./build/tools/caffe train --solver=examples/images/freesense/freesense_solver.prototxt $@
