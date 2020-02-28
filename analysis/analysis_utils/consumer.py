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


for message in consumer2:
    mycol2 = mydb["analysis_flow"]
    message = message.value
    mycol2.insert_one(message)



for message in consumer1:
    mycol1 = mydb["analysis_flow"]
    message = message.value
    mycol1.insert_one(message)


for message in consumer3:
    mycol3 = mydb["analysis_flow"]
    message = message.value
    mycol3.insert_one(message)
