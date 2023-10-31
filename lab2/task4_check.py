from pulsar import Client, MessageId
import json

# Pulsar client
client = Client('pulsar://localhost:6650')

# Subscribe to the topic
consumer = client.subscribe('persistent://sample/standalone/ns1/my-topic', 'my-subscription')

# Receive and print messages
while True:
    msg = consumer.receive()
    user = json.loads(msg.data())
    print(user)
    consumer.acknowledge(msg)

# Close the consumer and client to free up resources
consumer.close()
client.close()
