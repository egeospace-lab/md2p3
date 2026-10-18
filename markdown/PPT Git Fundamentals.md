# PPT: Git Fundamentals

# Initial Setup and Basic Configuration

---

## Basic Initialisation

### Setting Username and Email

- Git requires a username and email to identify authors of commits.
- These details are stored in the configuration and attached to every commit.
- Run `git config --global user.name "eGeoSpace"` to set the username.
- Run `git config --global user.email "hello@egeospace.in"` to set the email.
- Using `--global` ensures the settings apply across all repositories.
- Proper identification ensures accountability and traceability in collaboration.

### Configuring Default Editor

- Git uses a text editor for commit messages and other inputs.
- By default, it may use system editors like Vim or Nano.
- Run `git config --global core.editor "editor_name"` to set your preferred editor.
- Common choices include VS Code (`code --wait`) or Nano for simplicity.
- Configuring the editor improves comfort and productivity.
- This ensures commit messages are written clearly and consistently.

### Setting Default Branch Name

- Git traditionally used `master` as the default branch name.
- Modern workflows often prefer `production` for clarity and inclusivity.
- Run `git config --global init.defaultBranch production` to set the default branch.
- This ensures new repositories start with `production` automatically.
- Teams benefit from consistent naming conventions across projects.
- Setting the default branch avoids confusion in collaborative environments.

## Line Endings and File Mode

### `core.autocrlf` and Cross‑Platform Workflows

- Line endings differ between Windows (CRLF) and Unix/macOS/Linux (LF).
- Git can automatically adjust line endings to maintain consistency.
- Run `git config --global core.autocrlf true` on Windows to convert CRLF to LF on commit.
- Run `git config --global core.autocrlf input` on macOS/Linux to leave LF unchanged.
- This prevents issues when sharing code across platforms.
- Proper configuration ensures files behave consistently in all environments.

### `core.filemode` Behavior on Different Filesystems

- Git tracks file permissions as part of its metadata.
- On Linux/macOS, executable permissions are respected.
- On Windows, file permissions are often ignored.
- Run `git config core.filemode false` if permission changes should be ignored.
- This avoids unnecessary differences in cross‑platform repositories.
- Configuring file mode ensures smoother collaboration across systems.

## Global Ignore Rules

### `.gitignore` File

- A `.gitignore` file specifies patterns of files Git should not track.
- Common examples include build artifacts, logs, and temporary files.
- Each repository can have its own `.gitignore` file.
- Patterns ensure irrelevant files do not clutter version history.
- `.gitignore` improves efficiency and keeps repositories clean.
- It is a best practice in every project.

### Using a Global `.gitignore` via `core.excludesFile`

- Developers can define a global ignore file for all repositories.
- Run `git config --global core.excludesFile ~/.gitignore_global` to set it.
- This file applies ignore rules across every project.
- It is useful for personal preferences like ignoring OS‑specific files.
- Global ignores complement repository‑specific `.gitignore` files.
- Together, they ensure clean and consistent repositories.

## Understanding `.gitconfig`

### Configuration Scopes: System, Global, Local

- Git configurations exist at three levels: system, global, and local.
- System applies to all users on a machine.
- Global applies to a single user across all repositories.
- Local applies only to a specific repository.
- Local overrides global, and global overrides system.
- This hierarchy provides flexibility in managing settings.

### Viewing and Editing Configuration

- Run `git config --list` to view all active settings.
- Run `git config --global --edit` to edit global configuration in an editor.
- Local configuration can be edited with `git config --edit` inside a repository.
- Direct editing of `.gitconfig` files is also possible.
- Viewing and editing ensures transparency of applied settings.
- This helps developers maintain consistent environments.

## Common Quality‑of‑Life Settings

### `color.ui`

- Git can highlight output with colors for better readability.
- Run `git config --global color.ui auto` to enable automatic coloring.
- Colors help distinguish branches, commits, and statuses.
- This improves clarity when working in the terminal.
- Color settings enhance user experience without altering functionality.
- It is widely recommended for everyday use.

### Minimal Status Hints

- Git status output can be simplified for clarity.
- Run `git config --global advice.statusHints false` to disable extra hints.
- This reduces clutter in status messages.
- Minimal hints are useful for experienced users.
- Beginners may prefer keeping hints enabled for guidance.
- Adjusting hints tailors Git’s output to personal preference.

### Helpful Prompts

- Git provides prompts to prevent accidental actions.
- Run `git config --global advice.detachedHead true` to enable warnings for detached HEAD.
- Prompts guide users through potentially confusing states.
- They reduce mistakes in complex workflows.
- Helpful prompts are especially valuable for new users.
- Configuring prompts ensures safer Git usage.

# Creating and Managing Repositories

---

## `git init`

### Initialising a Repository

