from tinyunit import __version__
from tinyunit.engine.result import result

class Formatter(object):

        def __init__(self):
                pass

        def format_start_case(self,case):
                return ""

        def format_end_case(self,case):
                return ""

        def format_start_set(self):
                return ""

        def format_end_set(self,cases):
                return ""

        def format_method_result(self,case,record):
                return ""

class DefaultFormatter(Formatter):

        def format_start_set(self):
            return "tinyunit %(version)s: Starting test run\n" % { 'version' : __version__ }

        def format_end_set(self):
            return "Test run complete.\n"

        def format_method_result(self,case,record,width=30):
                method=record.method

                if len(method)>width:
                    method = method[0:width-1] + "*"

                method=method.ljust(width,'.')
                return method + ":" + result.toString(record.result,True) + "\n"
                    
