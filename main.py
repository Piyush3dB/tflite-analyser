
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import math
import numpy as np
from tflite import Model

import pdb as pdb


parser = argparse.ArgumentParser()
parser.add_argument('model', type=str, help='Name of the tflite flatbuffer file to load.')


def main(model):
    tfh = open(model, 'rb')
    fb = tfh.read()
    tfh.close()

    model_bytes = bytearray(fb)
    print("Model {} = {} bytes".format(model, len(fb)))

    model = Model.Model.GetRootAsModel(model_bytes, 0)
    subgraph = model.Subgraphs(0)
    for i in range(subgraph.TensorsLength()):
        t = subgraph.Tensors(i)
        tens = {}
        tens["id"]=i
        tens["shape"]=t.ShapeAsNumpy()
        tens["name"]=t.Name().decode("ascii")
        #producer=None
        #consumers=[]
        tens["type"]=t.Type()
        print(tens)
        #pdb.set_trace()


    for i in range(subgraph.OperatorsLength()):
        op = subgraph.Operators(i)
        assert op.OutputsLength() <= 1
        has_output = op.OutputsLength() == 1
        inputs = [j for j in op.InputsAsNumpy()]
        assert len(inputs) > 0

        #tflite_op = TFLiteOperator(id=i, output=tensors[op.Outputs(0)] if has_output else None, inputs=inputs)
        #tflite_op.output.producer = tflite_op
        #for t in inputs:
        #    t.consumers.append(tflite_op)
        #operators.append(tflite_op)


    pdb.set_trace()



if __name__ == '__main__':
    args = parser.parse_args()
    main(args.model)
