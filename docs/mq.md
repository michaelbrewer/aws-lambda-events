# Amazon MQ

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ.

## Input

ActiveMQ

```json
{
   "eventSource": "aws:amq",
   "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",
   "messages": [
      {
         "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
         "messageType": "jms/text-message",
         "data": "QUJDOkFBQUE=",
         "connectionId": "myJMSCoID",
         "redelivered": false,
         "destination": {
            "physicalname": "testQueue"
         },
         "timestamp": 1598827811958,
         "brokerInTime": 1598827811958,
         "brokerOutTime": 1598827811959
      },
      {
         "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
         "messageType": "jms/bytes-message",
         "data": "3DTOOW7crj51prgVLQaGQ82S48k=",
         "connectionId": "myJMSCoID1",
         "persistent": false,
         "destination": {
            "physicalname": "testQueue"
         },
         "timestamp": 1598827811958,
         "brokerInTime": 1598827811958,
         "brokerOutTime": 1598827811959
      }
   ]
}
```

RabbitMQ

```json
{
  "eventSource": "aws:rmq",
  "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:pizzaBroker:b-9bcfa592-423a-4942-879d-eb284b418fc8",
  "rmqMessagesByQueue": {
    "pizzaQueue::/": [
      {
        "basicProperties": {
          "contentType": "text/plain",
          "contentEncoding": null,
          "headers": {
            "header1": {
              "bytes": [
                118,
                97,
                108,
                117,
                101,
                49
              ]
            },
            "header2": {
              "bytes": [
                118,
                97,
                108,
                117,
                101,
                50
              ]
            },
            "numberInHeader": 10
          }
          "deliveryMode": 1,
          "priority": 34,
          "correlationId": null,
          "replyTo": null,
          "expiration": "60000",
          "messageId": null,
          "timestamp": "Jan 1, 1970, 12:33:41 AM",
          "type": null,
          "userId": "AIDACKCEVSQ6C2EXAMPLE",
          "appId": null,
          "clusterId": null,
          "bodySize": 80
        },
        "redelivered": false,
        "data": "eyJ0aW1lb3V0IjowLCJkYXRhIjoiQ1pybWYwR3c4T3Y0YnFMUXhENEUifQ=="
      }
    ]
  }
}
```

## Response

## Libraries

- [Python - Active MQ](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#active-mq)
- [Python - Rabbit MQ](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#rabbit-mq)

## Reference Docs

- [Using Lambda with Amazon MQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html)
- [Using Amazon MQ as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-mq-as-an-event-source-for-aws-lambda/)
