# lister

A simple command line tool to list directory contents, similar to the Unix `ls` command.

## Features
- List files and directories
- Show hidden files with `-a` or `--all`
- Long format with file size, permissions, and modification date using `-l` or `--long`

## Installation

From the project root, install in editable mode:

```
./.venv/bin/python -m pip install -e .
```

## Usage

```
lister [PATH] [-a] [-l]
```

- `PATH`: Directory to list (default: current directory)
- `-a`, `--all`: Show all files including hidden
- `-l`, `--long`: Long format (permissions, size, date)

## Example

```
lister -al /tmp
```
