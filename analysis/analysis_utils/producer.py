import aiohttp
import asyncio
from json import dumps
from kafka import KafkaProducer
import ast
from analysis.analysis_utils.data_parser import hash_object_id,parse_array_object


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))



async def fetch(session):
    while True:
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
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)


                    elif DPID == 2:
                        name = 'switch_2_flow'
                        data['switch_name'] = name
                        await parse_array_object(data)
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)

                    elif DPID == 3:
                        name = 'switch_3_flow'
                        data['switch_name'] = name
                        await parse_array_object(data)
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)

                    else:
                        print("SWITCH NUMBER ERROR")


async def go():
    async with aiohttp.ClientSession() as session:
        await fetch(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()