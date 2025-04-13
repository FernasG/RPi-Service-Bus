import redis, os, json

host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT", "6379")

r = redis.Redis(host=host, port=port, db=0)

def text_message(payload: dict):
    request_id = payload["id"]
    body = payload["body"]

    message = f"Olá {body["name"].capitalize()}, como você está?"
    response = {"message": message}

    r.publish(request_id, json.dumps(response))

def update_document(payload: dict):
    request_id = payload["id"]
    body = payload["body"]

    with open("file.txt", "a") as file:
        file.write(f"{body["content"]}\n")

    response = {"message": "Arquivo alterado com sucesso"}

    r.publish(request_id, json.dumps(response))

def calc_function(payload: dict):
    request_id = payload["id"]
    body = payload["body"]
    message = ""
    
    num1 = body["num1"]
    num2 = body["num2"]

    if body["method"] == "sum":
        result = num1 + num2
        message = f"{num1} + {num2} = {result:.2f}"

    if body["method"] == "sub":
        result = num1 - num2
        message = f"{num1} - {num2} = {result:.2f}"

    if body["method"] == "mul":
        result = num1 * num2
        message = f"{num1} * {num2} = {result:.2f}"

    if body["method"] == "div":
        result = num1 / num2
        message = f"{num1} / {num2} = {result:.2f}"

    response = {"message": message}

    r.publish(request_id, json.dumps(response))

while True:
    pubsub = r.pubsub()
    pubsub.subscribe("text_message", "update_document", "calc_function")
    print("Consumer is waiting for messages...")

    for message in pubsub.listen():
        if message["type"] != "message":
            continue

        payload = json.loads(message["data"])
        channel = message["channel"].decode("utf-8")

        print(f"Message Receveid\nChannel: {channel}\nPayload: {payload}")

        if channel == "text_message":
            text_message(payload)
            
        if channel == "update_document":
            update_document(payload)

        if channel == "calc_function":
            calc_function(payload)