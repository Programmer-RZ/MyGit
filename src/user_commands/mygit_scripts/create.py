import git
import os

class Create:
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        self.name = arguments[0]
        self.path = path

        print(os.path.abspath(os.join(self.path, self.name)))

        self.repo = git.Repo.init(os.path.abspath(os.join(self.path, self.name)))

        return repo

def perform(path, arguments, tags, repo):
    return Create.run(path, arguments, tags, repo)