import sys

class ProgressBar:
    def __init__(self, stages, status=''):
        self.size = len(stages)   # initialize the total size of the process to be tracked in the progress bar
        self.current = -1   # current stage of the process
        self.stages = stages
        self.status = status
        self.backspace = 0

    def updateBar(self):
        self.current += 1
        try:
            prog = int((float(self.current)/self.size)*100)
        except:
            prog = 0
        try:
            s = '\r' + self.status + str(self.stages[self.current]) + ' ['+'='*prog + ' '*(100-prog) + ']' + str(prog) + '%'  # \r used to overwrite the existing progress bar
            sys.stdout.write(s)  # using sys.stdout.write, we can print to current line
            sys.stdout.flush()
            self.backspace = len(s)
        except:
            self.endBar()

    def startBar(self):
        self.updateBar()

    def endBar(self):
        self.current += 1
        if self.current > self.size:
            self.current = self.size
        try:
            prog = int((float(self.current) / self.size) * 100)
        except:
            prog = 0
        s = '\r[' + '=' * prog + ' ' * (100 - prog) + ']' + str(prog) + '%\n'
        sys.stdout.write(s)
        sys.stdout.flush()