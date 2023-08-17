from django.shortcuts import render, redirect
import json


with open("./todo.json", "r") as file:
    tasks = json.load(file)


def WriteData(data):
    with open("./todo.json", "w") as file:
        json.dump(data, file)


def updateCompete(index):
    task = tasks[index]
    task["completed"] = not task["completed"]
    with open("./todo.json", "w") as file:
            json.dump(tasks, file)


def getIndex(taskId):
    index = None
    for ind, task in enumerate(tasks):
        if task["id"] == taskId:
            index = ind
            return index;
    return None


def removetask(index):
    del(tasks[index])
    WriteData(tasks)

def read(request):
    return render(request, "read.html", {"tasks": tasks})


def create(request):
    if request.method == 'POST':
        taskName = request.POST.get('taskName')
        if len(tasks) == 0:
            id = 0
        else:
            id = tasks[len(tasks) - 1]["id"]

        task = {"id":id+1,"title":taskName,"completed":"false"}
        tasks.append(task);
        WriteData(tasks)
        return render(request, 'taskCreated.html', {'task_title': taskName})
    
    return render(request, 'create.html')


def update(request, task_id):
    index = getIndex(task_id)
    task = tasks[index]
    if task is None:
        return render(request, "todolist/task_not_found.html")
    if request.method == "POST":
        updateCompete(index)

    return render(request, "update.html", {"task": task})


def delete(request,task_id):
    if task_id==None:
        return render(request,'read.html',{"tasks":tasks})
    index = getIndex(task_id)
    task = tasks[index]
    taskName = task['title']
    if request.method == "POST":
       removetask(index)
       return render(request, 'removed.html', {'task_title': taskName})
    return render(request, "delete.html",{'task':task})
