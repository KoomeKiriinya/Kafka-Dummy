from kafka import KafkaConsumer
from kafka import KafkaProducer
import json,os

KAFKA_BROKER_URL=os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC=os.environ.get("TRANSACTIONS_TOPIC")
LEGIT_TOPIC=os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC=os.environ.get("FRAUD_TOPIC")

def is_suspicous(transaction):
    """ returns true if transaction is suspicous"""
    return transaction['amount']>= 900
if __name__ == "__main__":
    consumer=KafkaConsumer(TRANSACTIONS_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=json.loads,
    )
    producer=KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer= lambda  value: json.dumps(value).encode()
    )
    for message in consumer:
    #process consumer message
        transaction=message.value
        topic = FRAUD_TOPIC if is_suspicous(transaction) else LEGIT_TOPIC
        producer.send(topic,value=transaction)
        print(topic,transaction)


