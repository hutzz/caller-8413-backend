import MySQLdb
# import mysql.connector

def count(mysql: MySQLdb):
    cur = mysql.connection.cursor()
    cur.execute("SELECT job_count FROM abbie")
    fetchdata = cur.fetchone()
    for f in fetchdata: return str(f)
def increment(mysql: MySQLdb, data):
    cur1 = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    try:
        cur1.execute(f"UPDATE abbie SET job_count = job_count + {data}")
        cur2.execute("SELECT job_count FROM abbie")
        mysql.connection.commit()
        print('jobs added')
        fetchdata = cur2.fetchone()
    except:
        mysql.connection.rollback()
    finally:
        cur1.close()
        cur2.close()
    for f in fetchdata: return str(f)
def decrement(mysql: MySQLdb, data):
    cur1 = mysql.connection.cursor()
    cur2 = mysql.connection.cursor()
    try:
        cur1.execute(f"UPDATE abbie SET job_count = job_count - {data}")
        cur2.execute("SELECT job_count FROM abbie")
        mysql.connection.commit()
        print('jobs removed')
        fetchdata = cur2.fetchone()
    except:
        mysql.connection.rollback()
    finally:
        cur1.close()
        cur2.close()
    for f in fetchdata: return str(f)