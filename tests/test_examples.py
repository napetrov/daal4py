#===============================================================================
# Copyright 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import unittest
import os
import sys
test_path = os.path.abspath(os.path.dirname(__file__))
unittest_data_path = os.path.join(test_path, "unittest_data")

#Executing examples
examples_path = os.path.join(os.path.dirname(test_path), "examples", "sklearnex")
sys.path.insert(0, examples_path)
os.chdir(examples_path)
print('Executing sklernex examples from ', examples_path)
# Import and run the test_examples_sklernex.py script
import test_examples_sklernex
sklernex_suite = unittest.TestLoader().loadTestsFromModule(test_examples_sklernex)
unittest.TextTestRunner().run(sklernex_suite)

examples_path = os.path.join(os.path.dirname(test_path), "examples", "daal4py")
sys.path.insert(0, examples_path)
os.chdir(examples_path)
print('Executing daal4py examples from ', examples_path)
# Import and run the test_examples_daal4py.py script
import test_examples_daal4py
daal4py_suite = unittest.TestLoader().loadTestsFromModule(test_examples_daal4py)
unittest.TextTestRunner().run(daal4py_suite)
