from repo import Repository
from sys import exit


# git actions
options = ["create repo template", "clone a repo"]
print("Git Actions: ")
for option in options:
    print(" - " + option)

action = ""
while action.lower() not in options:
    action = input("Choose a Git Action: ")
    if action == "./quit":
        exit()

print('\n')
action_index = options.index(action.lower())



# repo
my_repo = Repository(input("Repository name: "), "test_repos")

# action indexes
if action_index == 0:
    # create repo
    my_repo.create_repo()
    my_repo.create_gitignore()
    my_repo.create_readme()

    print("\nCreated .gitignore and README.md")

elif action_index == 1:
    # clone repo
    my_repo.clone_repo(input("URL: "), input("Branch: "), True)


# print git status
print("\nCurrent Git Status: ")
print(my_repo.git_status())
