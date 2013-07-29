from sys import stdin

class UserInput(object):
    
    def getline(self):
        return stdin.readline()

def make_polite_conversation(ui):

    print("Hello, what is your name?")
    name = ui.getline().rstrip('\n')
    output = "Well hello there, " + name
    print(output)
    return output