- Run `git init` inside a project directory to create a new repository.
- This command sets up the `.git` folder, which stores all version control data.
- The directory becomes a Git repository, ready to track changes.
- No files are committed yet; only the structure is prepared.
- It is the starting point for managing a project with Git.
- Initialisation ensures the project is under version control.

### First Commit and Setup

- After initialisation, add files to the staging area with `git add`.
- Run `git commit -m "Initial Commit"` to record the first snapshot.
- This creates the first entry in the repository’s history.
- The commit message should describe the project’s starting point.
- The first commit establishes a baseline for future changes.
- It marks the official beginning of version tracking.

## `git clone`

### Cloning via HTTPS

- Run `git clone https://repository_url.git` to copy a repository using HTTPS.
- HTTPS cloning requires username and password or token authentication.
- It is widely supported and easy to set up.
- HTTPS is suitable for most users, especially beginners.
- Cloning creates a local copy with full history.
- This method ensures secure access over standard web protocols.

### Cloning via SSH

- Run `git clone git@repository_url:user/project.git` to clone via SSH.
- SSH uses cryptographic keys for authentication.
- It avoids repeated password prompts during operations.
- SSH is preferred for frequent contributors to private repositories.
- Keys must be configured before using SSH.
- This method provides secure and efficient access.

### Shallow Clones

- Run `git clone --depth 1 https://repository_url.git` to create a shallow clone.
- Shallow clones download only recent history, not the full commit log.
- They reduce storage and speed up cloning.
- Useful for large repositories where full history is unnecessary.
- Shallow clones are ideal for quick testing or CI/CD pipelines.
- They trade completeness for efficiency.

## Repository Structure

### The `.git` Directory

- The `.git` directory is created when a repository is initialised or cloned.
- It contains all internal data Git needs to function.
- This includes objects, references, configuration, and logs.
- The directory is hidden by default to avoid accidental changes.
- Modifying `.git` directly can corrupt the repository.
- It is the core of Git’s version control system.

### Objects, Refs, and Config

- Objects store commits, trees, and blobs representing project history.
- References (refs) point to commits, such as branches and tags.
- Configuration files define repository settings.
- Together, these components make Git functional and flexible.
- They ensure history, navigation, and settings are preserved.
- Understanding them helps in advanced Git troubleshooting.

# Local Workflow States

---

## Main States

### Working Directory

- The working directory is where you actively edit files in your project.
- It reflects the current state of the repository on your computer.
- Changes here are not yet tracked by Git until staged.
- You can freely add, modify, or delete files.
- The working directory is your sandbox for experimentation.
- Run `git status` to see which files have been modified.

### Staging Area (Index)

- The staging area is an intermediate space between editing and committing.
- It holds a snapshot of changes prepared for the next commit.
- Developers choose which modifications to include, enabling selective commits.
- This ensures clarity and control over project history.
- Run `git add filename` to move changes into the staging area.
- Run `git status` to confirm which files are staged.

### Repository

- The repository is Git’s permanent storage of project history.
- It contains all commits, branches, and references.
- Once changes are committed, they are safely stored here.
- The repository ensures traceability and integrity of every version.
- It can exist locally or remotely (e.g., on GitHub or GitLab).
- Run `git log` to view the commit history stored in the repository.

## Moving Changes Between States

### Editing Files

- Editing happens in the working directory, where files are changed.
- Run `git status` to check which files have been modified.
- Files remain untracked until staged.
- This step is the beginning of Git’s workflow pipeline.
- Editing does not affect the repository until committed.
- It provides flexibility to experiment before recording changes.

### Staging Changes with `git add`

- Run `git add filename` to stage a specific file.
- Run `git add .` to stage all changes in the current directory.
- Staging prepares changes for the next commit.
- It allows grouping related changes together.
- Run `git status` to confirm which files are staged.
- This step ensures intentional commits with clear scope.

### Committing Changes with `git commit`

- Run `git commit -m "Message"` to record staged changes in the repository.
- Commits create permanent snapshots of the project.
- Each commit includes metadata like author, timestamp, and message.
- Run `git log` to view the commit history.
- Commits are linked together to form the project timeline.
- This step moves changes from staging into permanent history.

# Tracking and Managing Files

---

## `git add`

### Overview

- Run `git add filename` to stage a specific file for commit.
- Run `git add .` to stage all changes in the current directory.
- Staging prepares changes for inclusion in the next commit.
- It allows developers to selectively choose which edits to record.
- Run `git status` to confirm which files are staged.
- This step ensures commits are intentional and scoped correctly.

## `.gitignore`

### Syntax and Patterns

- A `.gitignore` file defines rules for files Git should not track.
- Patterns can match filenames, extensions, or directories.
- For example, `.log` ignores all log files.
- Prefixing with `/` restricts the rule to the repository root.
- Adding `!` negates a pattern, forcing Git to track specific files.
- Syntax ensures irrelevant files do not clutter version history.

