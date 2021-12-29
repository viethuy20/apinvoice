# -*- coding: utf-8 -*-
# from hdbcli import dbapi
from flask import  Flask,render_template,request,redirect,send_file,url_for,current_app, jsonify
import flask
from json import dumps
import csv , os
import json 
from datetime import datetime
import time


UPLOAD_FOLDER = './file'
file_name = 'file/ODINVOICE.csv'


def csv_to_json():
  
 
    # return jsonify(data)
    # jsonArray = []
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    csvFilePath = './file/ODINVOICE.csv'
    dic={}
    dic_va={}
    # read csv file
    with open(csvFilePath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
    
            print(type(row['BUDAT']))
             
 

    g = json.dumps(dic,indent=4)
    # return (g)
    return  g

csv_to_json()
