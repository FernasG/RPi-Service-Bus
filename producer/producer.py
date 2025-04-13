import redis, time, os

host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_HOST", "6379")

r = redis.Redis(host=host, port=port, db=0)

while True:
    message = "Hello World!"
    r.publish("test_channel", message)
    print(f"Produced: {message}")
    time.sleep(1)