### Common Templates

- Typical `.gitignore` entries include build artifacts, logs, and temporary files.
- For Java projects, `target/` is often ignored.
- For Node.js projects, `node_modules/` is excluded.
- For Python projects, `__pycache__/` and `.venv/` are ignored.
- IDE‑specific files like `.vscode/` or `.idea/` are commonly excluded.
- Using templates ensures clean and consistent repositories across teams.

## `git rm`

### Removing Files

- Run `git rm filename` to remove a file from both the working directory and staging area.
- This ensures the file is deleted and tracked as removed in the next commit.
- Run `git rm -r directory_name` to remove a directory.
- Removing files through Git preserves history of their deletion.
- Run `git status` to confirm the removal is staged.
- This keeps repository history consistent with project changes.

### Recovering Deleted Files

- Run `git checkout production -- filename` to restore a deleted file from the `production` branch.
- This retrieves the last committed version of the file.
- Recovery ensures accidental deletions are not permanent.
- Files can be restored from any commit in history.
- This makes Git safer than manual file deletion.
- Recovery is a key advantage of version control.

## `git mv`

### Renaming Files

- Run `git mv old_filename new_filename` to rename a file.
- This stages the rename for the next commit.
- Git tracks the change as a rename rather than a delete/add.
- Renaming through Git preserves file history.
- Run `git status` to confirm the rename is staged.
- This ensures clarity in project evolution.

### Tracking Renames in History

- Git automatically detects renames during history inspection.
- Commits show the file’s old and new names.
- This maintains continuity of file history across changes.
- Renames are traceable in `git log` and `git diff`.
- Tracking renames helps understand project evolution.
- It ensures accountability for structural changes.

# Inspecting and Exploring History

---

## `git status`

### Overview

- Run `git status` to view the current state of your working directory and staging area.
- It shows which files are modified, staged, or untracked.
- The command helps identify what needs to be committed next.
- It also indicates the branch you are currently on (e.g., `production`).
- Frequent use of `git status` prevents mistakes and confusion.
- It is the most commonly used command for workflow awareness.

## `git diff`

### What is `diff`?

- `git diff` shows differences between file versions.
- It highlights added, removed, or modified lines.
- Differences are displayed in a clear, line‑by‑line format.
- This helps developers review changes before committing.
- It ensures accuracy and prevents unintended edits.
- `diff` is a key tool for code review and validation.

### Comparing Working Directory vs Staging Area

- Run `git diff` to compare the working directory with the staging area.
- It shows changes that have not yet been staged.
- This helps decide which edits should be added with `git add`.
- Reviewing differences ensures commits are intentional.
- It prevents accidental inclusion of unfinished work.
- This comparison is essential for clean commit histories.

### Comparing Commits

- Run `git diff commit1 commit2` to compare two commits.
- This shows how the project evolved between those points.
- It highlights changes across files and directories.
- Comparing commits helps track progress and debug issues.
- It provides insight into the history of specific features.
- This makes `diff` valuable for long‑term project analysis.

## `git log`

### Viewing Commit Details

- Run `git log` to view the commit history of the repository.
- Each entry shows commit ID, author, date, and message.
- This provides a chronological record of project changes.
- Run `git log production` to view history on the `production` branch.
- Commit details ensure traceability of contributions.
- Logs are essential for accountability in collaborative projects.

### Formatting and Filtering Logs

- Run `git log --oneline` for a compact view of commits.
- Run `git log --author="eGeoSpace"` to filter by author.
- Run `git log --since="1 week ago"` to filter by date.
- Run `git log --grep="keyword"` to search commit messages.
- Formatting options make logs easier to navigate.
- Filtering ensures efficient exploration of history.

### Commit Graphs

- Run `git log --graph --oneline --decorate` to visualise branch history.
- The graph shows branching and merging patterns.
- It helps understand project topology at a glance.
- Graphs are useful in complex repositories with multiple branches.
- They provide clarity on how features were integrated.
- Commit graphs make history more accessible and visual.

## Searching History

### By Author, Date, or Message

- Run `git log --author="eGeoSpace"` to find commits by a specific contributor.
- Run `git log --since="2026-10-18"` to filter commits by date.
- Run `git log --grep="eGeoCloud"` to search commit messages.
- These filters make it easy to locate relevant changes.
- Searching history improves efficiency in large projects.
- It ensures accountability and traceability of contributions.

### Using `git log --grep`

- Run `git log --grep="fix"` to find commits mentioning “fix.”
- This highlights commits related to bug fixes.
- `--grep` searches commit messages for specific keywords.
- It is useful for tracking features or issues across history.
- Combining `--grep` with other filters refines searches further.
- This makes history exploration precise and powerful.