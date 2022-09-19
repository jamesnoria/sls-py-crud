import json
import os
import boto3
import uuid

DYNAMODB = boto3.resource('dynamodb')
TABLE = DYNAMODB.Table(os.environ['DYNAMODB_TABLE'])


def create_task(event, context):
    """Create a new task."""

    # parse the request body
    data = json.loads(event['body'])

    # create a new task
    task = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data['description'],
        'done': False,
    }

    # write the task to the database
    TABLE.put_item(Item=task)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(task)
    }

    return response


def get_task(event, context):
    """Get a task by ID."""

    # fetch task from the database
    result = TABLE.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response


def list_tasks(event, context):
    """List all tasks."""

    # fetch all tasks from the database
    result = TABLE.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response


def update_task(event, context):
    """Update a task by ID."""

    # parse the request body
    data = json.loads(event['body'])

    # update the task in the database
    result = TABLE.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
            '#task_title': 'title',
        },
        ExpressionAttributeValues={
            ':title': data['title'],
            ':description': data['description'],
            ':done': data['done'],
        },
        UpdateExpression='SET #task_title = :title, description = :description, done = :done',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response
