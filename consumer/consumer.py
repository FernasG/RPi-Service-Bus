import redis, os

host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_HOST", "6379")

r = redis.Redis(host=host, port=port, db=0)

while True:
    pubsub = r.pubsub()
    pubsub.subscribe("test_channel")
    print("Consumer is waiting for messages...")

    for message in pubsub.listen():
        if message["type"] != "message": continue
            
        print(f"Consumed: {message["data"].decode("utf-8")}")