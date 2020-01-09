#! python 3
# Queries for Experience verification
import datetime

qryWkl = {
    "qryWkl01": {
        "headers": ["Order Pad/OCB Description","Kitchen Monitor Description","Long Description (POS Reports)","Receipt Description","POS Code","EDM #","Comments"],
        "fileName": r"C:\temp\xpient ItemMaster.xlsx",
        "sheetName": "Sheet2",
        "query": """SELECT ItemDesc AS 'Item Description',MonitorDesc AS 'Kitchen Description',LongDesc AS 'Long Description',ReceiptDesc AS 'Receipt Description' ,ShortDesc AS 'POS Code',ItemNum AS 'Item Number', ImageFile AS 'Comment' from EDMUSER.IRIS_dbo_tbl_ItemMaster where CDMLOCID=-11""",
        "text": "Running xpient Item Master query..."
    },
    "qryWkl02": {
        "headers": ['Store #', 'Discount #', 'Description', 'Scope Item #', 'Scope Cat #', 'Description','Exclusive Flag (1 = include & apply, 2 = exclude, 3 = include & do not apply)', 'Quantity', 'Discount', 'PreReq Qty'],
        "fileName": r"C:\temp\Discount Table.xlsx",
        "sheetName": "Sheet1",
        "query": """select d.CDMLOCID,d.DiscountCode,d.Description,l.ItemNumber,l.CategoryNumber,l.Description,l.ExclusiveFlag,l.Quantity,l.DiscountQty,l.PreReqQty FROM EDMUSER.IRIS_dbo_tblDiscounts d,EDMUSER.IRIS_dbo_tblDiscountLinks l where d.CDMLOCID=l.CDMLOCID AND d.DiscountCode=l.DiscountCode and d.Active=1 ORDER BY d.CDMLOCID""",
        "text": "Running Discount and Special Tracking 1 query..."
    },
    "qryWkl03": {
        "headers": ['Store Number', 'Description', 'Item Num'],
        "fileName": r"C:\temp\More Promos Menu.xlsx",
        "sheetName": "Sheet1",
        "query": """select CDMLOCID,[Text],BtnValue from EDMUSER.IRIS_dbo_tbl_MenuBtns where MenuID=7151 and BtnValue NOT in (1,63) ORDER BY CDMLOCID""",
        "text": "Running Discount and Special Tracking 2 query..."
    },
    "qryWkl04": {
        "headers": ['Store Number', 'Location', 'Property ID', 'Property Description', 'Property Value'],
        "fileName": r"C:\temp\EDM Menu Tests.xlsx",
        "sheetName": "Sheet1",
        "query": """select p.SITEID, s.NAME, p.PROPID, v.PROPTEXT, p.PROPVAL from EDMUSER.CDMSPROP p, EDMUSER.CDMPROPS v, EDMUSER.CDMSITE s WHERE p.PROPID=v.PROPID and p.SITEID=s.SITEID AND p.PROPVAL='YES'""",
        "text": "Running EDM Property Values query..."
    },
    "qryWkl05": {
        "headers": ['Menu ID', 'Store ID', 'Package ID', 'Description', 'Programmer'],
        "fileName": r"C:\temp\Open Menu Button Packages0.xlsx",
        "sheetName": "Sheet1",
        "query": """SELECT DISTINCT CAST(CASE WHEN SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1, PATINDEX('%__"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1)) = ' ' THEN SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID"', a.Fields) + 8) + 1, PATINDEX('%___"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID"', a.Fields) + 8) + 1)) ELSE SUBSTRING(a.Fields, CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1, PATINDEX('%__"SeqNum"%', a.Fields) - (CHARINDEX(',', a.Fields, CHARINDEX('"MenuID",', a.Fields) + 9) + 1)) END AS INT) AS [Menu ID], a.ToLoc AS [Store Number], a.PkgId AS [Package ID], p.NAME AS [Package Name], a.UserId AS [Transaction User ID] FROM EDMUSER.CDMAUDIT a WITH (NOLOCK), EDMUSER.CDMPKG p WITH (NOLOCK) WHERE a.PkgId = p.Id AND tablename = 'IRIS_dbo_tbl_MenuBtns' AND a.StatusId = 0 ORDER BY [Menu ID], a.PkgId, a.ToLoc, a.UserID""",
        "text": "Running Open Menu Button Packages query..."
    },
    "qryWkl06": {
        "headers": ['FromLoc','ToLoc','Id','PkgId','TranDate','TranType','Override','EffDate','TableName','TblVersion','Conflict','Undo','UserId','StatusId','StatusDate','Fields','Fixed','CommitID','Force','DeployDate'],
        "fileName": r"C:\temp\Tax Update Monitoring.xlsx",
        "sheetName": "Update" + "{:%Y-%m-%d-%H%M%S}".format(datetime.datetime.now()),
        "query": """select * from EDMUSER.CDMAUDIT with (NOLOCK) where TableName='IRIS_dbo_tblTax'""",
        "text": "Running Tax Update Verification query..."
    },
    "qryWkl07": {
        "headers": ['CDMLOCID','ItemNum','SeqNum','InsMarker','IsModifier','IsItem','ID','MinChoices','MaxChoices','PromptSoundFile','ReplacePrice','PriceAdjust','DeductItemPrice','NoNegativePrice','AllowQty','Destination','RegMode'],
        "fileName": r"C:\temp\Open Menu Button Packages0.xlsx",
        "sheetName": "Sheet1",
        "query": """select * from EDMUSER.IRIS_dbo_tbl_ItemAttachments where CDMLOCID = -11 AND IsItem = 1""",
        "text": "Running Open Menu Button Packages query..."
    },
}

