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

        def format_stats(self,results):
                return ""

class XmlFormatter(Formatter):

    def __init__(self):
        pass

    def format_start_set(self):
        strs=[]
        strs.append("<?xml version='1.0' encoding='ISO-8859-1'?>")
        strs.append("<?xml-stylesheet type='text/xsl' href='results.xsl'?>")
        strs.append("<testrun>\n")

        return "\n".join(strs) 

    def format_start_case(self,case):
        return "<testcase name='%s'>\n" % case.__class__.__name__ 


    def format_method_result(self,case,record):
        strs=[]
        strs.append("<method>")
        strs.append("<name>%s</name>" % record.method)
        strs.append("<result>%s</result>" % result.toString(record.result) )
        strs.append("</method>\n")

        return "\n".join(strs)

    def format_end_case(self,cases):
        return "</testcase>\n"

    def format_end_set(self):
        return "</testrun>\n"

    def format_stats(self,results):
        return results.toXml() + "\n"

class DefaultFormatter(Formatter):

        def format_start_set(self):
            return "tinyunit %(version)s: Starting test run\n" % { 'version' : __version__ }

        def format_end_set(self):
            return "Test run complete.\n"

        def format_method_result(self,case,record,width=40):
                method=record.method

                if len(method)>width:
                    method = method[0:width-1] + "*"

                method=method.ljust(width,'.')
                return method + ":" + result.toString(record.result,True) + "\n"
                    
        def format_start_case(self,case):
            return "-----> Starting case %s \n" % case.__class__.__name__

        def format_end_case(self,case):
            return "Case complete.\n"

        def format_stats(self,results):
            return str(results) + "\n"
