# from fastapi import FastAPI
import json
import argparse
import os
import csv
import requests
import time
from event import Trakit,url,headers
# app=FastAPI()

parser=argparse.ArgumentParser(description="Trakit Event Simulation")
parser.add_argument('routefile',type=str,help='read .csv file')
parser.add_argument('--d','--timestamp-offset',type=int,default=0,help='for real-time')
parser.add_argument('--i','--timestamp-interval',type=int,default=1,help='1 day back data')

args=parser.parse_args()

ASSET_ID = os.path.basename(args.routefile).split('.')[0]

print(ASSET_ID)
with open(args.routefile, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # route = [map(float, o) for o in reader ]
    # print(reader)
    rows=[]
    header=next(reader)
    for row in reader:
        rows.append(row)
# print(header)

# Type_of_message=rows[0][0]
# Emergency=rows[0][1]
SPEED=rows[0][2]
# latitude=rows[0][4]
# longitude=rows[0][5]
# equipment_type=rows[0][6]
# user_id=rows[0][7]
# vini=rows[0][8]

# config=json.load(open('config.json'))
# url=config['url']
# headers=config['headers']

p=Trakit(ASSET_ID)


while True:
    print ('starting route...')
    try:
        print(p.to_json())
        r=requests.post(url,data=p.to_json(),headers=headers)
        print(r)
        if(r.status_code == 201):
            print('success')
        else:
            print('error')
    except:
        print('error posting, retrying in 10 seconds')
        print('hit ctrl+c to exit')
        time.sleep(10)
    


