from createRepo import CreateRepo
from cloneRepo import CloneRepo
from directory import Directory

dir = Directory()

# autogit commands
autogit_commands = {"create" : CreateRepo().run, 
                  "clone" : CloneRepo().run
                  }

autodir_commands = {"cd" : dir.switchDir}

parent_commands = {"autogit" : autogit_commands,
                   "autodir" : autodir_commands
                   }

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
        parent_commands[parent][child](dir.getPath(), arguments, tags)
    except Exception as e:
        print(f"Failed to execute '{command}'. {e}")
    