import sys
import os

class RedirectStdout(object):
    def __init__(self,stdout):
        self._stdout = stdout

    def __enter__(self):
        self.old_stdout = sys.stdout
        sys.stdout = self._stdout

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        sys.stdout = self.old_stdout

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
        self._fn(*args,**kwargs)
