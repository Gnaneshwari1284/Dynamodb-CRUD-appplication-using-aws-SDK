"""
DynamoDB CRUD Application using Python and Local DynamoDB
Author: J. Gnaneshwari
Date: 2025-09-20

This script demonstrates basic CRUD operations:
- Create table (if not exists)
- Add items
- Read items
- Update items
- Delete items
"""

import boto3
from botocore.exceptions import ClientError

# -----------------------------
# Connect to Local DynamoDB
# -----------------------------
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-west-2',
    endpoint_url='http://localhost:8000'  # Local DynamoDB URL
)

TABLE_NAME = "Students"


# -----------------------------
# Function to create a table
# -----------------------------
def create_table():
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {'AttributeName': 'student_id', 'KeyType': 'HASH'}  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'student_id', 'AttributeType': 'N'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print(f"Table '{TABLE_NAME}' created successfully!")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table '{TABLE_NAME}' already exists.")
        else:
            print("Error creating table:", e)


# -----------------------------
# Function to add an item
# -----------------------------
def add_student(student_id, name, age):
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'student_id': student_id,
            'name': name,
            'age': age
        }
    )
    print(f"Added student: {student_id}, {name}, {age}")


# -----------------------------
# Function to read an item
# -----------------------------
def get_student(student_id):
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'student_id': student_id})
    item = response.get('Item')
    if item:
        print("Student Found:", item)
    else:
        print(f"No student found with ID {student_id}")


# -----------------------------
# Function to update an item
# -----------------------------
def update_student_age(student_id, new_age):
    table = dynamodb.Table(TABLE_NAME)
    table.update_item(
        Key={'student_id': student_id},
        UpdateExpression="set age = :a",
        ExpressionAttributeValues={':a': new_age}
    )
    print(f"Updated student {student_id} age to {new_age}")


# -----------------------------
# Function to delete an item
# -----------------------------
def delete_student(student_id):
    table = dynamodb.Table(TABLE_NAME)
    table.delete_item(Key={'student_id': student_id})
    print(f"Deleted student with ID {student_id}")


# -----------------------------
# Main program with examples
# -----------------------------
if __name__ == "__main__":
    # 1. Create the table
    create_table()

    # 2. Add example students
    add_student(1, "Alice", 20)
    add_student(2, "Bob", 22)
    add_student(3, "Charlie", 19)
    add_student(4, "David", 21)

    # 3. Read student data
    get_student(2)  # Bob

    # 4. Update student data
    update_student_age(3, 20)  # Charlie's age changed

    # 5. Delete a student
    delete_student(4)  # Delete David

    # 6. Try reading deleted student
    get_student(4)
