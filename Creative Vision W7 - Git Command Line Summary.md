### ✅ GIT + VS CODE COMMAND DOCUMENTATION

(From zero setup → commit → push → branch → merge)

## ✅ 1. First-Time One-Machine Setup

Run these once per computer:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Check if Git is installed:
```bash
git --version
```
-------------------------
## ✅ 2. Create or Initialize a Project (.sh script method)

Create a setup.sh file:
```bash
#!/bin/bash
git init
git add .
git commit -m "Initial commit"
```

Run it:
```bash
bash setup.sh
```

This:

✅ creates .git
✅ stages all files
✅ makes first commit

## ✅ 3. Connect a Local Project to GitHub

(1) Create a repository on GitHub (empty, no README).

(2) In VS Code Terminal:
```bash
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
git push -u origin main
```

## ✅ 4. Everyday Workflow Commands
✅ Check what changed
```bash
git status
```
✅ Add files before commit

Add all files:
```bash
git add .
```

Add a specific file:
```bash
git add filename.py
```
✅ Commit changes with a message
```bash
git commit -m "Explain what you changed"
```
✅ Push to GitHub

```bash
git push
```

If first push:
```bash
git push -u origin main
```

## ✅ 5. Cloning a Repo Into VS Code

Copy the GitHub HTTPS or SSH link, then:
```bash
git clone https://github.com/<username>/<repo>.git
```

Open in VS Code:
```bash
code <repo>
```
## ✅ 6. Branch Workflow (Very common in team projects)

✅ Create a branch and switch to it
```bash
git checkout -b new-feature
```
✅ Switch branches
```bash
git checkout main
```
✅ Push that branch to GitHub
```bash
git push -u origin new-feature
```

## ✅ 7. Pulling Updates (so your code doesn’t conflict)

Pull latest code from GitHub into your local:
```bash
git pull
```

Pull specific branch:
```bash
git pull origin main
```

## ✅ 8. Merging Code

(1) Switch back to main:
```bash
git checkout main
```

(2) Merge the feature branch:
```bash
git merge new-feature
```

(3) Push updated main:
```bash
git push
```
## ✅ 9. Stashing Work (if you need to switch tasks without committing messy code)

Save messy, unfinished code:
```bash
git stash
```

Restore it later:
```bash
git stash pop
```
## ✅ 10. Undoing & Fixing Mistakes
✅ Unstage a file
```bash
git reset HEAD filename.py
```
✅ Undo last commit (but keep changes)
```bash
git reset --soft HEAD~1
```
✅ Discard file changes permanently
```bash
git checkout -- filename.py
```

## ✅ 11. Most Common Everyday Commands (Cheat Sheet)
| Action | Command |
|--------|---------|
|initialize repo | `git init` |
|check changes	| `git status` |
|stage all	| `git add .` |
|commit	| `git commit -m "msg"` |
|push | `git push` |
|pull | `git pull` |
|make branch | `git checkout -b branchname` |
|switch branch | `git checkout branchname` |
|merge branch | `git merge branchname` |

## ✅ 12. Connecting VS Code Git GUI

VS Code has built-in Git controls:

![](Image/Source%20Control.png)

- left sidebar → Source Control
- commit button
- stage/unstage with + and −
- push/pull from bottom-left corner

Terminal commands still work inside VS Code.

## ✅ 13. Example Project Workflow (Start to Finish)

```bash
git init
git add .
git commit -m "Initial setup"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Then daily:

```bash
git pull
git add .
git commit -m "Updated feature"
git push
```

## ✅ 14. Most Common Errors & Fixes
❌ rejected - non-fast-forward

Your local is old. Fix:
```bash
git pull
```

If conflicts appear: open conflict files manually → edit → then:
```bash
git add .
git commit -m "resolved conflicts"
git push
```
❌ fatal: remote origin already exists

Means you already linked GitHub. Fix:
```bash
git remote set-url origin https://github.com/<username>/<repo>.git
```
❌ Want to delete a local branch?
```bash
git branch -d branchname
```
## ✅ 15. Bonus: Automatic Push Script (.sh)

Create push.sh:
```bash
#!/bin/bash
git add .
git commit -m "$1"
git push
```

Run:
```bash
bash push.sh "updated feature"
```