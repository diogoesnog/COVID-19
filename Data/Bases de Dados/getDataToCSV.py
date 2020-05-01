#coding: utf-8

import requests
import stat
import time
import csv
import re
import os

class DataToCSV():

    def getData(self):
        
        os.system('chmod 755 data.sh')
        os.system('./data.sh')
    
    def  JSONtoCSV(self, name):

        fileJSON = 0
        fileCSV = 0
        
        if(name == "UE"):
            fileJSON = open("dadosUE.json", "r")
            fileCSV = open("dadosUE.csv", "w")

        elif(name == "PT"):
            fileJSON = open("dadosPT.json", "r")
            fileCSV = open("dadosPT.csv", "w")
        
        else:
            print("Name Errado\n")

        with fileCSV:
            reader = csv.writer(fileCSV)
            
            reader.writerow(["Data", "Reservas"])

            for line in fileJSON:
                linesTable = re.findall('C":\[(.*?)\]', line)

            for element in linesTable:
                cleanElement =  element.replace('"', '')
                line = cleanElement.split(',')
                
                data = time.strftime('%d/%m/%Y', time.localtime(int(str(line[0])[:-3])))
                reservas = line[1]

                reader.writerow([data, reservas])

        fileJSON.close()
        fileCSV.close()
    
# Run
myDataToCSV = DataToCSV()

myDataToCSV.getData()
myDataToCSV.JSONtoCSV("UE")
myDataToCSV.JSONtoCSV("PT")