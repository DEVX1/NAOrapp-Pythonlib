#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MIT License (MIT)

#Copyright (c) <2014> <Rapp Project EU>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

# Authors: Konstantinos Panayiotou, Manos Tsardoulias
# contact: klpanagi@gmail.com, etsardou@iti.gr

import sys
import os
import timeit
import argparse

__path__ = os.path.dirname(os.path.realpath(__file__))

## ------ Access the RappCloud python module ------- ##
module_path = __path__ + '/../../python'
sys.path.append(module_path)
from RappCloud import *

class RappInterfaceTest:

  def __init__(self):
    self.rappCloud = RappCloud()
    self.file_uri = __path__  + '/../test_data/Lenna.png'
    self.valid_faces_up_left = [ {'y': 200.0, 'x': 212.0, 'z': 0.0} ]
    self.valid_faces_down_right = [ {'y': 379.0, 'x': 391.0, 'z': 0.0} ]

  def execute(self):

    start_time = timeit.default_timer()
    response = self.rappCloud.face_detection(self.file_uri)
    end_time = timeit.default_timer()
    self.elapsed_time = end_time - start_time
    return self.validate(response)

  def validate(self, response):
    
    faces_up_left = response['faces_up_left']
    faces_down_right = response['faces_down_right']
    error = response['error']

    if error != "0":
      return [error, self.elapsed_time]
    if self.valid_faces_up_left == faces_up_left and \
        self.valid_faces_down_right == faces_down_right:
      return [True, self.elapsed_time]
    else:
      return ["Unexpected result", self.elapsed_time]

