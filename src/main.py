from sys import exit

import repo


# autogit commands
child_commands = {"create" : repo.CreateRepo(), 
                  "clone" : repo.CloneRepo()}

parent_commands = {"autogit" : child_commands}

command = input("AutoGit command: ")


try:
    parent = command.split(" ")[0]
except IndexError:
    parent = " "
try:
    child = command.split(" ")[1]
except IndexError:
    child = " "
try:
    child_inputs = command.split(" ")[2:None]
except IndexError:
    child_inputs = [" "]


try:
    parent_commands[parent][child].run(child_inputs)
except:
    print(f"Failed to execute '{command}'. Please check your spelling and try again")

//find binary search in python.
    