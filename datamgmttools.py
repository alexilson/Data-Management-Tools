#! python3
# Written by Alex Ilson
# Various functions for Data Management stuff
# version 0.2
# last updated 01/13/2020

import pypyodbc, pandas as pd, sys, os
import asana
from openpyxl import load_workbook
from subprocess import call
from shutil import copy2


asanaAuth = '0/0fec0d145ba4d0cb4d4b0cf0cb8966a3'
asanaWorkspace = '9831877553179'
asanaTeam = '41652546591765'


def connectEDM():
    # Attempt to connect to EDM and create connect object
    try:
        print("Attemping to connect to EDM...")
        connectionEDM = pypyodbc.connect("Driver={SQL Server};"
                                "Server=SQL901C1;"
                                "Database=TacoBellHQ1;"
                                "Trusted_Connection=yes;")
    except pypyodbc.Error as e:
        print("Unable to connect to EDM. Exiting.")
        print(e.args[1])
        sys.exit()
    else:
        print("Connection successful!")
        return connectionEDM


def edmgetint(msg):
        while True:
            try:
                value = int(input(msg))
                return str(value)
                break
            except ValueError:
                print("Please enter a number.")
                continue


def queryAndWrite(EDMConnection, inQuery, outputFilename, headerNames, worksheetName):
    # create writer object
    print("Creating writer object with filename:", outputFilename)
    try:
        writer = pd.ExcelWriter(outputFilename)
    except Exception as e:
        print("Error", e)
    # create dataframe from query results
    print("Creating dataframe object.")
    try:
        df = pd.read_sql_query(inQuery, EDMConnection)
    except Exception as e:
        print("Error", e)
    # write dataframe to Excel spreadsheet
    print("Write dataframe to",outputFilename)
    try:
        df.to_excel(writer, sheet_name=worksheetName, na_rep="NULL", header=headerNames, index=False)
    except Exception as e:
        print("Error", e)
    # get worksheet object
    print("Getting worksheet object...")
    try:
        worksheet = writer.sheets[worksheetName]
    except Exception as e:
        print("Error", e)
    # resize columns to width of 30
    print("Resizing columns...")
    try:
        worksheet.set_column(0, len(headerNames), 30)
    except Exception as e:
        print("Error", e)
    # save writer
    print("Saving spreadsheet...")
    try:
        writer.save()
    except Exception as e:
        print("Error", e)


def queryAndAppend(EDMConnection, inQuery, outputFilename, headerNames, worksheetName):
    # load existing workbook
    try:
        book = load_workbook(outputFilename)
    except Exception as e:
        print("Error", e)
    # create writer object
    print("Creating writer object with filename:", outputFilename)
    try:
        writer = pd.ExcelWriter(outputFilename, engine = "openpyxl")
        writer.book = book
    except Exception as e:
        print("Error", e)
    # create dataframe from query results
    print("Creating dataframe object.")
    try:
        df = pd.read_sql_query(inQuery, EDMConnection)
    except Exception as e:
        print("Error", e)
    # write dataframe to Excel spreadsheet
    print("Write dataframe to",outputFilename)
    try:
        df.to_excel(writer, sheet_name=worksheetName, na_rep="NULL", header=headerNames, index=False)
    except Exception as e:
        print("Error", e)
    # get worksheet object
    print("Getting worksheet object...")
    try:
        worksheet = writer.sheets[worksheetName]
    except Exception as e:
        print("Error", e)
    # save writer
    print("Saving spreadsheet...")
    try:
        writer.save()
    except Exception as e:
        print("Error", e)


def runFIS_Export():
    try:
        call(r"c:\FIS_Export_Prod\ERSUIInterface.exe -usePK 0 -region ALL -startOffset 1 -endOffset 0")
    except Exception as e:
        print("Error", e)


# Runs the FIS Export batch file on the local C: drive

def FIS_Export():
    print('you picked to run the FIS Export')
    params = [r"C:\FIS_Export_Prod\Batch.bat"]
    print(subprocess.check_call(params))
    print("Process complete, returning to main menu.")
    return


def copyFIS_ExportForDataCheck():
    sourceFolder = r'C:\FIS_Export\output'
    newFolder = r'\\us\irv\Information_Technology\Data_Management\Automation\python\test\new'
    oldFolder = r'\\us\irv\Information_Technology\Data_Management\Automation\python\test\old'
    for j in os.listdir(newFolder):
        copy2(os.path.join(newFolder, j), oldFolder)
    for i in os.listdir(sourceFolder):
        copy2(os.path.join(sourceFolder, i), newFolder)


def asanaConnect():
    client = asana.Client.access_token(asanaAuth)
    return client


def asanaCreateProject(client, name):
    projectIn = {'name': name, 'workspace': asanaWorkspace, 'team': asanaTeam}
    project = client.projects.create(projectIn)
    return project['gid']


def asanaCreateTask(client, projectID, parameters):
    task = client.tasks.create_in_workspace(asanaWorkspace, parameters)
    return task['gid']


def asanaCreateTaskWorkspace(client, projectID, parameters):
    task = client.tasks.add_project(projectID, parameters)
    return task['gid']


def asanaCreateSubtask(client, taskID, parameters):
    subtask = client.tasks.add_subtask(taskID, parameters)
    return subtask['gid']
