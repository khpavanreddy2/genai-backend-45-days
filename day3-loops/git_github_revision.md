# Git and GitHub – Revision Notes

## Git vs GitHub

- **Git** is a version control system that tracks changes and stores project history.
- **GitHub** is an online platform for hosting Git repositories and collaborating.

## Basic workflow

1. Edit or create project files.
2. Stage selected changes with `git add`.
3. Save staged changes in a local commit with `git commit`.
4. Upload local commits to the remote repository with `git push`.

## Commands reviewed

| Command | Purpose |
|---|---|
| `git init` | Initialize a Git repository in the current folder |
| `git status` | Show working-tree and staging-area status |
| `git add .` | Stage eligible changes in the current directory and subdirectories |
| `git commit -m "message"` | Create a local commit from staged changes |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git branch -M main` | Rename the current branch to `main` |
| `git remote add origin URL` | Add a remote named `origin` |
| `git push -u origin main` | Push the `main` branch and set its upstream |

## Important differences

- `git add` stages changes; it does not upload them.
- `git commit` saves a snapshot locally; it does not upload it.
- `git push` uploads commits to the remote repository.
- `git status` reports repository state; it does not modify files.
- `git diff` shows unstaged changes, while `git diff --staged` shows staged changes.

## First push workflow

Use this only when initializing and connecting a local repository for the first time. Replace the URL with your actual GitHub repository URL.

```bash
git init
git status
git add .
git diff --staged
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

## Daily update workflow

For an already connected repository:

```bash
git status
git add .
git diff --staged
git commit -m "Describe your changes"
git push
```

Do not run `git init` or `git remote add origin` again if the repository is already initialized and connected.
