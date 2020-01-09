import datamgmttools as dmt
from queries import asanaTaskList as taskList

cnxn = dmt.asanaConnect()

#subtask_name = input("Enter a subtask name: ")
#subtask_id = dmt.asanaCreateSubtask(cnxn, task_id, subtask_name)

project_name = input("Enter a project name: ")
project_id = dmt.asanaCreateProject(cnxn, project_name)

for i in taskList:
    taskParams = taskList[i]
    taskParams['projects'] = project_id
    print(dmt.asanaCreateTask(cnxn, project_id, taskParams))