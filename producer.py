from confluent_kafka import Producer
import socket

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

topic = 'test-topic'
for i in range(10):
    message = f"Message {i}"
    producer.produce(topic, value=message, callback=acked)
    producer.poll(1)

producer.flush()