# Todo Application

This is a simple Todo project implemented in Python. It allows you to create, update, delete, and read a list of tasks. The project uses PostgreSQL as the database, Kafka as the message broker, and gRPC for communication between services. Additionally, SQLAlchemy is used for interacting with the database. Webhook is used to publish events.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Webhook Integration](#webhook-integration)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker (for running the project using docker-compose)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:malikfaiq/gRPCBoilterPlate.git
   cd gRPCBoilterPlate

### Project Structure
```bash
├── business_logic
│   ├── models.py
│   └── todo_manager.py
├── database
│   ├── db_connector.py
│   └── models.py
├── gRPC
│   ├── grpc_client.py
│   ├── grpc_server.py
│   ├── todo.proto
│   ├── todo_pb2.py
│   └── todo_pb2_grpc.py
├── message_broker
│   └── kafka_producer.py
├── webhook
│   └── webhook_publisher.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── dockerFile.
├── requirements.txt
├── .configurations.py
└── README.md
```

- business_logic: Contains the business logic of the application, including the TodoManager and models.
- gRPC: Contains all the fiels related to google remote procedure calls.
- database: Contains all the information regarding database connections and models.
- message_broker: Contains kafka producer configuration and usage.
- main.py: Main application file with gRPC service implementation.
- Dockerfile: Configuration file for building a Docker image.
- docker-compose.yml: Configuration file for running the project using Docker Compose.


### Usage

To run the project using Docker Compose, follow these steps:

1. Build the Docker image:
    ```bash
    Build the Docker image:
    ```
2. Start the services:
    ```bash 
    docker-compose up 
    ```
3. There is been a already client written which will utilize and return the response from gRPC to utilize that run:

    ```bash
    python -m gRPC.grpc_client
    ```
4. For event logs of webhook_publisher and web application use following commands:
    ```bash
    docker-compose logs web webhook_publisher
    ```


### Environment Variables:

The application uses environment variables for configuration. You can set these in the .env file.

* POSTGRES_CONNECTION_STRING: PostgreSQL connection string (e.g., postgresql://username:password@localhost:5432/todo_db).
* KAFKA_BROKER: Kafka broker address (e.g., kafka:9092).
* WEBHOOK_URL: URL for webhook integration (e.g., http://webhook_listener:5000/webhook).



### Webhook Integration
The application supports webhook integration. When a todo is created or updated, its details are published to the webhook URL provided in the environment variables.