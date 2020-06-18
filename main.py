
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import math

from tflite import Model

import pdb as pdb


parser = argparse.ArgumentParser()
parser.add_argument('model', type=str, help='Name of the tflite flatbuffer file to load.')


def main(model):
    tfh = open(model, 'rb')
    fb = tfh.read()
    tfh.close()

    print("Flatbuffer size = ")
    pdb.set_trace()



if __name__ == '__main__':
    args = parser.parse_args()
    main(args.model)
