import os

class Directory:
    def __init__(self):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.path = os.path.abspath(os.path.join(self.path, 'test_repos'))
    
    def getPath(self):
        return self.path
    
    def switchDir(self, path, arguments, tags, repo):
        self.path = os.path.abspath(os.path.join(path, arguments[0]))

        return None