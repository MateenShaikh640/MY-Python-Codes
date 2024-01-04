import git

PATH = "C:\\Users\\Nadeem\\kube\\python\Python_visula_path\\py-git\\git-download"
GIT_LINK = "https://github.com/MateenShaikh640/MY-Python-Codes.git"
BRANCH_NAME = "mateen_automation_branch"

# Clone the repository or open it if it already exists
try:
    git.Repo.clone_from(GIT_LINK, PATH)
except git.exc.GitCommandError:
    pass

# Change working directory to the repository
repo = git.Repo(PATH)

# Checkout the branch or create it if it doesn't exist
try:
    repo.git.checkout("-b", BRANCH_NAME)
except git.exc.GitCommandError:
    repo.git.checkout(BRANCH_NAME)

# Add changes and commit
repo.git.add("--all")
repo.git.commit("-m", "my-demo commit")

# Set up remote tracking branch and pull changes
repo.git.pull("origin", BRANCH_NAME)

# Push changes and set the upstream branch
repo.git.push("--set-upstream", "origin", BRANCH_NAME)
