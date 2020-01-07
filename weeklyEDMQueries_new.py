#! python 3
# Queries for Experience verification

import datamgmttools as dmt, datetime, queries as qry

#TODO: get input from user: Type of Project (National/RIT/etc), Type of item (Combo/etc), and PLU

#TODO: Populate a list or something? a dict? with the queries, depending on types

if __name__ == "__main__":
    while True:
        # Connect to EDM
        cnxn = dmt.connectEDM()
        for i in qry.qryWkl:
            print(qry.qryWkl[i]["text"])
            dmt.queryAndWrite(cnxn, qry.qryWkl[i]["query"], qry.qryWkl[i]["fileName"], qry.qryWkl[i]["headers"], qry.qryWkl[i]["sheetName"])
        print("Disconnecting...")
        cnxn.close()
        break
