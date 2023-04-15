import git

from repo import Repository

class CloneRepo(Repository):
    def __init__(self, path):
        name = ""
        super().__init__(name, path)
    
    def run(self, arguments, tags):
        self.name = arguments[0]
        self.clone_repo(arguments[1], tags[0], True)

    # functions to clone a repo
    def clone_repo(self, url, branch, recursive):

        class Progress(git.remote.RemoteProgress):
           def update(self, op_code, cur_count, max_count=None, message=''):
                print(self._cur_line)

        print("Cloning...")

        self.repo = git.Repo.clone_from(url, f"{self.path}/{self.name}", branch=branch, recursive=recursive, progress=Progress())
        print(f"Successfully cloned into {self.path}/{self.name}")