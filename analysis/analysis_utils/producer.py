#import requests
import json
from ryurest import ryufunc
#from time import sleep
from json import dumps
from kafka import KafkaProducer
ryufunc.API = "http://172.17.0.2:8080"
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

data_sayisi = 0
DPID_list = ryufunc.get_switches()
for switch in range(len((DPID_list))):
    DPID = DPID_list[switch]
    flows = ryufunc.get_flows(DPID)
    flows_stats = ryufunc.get_flow_stats(DPID)
    flow_count = flows_stats[str(DPID)][0]['flow_count']
    clean_data_flow = eval(json.dumps(flows))

    for flow in range(flow_count):

        data = clean_data_flow[str(DPID)][flow]
        if DPID == 1:
            name = 'switch_1_flow'
            producer.send(name, value=data)
            data_sayisi +=1
        elif DPID == 2:
            name = 'switch_2_flow'
            producer.send(name, value=data)
            data_sayisi += 1
        elif DPID == 3:
            name = 'switch_3_flow'
            producer.send(name, value=data)
            data_sayisi += 1
        else:
            print("SWITCH NUMBER ERROR")
print(data_sayisi)