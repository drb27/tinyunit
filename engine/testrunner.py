from ..core.testcase import TestCase
from .inspector import Inspector
from .formatters import XmlFormatter,DefaultFormatter
from .result import result
from .stats import Stats

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
        return rec

def runcase(case):
    """ Runs all the tests in the given test case"""

    # create a recorder
    recorder = TestRecorder()

    # create a stats object
    s = Stats()

    # create a default formatter
    f = XmlFormatter()

    # start the case
    print(f.format_start_set(),end="")
    print(f.format_start_case(case),end="")

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
            record = recorder.record(case,testname,r)
            s.addResult(r)

            # Display progress
            print(f.format_method_result(case,record),end="")

    # end the case
    print(f.format_end_case(case),end="")
    print(f.format_end_set(),end="")
    print(str(s))
    return recorder
