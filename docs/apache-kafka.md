# Apache Kafka

Lambda internally polls for new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the messages in batches and provides these to your function as an event payload. The maximum batch size is configurable. (The default is 100 messages.)

## Request

!!! NOTE
      Shares the same structure as [Amazon MSK](./amazon-msk.md), except for the eventSource field is set to "aws:SelfManagedKafka".

```json title="Self managed kafka example"
--8<-- "docs/events/apache-kafka/apache-kafka.json"
```

## Response

## Resources

- [Go - KafkaEvent](https://github.com/aws/aws-lambda-go/blob/main/events/kafka.go)
- [Java - KafkaEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/KafkaEvent.java)

## Documentation

- [Using Lambda with self-managed Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)
- [Using self-hosted Apache Kafka as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/)
