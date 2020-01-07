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

