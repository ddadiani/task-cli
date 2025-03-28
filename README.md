# **task-cli**: CLI TODO App
task-cli is a CLI application where you can add, remove and manage your tasks with various commands. It stores the data in a JSON file.

## Installation

Installation can be done by downloading the zip file and extracting it or 
by cloning the repo with git
```
git clone https://github.com/ddadiani/task-cli.git
```


## Usage

```
python3 ./task-cli.py [command] [arguments]
```

* Adding a new task
```
python3 ./task-cli add [description]
python3 ./task-cli add "Buy groceries"
```

* Updating and deleting a task (by id)
```
python3 ./task-cli update [id] [description]
python3 ./task-cli update 1 "Cook dinner"
```

* Marking a task in progress or done
```
python3 ./task-cli mark-in-progress [id]
python3 ./task-cli mark-done [id]
```

* List all tasks
```
python3 ./task-cli list
```

* List tasks by status
```
python3 ./task-cli list done
python3 ./task-cli list todo
python3 ./task-cli list in-progress
```