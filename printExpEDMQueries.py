#! python 3
# Queries for Experience verification

import datamgmttools as dmt
import queries as qry

if __name__ == "__main__":
    #cnxn = dmt.connectEDM()
    while True:
        # Connect to EDM
        #cnxn = dmt.connectEDM()
        #TODO Iterate through a list of PLUs
        #TODO Add Control Query
        PLU = input("Enter the PLU: ")
        #fileName = input("Enter the file name with no extension: ")
        itemType = input("Enter 'Item' or 'Combo': ")
        if itemType == "Item":
            for i in qry.qryPreItem:
                print(qry.qryPreItem[i]["text"])
                query = qry.qryPreItem[i]["query"] + str(PLU)
                fileNamef = """C:\\temp\\""" + str(PLU) + ".xlsx"
                dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreItem[i]["headers"], PLU)
        if itemType == "Combo":
            attachmentPLU = input("Enter the attachment PLU: ")
            #TODO Make this into a function and loop instead of a repeated bunch of statements
            print(qry.qryPreCombo["qryPre102"]["text"])
            #TODO Iterate through a list of attachment PLUs
            #TODO Use variables in the string instead of concat'ing strings
            query = qry.qryPreCombo["qryPre102"]["query"]["queryPt01"] + str(PLU) + qry.qryPreCombo["qryPre102"]["query"]["queryPt02"] + str(attachmentPLU)
            sheetName = "Child" + PLU + " " + attachmentPLU
            fileNamef = """C:\\temp\\""" + str(PLU) + "-" + str(attachmentPLU) + "Child.xlsx"
            dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreCombo["qryPre102"]["headers"], sheetName)
            print(qry.qryPreCombo["qryPre103"]["text"])
            query = qry.qryPreCombo["qryPre103"]["query"]["queryPt03"] + str(PLU) + qry.qryPreCombo["qryPre103"]["query"]["queryPt04"] + str(attachmentPLU)
            sheetName = "Atch" + PLU + " " + attachmentPLU
            fileNamef = """C:\\temp\\""" + str(PLU) + "-" + str(attachmentPLU) + "Attach.xlsx"
            dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreCombo["qryPre103"]["headers"], sheetName)
        #TODO Add option to run it again before disconnect
        if input("Would you like to go again? y/n: ") == "n":
            print("Disconnecting...")
            #cnxn.close()
            break
        else:
            continue
