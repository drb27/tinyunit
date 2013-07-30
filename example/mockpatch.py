from sys import stdin

class UserInput(object):
    
    def getline(self):
        return stdin.readline()

def make_polite_conversation(capitalise=True):

    ui = UserInput()
    #print("Hello, what is your name?")
    name = ui.getline().rstrip('\n')
    output = "Well hello there, " + name
    if capitalise:
        output = output.upper()
    print(output)
    return output
