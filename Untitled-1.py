from flask import  Flask
import flask
from json import dumps
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import csv , os
import json 
csvFilePath = os.path.basename('ODINVOICE.csv')
dic={}
#read csv file
with open(csvFilePath, encoding='utf-8-sig') as csvf: 
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf) 

    #convert each csv row into python dict
    for row in csvReader: 
        
        dic[row['OD']] = row['XBLNR']
        # print(row['XBLNR'],row['OD'])
     
        # for i,j in row.items():
        #     # print(i,j)
        #     # dic[j[0]] = j
        #     print (type(i))
        # print("@@@@@@@")
        print(dic)
       

        #add this python dict to json array
    

       
