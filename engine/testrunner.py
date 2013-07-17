from ..core.testcase import TestCase
from .inspector import Inspector

class result(object):
    success=0
    failure=1
    error=2
    unknown=3

def runcase(case):
    """ Runs all the tests in the given test case"""

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
            if r==result.success:
                print(".",end="")
            if r==result.failure:
                print("F",end="")
            if r==result.error:
                print("E",end="")

