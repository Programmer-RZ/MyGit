import os
import git

from repo import Repository

class CreateRepo(Repository):
    def __init__(self, path):
        name = ""

        super().__init__(name, path)
    
    def run(self, arguments, tags):
        self.name = arguments[0]

        self.create_repo()
        for tag in tags:
            self.create_gitignore(tag)
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
