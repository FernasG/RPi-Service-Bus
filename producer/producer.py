import redis, os, uuid, json

host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT", "6379")

r = redis.Redis(host=host, port=port, db=0)

def show_menu():
    print("=" * 30)
    print("Escolha uma das opções abaixo:")
    print("1 - Mensagem de texto")
    print("2 - Atualizar documento txt")
    print("3 - Calcular função")
    print("0 - Sair")
    print("=" * 30)

def wait_response(channel: str):
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    response = {}

    for message in pubsub.listen():
        if message["type"] != "message":
            continue

        response = json.loads(message["data"])
        pubsub.unsubscribe(channel)

        break
    
    return response

def text_message():
    name = input("Digite seu nome: ")
    request_id = str(uuid.uuid4())

    request = {"id":  request_id, "body": {"name": name}}

    r.publish("text_message", json.dumps(request))
    
    response = wait_response(request_id)
    print(response["message"])

def update_document():
    content = input("Digite o conteudo do documento: ")
    request_id = str(uuid.uuid4())

    request = {"id":  request_id, "body": {"content": content}}

    r.publish("update_document", json.dumps(request))

    response = wait_response(request_id)
    print(response["message"])

def calc_function():
    allowed_methods = ["sum", "sub", "mul", "div"]
    method = input("Digite o metodo desejada (sum, sub, mul, div): ")

    if method not in allowed_methods:
        print("Metodo inválido")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    body = {"method": method, "num1": num1, "num2": num2}
    request_id = str(uuid.uuid4())

    request = {"id":  request_id, "body": body}

    r.publish("calc_function", json.dumps(request))

    response = wait_response(request_id)
    print(response["message"])

if __name__ == "__main__":
    while True:
        show_menu()
        option = int(input("Digite a opção desejada: "))

        if option == 0:
            break

        if option == 1:
            text_message()
        
        if option == 2:
            update_document()
        
        if option == 3:
            calc_function()
