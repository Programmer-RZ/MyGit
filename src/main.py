from repo import Repository



# git actions
options = ["Create Repo template"]
print("Git Actions: ")
for option in options:
    print(option)

action = ""
while action not in options:
    action = input("Choose a Git Action: ")

action_index = options.index(action)



# repo
my_repo = Repository(input("Repository name: "))


# action indexes
if action_index == 0:
    # create repo
    my_repo.create_repo()
    my_repo.create_gitignore()
    my_repo.create_readme()
