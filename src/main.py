from repo import Repository
from createRepo import CreateRepo
from cloneRepo import CloneRepo
from editRepo import OpenRepo, StageCommit

from directory import Directory
from utils import TextColor

# fix Windows ANSI escape handling
from colorama import init
init()

dir = Directory()
repo = None

# autogit commands
autogit_commands = {"create" : CreateRepo().run, 
                  "clone" : CloneRepo().run,
                  "open" : OpenRepo().run,
                  "stageCommit" : StageCommit().run 
                  }

autodir_commands = {"cd" : dir.switchDir}

parent_commands = {"autogit" : autogit_commands,
                   "autodir" : autodir_commands
                   }

while True:
    print(TextColor.LIGHT_GREEN + dir.getPath() + TextColor.END)
    command = input(">> ")

    if command == "autogit/.quit":
        break
    
    # split the command
    try:
        parent = command.split(",")[0]
    except IndexError:
        parent = " "
    try:
        child = command.split(",")[1]
    except IndexError:
        child = " "

    try:
        user_inputs = command.split(",")[2:None]
    except IndexError:
        user_inputs = [" "]

    arguments = []
    tags = []
    for i in user_inputs:
        if i[0:2] == "--":
            tags.append(i[2:None])
        
        else:
            arguments.append(i)

    # execute it
    try:
        repo = parent_commands[parent][child](dir.getPath(), arguments, tags, repo)
        

    except Exception as e:
        print(f"{TextColor.LIGHT_RED} Failed to execute '{command}'. {e}{TextColor.END}")
    