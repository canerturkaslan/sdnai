from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import datetime

consumer_port = KafkaConsumer(
    'analysis_port',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    consumer_timeout_ms=1000,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
mydb = client["ryu-controller"]


def consume_port():
    for message in consumer_port:
        mycol = mydb["analysis_port"]
        message = message.value
        mac_addr = message['mac_addr']
        created_at = datetime.datetime.utcnow()
        message['created_at'] = created_at
        mycol.update_one({'mac_addr': mac_addr}, {'$set': message}, upsert=True)


consume_port()
