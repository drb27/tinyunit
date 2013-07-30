import sys
import os
import io

class StdoutBase(object):
        def __init__(self,fn):
                self._fn=fn

        def execute_wrapped(self,*args,**kwargs):
            return self._fn(*args,**kwargs)
        
class StdoutSuppression(StdoutBase):
    def __init__(self,fn):
        super(StdoutSuppression,self).__init__(fn)
        
    def __enter__(self):
        
        # Open devnull and redirect to stdout
        self._devnull = open(os.devnull,'w')
        self._stdout = sys.stdout
        sys.stdout = self._devnull
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout
        self._devnull.close()


class StdoutCapture(StdoutBase):
        def __init__(self,fn):
                super(StdoutCapture,self).__init__(fn)
                self.membuffer = io.StringIO()

        def __enter__(self):

                # Redirect stdout to the internal buffer
                self._stdout = sys.stdout
                sys.stdout = self.membuffer
                return self

        def __exit__(self,exc_type,exc_value, traceback):
                sys.stdout = self._stdout

