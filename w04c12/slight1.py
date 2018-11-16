import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
all_rows = cur.fetchall()
print('1):', all_rows)

conn.close()
