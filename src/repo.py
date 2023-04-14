import git
import os

class Repository:
    def __init__(self, name, path):
        self.sub_actions = []

        self.name = name
        self.path = path
        self.repo = None

class CreateRepo(Repository):
    def __init__(self, path):
        name = ""

        super().__init__(name, path)
    
    def run(self, arguments, tags):
        self.name = arguments[0]

        self.create_repo()
        self.create_gitignore(tags[0])
        self.create_readme()

    # functions to create template repo
    def create_repo(self):
        # create a git repo
        print("Initilizing Repository")
        self.repo = git.Repo.init(self.path + "/" + self.name)

        print("Successfully initilized repository")

    def create_gitignore(self, gitignore_type):
        # create .gitignore
        print("Creating .gitignore")
        with open(f"{self.path}/{self.name}/.gitignore", "w") as gitignore:
            # open .gitignore
            gitignore_types_path = os.path.join(self.path, "..")

            gitignore_info = open(f"{gitignore_types_path}/gitignore_templates/{gitignore_type}_gitignore.txt", "r")
            for line in gitignore_info.readlines():
                gitignore.write(line)

            gitignore_info.close()

        print("Successfully created .gitignore")
    
    def create_readme(self):
        # create README.md
        print("Creating README.md")
        with open(f"{self.path}/{self.name}/README.md", "w") as readme:
            readme.write(f"# {self.name}")

        print("Successfully created README.md")


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
    