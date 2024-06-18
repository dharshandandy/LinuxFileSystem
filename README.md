# Linux File System Emulator

This project is a Python implementation of a simplified Linux file system emulator. It supports various basic Linux commands for managing files and directories. The emulator provides an interactive command-line interface where users can navigate and manipulate a virtual file system.

## Features

- **Directory Operations**: Create and remove directories.
- **File Operations**: Create, view, and modify files.
- **Navigation**: Navigate through the directory structure.
- **Listing Contents**: List the contents of directories.
- **Present Working Directory**: Display the current directory path.
- **Help Command**: Show available commands.

## Commands

### `ls` - List Directory Contents
**Abbreviation**: `list`

Lists the contents of the current directory.

**Usage**:
```shell
ls
```
### `cd` - Change Directory

**Abbreviation**: `change directory`

Changes the current directory to the specified path.

**Usage**:
```shell
cd <directory_path>
```
### `mkdir` - Make Directory

**Abbreviation**: `make directory`

Creates a new directory with the specified name.

**Usage**:
```shell
mkdir <directory_name>
```

### `touch` - Create Empty File

**Abbreviation**: `touch`

Creates an empty file with the specified name.

**Usage**:
```shell
touch <file_name>
```

### `rm` - Remove File

**Abbreviation**: `remove`

Removes the specified file from the current directory.

**Usage**:
```shell
rm <file_name>
```

### `rmdir` - Remove Directory

**Abbreviation**: `remove directory`

Removes the specified directory from the current directory.

**Usage**:
```shell
rmdir <directory_name>
```

### `vi` - Edit File Content

**Abbreviation**: `vi`

Allows editing the content of a specified file.

**Usage**:
```shell
vi <file_name>
```

### `cat` - View File Content

**Abbreviation**: `cat`

Displays the content of a specified file.

**Usage**:
```shell
cat <file_name>
```

### `pwd` - Present Working Directory

**Abbreviation**: `print working directory`

Prints the full path of the current directory.

**Usage**:
```shell
pwd
```


### `help` - Show Available Commands

**Abbreviation**: `help`

Displays a list of all available commands.

**Usage**:
```shell
help
```

