#! python 3
# Queries for Pre Deployment verification

import datamgmttools as dmt
import queries as qry


# noinspection SpellCheckingInspection
def getinput():
    while True:
        itemtype = input("Welcome to the Pre-Deployement Package Record Recorder! What type of item is being queried "
                         "today? Type 'i' for an Item or 'c' for a Combo: ")
        plu = dmt.edmgetint("Enter the PLU: ")
        if itemtype == 'i':
            menuid = dmt.edmgetint("Enter the MenuID where the button appears: ")
            return itemtype, plu, menuid, 0
        if itemtype == 'c':
            attachmentplu = dmt.edmgetint("Enter the PLU of the attachment: ")
            return itemtype, plu, 0, attachmentplu
        else:
            print("Try again.")
            continue


# def doTheThing(itemtype, )

if __name__ == "__main__":
    # Connect to EDM
    cnxn = dmt.connectEDM()
    while True:
        # TODO Iterate through a list of PLUs
        # TODO Add Control Query
        # TODO Add analysis of returned data
        itemType, PLU, menuID, attachmentPLU = getinput()
        if itemType == "i":
            print(qry.qryPreItem["qryPre101"]["text"])
            query = qry.qryPreItem["qryPre101"]["query"] + str(PLU)
            fileNamef = """C:\\temp\\""" + str(PLU) + ".xlsx"
            dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreItem["qryPre101"]["headers"], PLU)

            print(qry.qryPreItem["qryPre102"]["text"])
            query = qry.qryPreItem["qryPre102"]["query"]["queryPt01"] + str(menuID) + qry.qryPreItem["qryPre102"]["query"]["queryPt02"] + str(PLU)
            sheetName = "Btns " + PLU + " " + menuID
            fileNamef = """C:\\temp\\""" + str(PLU) + "-" + str(menuID) + "Buttons.xlsx"
            dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreItem["qryPre102"]["headers"], sheetName)

        if itemType == "c":
            while True:
                print(qry.qryPreCombo["qryPre102"]["text"])
                # TODO Iterate through a list of attachment PLUs
                # TODO Use variables in the string instead of concat'ing strings
                query = qry.qryPreCombo["qryPre102"]["query"]["queryPt01"] + str(attachmentPLU) + \
                    qry.qryPreCombo["qryPre102"]["query"]["queryPt02"] + str(PLU)
                sheetName = "Child " + PLU + " " + attachmentPLU
                fileNamef = """C:\\temp\\""" + str(PLU) + "-" + str(attachmentPLU) + "Child.xlsx"
                dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreCombo["qryPre102"]["headers"], sheetName)

                print(qry.qryPreCombo["qryPre103"]["text"])
                query = qry.qryPreCombo["qryPre103"]["query"]["queryPt03"] + str(PLU) + \
                    qry.qryPreCombo["qryPre103"]["query"]["queryPt04"] + str(attachmentPLU)
                sheetName = "Atch " + PLU + " " + attachmentPLU
                fileNamef = """C:\\temp\\""" + str(PLU) + "-" + str(attachmentPLU) + "Attach.xlsx"
                dmt.queryAndWrite(cnxn, query, fileNamef, qry.qryPreCombo["qryPre103"]["headers"], sheetName)

                if input("Press Enter to run another attachment PLU or type anything and press enter to exit : ") == "":
                    attachmentplu = dmt.edmgetint("Enter the PLU of the attachment: ")
                    continue
                else:
                    break
        if input("Would you like to go again? y/n: ") == "n":
            print("Disconnecting...")
            cnxn.close()
            break
        else:
            continue
