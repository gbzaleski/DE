from pulsar import Client, MessageId
from faker import Faker
import random
import json

fake = Faker()

# Pulsar client
client = Client('pulsar://localhost:6650')

# Get a producer on the specified topic
# Note it requires script from lab1
producer = client.create_producer('persistent://sample/standalone/ns1/my-topic')

for _ in range(1000):
    user = {"name": fake.name(), "age": random.randint(20, 60), "location": fake.city()}
    producer.send(json.dumps(user).encode('utf-8'))

producer.close()
client.close()