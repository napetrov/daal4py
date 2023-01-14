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
import subprocess
test_path = os.path.abspath(os.path.dirname(__file__))
unittest_data_path = os.path.join(test_path, "unittest_data")
python_executable = subprocess.run(['/usr/bin/which', 'python'],
    capture_output=True).stdout.decode().strip()

#Executing examples
examples_path = os.path.join(os.path.dirname(test_path), "examples", "sklearnex")
sys.path.insert(0, examples_path)
print('Executing sklernex examples from ', examples_path)
# Import and run the test_examples_sklernex.py script
subprocess.run([python_executable, "test_examples_sklernex.py"], cwd=examples_path)

examples_path = os.path.join(os.path.dirname(test_path), "examples", "daal4py")
sys.path.insert(0, examples_path)
print('Executing daal4py examples from ', examples_path)
# Import and run the test_examples_daal4py.py script
subprocess.run([python_executable, "test_examples_daal4py.py"], cwd=examples_path)
