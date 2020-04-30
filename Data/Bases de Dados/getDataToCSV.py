#coding: utf-8

import requests
import time
import csv
import re

class DataToCSV():

    def getEuropeanUnionData(self):

        url = "https://wabi-west-europe-d-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true"

        payload = "{\"version\":\"1.0.0\",\"queries\":[{\"Query\":{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"f1\",\"Entity\":\"FORWARDKEYS_BOOKING_EU\"},{\"Name\":\"d\",\"Entity\":\"D_TEMPO\"}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"Data\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.Data\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"% Reservas EU - Variação dia a dia\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.% Reservas EU - Var\"}],\"Where\":[{\"Condition\":{\"Between\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"d\"}},\"Property\":\"DES_DIA\"}},\"LowerBound\":{\"DateSpan\":{\"Expression\":{\"Now\":{}},\"TimeUnit\":0}},\"UpperBound\":{\"DateSpan\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"Now\":{}},\"Amount\":-1,\"TimeUnit\":0}},\"Amount\":1,\"TimeUnit\":2}},\"TimeUnit\":0}}}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"BinnedLineSample\":{}}},\"Version\":1}}}]},\"CacheKey\":\"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"f1\",\"Entity\":\"FORWARDKEYS_BOOKING_EU\"},{\"Name\":\"d\",\"Entity\":\"D_TEMPO\"}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"Data\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.Data\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"% Reservas EU - Variação dia a dia\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.% Reservas EU - Var\"}],\"Where\":[{\"Condition\":{\"Between\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"d\"}},\"Property\":\"DES_DIA\"}},\"LowerBound\":{\"DateSpan\":{\"Expression\":{\"Now\":{}},\"TimeUnit\":0}},\"UpperBound\":{\"DateSpan\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"Now\":{}},\"Amount\":-1,\"TimeUnit\":0}},\"Amount\":1,\"TimeUnit\":2}},\"TimeUnit\":0}}}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"BinnedLineSample\":{}}},\"Version\":1}}}]}\",\"QueryId\":\"\",\"ApplicationContext\":{\"DatasetId\":\"64e94dc9-a795-419c-95aa-98fe52509c94\",\"Sources\":[{\"ReportId\":\"8639b885-081e-40ee-a2b3-a7ade2da5d0c\"}]}}],\"cancelQueries\":[],\"modelId\":221950}"
        headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'RequestId': 'f9b812ed-d7e3-a2ff-4fc1-a61261844b08',
        'X-PowerBI-ResourceKey': '6e2a3269-ab56-40ef-859b-f749ed24f6fe',
        'ActivityId': '655833b2-b5de-450c-ae6a-a9ba6667d933',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://app.powerbi.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://app.powerbi.com/view?r=eyJrIjoiNmUyYTMyNjktYWI1Ni00MGVmLTg1OWItZjc0OWVkMjRmNmZlIiwidCI6IjczYzc3MWNkLTFjNzUtNDc5OS1hYTQwLTFjOWZmM2NmM2U1ZSIsImMiOjl9',
        'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        file = open("DadosUE.json", "w")
        file.write(response.text.encode('utf8'))
        file.close()

    def getPortugalData(self):

        url = "https://wabi-west-europe-d-primary-api.analysis.windows.net/public/reports/querydata?synchronous=true"

        payload = "{\"version\":\"1.0.0\",\"queries\":[{\"Query\":{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"f1\",\"Entity\":\"FORWARDKEYS_BOOKING_EU\"},{\"Name\":\"d\",\"Entity\":\"D_TEMPO\"}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"Data\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.Data\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"% Reservas EU - Variação dia a dia\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.% Reservas EU - Var\"}],\"Where\":[{\"Condition\":{\"Between\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"d\"}},\"Property\":\"DES_DIA\"}},\"LowerBound\":{\"DateSpan\":{\"Expression\":{\"Now\":{}},\"TimeUnit\":0}},\"UpperBound\":{\"DateSpan\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"Now\":{}},\"Amount\":-1,\"TimeUnit\":0}},\"Amount\":1,\"TimeUnit\":2}},\"TimeUnit\":0}}}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"BinnedLineSample\":{}}},\"Version\":1}}}]},\"CacheKey\":\"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"f1\",\"Entity\":\"FORWARDKEYS_BOOKING_EU\"},{\"Name\":\"d\",\"Entity\":\"D_TEMPO\"}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"Data\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.Data\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"f1\"}},\"Property\":\"% Reservas EU - Variação dia a dia\"},\"Name\":\"FORWARDKEYS_BOOKING_EU.% Reservas EU - Var\"}],\"Where\":[{\"Condition\":{\"Between\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"d\"}},\"Property\":\"DES_DIA\"}},\"LowerBound\":{\"DateSpan\":{\"Expression\":{\"Now\":{}},\"TimeUnit\":0}},\"UpperBound\":{\"DateSpan\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"DateAdd\":{\"Expression\":{\"Now\":{}},\"Amount\":-1,\"TimeUnit\":0}},\"Amount\":1,\"TimeUnit\":2}},\"TimeUnit\":0}}}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"BinnedLineSample\":{}}},\"Version\":1}}}]}\",\"QueryId\":\"\",\"ApplicationContext\":{\"DatasetId\":\"64e94dc9-a795-419c-95aa-98fe52509c94\",\"Sources\":[{\"ReportId\":\"8639b885-081e-40ee-a2b3-a7ade2da5d0c\"}]}}],\"cancelQueries\":[],\"modelId\":221950}"
        headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'RequestId': 'f9b812ed-d7e3-a2ff-4fc1-a61261844b08',
        'X-PowerBI-ResourceKey': '6e2a3269-ab56-40ef-859b-f749ed24f6fe',
        'ActivityId': '655833b2-b5de-450c-ae6a-a9ba6667d933',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://app.powerbi.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://app.powerbi.com/view?r=eyJrIjoiNmUyYTMyNjktYWI1Ni00MGVmLTg1OWItZjc0OWVkMjRmNmZlIiwidCI6IjczYzc3MWNkLTFjNzUtNDc5OS1hYTQwLTFjOWZmM2NmM2U1ZSIsImMiOjl9',
        'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        fileJSON = open("DadosUE.json", "w")
        fileJSON.write(response.text.encode('utf8'))
        fileJSON.close()
    
    def  JSONtoCSV(self, name):

        fileJSON = 0
        fileCSV = 0
        
        if(name == "UE"):
            fileJSON = open("DadosUE.json", "r")
            fileCSV = open("DadosUE.csv", "w")

        elif(name == "PT"):
            fileJSON = open("DadosPT.json", "r")
            fileCSV = open("DadosPT.csv", "w")
        
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
                
                reader.writerow([line[0], line[1]])

        fileJSON.close()
        fileCSV.close()

# Run
myDataToCSV = DataToCSV()

myDataToCSV.getEuropeanUnionData()
myDataToCSV.JSONtoCSV("UE")

myDataToCSV.getPortugalData()
myDataToCSV.JSONtoCSV("PT")