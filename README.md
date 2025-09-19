
# DynamoDB CRUD App using AWS SDK Python

## Description
This is a Python application that performs **Create, Read, Update, and Delete (CRUD)** operations on **AWS DynamoDB**.  
The project uses **Local DynamoDB**, **Java (JDK)** for the local server, and **Python** with the **boto3 SDK**.

## Tech Stack
- **Local DynamoDB**: To simulate DynamoDB on your local machine without AWS costs.
- **Java (JDK 8+)**: Required to run Local DynamoDB.
- **Python 3.x**: Main programming language for CRUD operations.
- **boto3**: AWS SDK for Python.

## Features
- Create tables in DynamoDB
- Add, read, update, and delete items
- Works with local DynamoDB instance

## Prerequisites
1. **Java JDK** installed (8+)
2. **Python 3.x**
3. **boto3 library**: `pip install boto3`
4. **Local DynamoDB** downloaded from AWS:
   - [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

## Setup
1. Run Local DynamoDB:
```bash
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
