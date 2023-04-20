import git

from repo import Repository

from utils import TextColor

class OpenRepo(Repository):
    def __init__(self):
        super().__init__("", "")
    
    def run(self, path, arguments, tags, repo):
        self.repo = git.Repo(f"{path}/{arguments[0]}")

        return self.repo

class StageCommit(Repository):
    def __init__(self):
        super().__init__("", "")
    
    def run(self, path, arguments, tags, repo):
        self.repo = repo

        message = ""

        for word in arguments:
            word.replace('"', "")

            message += word + " "

        self.stageAndCommit(message)

        return self.repo
    
    def stageAndCommit(self, message):
        self.repo.git.add(".")

        self.repo.index.commit(message)

class Branch(Repository):
    def __init__(self):
        super().__init__("", "")
    
    def run(self, path, arguments, tags, repo):
        self.repo = repo

        # list all branches
        if arguments[0] == "list":
            self.listBranch()
            return self.repo

        if tags[0] == "new":
            self.newBranch(arguments[0])
        elif tags[0] == "switch":
            self.switchBranch(arguments[0])
        elif tags[0] == "delete":
            self.deleteBranch(arguments[0])
        
        return self.repo
    
    def listBranch(self):
        print(TextColor.CYAN)
        branches = self.repo.heads
        for branch in branches:
            print(branch.name)
        
        print(TextColor.END)

    def newBranch(self, name):
        current = self.repo.create_head(name)
        current.checkout()
    
    def switchBranch(self, name):
        self.repo.git.checkout(name)
    
    def deleteBranch(self, name):
        self.repo.delete_head(name)