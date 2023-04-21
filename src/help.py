import os

from utils import TextColor


class Help:
    def __init__(self):
        pass

    def run(self, path, arguments, tags, repo):
        self.printHelp()

        return repo

    def printHelp(self):

        help_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..'))
        with open(f"{help_path}/help/help.txt", "r") as file:
            for line in file.readlines():
                print(line, end="\b")

        print("\n")
