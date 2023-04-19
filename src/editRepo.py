import git

from repo import Repository

class OpenRepo(Repository):
    def __init__(self):
        super().__init__("", "")
    
    def run(self, path, arguments, tags, repo):
        self.repo = git.Repo(path)

        return self.repo

class StageCommit(Repository):
    def __init__(self):
        super().__init__("", "")
    
    def run(self, path, arguments, tags, repo):
        self.repo = repo

        message = arguments[0]

        self.stageAndCommit(message)

        return self.repo
    
    def stageAndCommit(self, message):
        self.repo.git.add(update=True)

        self.repo.index.commit(message)