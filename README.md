# **task-cli**: CLI TODO App
task-cli is a CLI application where you can add, remove and manage your tasks with various commands. 

## Installation

Installation can be done by downloading the zip file and extracting it or 
by cloning the repo with git
```
git clone https://github.com/ddadiani/task-cli.git
```


## Usage
```
task-cli [command] [arguments]
```

* Adding a new task
```
task-cli add [description]
task-cli add "Buy groceries"
```

* Updating and deleting a task (by id)
```
task-cli update [id] [description]
task-cli update 1 "Cook dinner"
```

* Marking a task in progress or done
```
task-cli mark-in-progress [id]
task-cli mark-done [id]
```

* List all tasks
```
task-cli list
```

* List tasks by status
```
task-cli list done
task-cli list todo
task-cli list in-progress
```