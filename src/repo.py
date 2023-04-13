import git

class Repository:
    def __init__(self, name, path):
        self.sub_actions = []

        self.name = name
        self.path = path
        self.repo = None

class CreateRepo(Repository):
    def __init__(self):
        self.gitignore_types = ["python_vscode"]
        name = ""
        path = "test_repos"

        super().__init__(name, path)
    
    def run(self, inputs):
        self.name = inputs[0]

        self.create_repo()
        self.create_gitignore(inputs[1])
        self.create_readme()

    # functions to create template repo
    def create_repo(self):
        # create a git repo
        self.repo = git.Repo.init(self.path + "/" + self.name)

    def create_gitignore(self, gitignore_type):
        # create .gitignore
        with open(f"{self.path}/{self.name}/.gitignore", "w") as gitignore:
            # open .gitignore
            gitignore_info = open(f"gitignore_templates/{gitignore_type}_gitignore.txt", "r")
            for line in gitignore_info.readlines():
                gitignore.write(line)

            gitignore_info.close()
    
    def create_readme(self):
        # create README.md
        with open(f"{self.path}/{self.name}/README.md", "w") as readme:
            readme.write(f"# {self.name}")
    


class CloneRepo(Repository):
    def __init__(self):
        name = ""
        path = "test_repos"
        super().__init__(name, path)
    
    def run(self, inputs):
        self.name = inputs[0].split('/')[-1]

        self.clone_repo(inputs[0], inputs[1])

    # functions to clone a repo
    def clone_repo(self, url, branch, recursive):
        print("Cloning...")

        try:
            self.repo = git.Repo.clone_from(url, f"{self.path}/{self.name}", branch=branch, recursive=recursive)
            print(f"Successfully cloned into {self.path}/{self.name}")

        except git.exc.GitCommandError:
            print(f"fatal: unable to access '{url}'")
    