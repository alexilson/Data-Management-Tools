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
        #  TODO update headers with correct names
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
        # TODO update headers with correct names
        "headers": ['1', '2', '3', '4', '5', '6', '7', '8',
                              '9', '10', '11', '12','13','14','15','16','17','18','19','20'],
        "query": {
            "queryPt01": """select * from EDMUSER.IRIS_dbo_tbl_ItemPricing_Child where ItemNum=""",
            "queryPt02": """ and ParentID="""
                  },
        "text": "Running Child Item Pricing query..."
    },
    "qryPre103": {
        # TODO update headers with correct names
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
    'task000': {'name': 'RMDM Request all Project Info', 'due_on': '2019-12-23', 'assignee': 'alexander.ilson@yum.com'},
    'task001': {'name': 'RMDM Received all Project Info', 'due_on': '2019-12-30',
                'assignee': 'alexander.ilson@yum.com'},
    'task002': {'name': 'Send POS Page to Training', 'due_on': '2020-01-02', 'assignee': 'alexander.ilson@yum.com'},
    'task003': {'name': 'Route Skeleton Button Placement for Review', 'due_on': '2020-01-02',
                'assignee': 'alexander.ilson@yum.com'},
    'task004': {'name': 'Training Material Content Due', 'due_on': '2020-01-02', 'assignee': 'alexander.ilson@yum.com'},
    'task005': {'name': 'Send NTL Deck/POS/Recipe Pages to Leanne Greenwell and Team', 'due_on': '2020-01-06',
                'assignee': 'alexander.ilson@yum.com'},
    'task006': {'name': 'EDM Programming', 'due_on': '2020-01-16', 'assignee': 'alexander.ilson@yum.com'},
    'task007': {'name': 'Update Ohio Combo Pricing', 'due_on': '2020-01-16', 'assignee': 'alexander.ilson@yum.com'},
    'task008': {'name': 'Update Box Pricing for stores 34273, 34922, 34646, 36322', 'due_on': '2020-01-16',
                'assignee': 'alexander.ilson@yum.com'},
    'task009': {'name': 'Send email to Digital team when programming is done', 'due_on': '2020-01-16',
                'assignee': 'alexander.ilson@yum.com'},
    'task010': {'name': 'Send Aligned Screen Shots to project team', 'due_on': '2020-01-16',
                'assignee': 'alexander.ilson@yum.com'},
    'task011': {'name': 'Submit Recipe Page to BOH Team', 'due_on': '2020-01-16',
                'assignee': 'alexander.ilson@yum.com'},
    'task012': {'name': 'Programmer Test', 'due_on': '2020-01-27', 'assignee': 'alexander.ilson@yum.com'},
    'task013': {'name': 'DM Team POS Review', 'due_on': '2020-01-27', 'assignee': 'alexander.ilson@yum.com'},
    'task014': {'name': 'POS Review', 'due_on': '2020-01-30', 'assignee': 'alexander.ilson@yum.com'},
    'task015': {'name': 'Experience Readiness', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
    'task016': {'name': 'Request bitmaps from Creative', 'due_on': '2020-01-30', 'assignee': 'alexander.ilson@yum.com'},
    'task017': {'name': 'Request POP', 'due_on': '2020-01-30', 'assignee': 'alexander.ilson@yum.com'},
    'task018': {'name': 'Send POS Review Confirmation Email', 'due_on': '2020-02-06',
                'assignee': 'alexander.ilson@yum.com'},
    'task019': {'name': 'Receive POP', 'due_on': '2020-02-06', 'assignee': 'alexander.ilson@yum.com'},
    'task020': {'name': 'Update Training key setup in EDM', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
    'task021': {'name': 'Add items to PS Category', 'due_on': '2020-02-06', 'assignee': 'alexander.ilson@yum.com'},
    'task022': {'name': 'Send Experience Items to Sandip for Verification', 'due_on': '2019-12-02',
                'assignee': 'alexander.ilson@yum.com'},
    'task023': {'name': 'Send ALL POS Pages to Finance', 'due_on': '2020-02-13', 'assignee': 'alexander.ilson@yum.com'},
    'task024': {'name': 'Receive Cashier Card from Training', 'due_on': '2020-02-13',
                'assignee': 'alexander.ilson@yum.com'},
    'task025': {'name': 'Add Buttons to Menu(s)', 'due_on': '2020-02-17', 'assignee': 'alexander.ilson@yum.com'},
    'task026': {'name': 'Send Big Fix Button Verification', 'due_on': '2020-02-21',
                'assignee': 'alexander.ilson@yum.com'},
    'task027': {'name': 'Create Experience News', 'due_on': '2020-02-27', 'assignee': 'alexander.ilson@yum.com'},
    'task028': {'name': 'Send MX Category Spreadsheet to Finance', 'due_on': '2020-03-05',
                'assignee': 'alexander.ilson@yum.com'},
    'task029': {'name': 'Send Experience News to the Service Desk', 'due_on': '2020-03-05',
                'assignee': 'alexander.ilson@yum.com'},
    'task030': {'name': 'Menu Button Issues Resolved', 'due_on': '2020-03-05', 'assignee': 'alexander.ilson@yum.com'},
    'task031': {'name': 'Start Sell', 'due_on': '2020-03-12', 'assignee': 'alexander.ilson@yum.com'},

}

asanaSubTaskList = {
    'subtask014': {
        'taskParams': {
            'name': 'eRestaurant', 'due_on': '2020-01-30', 'assignee': 'alexander.ilson@yum.com'
        },
                   'parentTask': 'task015'},
    'subtask000': {
        'taskParams': {'name': 'Add Vendor Item to Hawaii Vendor', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
        'parentTask': 'subtask014'},
    'subtask001': {'taskParams': {'name': 'Codes Match POS Page', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask002': {'taskParams': {'name': 'Recipes', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask003': {'taskParams': {'name': 'Count Frequency', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask004': {'taskParams': {'name': 'Ingredient ID', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask005': {'taskParams': {'name': 'Unique VINs', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask006': {'taskParams': {'name': 'PMIX', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask007': {'taskParams': {'name': 'IMIX', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask008': {
        'taskParams': {'name': 'POS No (PLU #) match Recipe Page', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
        'parentTask': 'subtask014'},
    'subtask009': {'taskParams': {'name': 'Prep and Pull Chart', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask010': {'taskParams': {'name': 'Storage Location', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask011': {'taskParams': {'name': 'Count Unit of Measure', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'subtask014'},
    'subtask012': {
        'taskParams': {'name': 'Reporting Unit of Measure', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
        'parentTask': 'subtask014'},
    'subtask013': {
        'taskParams': {'name': 'Check Usage in PRE PROD', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
        'parentTask': 'subtask014'},
    'subtask015': {
        'taskParams': {'name': 'EDM Second Tester', 'due_on': '2020-01-30', 'assignee': 'alexander.ilson@yum.com'},
        'parentTask': 'task015'},
    'subtask016': {'taskParams': {'name': 'All Program Packages are committed or scheduled', 'due_on': '2020-02-20',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask017': {'taskParams': {'name': 'Review New Items in the Pricing App', 'due_on': '2020-02-13',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask018': {'taskParams': {'name': 'Query to ensure all stores are set to Corporate recommended pricing',
                                  'due_on': '2019-11-21', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task015'},
    'subtask019': {'taskParams': {'name': 'Query for Child Item Pricing Records', 'due_on': '2019-11-21',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask020': {'taskParams': {'name': 'Query for Attachment Records', 'due_on': '2020-01-30',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask021': {'taskParams': {'name': 'Verify Recipe Page is complete', 'due_on': '2020-01-30',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask022': {'taskParams': {'name': 'All documentation is attached in OneNote', 'due_on': '2020-02-27',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask023': {'taskParams': {'name': 'Query Ohio Combo Pricing for Corporate Stores', 'due_on': '2020-01-30',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask024': {
        'taskParams': {'name': 'Query to Verify there is a pricing record for the new item(s) for every store',
                       'due_on': '2019-11-21', 'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask025': {
        'taskParams': {'name': 'Query for menu buttons on the menu for all appropriate stores.', 'due_on': '2020-02-17',
                       'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task015'},
    'subtask026': {'taskParams': {'name': 'GIN Data', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask027': {'taskParams': {'name': 'Recipe Info', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask028': {'taskParams': {'name': 'Naming', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask029': {'taskParams': {'name': 'Pricing', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask030': {'taskParams': {'name': 'PMIX/IMIX/FryMIX', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask031': {'taskParams': {'name': 'Prep Guide Info', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task000'},
    'subtask032': {'taskParams': {'name': 'Available in Cantina Restaurants (Beverages Only)', 'due_on': '',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task000'},
    'subtask033': {'taskParams': {'name': 'Load bitmaps into lab', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task018'},
    'subtask034': {'taskParams': {'name': 'Take Screen shots for final e-mail', 'due_on': '',
                                  'assignee': 'alexander.ilson@yum.com'}, 'parentTask': 'task018'},
    'subtask035': {'taskParams': {'name': 'Test Training Key', 'due_on': '', 'assignee': 'alexander.ilson@yum.com'},
                   'parentTask': 'task020'},
}
