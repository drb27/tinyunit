from ..core.testcase import TestCase
from .inspector import Inspector

class result(object):
    success=0
    failure=1
    error=2
    unknown=3

class TestRecord(object):

    def __init__(self,method,result):
        self.method=method
        self.result=result

class TestRecorder(object):

    def __init__(self):
        self.casemap= {}
    
    def record(self,case,testmethod,result):
        rec=TestRecord(testmethod,result)
        
        if not case in self.casemap.keys():
            self.casemap[case]=[]
        
        self.casemap[case].append(rec)

def runcase(case):
    """ Runs all the tests in the given test case"""

    # create a recorder
    recorder = TestRecorder()

    # Discover the tests in the test case
    i=Inspector()
    tests=i.testmethods(case)

    # Execute each
    for testname in tests:
        r = result.unknown

        try:
            # Convert method name to actual method
            test = getattr(case,testname)       
     
            # Execute the method
            test()
            r=result.success
        
        except TestCase.AssertFailureException as e:
            r = result.failure
        except Exception as e:
            r = result.error
            raise e
        finally:

            # record the result
            recorder.record(case,testname,r)

            # Display progress
            if r==result.success:
                print(".",end="")
            if r==result.failure:
                print("F",end="")
            if r==result.error:
                print("E",end="")

    return recorder
