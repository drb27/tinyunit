from .result import result,bcolors

class Stats(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.results = {}        

    def addResult(self,r):
        if not r in self.results.keys(): 
            self.results[r] = 0

        self.results[r] += 1    

    def __str__(self):
        strlist = [str(self.results[x]) + " " + result.toString(x,True) for x in self.results.keys()]
        return ",".join(strlist)
