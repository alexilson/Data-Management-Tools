#! python3
#Written by Alex Ilson
#Queries EDM ItemMaster and creates spreadsheet with the results.
#

import pypyodbc, pandas as pd, sys, os

def connectEDM():
    #Attempt to connect to EDM and create connect object
    try:
        print("Attempting to connect to EDM...")
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
    print("getting worksheet object...")
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

if __name__ == "__main__":
    while True:
        #Connect to EDM
        cnxn = connectEDM()
        #Define variables for xpient Item Master query
        headers = ["Order Pad/OCB Description","Kitchen Monitor Description","Long Description (POS Reports)","Receipt Description","POS Code","EDM #","Comments"]
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\xpient ItemMaster.xlsx'
        sheetName = "Sheet2"
        query = """SELECT ItemDesc AS 'Item Description',MonitorDesc AS 'Kitchen Description',LongDesc AS 'Long Description',ReceiptDesc AS 'Receipt Description' ,ShortDesc AS 'POS Code',ItemNum AS 'Item Number', ImageFile AS 'Comment' from EDMUSER.IRIS_dbo_tbl_ItemMaster where CDMLOCID=-11"""
        print("Running xpient Item Master query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        #Define variables for Discount and Special Tracking 1 query
        headers = ['Store #', 'Discount #', 'Description', 'Scope Item #', 'Scope Cat #', 'Description','Exclusive Flag', 'Quantity', 'Discount', 'PreReq Qty']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\Discounts & Specials in EDM\Discount Table.xlsx'
        sheetName = "Sheet1"
        query = """select d.CDMLOCID,d.DiscountCode,d.Description,l.ItemNumber,l.CategoryNumber,l.Description,l.ExclusiveFlag,l.Quantity,l.DiscountQty,l.PreReqQty FROM EDMUSER.IRIS_dbo_tblDiscounts d,EDMUSER.IRIS_dbo_tblDiscountLinks l where d.CDMLOCID=l.CDMLOCID AND d.DiscountCode=l.DiscountCode and d.Active=1 ORDER BY d.CDMLOCID"""
        print("Running Discount and Special Tracking 1 query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        headers = ['Store Number', 'Description', 'Item Num']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\Discounts & Specials in EDM\More Promos Menu.xlsx'
        sheetName = "Sheet1"
        query = """select CDMLOCID,[Text],BtnValue from EDMUSER.IRIS_dbo_tbl_MenuBtns where MenuID=7151 and BtnValue NOT in (1,63) ORDER BY CDMLOCID"""
        print("Running Discount and Special Tracking 2 query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        headers = ['Store Number', 'Location', 'Property ID', 'Property Description', 'Property Value']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\_Menu Updates\EDM Menu Tests.xlsx'
        sheetName = "Sheet1"
        query = """select p.SITEID, s.NAME, p.PROPID, v.PROPTEXT, p.PROPVAL from EDMUSER.CDMSPROP p, EDMUSER.CDMPROPS v, EDMUSER.CDMSITE s WHERE p.PROPID=v.PROPID and p.SITEID=s.SITEID AND p.PROPVAL='YES'"""
        print("Running EDM Property Values query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        headers = ['Menu ID', 'Store ID', 'Package ID', 'Description', 'Programmer']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\Open Menu Button Packages.xlsx'
        sheetName = "Sheet1"
        query = """SELECT DISTINCT CAST(CASE WHEN SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1, PATINDEX('%__"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1)) = ' ' THEN SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID"', a.Fields) + 8) + 1, PATINDEX('%___"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID"', a.Fields) + 8) + 1)) ELSE SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1, PATINDEX('%__"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1)) END AS INT) AS [Menu ID], a.ToLoc AS [Store Number], a.PkgId AS [Package ID], p.NAME AS [Package Name], a.UserId AS [Transaction User ID] FROM EDMUSER.CDMAUDIT a WITH (NOLOCK), EDMUSER.CDMPKG p WITH (NOLOCK) WHERE a.PkgId = p.Id AND tablename = 'IRIS_dbo_tbl_MenuBtns' AND a.StatusId = 0 ORDER BY [Menu ID], a.PkgId, a.ToLoc, a.UserID"""
        print("Running Open Menu Button Packages query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        headers = ['FromLoc','ToLoc','Id','PkgId','TranDate','TranType','Override','EffDate','TableName','TblVersion','Conflict','Undo','UserId','StatusId','StatusDate','Fields','Fixed','CommitID','Force','DeployDate']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\Tax Update Monitoring.xlsx'
        sheetName = "Sheet1"
        query = """select * from EDMUSER.CDMAUDIT with (NOLOCK) where TableName='IRIS_dbo_tblTax'"""
        print("Running Tax Update Verification query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        headers = ['StoreID','NAME','ProcessorID','DMB','bOption','DATASITE','PROPID','PROPTEXT']
        fileName = r'\\us\irv\Information_Technology\Data_Management\CFM TEAM INFORMATION\POF\Store Data Verification.xlsx'
        sheetName = "Sheet1"
        query = """select c.StoreID,d.NAME, c.ProcessorID, s.DMB, p.bOption, r.DATASITE, e.PROPID,f.PROPTEXT from EDMUSER.IRIS_dbo_tblCCDataTB c, EDMUSER.IRIS_dbo_tblStoreConfigurationCodeTB s, EDMUSER.IRIS_dbo_tblPayrollSetupOptions p, EDMUSER.CDMRTBL r, EDMUSER.CDMSITE d, EDMUSER.CDMSPROP e, EDMUSER.CDMPROPS f where c.StoreID=s.CDMLOCID and c.StoreID=p.CDMLOCID and s.CDMLOCID=p.CDMLOCID and c.StoreID=r.SITE and s.CDMLOCID=r.SITE and p.CDMLOCID=r.SITE and c.StoreID=d.SITEID and s.CDMLOCID=d.SITEID and p.CDMLOCID=d.SITEID and r.SITE=d.SITEID and c.StoreID=e.SITEID and s.CDMLOCID=e.SITEID and p.CDMLOCID=e.SITEID and r.SITE=e.SITEID and d.SITEID=e.SITEID and e.PROPID=f.PROPID and p.OptionID=44 and r.NAME='IRIS_dbo_tbl_Application' and e.PROPVAL='YES'"""
        print("Running Store Data Verification query...")
        queryAndWrite(cnxn, query, fileName, headers, sheetName)
        #close connection
        print("Disconnecting...")
        cnxn.close()
        break
