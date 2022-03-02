import json
import requests
import datetime
import random
import time


config=json.load(open('config.json'))
url=config['url']
headers=config['headers']

class Trakit(object):
    emergency_mode = False
    def __init__(self,asset_id,latitude = 55.15, longitude = 82.12, offset=0):#Type_of_message,Emergency,speed,lat,long,equipment_type,user_id,vini,offset=0):
        self.payload = {
            'speed':0,
            'longitude':longitude,
            'device_address':asset_id,
            'latitude':latitude,
            'timestamp':datetime.datetime.now() - datetime.timedelta(days=offset),
            'data':{
                'message_type':'',
                'time':'',
                'urgent':'',
                'subscription_node':'',
                'trakit_emergency_mode':'',
                'statuses':[{
                    'ipv4':'',
                    'node':'',
                    'vini':'vini',
                    'alert':{
                        "time": '',
                        "clearer_id": '',
                        "clearer_type": ''
                    },
                     'alias': 'Tulsa_Test_Scott',
                     'user_id': 'user_id',
                     'equipment_type':'equipment_type'
                }]
            }
        }
    def to_json(self):
        dump=self.payload.copy()
        dump['speed'] = '%.1f' % dump['speed']
        print(dump['speed'])

        if (dump['longitude'] != None):
            dump['longitude'] = '%.10f' % dump['longitude']   
            print(dump['longitude'])
        else:
            pass
        if (dump['latitude']) != None:
            dump['latitude'] = '%.10f' % dump['latitude']
            print(dump['latitude'])
        else:
            pass     

        offset=time.timezone if (time.localtime().tm_isdst==0) else time.altzone 
        dump['timestamp'] = dump['timestamp'].isoformat() + ('-%02d' % (offset / 60 / 60))
        dump['data']['trakit_emergency_mode'] = ('true' if self.emergency_mode else 'false')

        return json.dumps(dump)


