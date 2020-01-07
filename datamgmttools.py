#! python3
#Written by Alex Ilson
#Various functions for Data Management stuff
#version 0.2
#last updated 12/27/18

import pypyodbc, pandas as pd, sys, os
from openpyxl import load_workbook
from subprocess import call
from shutil import copy2

def connectEDM():
    #Attempt to connect to EDM and create connect object
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
    #create writer object
    print("Creating writer object with filename:", outputFilename)
    try:
        writer = pd.ExcelWriter(outputFilename)
    except Exception as e:
        print("Error", e)
    #create dataframe from query results
    print("Creating dataframe object.")
    try:
        df = pd.read_sql_query(inQuery, EDMConnection)
    except Exception as e:
        print("Error", e)
    #write dataframe to Excel spreadsheet
    print("Write dataframe to",outputFilename)
    try:
        df.to_excel(writer, sheet_name=worksheetName, na_rep="NULL", header=headerNames, index=False)
    except Exception as e:
        print("Error", e)
    #get worksheet object
    print("Getting worksheet object...")
    try:
        worksheet = writer.sheets[worksheetName]
    except Exception as e:
        print("Error", e)
    #resize columns to width of 30
    print("Resizing columns...")
    try:
        worksheet.set_column(0, len(headerNames), 30)
    except Exception as e:
        print("Error", e)
    #save writer
    print("Saving spreadsheet...")
    try:
        writer.save()
    except Exception as e:
        print("Error", e)


def queryAndAppend(EDMConnection, inQuery, outputFilename, headerNames, worksheetName):
    #load existing workbook
    try:
        book = load_workbook(outputFilename)
    except Exception as e:
        print("Error", e)
    #create writer object
    print("Creating writer object with filename:", outputFilename)
    try:
        writer = pd.ExcelWriter(outputFilename, engine = "openpyxl")
        writer.book = book
    except Exception as e:
        print("Error", e)
    #create dataframe from query results
    print("Creating dataframe object.")
    try:
        df = pd.read_sql_query(inQuery, EDMConnection)
    except Exception as e:
        print("Error", e)
    #write dataframe to Excel spreadsheet
    print("Write dataframe to",outputFilename)
    try:
        df.to_excel(writer, sheet_name=worksheetName, na_rep="NULL", header=headerNames, index=False)
    except Exception as e:
        print("Error", e)
    #get worksheet object
    print("Getting worksheet object...")
    try:
        worksheet = writer.sheets[worksheetName]
    except Exception as e:
        print("Error", e)
    #save writer
    print("Saving spreadsheet...")
    try:
        writer.save()
    except Exception as e:
        print("Error", e)

def runFIS_Export():
    try:
        call(r"c:\FIS_Export\pyBatch.bat")
    except Exception as e:
        print("Error", e)

def copyFIS_ExportForDataCheck():
    sourceFolder = r'C:\FIS_Export\output'
    newFolder = r'\\us\irv\Information_Technology\Data_Management\Automation\python\test\new'
    oldFolder = r'\\us\irv\Information_Technology\Data_Management\Automation\python\test\old'
    for j in os.listdir(newFolder):
        copy2(os.path.join(newFolder, j), oldFolder)
    for i in os.listdir(sourceFolder):
        copy2(os.path.join(sourceFolder, i), newFolder)