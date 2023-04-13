from sys import exit

import repo


# autogit commands
child_commands = {"create" : repo.CreateRepo(), 
                  "clone" : repo.CloneRepo()}

parent_commands = {"autogit" : child_commands}

command = input("AutoGit command: ").split(" ")

try:   
    parent = command[0]
except IndexError:
    parent = " "

try:
    child = command[1]
except IndexError:
    child = " "

try:
    child_inputs = command[2:None]
except IndexError:
    child_inputs = [" "]

if parent in parent_commands.keys():
    if child in parent_commands[parent].keys():
        try:
            parent_commands[parent][child].run(child_inputs)
        except:
            print(f"command failed to execute")
    
    else:
        print(f"'{child}' is not recognized as an AutoGit command")
else:
    print(f"'{parent}' is not recognized as an AutoGit command")
