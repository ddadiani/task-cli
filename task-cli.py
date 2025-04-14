import json
import sys
import os
from datetime import datetime



def main() -> None:
    # correct usage message
    correctUsageMessage = "usage: task-cli [command] [description/id]"

    # get cli arguments
    args = sys.argv

    if len(args) <= 1 or len(args) > 4:
        print(correctUsageMessage)
        return
    command = args[1]


    # open or create json file
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r") as file:
            data = json.load(file)
    else:
        with open("data.json", "w") as file:
            pass
        data = {
            "incrementId": 0,
            "tasks": []
        }

    # to check if file was changed
    state = {"changed": False}


    # check first argument for the desired user command and execute it
    match command:
        case "add":
            if len(args) < 3:
                print("Please provide a task description.\nusage: task-cli add [description]")
                return
            add(data, args[2], state)
        case "update":
            if len(args) < 4:
                print("Please provide task ID and new description\ntask-cli update [id] [new description]")
                return
            update(data, args[2], args[3], state)
        case "delete":
            if len(args) < 3:
                print("Please provide the ID of the task to delete. (task-cli delete [id])")
                return
            delete(data, args[2], state)
        case "mark-in-progress":
            if len(args) < 3:
                print("Please provide the ID of the task to mark in progress. (task-cli mark-in-progress [id])")
                return
            mark_in_progress(data, args[2], state)
        case "mark-done":
            if len(args) < 3:
                print("Please provide the ID of the task to mark done. (task-cli mark-done [id])")
                return
            mark_done(data, args[2], state)
        case "list":
            if len(args) == 2:
                list_all(data)
            elif args[2] == "done":
                list_done(data)
            elif args[2] == "todo":
                list_todo(data)
            elif args[2] == "in-progress":
                list_in_progress(data)
            else:
                print(correctUsageMessage)
        case _:
            print(correctUsageMessage)


    # write the data to the json file
    if state["changed"]:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    




def getnextid(data):
    data["incrementId"] += 1
    return str(data["incrementId"])




def getdatetime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")




def add(data, desc, state):
    id = getnextid(data)
    data["tasks"].append(
        {
        "id": id,
        "description": desc,
        "status": "todo",
        "createdAt": getdatetime(),
        "updatedAt": getdatetime()
        }
    )

    state["changed"] = True
    print(f"Task successfully added (ID: {id})")




def update(data, id, desc, state):
    for task in data["tasks"]:
        if task["id"] == id:
            task["description"] = desc
            task["updatedAt"] = getdatetime()

            state["changed"] = True
            print("Task successfully updated")
            return
    print("Couldn't find task with that id")    
    



def delete(data, id, state):
    index = 0

    for task in data["tasks"]:
        if task["id"] == id:
            data["tasks"].pop(index)

            state["changed"] = True
            print("Task successfully deleted")
            return

        index += 1

    print("Couldn't find task with provided id")    




def mark_in_progress(data, id, state):
    for task in data["tasks"]:
        if task["id"] == id:
            task["status"] = "in-progress"
            task["updatedAt"] = getdatetime()

            state["changed"] = True
            print("Task successfully updated")
            return
    print("Couldn't find task with that id")    




def mark_done(data, id, state):
    for task in data["tasks"]:
        if task["id"] == id:
            task["status"] = "done"
            task["updatedAt"] = getdatetime()

            state["changed"] = True
            print("Task successfully updated")
            return
    print("Couldn't find task with that id")    




def list_all(data):
    for task in data["tasks"]:
        print(json.dumps(task, indent=4))




def list_done(data):
    for task in data["tasks"]:
        if task["status"] == "done":
            print(json.dumps(task, indent=4))



def list_todo(data):
    for task in data["tasks"]:
        if task["status"] == "todo":
            print(json.dumps(task, indent=4))




def list_in_progress(data):
    for task in data["tasks"]:
        if task["status"] == "in-progress":
            print(json.dumps(task, indent=4))







if __name__ == "__main__":
    main()