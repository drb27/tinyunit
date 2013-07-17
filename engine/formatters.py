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
            return "tinyunit vx.yz: Starting test run\n"

        def format_end_set(self):
            return "Test run complete.\n"

        def format_method_result(self,case,record):
                return "%(method)s ... %(result)d\n" % record.__dict__


