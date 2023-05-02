from repo import Repository

import os
import importlib

class AddCommands(Repository):
    def __init__(self):
        super().__init__(" ", " ")
    
    def run(self, path, arguments, tags, repo):
        self.repo = repo

        self.addCommand(path, arguments[0])

        return repo
    
    def addCommand(self, path, name):
        # create a new .mygit script with the appropiate name
        # get name of file in path
        file = name
        scripts_path = os.path.abspath(os.join(os.path.dirname(__file__), "mygit_scripts"))
        with open(f"{scripts_path}\\{file}", "w") as script:
            # copy contents of user inputed file to script
            user_script = open(f"{path}\\{name}", "r")
            contents = user_script.read()

            # write the contents to the script
            script.write(contents)

            user_script.close()

class RunCommands(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        python_script = importlib.import_module(f"user_commands.mygit_scripts.{arguments[0]}")
        self.repo = python_script.perform(path, arguments[1:None], tags, repo)

        return repo

class CreateTemplate(Repository):
    def __init__(self):
        super().__init__(" ", " ")

    def run(self, path, arguments, tags, repo):
        self.repo = repo

        return repo
        
