from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import numpy as np
import math

import pdb as pdb


parser = argparse.ArgumentParser()
parser.add_argument('file_name', type=str, help='Name of the tflite flatbuffer file to load.')

def main(file_name):

    tfh = open(file_name, 'rb')
    flatbuffer = tfh.read()
    tfh.close()

    print("Flatbuffer sise = ")



    pdb.set_trace()



if __name__ == '__main__':
    args = parser.parse_args()
    main(args.file_name)
