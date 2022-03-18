# Amazon MQ

Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ, invokes the function synchronously

## Request

### ActiveMQ

```json title="AWS MQ message event example"
--8<-- "docs/events/amazon-mq/active-mq.json"
```

### RabbitMQ

```json
--8<-- "docs/events/amazon-mq/rabbit-mq.json"
```

## Response

## Resources

- [Python - Active MQ](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#active-mq) - PIP `aws-lambda-powertools`
- [Python - Rabbit MQ](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#rabbit-mq) - PIP `aws-lambda-powertools`

## Documentation

- [Using Lambda with Amazon MQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html)
- [Using Amazon MQ as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-mq-as-an-event-source-for-aws-lambda/)
