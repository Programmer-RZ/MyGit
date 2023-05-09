import os
import git

from repo import Repository


class CreateRepo(Repository):
    def __init__(self):

        super().__init__("", "")

    def run(self, path, arguments, tags, repo):
        self.name = arguments[0]
        self.path = path

        self.create_repo()
        for tag in tags:
            self.create_gitignore(tag)

        if len(tags) == 0:
            # no gitignore templates
            # so create an empty gitignore
            gitignore = open(f"{self.path}/{self.name}/.gitignore", "w")
            gitignore.close()

        self.create_readme()

        return self.repo

    # functions to create template repo
    def create_repo(self):
        # create a git repo
        #print(TextColor.CYAN)
        print("Initilizing Repository")
        self.repo = git.Repo.init(os.path.abspath(os.path.join(self.path, self.name)))

        print("Successfully initilized repository")
        #print(TextColor.END)

    def create_gitignore(self, gitignore_type):
        # create .gitignore
        #print(TextColor.CYAN)
        print(f"Creating .gitignore {gitignore_type}")
        with open(f"{self.path}/{self.name}/.gitignore", "w") as gitignore:
            # open .gitignore
            gitignore_types_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', '..'))

            gitignore_info = open(
                f"{gitignore_types_path}/gitignore_templates/{gitignore_type}.txt", "r")
            for line in gitignore_info.readlines():
                gitignore.write(line)

            gitignore_info.close()

        print(f"Successfully created .gitignore {gitignore_type}")
        #print(TextColor.END)

    def create_readme(self):
        # create README.md
        #print(TextColor.CYAN)
        print("Creating README.md")
        with open(f"{self.path}/{self.name}/README.md", "w") as readme:
            readme.write(f"# {self.name}")

        print("Successfully created README.md")
        #print(TextColor.END)