qryPreItem = {
    "qryPre101": {
        #TODO update headers with correct names
        "headers":  ['1', '2', '3', '4', '5', '6', '7', '8',
                    '9', '10', '11', '12'],
        "query": """select * from EDMUSER.IRIS_dbo_tbl_ItemPricing where ItemNum = """,
        "text": "Running Corporate Recommended Pricing Check query..."
    },
    "qryPre102": {
        "headers": ['CDMLOCID', 'MenuID', 'SeqNum', 'Text', 'Style', 'BtnType', 'BtnValue', 'BtnData0', 'BtnData1',
                    'StartX', 'StartY', 'Width', 'Height', 'UpFgAttr', 'UpBgAttr', 'DnFgAttr', 'DnBgAttr', 'Color0',
                    'Color1', 'Color2', 'ItemCategory', 'ImageFile', 'BtnID', 'ReplacePrice', 'PriceAdjust',
                    'DeductItemPrice', 'NoNegativePrice', 'UIXml', 'UIBtnStyle'],
        "query": {
            "queryPt01": """select * from EDMUSER.IRIS_dbo_tbl_MenuBtns where CDMLOCID < 50000 and MenuID = """,
            "queryPt02": """ and BtnValue = """
        },
        "text": "Running Menu Buttons query..."

    }
}

qryPreCombo = {
    "qryPre102": {
        #TODO update headers with correct names
        "headers": ['1', '2', '3', '4', '5', '6', '7', '8',
                              '9', '10', '11', '12','13','14','15','16','17','18','19','20'],
        "query": {
            "queryPt01": """select * from EDMUSER.IRIS_dbo_tbl_ItemPricing_Child where ItemNum=""",
            "queryPt02": """ and ParentID="""
                  },
        "text": "Running Child Item Pricing query..."
    },
    "qryPre103": {
        #TODO update headers with correct names
        "headers": ['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12','13','14','15','16','17'],
        "query": {
            "queryPt03": """select * from EDMUSER.IRIS_dbo_tbl_ItemAttachments where ItemNum=""",
            "queryPt04": """ and ID="""
              },
        "text": "Running Item Attachments query..."
    },
    "qryPre104": {
        "headers": ['CDMLOCID', 'MenuID', 'SeqNum', 'Text', 'Style', 'BtnType', 'BtnValue', 'BtnData0', 'BtnData1',
                    'StartX', 'StartY', 'Width', 'Height', 'UpFgAttr', 'UpBgAttr', 'DnFgAttr', 'DnBgAttr', 'Color0',
                    'Color1', 'Color2', 'ItemCategory', 'ImageFile', 'BtnID', 'ReplacePrice', 'PriceAdjust',
                    'DeductItemPrice', 'NoNegativePrice', 'UIXml', 'UIBtnStyle'],
        "query": {
            "queryPt05": """select * from EDMUSER.IRIS_dbo_tbl_MenuBtns where CDMLOCID < 50000 and MenuID = """,
            "queryPt06": """ and BtnValue = """
        },
        "text": "Running Menu Buttons query..."
    }
}
# TODO Add Ohio Pricing Query

