import psycopg2
from datetime import datetime
import time
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="ec2-54-204-99-176.compute-1.amazonaws.com",database="d1m8qisg5a9i1t", user="zbrqxkwnzsxgmt", password="1aa020dc99d5dd285c2bcc96ac0288d08416b0f35891914344afc08c2e567def")
    # create a cursor
    cur = conn.cursor()
    # Execute a sql
    cur.execute('SELECT * FROM invoice limit 2 ')
    # display the PostgreSQL database server version
    row = cur.fetchall()
    dic = {}
    dic_va={}
    for i in row:
        
        date = datetime.strptime(str(i[2]), '%Y-%m-%d')
      
        date = time.mktime((date).timetuple())
        dic_va["invoice_code"] = "invoice" + " " + i[0] +""
        dic_va["invoice_date"] = str((date))
        dic[i[1]] = [dic_va]
        
   
    # close the communication with the PostgreSQL
    print(dic)
    cur.close()
except Exception as e:
    print('Unable to connect %s' % str(e))
finally:
    if conn is not None:
        conn.close()