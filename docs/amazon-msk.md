# Amazon MSK

Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that you can use to build and run applications that use Apache Kafka to
process streaming data.

Lambda internally polls for new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the messages in 
batches and provides these to your function as an event payload.

## Limits

- The maximum batch size is configurable. (The default is 100 messages.)
- Lambda can run your function for up to 14 minutes.

## Request

!!! Note
      Shares the same structure as [Self managed Apache Kafka](./apache-kafka.md), except for the eventSource field is set to "aws:msk".

```json title="Managed Kafka"
--8<-- "docs/events/amazon-msk/amazon-msk-1.json"
```

```json title="Another managed Kafka example"
--8<-- "docs/events/amazon-msk/amazon-msk-2.json"
```

## Response

## Resources

Typed Lambda handlers by Language

- [Typescript - MSKEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/msk.d.ts) - NPM `@types/aws-lambda`

### Code examples

- [Amazon MSK AWS Lambda Integration Lab - Code](https://github.com/aws-samples/integration-sample-lambda-msk)

## Documentation

- [Using Lambda with Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
- [Using Amazon MSK as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-msk-as-an-event-source-for-aws-lambda/)
