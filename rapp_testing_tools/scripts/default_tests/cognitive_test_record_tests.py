#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright 2015 RAPP

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

# Authors: Konstantinos Panayiotou, Manos Tsardoulias
# contact: klpanagi@gmail.com, etsardou@iti.gr

import os
import timeit
import unittest


__path__ = os.path.dirname(os.path.realpath(__file__))

from RappCloud import RappPlatformAPI

class CognitiveTestRecordTests(unittest.TestCase):

    def setUp(self):
        self.ch = RappPlatformAPI()

    def test_recordReasoning(self):
        response = self.ch.cognitiveExerciseSelect('ReasoningCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(instance, 50)
        self.assertEqual('CognitiveTestPerformed' in response['performance_entry'], True)

    def test_recordAwareness(self):
        response = self.ch.cognitiveExerciseSelect('AwarenessCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(instance, 50)
        self.assertEqual('CognitiveTestPerformed' in response['performance_entry'], True)

    def test_recordArithmetic(self):
        response = self.ch.cognitiveExerciseSelect('ArithmeticCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(instance, 50)
        self.assertEqual('CognitiveTestPerformed' in response['performance_entry'], True)

    def test_recordWrongType(self):
        response = self.ch.cognitiveExerciseSelect('ArithmeticCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(3, 50)
        self.assertNotEqual(response['error'], u'')

    def test_recordWrongScoreType(self):
        response = self.ch.cognitiveExerciseSelect('ArithmeticCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(instance, '200')
        self.assertNotEqual(response['error'], u'')

    def test_recordWrongScoreValues(self):
        response = self.ch.cognitiveExerciseSelect('ArithmeticCts')
        self.assertEqual(response['error'], u'')
        self.assertNotEqual(response['test_instance'], u'')
        instance = response['test_instance']

        response = self.ch.cognitiveRecordPerformance(instance, 200)
        self.assertNotEqual(response['error'], u'')
        response = self.ch.cognitiveRecordPerformance(instance, -200)
        self.assertNotEqual(response['error'], u'')

if __name__ == "__main__":
    unittest.main()
