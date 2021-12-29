
from flask import  Flask,render_template,request,redirect,send_file,url_for,current_app, jsonify
import flask
from json import dumps
import csv , os
import json 
from datetime import datetime
import time
import psycopg2

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# UPLOAD_FOLDER = './file'
# file_name = 'file/ODINVOICE.csv'
APP_ROOT = os.path.dirname(__file__)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/get-invoice', methods=['GET','POST'])

def csv_to_json():
    data = request.json
    dic={}

    try:
    # connect to the PostgreSQL server
        conn = psycopg2.connect(host="ec2-54-204-99-176.compute-1.amazonaws.com",database="d1m8qisg5a9i1t", user="zbrqxkwnzsxgmt", password="1aa020dc99d5dd285c2bcc96ac0288d08416b0f35891914344afc08c2e567def")
        # create a cursor
        cur = conn.cursor()
        # Execute a sql
        cur.execute('SELECT * FROM invoice')
        # display the PostgreSQL database server version
        row = cur.fetchall()
        for i in row:
            dic_va={}
            if i[1]  in data['order_partner_id_list']:
                # print(row['OD'])
                # print(row['BUDAT'])
                date = datetime.strptime(str(i[2]), '%Y-%m-%d')
      
                date = time.mktime((date).timetuple())
                dic_va["invoice_code"] = "invoice" + " " + i[0] +""
                dic_va["invoice_date"] = str((date))
                dic[i[1]] = [dic_va]
 
                
             
        # close the communication with the PostgreSQL
        cur.close()
    except Exception as e:
        print('Unable to connect %s' % str(e))
    finally:
        if conn is not None:
            conn.close()

    return  dic
 
if __name__ == '__main__':
    app.run(host="0.0.0.0")