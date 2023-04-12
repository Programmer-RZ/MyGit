import git

class Repository:
    def __init__(self, name, path):
        self.gitignore_types = ["python_vscode"]

        self.name = name
        self.path = path
        self.repo = None

    # functions to create template repo
    def create_repo(self):
        # create a git repo
        self.repo = git.Repo.init(self.path + "/" + self.name)

    def create_gitignore(self):
        # create .gitignore
        with open(f"{self.path}/{self.name}/.gitignore", "w") as gitignore:
            # get gitignore type
            print("\nGitignore Templates:")
            for type in self.gitignore_types:
                print(type)

            # repeat until user inputed type is in the list
            gitignore_type = ""
            while gitignore_type not in self.gitignore_types:
                gitignore_type = input("Choose a gitignore template: ")

            # open .gitignore
            gitignore_info = open(f"gitignore_templates/{gitignore_type}_gitignore.txt", "r")
            for line in gitignore_info.readlines():
                gitignore.write(line)

            gitignore_info.close()
    
    def create_readme(self):
        # create README.md
        with open(f"{self.path}/{self.name}/README.md", "w") as readme:
            readme.write(f"# {self.name}")
    

    # functions to clone a repo
    def clone_repo(self, url, branch, recursive):
        print("Cloning...")

        try:
            self.repo = git.Repo.clone_from(url, f"{self.path}/{self.name}", branch=branch, recursive=recursive)
            print(f"Successfully cloned into {self.path}/{self.name}")

        except git.exc.GitCommandError:
            print(f"fatal: unable to access '{url}'")
    