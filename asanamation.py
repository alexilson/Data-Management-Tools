import datamgmttools as dmt
from queries import asanaTaskList as taskList
from queries import asanaSubTaskList as subtasks

# Connect to Asana
cnxn = dmt.asanaConnect()

# subtask_name = input("Enter a subtask name: ")
# subtask_id = dmt.asanaCreateSubtask(cnxn, task_id, subtask_name)

# Get project name
project_name = input("Enter a project name: ")

# Creat project with input name and give back the gid of the new project
project_id = dmt.asanaCreateProject(cnxn, project_name)

# iterates through every data thing in the data dictionary for the details of each task and
# adds it to the taskList data thing.
for i in taskList:
    taskParams = taskList[i]
    taskParams['projects'] = project_id
    taskList[i]['taskid'] = dmt.asanaCreateTask(cnxn, project_id, taskParams)
    print("Created task with ID", taskList[i]['taskid'])

for i in subtasks:
    subtaskParams = subtasks[i]['taskParams']
    parentTaskNumber = subtasks[i]['parentTask']
    parentTaskID = taskList[parentTaskNumber]['taskid']
    # TODO: figure out how to make it look at the subtask list if the parent is a subtask.
    print(dmt.asanaCreateSubtask(cnxn, parentTaskID, subtaskParams))

"""
for i in taskList:
    if taskList[i]['parent'] == '':
        continue
    else:
        print(dmt.asanaCreateSubtask(cnxn, taskList[i]['parent'], taskParams))
"""