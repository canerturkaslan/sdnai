from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer3 = KafkaConsumer(
     'switch_3_flow',
auto_offset_reset='earliest',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8')))
consumer1 = KafkaConsumer(
     'switch_1_flow',
auto_offset_reset='earliest',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8')))
consumer2 = KafkaConsumer(
     'switch_2_flow',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8')))


client = MongoClient('localhost:27017')
mydb = client["ryu-controller"]
mesaj_sayisi=0

for message in consumer2:
    mycol2 = mydb["switch_2_flow"]
    message = message.value
    print(message)
    mycol2.insert_one(message)
    print('{} added to {}'.format(message, mycol2))
    mesaj_sayisi+=1

for message in consumer1:
    mycol1 = mydb["switch_1_flow"]
    message = message.value
    print(message)
    mycol1.insert_one(message)
    print('{} added to {}'.format(message, mycol1))

for message in consumer3:
    mycol3 = mydb["switch_3_flow"]
    message = message.value
    print(message)
    mycol3.insert_one(message)
    print('{} added to {}'.format(message, mycol3))