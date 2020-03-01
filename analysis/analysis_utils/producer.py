from data_parser import *
import aiohttp
import asyncio
from json import dumps
from kafka import KafkaProducer
import ast

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


# async def parse_array_object(data):
#     a = data['actions']
#     b = str(a)
#     s = b.replace("[", "{")
#     c = s.replace("']", "'}")
#     d = c.replace(":", "':'")
#     res = ast.literal_eval(d)
#     data['actions'] = res
#     return data


async def fetch(session):
    print('Query http://172.17.0.2:8080/stats/switches')
    async with session.get(
            'http://172.17.0.2:8080/stats/switches') as resp:

        DPID_list = await resp.json()
        print(DPID_list)
        for switch in range(len((DPID_list))):
            DPID = DPID_list[switch]
            print('Query http://172.17.0.2:8080/stats/flow/' + str(DPID))
            async with session.get('http://172.17.0.2:8080/stats/flow/' + str(DPID)) as resp:
                flows = await resp.json()
                print(flows)
            print('Query http://172.17.0.2:8080/stats/aggregateflow/' + str(DPID))
            async with session.get('http://172.17.0.2:8080/stats/aggregateflow/' + str(DPID)) as resp:
                flows_stats = await resp.json()

            flow_count = flows_stats[str(DPID)][0]['flow_count']
            clean_data_flow = eval(dumps(flows))

            for flow in range(flow_count):

                data = clean_data_flow[str(DPID)][flow]

                if DPID == 1:
                    name = 'switch_1_flow'
                    data['switch_name'] = name
                    await parse_array_object(data)
                    data['_id'] = hash_object_id(data)
                    producer.send(name, value=data)


                elif DPID == 2:
                    name = 'switch_2_flow'
                    data['switch_name'] = name
                    await parse_array_object(data)
                    producer.send(name, value=data)

                elif DPID == 3:
                    name = 'switch_3_flow'
                    data['switch_name'] = name
                    await parse_array_object(data)
                    producer.send(name, value=data)

                else:
                    print("SWITCH NUMBER ERROR")


async def go():
    async with aiohttp.ClientSession() as session:
        await fetch(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()