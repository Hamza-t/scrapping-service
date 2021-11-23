#database.py
import sqlite3


def save_insat_db(data):
	conn = sqlite3.connect("database.sql")
	cur = conn.cursor()
	cols = "`,`".join([str(i) for i in data.columns.tolist()])
	for i,row in data.iterrows():
	    sql = "INSERT INTO `insat_page` (`" +cols + "`) VALUES (" + "%s,"*(len(tmp)-1) + "%s)"
	    cur.execute(sql, tuple(tmp))
	    conn.commit()
	conn.close()
