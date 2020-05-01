from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import datetime
consumer_flow = KafkaConsumer(
     'analysis_flow',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     consumer_timeout_ms=1000,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
mydb = client["ryu-controller"]

def consume_flow():
    for message in consumer_flow:
        mycol = mydb["analysis_flow"]
        message = message.value
        check_id = message['check_id']
        created_at = datetime.datetime.utcnow()
        message['created_at'] = created_at
        mycol.update_one({'check_id': check_id}, {'$set': message}, upsert=True)
consume_flow()
