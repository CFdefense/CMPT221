# Welcome to CMPT 221L: Software Development 2!

In this repository, you will find all of your labs for the semester. We will be leveraging Github to submit and review assignments. This will help us stay organized and expose you to some real-life best practices.

In this README, I've provided everything you need to get yourself set up for the semester, along with some helpful reminders.

# Getting Started

### Step 1: Download VSCode
You'll need a code editor to actually complete these labs. If you already have VSCode or another editor of your choosing, you can skip this step.

I strongly recommend using VSCode, as that's what I'll be using for demonstrations throughout the semester, but you can use whatever best suits you.

I like VSCode because it has a bunch of helpful features and (optional) plugins which will make navigating this course a breeze. You can download VSCode here: https://code.visualstudio.com/download

The first feature I recommend enabling is the `code .` feature. This will enable you to open VSCode from the command line by adding VSCode to your PATH (your PATH is an environment variable that tells your computer where things are installed!).
1. Open VSCode
2. Click `View` ❯ `Command Palette`
3. Type `shell command` into the command palette to find `Shell Command: Install 'code' command in PATH` and click on it to install it.  

### Step 2: Fork the `cmpt221` repository
You are going to create your own copy of the cmpt221 repository by forking this one. Forking allows you to work in your own copy of the repository without affecting the original project.  
1. Navigate to https://github.com/profphip/cmpt221 (if you aren't here already).
2. Click `Fork` in the upper right corner.
3. Name your repository. I suggest naming it `cmpt221` since that is what my examples will use, but you can name it whatever you'd like.
4. Make sure `copy the main branch only` is checked.
5. Click `Create fork`.

### Step 3: Add `profphip` as a collaborator
This allows me to see the activity going on in your repository, create issues, review PRs, etc. even if your repository is private.
1. Navigate to your `cmpt221` repository if you aren't there already
2. Click `settings` in the top menu bar
3. In the top of the left sidebar, click `Collaborators`.
4. Click `Add People` and type `profphip` into the text box. Click `Add profphip to this repository`

### Step 4: Clone your repository
You've created your repository, but you don't have the code locally on your computer yet. Clone your repo by clicking the `<code>` button, and copying the HTTPS URL provided in the drop down box. Then, open your terminal, use the `cd /path/to/directory` command to go to the directory of your choosing on your computer (I created a `Github` folder), and issue the `git clone` command to clone your repository to your computer.   

Note: If you are a Windows user, you will have to install git if you do not have it already: https://git-scm.com/downloads

```bash
# this can be wherever you want!
cd /path/to/directory
git clone <HTTPS URL>
```
Once your repository is cloned and I'm added as a collaborator, you're all set!

# Working on & Submitting a Lab
Submitting a lab in this class might be different than how you submit an assignment in your other classes, but it simulates how your work will be reviewed in the real world.

1. When a lab is posted, you'll need to pull it into your own repository. To do this,
go to your cmpt221 repository in Github and click `Sync fork` then click `Update branch`. This will ensure you have the most up to date version of the class repository, inlcuding the latest lab(s). Then, from the command line in your local repository, pull the changes downstream
    ```bash
    # --no-edit avoids creating a commit message, which is fine for this situation
    git pull --no-edit
    ```

2. Next, create a new branch and give that branch the same name as the lab (x = lab #)
    ```bash
    # create a new branch named lab-x switch to it
    git checkout -b "lab-x"
    ```
3. Work on your lab in the newly created branch. When you're ready to commit and push your changes, write up a somewhat detailed and/or entertaining commit message explaining what you're committing. Please don't push your changes at once. Instead, complete a section of the lab, then push those changes. You should have multiple commits for each lab.
    ```bash
    git add . 
    git commit -m "your message here"
    git push
    ```
    **NOTE**: The first time you push, you might have to authenticate by signing into Github. You will also need to run the following commands to push your new local branch to your remote repository. You'll have to run these every time you make a new branch to create and push to the upstream branch.
    ```bash
    git push --set-upstream origin <branch name>
    git push -u origin <branch name>
    ```
4. Once your lab is complete and you're ready to submit it, push your code. Then, go to your `cmpt221` repository and click `Pull requests` in the top menu bar. Click `New pull request`. Make sure your OWN project is selected (not mine), keep the `base:main`, and select the branch you'd like to compare: `compare:<branch name>`. Then click `Create pull request`. Add a title and a description, and click `Create pull request`. Once the pull request is created, add `profphip` as a reviewer, copy the link to your pull request, and submit it under the corresponding lab in Brightspace. 
