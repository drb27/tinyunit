#!/usr/bin/env python3
import argparse
import os
import sys

from tinyunit.client import *

import mockpatch
from mockpatch import make_polite_conversation

class RedirectStdout(object):
    def __init__(self,stdout):
        self._stdout = stdout

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self._stdout

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        sys.stdout = self.old_stdout


class MockUserInput(Mock):

    def __init__(self):
        super(MockUserInput,self).__init__()

    def getline(self):
        return "FRED\n"

class MockPatchTests(TestCase):
        
        @testmethod
        @patch('mockpatch.UserInput','__main__.MockUserInput')
        def testMakePoliteConversation(self):

                # Ensure we're starting from a clean mock object context
                Mock.reset_context()

                # Temporarily silence stdout
                f=open(os.devnull, 'w')

                try:
                    def _decorated():
                        with RedirectStdout(f):
                            return make_polite_conversation()

                    # Check the output
                    self.assertEquals('Well hello there, FRED', _decorated())                
                finally:
                    f.close()

                # Retrieve the created mock object from the context
                instances = Mock.get_instances_of(MockUserInput)

                # Check that only one object was created
                self.assertEquals(1,len(instances))

                # Check that UserInput.getline was called just once
                self.assertEquals(1,instances[0].calls())

if __name__=='__main__':

        # Check to see if XML output is enabled
        parser = argparse.ArgumentParser()
        parser.add_argument("-x","--xml",help="Output XML report", action="store_true")
        args = parser.parse_args()

        # Create an inspector to retrieve test cases automatically
        i=Inspector()
        
        # Run a set of test cases
        runset(i.cases(), enable_xml=args.xml)
