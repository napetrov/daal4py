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

import os
import subprocess
import sys
import unittest
from sklearnex._utils import get_sklearnex_version
test_path = os.path.abspath(os.path.dirname(__file__))
unittest_data_path = os.path.join(test_path, "unittest_data")
examples_path = os.path.join(os.path.dirname(test_path), "examples", "sklearnex")
sys.path.insert(0, examples_path)
os.chdir(examples_path)

python_executable = subprocess.run(['/usr/bin/which', 'python'], check=True, 
                                    capture_output=True).stdout.decode().strip()

# First item is major version - 2021,
# second is minor+patch - 0110,
# third item is status - B
sklearnex_version = get_sklearnex_version()
print('oneDAL version:', sklearnex_version)


def check_version(rule, target):
    if not isinstance(rule[0], type(target)):
        if rule > target:
            return False
    else:
        for rule_item in rule:
            if rule_item > target:
                return False
            if rule_item[0] == target[0]:
                break
    return True


def check_libraries(rule):
    for rule_item in rule:
        try:
            __import__(rule_item, fromlist=[''])
        except ImportError:
            return False
    return True


class TestExamples(unittest.TestCase):
    def setUp(self):
        self.path = examples_path

    def add_test(self, e, ver=(0, 0), req_libs=[]):

        @unittest.skipUnless(
            check_version(ver, sklearnex_version),
            str(ver) + " not supported in this library version " + str(sklearnex_version)
        )
        @unittest.skipUnless(
            check_libraries(req_libs),
            "cannot import required libraries " + str(req_libs)
        )
        def testit(self):
            result = subprocess.run([python_executable, e], cwd=self.path)
            self.assertEqual(result.returncode, 0)
        setattr(TestExamples, 'test_' + e, testit)


gen_examples = [
    ('patch_sklern', (2020, 'P', 0))
]

for example in gen_examples:
    TestExamples.add_test(*example)


if __name__ == '__main__':
    unittest.main()
