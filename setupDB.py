import sqlite3 as sqlite

createTxTable = '''
    CREATE TABLE IF NOT EXISTS txs (
        id integer PRIMARY KEY,
        chain text NOT NULL,
        tx text NOT NULL
    );
'''

createHeightTable = '''
    CREATE TABLE IF NOT EXISTS heights (
        id integer PRIMARY KEY,
        chain text NOT NULL,
        height integer
    );
'''

createTunnelTable = '''
    CREATE TABLE IF NOT EXISTS tunnel (
        id integer PRIMARY KEY,
        sourceAddress text NOT NULL,
        targetAddress text NOT NULL
    );
'''

createTableExecuted = '''
    CREATE TABLE IF NOT EXISTS executed (
        id integer PRIMARY KEY,
        sourceAddress text NOT NULL,
        targetAddress text NOT NULL,
        tnTxId text NOT NULL,
        ethTxId text NOT NULL,
        timestamp text,
        amount real,
        amountFee real
    );
'''

con = sqlite.connect('gateway.db')
cursor = con.cursor()
cursor.execute(createTxTable)
cursor.execute(createHeightTable)
cursor.execute(createTunnelTable)
cursor.execute(createTableExecuted)
# TODO: edit to start values
cursor.execute('INSERT INTO heights ("chain", "height") VALUES ("ETH", 8980500)')
cursor.execute('INSERT INTO heights ("chain", "height") VALUES ("TN", 832013)')
con.commit()
con.close()