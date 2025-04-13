# Rasberry Pi Service Bus

This project sets up a containerized environment using **Redis**, **Kafka**, and **RabbitMQ** to support multiple types of message-based communication. It includes a **Python producer** and **Python consumer** that interact via Redis, showcasing a simple request-response pattern.

## 🚀 Features

- 🔧 **Dockerized Setup**: Easily run Redis, Kafka, and RabbitMQ using Docker containers.
- 💬 **Multi-Protocol Messaging**: Supports integration with various message brokers (currently Redis-based implementation is functional).
- 🐍 **Python Clients**:
  - **Producer**: Sends messages via Redis and waits for a response.
  - **Consumer**: Listens for messages on Redis and returns appropriate responses.

## 🧠 Functionality

The Python clients support the following operations:

1. **Send Welcome Message**  
   → The producer sends a welcome message to the consumer and receives a greeting in response.

2. **Write to Document**  
   → Sends a message to write text into a server-side document (e.g., log or text file).

3. **Calculate a Function**  
   → Sends two numbers to the consumer, which performs a predefined calculation (e.g., sum, product, etc.) and returns the result.

## 🐳 Docker Services

| Service     | Description                     |
|-------------|---------------------------------|
| Redis       | Used for message communication  |
| Kafka       | Future support planned          |
| RabbitMQ    | Future support planned          |

## 📁 Project Structure

```bash
.
├── Makefile
├── .env.example
├── docker-compose.yml
├── docker-compose.services.yml
├── producer/
│   └── producer.py
│   └── Dockerfile
│   └── requirements.txt
├── consumer/
│   └── consumer.py
│   └── Dockerfile
│   └── requirements.txt
└── README.md
```

## ⚙️ Usage

### 1. Start Services

```bash
make up
```

### 2. Run Consumer

```bash
make up:consumer
```

### 3. Run Producer

```bash
make up:producer
```

You'll be prompted to choose an operation: welcome message, document write, or calculation.

## ✅ Requirements

- Docker & Docker Compose
- Make

Install dependencies with:

## 📌 Notes

- The Redis implementation is fully functional.
- Kafka and RabbitMQ containers are included for future development/experimentation.
- Make sure the Redis service is fully running before launching the clients.
