import git, os

from repo import Repository

class testcommand(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        return repo

def run(path, arguments, tags, repo):
    testcommand.run(testcommand, path, arguments, tags, repo)