qryFIS = {
    "qryTruncateLoadTables": ['truncate table FISLoad_']
}

asanaTaskList = {
    'task0': {'name': 'RMDM Request all Project Info', 'due_on': '2019-11-16', 'assignee': '1156312730595801'},
    'task1': {'name': 'GIN Data', 'due_on': '', 'assignee': '1156312730595801'},
    'task2': {'name': 'Recipe Info', 'due_on': '', 'assignee': '1156312730595801'},
    'task3': {'name': 'Naming', 'due_on': '', 'assignee': '1156312730595801'},
    'task4': {'name': 'Pricing', 'due_on': '', 'assignee': '1156312730595801'},
    'task5': {'name': 'PMIX/IMIX/FryMIX', 'due_on': '', 'assignee': '1156312730595801'},
    'task6': {'name': 'Prep Guide Info', 'due_on': '', 'assignee': '1156312730595801'},
    'task7': {'name': 'Available in Cantina Restaurants (Beverages Only)', 'due_on': '',
              'assignee': '1156312730595801'},
    'task8': {'name': 'RMDM Received all Program Info', 'due_on': '2019-11-23', 'assignee': '1156312730595801'},
    'task9': {'name': 'Send POS Page to Training', 'due_on': '2020-01-25', 'assignee': '1156312730595801'},
    'task10': {'name': 'Route Skeleton Button Placement for Review', 'due_on': '2020-01-25',
               'assignee': '1156312730595801'},
    'task11': {'name': 'Training Material Content Due', 'due_on': '2020-01-25', 'assignee': '1156312730595801'},
    'task12': {'name': 'Send NTL Deck/POS/Recipe Pages to Leanne Greenwell and Team', 'due_on': '2019-11-23',
               'assignee': '1156312730595801'},
    'task13': {'name': 'EDM Programming', 'due_on': '2019-11-30', 'assignee': '1156312730595801'},
    'task14': {'name': 'Update Boxes to $5.49 for stores 34273, 34922, 34646', 'due_on': '2019-11-30',
               'assignee': '1156312730595801'},
    'task15': {'name': 'Send email to Digital team when programming is done', 'due_on': '2019-11-30',
               'assignee': '1156312730595801'},
    'task16': {'name': 'Send Aligned Screen Shots to Training', 'due_on': '2020-02-08', 'assignee': '1156312730595801'},
    'task17': {'name': 'Submit Recipe Page to BOH Team', 'due_on': '2019-12-07', 'assignee': '1156312730595801'},
    'task18': {'name': 'Programmer Test', 'due_on': '2020-01-22', 'assignee': '1156312730595801'},
    'task19': {'name': 'Update Ohio Combo Pricing', 'due_on': '2020-01-22', 'assignee': '1156312730595801'},
    'task20': {'name': 'DM Team POS Review', 'due_on': '2020-01-22', 'assignee': '1156312730595801'},
    'task21': {'name': 'POS Review', 'due_on': '2020-01-25', 'assignee': '1156312730595801'},
    'task22': {'name': 'Experience Readiness', 'due_on': '', 'assignee': '1156312730595801'},
    'task23': {'name': 'eRestaurant', 'due_on': '2019-12-21', 'assignee': '1156312730595801'},
    'task24': {'name': 'Add Vendor Item to Hawaii Vendor', 'due_on': '', 'assignee': '1156312730595801'},
    'task25': {'name': 'Codes Match POS Page', 'due_on': '', 'assignee': '1156312730595801'},
    'task26': {'name': 'Recipes', 'due_on': '', 'assignee': '1156312730595801'},
    'task27': {'name': 'Count Frequency', 'due_on': '', 'assignee': '1156312730595801'},
    'task28': {'name': 'Ingredient ID', 'due_on': '', 'assignee': '1156312730595801'},
    'task29': {'name': 'Unique VINs', 'due_on': '', 'assignee': '1156312730595801'},
    'task30': {'name': 'PMIX', 'due_on': '', 'assignee': '1156312730595801'},
    'task31': {'name': 'IMIX', 'due_on': '', 'assignee': '1156312730595801'},
    'task32': {'name': 'POS No (PLU #) match Recipe Page', 'due_on': '', 'assignee': '1156312730595801'},
    'task33': {'name': 'Prep and Pull Chart', 'due_on': '', 'assignee': '1156312730595801'},
    'task34': {'name': 'Storage Location', 'due_on': '', 'assignee': '1156312730595801'},
    'task35': {'name': 'Count Unit of Measure', 'due_on': '', 'assignee': '1156312730595801'},
    'task36': {'name': 'Reporting Unit of Measure', 'due_on': '', 'assignee': '1156312730595801'},
    'task37': {'name': 'Check Usage in PRE PROD', 'due_on': '', 'assignee': '1156312730595801'},
    'task38': {'name': 'EDM Second Tester', 'due_on': '2019-12-14', 'assignee': '1156312730595801'},
    'task39': {'name': 'All Program Packages are committed or scheduled', 'due_on': '2020-01-04',
               'assignee': '1156312730595801'},
    'task40': {'name': 'Review New Items in the Pricing App', 'due_on': '', 'assignee': '1156312730595801'},
    'task41': {'name': 'Query to ensure all stores are set to Corporate recommended pricing', 'due_on': '2019-12-07',
               'assignee': '1156312730595801'},
    'task42': {'name': 'Query for Child Item Pricing Records', 'due_on': '2019-12-07', 'assignee': '1156312730595801'},
    'task43': {'name': 'Query for Attachment Records', 'due_on': '2019-12-14', 'assignee': '1156312730595801'},
    'task44': {'name': 'Verify Recipe Page is complete', 'due_on': '2019-12-14', 'assignee': '1156312730595801'},
    'task45': {'name': 'All documentation is attached in OneNote', 'due_on': '2020-01-11',
               'assignee': '1156312730595801'},
    'task46': {'name': 'Verify Ohio Combo Pricing for Corporate Stores', 'due_on': '2019-12-14',
               'assignee': '1156312730595801'},
    'task47': {'name': 'Verify there is a pricing record for the new item(s) for every store', 'due_on': '2019-12-14',
               'assignee': '1156312730595801'},
    'task48': {'name': 'Query for menu buttons on the menu for all appropriate stores.', 'due_on': '',
               'assignee': '1156312730595801'},
    'task49': {'name': 'Request bitmaps from Creative', 'due_on': '2020-01-04', 'assignee': '1156312730595801'},
    'task50': {'name': 'Request POP', 'due_on': '2019-12-14', 'assignee': '1156312730595801'},
    'task51': {'name': 'Send POS Review Confirmation Email', 'due_on': '2020-01-11', 'assignee': '1156312730595801'},
    'task52': {'name': 'Load bitmaps into lab', 'due_on': '', 'assignee': '1156312730595801'},
    'task53': {'name': 'Take Screen shots for final e-mail', 'due_on': '', 'assignee': '1156312730595801'},
    'task54': {'name': 'Receive POP', 'due_on': '2019-12-21', 'assignee': '1156312730595801'},
    'task55': {'name': 'Update Training key setup in EDM', 'due_on': '', 'assignee': '1156312730595801'},
    'task56': {'name': 'EDM Testing (See OneNote)', 'due_on': '', 'assignee': '1156312730595801'},
    'task57': {'name': 'Add items to PS100NAT Category / Program in EDM / Add buttons off Screen',
               'due_on': '2019-12-21', 'assignee': '1156312730595801'},
    'task58': {'name': 'Send Experience Items to Sandip for Verification', 'due_on': '',
               'assignee': '1156312730595801'},
    'task59': {'name': 'Send ALL POS Pages to Finance', 'due_on': '2019-12-28', 'assignee': '1156312730595801'},
    'task60': {'name': 'Receive Cashier Card from Training', 'due_on': '2020-01-18', 'assignee': '1156312730595801'},
    'task61': {'name': 'Buttons on POS BY...', 'due_on': '2020-01-04', 'assignee': '1156312730595801'},
    'task62': {'name': 'Send Big Fix Button Verification', 'due_on': '2020-01-26', 'assignee': '1156312730595801'},
    'task63': {'name': 'Create Experience News', 'due_on': '2020-01-11', 'assignee': '1156312730595801'},
    'task64': {'name': 'Send MX Category Spreadsheet to Finance', 'due_on': '2020-01-18',
               'assignee': '1156312730595801'},
    'task65': {'name': 'Send Experience News to the Service Desk', 'due_on': '2020-01-18',
               'assignee': '1156312730595801'},
    'task66': {'name': 'Menu Button Issues Resolved', 'due_on': '2020-01-18', 'assignee': '1156312730595801'},
    'task67': {'name': 'Start Sell', 'due_on': '2020-01-25', 'assignee': '1156312730595801'}

}