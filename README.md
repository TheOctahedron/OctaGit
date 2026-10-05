# OctaGit
A minimalistic Git command generator for Windows. Fast, clean, and built from scratch.

## HOW IT WORKS?

OctaGit is a minimalistic desktop application for generating and running Git commands:

1. The application starts with `main.py`, which opens the main window.
2. The left panel contains buttons for common Git commands (`git status`, `git add .`, `git commit`, `git push`).
3. Clicking a button inserts the corresponding command into the input field on the right.
4. The user can edit the command manually (for example, add a commit message).
5. Pressing **Run** executes the command via `subprocess` and shows the output in the terminal panel.
6. The status bar at the bottom displays the current branch and repository state (`main | clean | ready`).
7. All errors are captured, translated into human-readable hints, and logged to `octagit.log`.

No AI. No internet. Just Git commands at your fingertips.