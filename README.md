# Serverless CRUD with Python3

```sh
endpoints:
  POST - https://jya2soi3v9.execute-api.us-east-1.amazonaws.com/task
  GET - https://jya2soi3v9.execute-api.us-east-1.amazonaws.com/task/{id}
  GET - https://jya2soi3v9.execute-api.us-east-1.amazonaws.com/tasks
  PUT - https://jya2soi3v9.execute-api.us-east-1.amazonaws.com/task/{id}
functions:
  create-task: aws-py-crud-dev-create-task (2.8 kB)
  get-task: aws-py-crud-dev-get-task (2.8 kB)
  list-tasks: aws-py-crud-dev-list-tasks (2.8 kB)
  update-task: aws-py-crud-dev-update-task (2.8 kB)
```