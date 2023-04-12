import git

class Repository:
    def __init__(self, name):
        self.gitignore_types = ["python_vscode"]

        self.name = name
        self.repo = None

    # functions to create template repo
    def create_repo(self):
        # create a git repo
        self.repo = git.Repo.init(self.name)

    def create_gitignore(self):
        # create .gitignore
        with open(f"{self.name}/.gitignore", "w") as gitignore:
            # get gitignore type
            print("\nGitignore Templates:")
            for type in self.gitignore_types:
                print(type)

            # repeat until user inputed type is in the list
            gitignore_type = ""
            while gitignore_type not in self.gitignore_types:
                gitignore_type = input("Choose a gitignore template: ")

            # open .gitignore
            gitignore_info = open(f"files/{gitignore_type}_gitignore.txt", "r")
            for line in gitignore_info.readlines():
                gitignore.write(line)

            gitignore_info.close()
    
    def create_readme(self):
        # create README.md
        with open(f"{self.name}/README.md", "w") as readme:
            readme.write(f"# {self.name}")
    

    # functions to clone a repo
    