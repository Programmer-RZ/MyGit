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

        if len(arguments) == 0:
            raise RuntimeError("No commit message was inputted")

        for word in arguments:
            word.replace('"', "")

            message += word + " "

        self.stageAndCommit(message)

        print("Successfully staged and commited all changes")

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

        if arguments[0] == "create":
            self.newBranch(arguments[1])
            print(f"Successfully created branch {arguments[1]}")
        elif arguments[0] == "switch":
            self.switchBranch(arguments[1])
            print(f"Successfully switched to branch {arguments[1]}")
        elif arguments[0] == "delete":
            self.deleteBranch(arguments[1])
            print(f"Successfully deleted branch {arguments[1]}")
        elif arguments[0] == "merge":
            self.mergeBranch(arguments[1])
            print(f"Successfully merged branch {self.repo.head} with {arguments[1]}")

        return self.repo

    def listBranch(self):
        print(TextColor.CYAN)
        branches = self.repo.heads
        for branch in branches:
            print(branch.name)

        print(TextColor.END)

    def mergeBranch(self, name):
        # use CLI merge command because it has better merge conflict handling
        self.repo.git.execute(["git", "merge", f"{name}"])

    def newBranch(self, name):
        current = self.repo.create_head(name)
        current.checkout()

    def switchBranch(self, name):
        self.repo.git.checkout(name)

    def deleteBranch(self, name):
        self.repo.delete_head(name)


class Status(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.path = path
        self.repo = repo

        self.get_status()

        return self.repo

    def get_status(self):
        modified = self.repo.git.diff('--name-only').split('\n')
        untracked = self.repo.untracked_files

        print(TextColor.CYAN)

        print("Modified")
        for file in modified:
            print(" - " + file)

        print("Untracked")
        for file in untracked:
            print(" - " + file)

        print(TextColor.END)


class Sync(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        self.pull()
        self.push()

        return self.repo

    def pull(self):
        self.repo.git.pull('origin', self.repo.head)

    def push(self):
        self.repo.git.push('origin', self.repo.head)


class Publish(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        if not self.repo.remotes:
            self.createOrigin(arguments[0])

        self.publish()

        return self.repo

    def publish(self):
        self.repo.git.push('origin', self.repo.head)

    def createOrigin(self, url):
        self.repo.create_remote('origin', url)
