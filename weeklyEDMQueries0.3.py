#! python3
#Written by Alex Ilson
#Queries EDM ItemMaster and creates spreadsheet with the results.
#

import pypyodbc, pandas as pd, sys

def connectEDM():
    #Attempt to connect to EDM and create connect object
    try:
        print('Attemping to connect to EDM...')
        connectionEDM = pypyodbc.connect("Driver={SQL Server};"
                                "Server=SQL901C1;"
                                "Database=TacoBellHQ1;"
                                "Trusted_Connection=yes;")
    except pypyodbc.Error as e:
        print('Unable to connect to EDM. Exiting.')
        print(e.args[1])
        sys.exit()
    else:
        print('Connection successful!')
        return connectionEDM

def queryAndWrite(EDMConnection, inQuery, outputFilename, headerNames, worksheetName):
    #create writer object
    writer = pd.ExcelWriter(outputFilename)
    #create dataframe from query results
    df = pd.read_sql_query(inQuery, EDMConnection)
    #write dataframe to Excel spreadsheet
    df.to_excel(writer, sheet_name=worksheetName, na_rep='NULL', header=headerNames, index=False)
    #get worksheet object
    worksheet = writer.sheets[worksheetName]
    #resize columns to width of 30
    worksheet.set_column(0, len(headerNames), 30)
    #save writer
    writer.save()

if __name__ == "__main__":
    while True:
        #Define variables
        headers = ['Store #','Discount #','Description','Scope Item #','Scope Cat #','Description','Exclusive Flag','Quantity','Discount','PreReq Qty']
        fileName = r'.\xpient ItemMasterTEST.xlsx'
        sheetName = 'Sheet2'
        query = """select d.CDMLOCID,d.DiscountCode,d.Description,l.ItemNumber,l.CategoryNumber,l.Description,l.ExclusiveFlag,l.Quantity,l.DiscountQty,l.PreReqQty FROM EDMUSER.IRIS_dbo_tblDiscounts d,EDMUSER.IRIS_dbo_tblDiscountLinks l where d.CDMLOCID=l.CDMLOCID AND d.DiscountCode=l.DiscountCode and d.Active=1 ORDER BY d.CDMLOCID"""
        cnxn = connectEDM()
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        #close connection
        cnxn.close()
        break
