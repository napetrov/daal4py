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

# Import and run the test_examples_sklernex.py script
import test_examples_sklernex
sklernex_suite = unittest.TestLoader().loadTestsFromModule(test_examples_sklernex)

# Import and run the test_examples_daal4py.py script
import test_examples_daal4py
daal4py_suite = unittest.TestLoader().loadTestsFromModule(test_examples_daal4py)

# Create a combined test suite containing the tests from both scripts
combined_suite = unittest.TestSuite([sklernex_suite, daal4py_suite])

# Run the combined test suite
unittest.TextTestRunner().run(combined_suite)
