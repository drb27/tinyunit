#!/usr/bin/env python3
import argparse
import os
import sys

from tinyunit.client import *
from tinyunit.core.util import StdoutSuppression,StdoutCapture

import mockpatch
from mockpatch import make_polite_conversation

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

                # Execute the method under test with output suppressed
                # with StdoutSuppression(make_polite_conversation) as suppressor:
                #     self.assertEquals('Well hello there, FRED',suppressor.execute_wrapped(False))

                with StdoutCapture(make_polite_conversation) as capture:
                        capture.execute_wrapped(False)
                        self.assertEquals('Well hello there, FRED\n',capture.membuffer.getvalue())

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
