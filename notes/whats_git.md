# What is Git?

Git is a form of VCS (Version Control System), it differs from other VCS through it's process of working with data. Conceptually, Git works through what is known as snapshots, unlike other VCS where all changes to files through versions are each stored as base files. Git sees the data as a series of snapshots, where whenever you commit a save to Git, it takes a snapshot of what the files look like in that instance and stores it as a snapshot. Git doesn't copy over files that obtain no changes between versions, instead pulling forward that file from previous snapshot, this is shown in the diagram below.

![](C:\Users\lukew\OneDrive\Documents\Sparta\Git_Snapshots.png)
Figure 1. Storing data through Git system of snapshots.

### Localisation 
Git works in a local system meaning you don't need to access an online repository such as GitHub, although you still can if chosen, it's not a necessity. All versions saved work locally. This makes Git work faster, not needing to link up to cloud net.

## The Three States of Git

- **Modified** - this is where you have created changes in the file, but git doesn't know what has changed. However, Git does know that changes have occurred, jut not the exact details
- **Staged** - this is where you know tell Git you have made changes and Git can see what the detail of these changes are, but the changes aren't yet saved
- **Committed** - this is where you save your changes to git and the files are safely stores in the local repo

Files are always found in one of these three stages!

![](C:\Users\lukew\OneDrive\Documents\Sparta\Git_Working_Tree.png)
Figure 6. Working tree of the Git directory

Figure 6. above shows the process of files within git, the working directory is files that you are working on, making changed. The staging area, where git knows the changes made and is ready to commit. .git directory / repo is where all the saved screenshots are found.


### CLI and Git Commands

`cd "folder directory"` - used to enter a folder within the current directory

`cd ..` - to back one stage in the directory

`pwd` - view your current directory path

`ls` - view files / folders in current directory `ls -a` to show all including hidden files / folders

`git init` - creates a local working directory in that folder

`git status` - shows which files are in working directory and staging area

`git add .` - adds all files in working directory to the staging area

`git commit -m "Enter the change to version"` - commits all files in staging area to git repo with a note explaining the change

`git log` - shows all versions of git commits including comments.

`.gitignore` - creates a file which you include any file type you want git to ignore.

`ctrl` + `C` - exit out of command line prompts.

