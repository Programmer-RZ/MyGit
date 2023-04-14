import os

class Directory:
    def __init__(self):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.path = os.path.abspath(os.path.join(self.path, 'test_repos'))
    
    def getPath(self):
        return self.path
    
    def switchDir(self, arguments, tags):
        self.path = os.path.abspath(os.path.join(self.path, arguments[0]))