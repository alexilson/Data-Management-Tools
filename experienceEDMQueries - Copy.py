#! python 3
# Queries for Experience verification

import datamgmttools as dmt, datetime, queries as qrs

#TODO: get input from user: Type of Project (National/RIT/etc), Type of item (Combo/etc), and PLU

#TODO: Populate a list or something? a dict? with the queries, depending on types

if __name__ == "__main__":
    while True:
        cnxn = dmt.connectEDM()
        for i in qrs.qrsExp:
            #Connect to EDM
            print(qrs.qrsExp[i]["text"])
            dmt.queryAndWrite(cnxn, qrs.qrsExp[i]["query"], qrs.qrsExp[i]["fileName"], qrs.qrsExp[i]["headers"], qrs.qrsExp[i]["sheetName"])
        break
