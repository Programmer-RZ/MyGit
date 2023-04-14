from sys import exit

from repo import CreateRepo, CloneRepo
from directory import Directory

dir = Directory()

# autogit commands
child_commands = {"create" : CreateRepo(dir.getPath()).run, 
                  "clone" : CloneRepo(dir.getPath()).run,
                  "cd" : dir.switchDir}

parent_commands = {"autogit" : child_commands}


while True:
    command = input(dir.getPath() + " ")

    if command == "autogit ./quit":
        break
    
    # split the command
    try:
        parent = command.split(" ")[0]
    except IndexError:
        parent = " "
    try:
        child = command.split(" ")[1]
    except IndexError:
        child = " "

    try:
        user_inputs = command.split(" ")[2:None]
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
        parent_commands[parent][child](arguments, tags)
    except Exception as e:
        print(f"Failed to execute '{command}'. {e}")
    