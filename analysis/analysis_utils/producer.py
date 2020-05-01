import aiohttp
import asyncio
from json import dumps
from kafka import KafkaProducer
from analysis.analysis_utils.data_parser import hash_object_id,parse_array_object,clean_port_data


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
async def fetch(session):
    while True:
        async with session.get(
                'http://172.17.0.2:8080/stats/switches') as resp:
            DPID_list = await resp.json()
            for switch in range(len((DPID_list))):
                DPID = DPID_list[switch]
                async with session.get('http://172.17.0.2:8080/stats/flow/' + str(DPID)) as resp:
                    flows = await resp.json()
                async with session.get('http://172.17.0.2:8080/stats/aggregateflow/' + str(DPID)) as resp:
                    flows_stats = await resp.json()
                flow_count = flows_stats[str(DPID)][0]['flow_count']
                clean_data_flow = eval(dumps(flows))
                for flow in range(flow_count):
                    data = clean_data_flow[str(DPID)][flow]
                    if DPID == 1:
                        name = 'analysis_flow'
                        data['switch_name'] = 'switch_1_flow'
                        await parse_array_object(data)
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)
                    elif DPID == 2:
                        name = 'analysis_flow'
                        data['switch_name'] = 'switch_2_flow'
                        await parse_array_object(data)
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)
                    elif DPID == 3:
                        name = 'analysis_flow'
                        data['switch_name'] = 'switch_3_flow'
                        await parse_array_object(data)
                        instance_data = data.copy()
                        data['check_id'] = hash_object_id(instance_data)
                        producer.send(name, value=data)
                    else:
                        print("SWITCH NUMBER ERROR")
        for switches in range(1, 4):
            async with session.get(
                    'http://172.17.0.2:8080/stats/port/' + str(switches)) as resp:
                port_list = await resp.json()
            async with session.get(
                    'http://172.17.0.2:8080/stats/portdesc/' + str(switches)) as resp:
                portdesc = await resp.json()
                switch_portdesc = portdesc[str(switches)]
                switch_port_stats = port_list[str(switches)]
                for port_number in range(len(switch_port_stats)):
                    desc_data_port = switch_portdesc[port_number]
                    instance_data_desc = desc_data_port.copy()
                    stats_data_port = switch_port_stats[port_number]
                    instance_data_stats = stats_data_port.copy()
                    port_data = clean_port_data(instance_data_desc, instance_data_stats)
                    producer.send("analysis_port", value=port_data)


async def go():
    async with aiohttp.ClientSession() as session:
        await fetch(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()