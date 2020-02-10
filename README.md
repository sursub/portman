# portman

Learning.
Learning more. Don't use this project.

Git commands:

# Add a remote origin repository
git remote add origin https://github.com/sursub/portman.git
git push -u origin master

# Fix Emails.
git config --global user.email "29233777+sursub@users.noreply.github.com"
git commit --amend --reset-author


# Remove a folder from Git only, leave the folder on the file system:
git rm -r --cached __pycache__
git commit -m "removed cache"

# List Files
Git list all files
git ls-tree -r master --name-only