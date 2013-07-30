import sys
import os

class StdoutSuppression(object):
    def __init__(self,fn):
        self._fn = fn

    def __enter__(self):
        
        # Open devnull and redirect to stdout
        self._devnull = open(os.devnull,'w')
        self._stdout = sys.stdout
        sys.stdout = self._devnull
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout
        self._devnull.close()

    def execute_suppressed(self,*args,**kwargs):
        return self._fn(*args,**kwargs)
