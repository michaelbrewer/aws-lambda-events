# SQS

Lambda polls the queue and invokes your Lambda function synchronously with an event that contains queue messages. By default, Lambda polls up to 10 messages in your queue at once and sends that batch to your function. 

## Input

### Input fields

`Records` - An array of records.

`messageId` (String)
: A unique identifier for the message. A messageId is considered unique across all AWS accounts 
for an extended period of time.

`receiptHandle` (String)
: An identifier associated with the act of receiving the message.
  A new receipt handle is returned every time you receive a message. When deleting a message,
  you provide the last received receipt handle to delete the message.

`body` (String)
: The message's contents (not URL-encoded).

`attributes` (Object)
: A map of the attributes requested in ReceiveMessage to their respective values.

- `AWSTraceHeader` (Optional, String) - Returns the AWS X-Ray trace header string.
- `ApproximateReceiveCount` (String) - Returns the number of times a message has been received across all queues but not deleted.
- `SentTimestamp` (String) - Returns the time the message was sent to the queue (epoch time in milliseconds).
- `SenderId` (String) - For an IAM user, returns the IAM user ID, For an IAM role, returns the IAM role ID
- `ApproximateFirstReceiveTimestamp` (String) - Returns the time the message was first received from the queue (epoch time in milliseconds).
- `SequenceNumber` (Optional, String) - The large, non-consecutive number that Amazon SQS assigns to each message.
- `MessageGroupId` (Optional, String) - The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are always processed one by one, in a strict order relative to the message group (however, messages that belong to different message groups might be processed out of order).
- `MessageDeduplicationId` (Optional, String) - The token used for deduplication of sent messages. If a message with a particular message deduplication ID is sent successfully, any messages sent with the same message deduplication ID are accepted successfully but aren't delivered during the 5-minute deduplication interval.

`messageAttributes` (Object)
: Each message attribute consists of a Name, Type, and Value.

`md5OfBody` (String)
: An MD5 digest of the non-URL-encoded message body string.

`eventSource` (String)
: The AWS service from which the SQS record originated. For SQS, this is `aws:sqs`

`eventSourceARN` (String)
: The Amazon Resource Name (ARN) of the event sourc

`awsRegion` (String)
: aws region eg: us-east-1

### Generating sample events via SAM CLI

```shell
sam local generate-event sqs receive-message
```

### Example event

```json title="Example Amazon SQS message event (standard queue)"
{
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185"
            },
            "messageAttributes": {},
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2"
        },
        {
            "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
            "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082650636",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082650649"
            },
            "messageAttributes": {},
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2"
        }
    ]
}
```

```json title="Example Amazon SQS message event (FIFO queue)"
{
    "Records": [
        {
            "messageId": "11d6ee51-4cc7-4302-9e22-7cd8afdaadf5",
            "receiptHandle": "AQEBBX8nesZEXmkhsmZeyIE8iQAMig7qw...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1573251510774",
                "SequenceNumber": "18849496460467696128",
                "MessageGroupId": "1",
                "SenderId": "AIDAIO23YVJENQZJOL4VO",
                "MessageDeduplicationId": "1",
                "ApproximateFirstReceiveTimestamp": "1573251510774"
            },
            "messageAttributes": {},
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:fifo.fifo",
            "awsRegion": "us-east-2"
        }
    ]
}
```

## Response

Success and failure conditions

Lambda treats a batch as a complete success if your function returns any of the following:

- An empty `batchItemFailures` list
- A null `batchItemFailures` list
- An empty EventResponse
- A `null` EventResponse

Lambda treats a batch as a complete failure if your function returns any of the following:

- An invalid JSON response
- An empty string `itemIdentifier`
- A null `itemIdentifier`
- An `itemIdentifier` with a bad key name
- An `itemIdentifier` value with a message ID that doesn't exist

```json title="Example of partial failures"
{
    "batchItemFailures": [
        {
            "itemIdentifier": "244fc6b4-87a3-44ab-83d2-361172410c3a"
        }
    ]
}
```

## Libraries

Typings in different languages

- [SQSEvent - Python](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#sqs) - PIP `aws-lambda-powertools`
- [SQSEvent - Go](https://github.com/aws/aws-lambda-go/blob/main/events/README_SQS.md) - Go `github.com/aws/aws-lambda-go/events`
- [SqsEvent - Php](https://bref.sh/docs/function/handlers.html#sqs-events) - Composer `bref/bref`
- [SQSEvent - Java](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/SQSEvent.java)
- [SQSEvent - DotNet](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.SQSEvents)
- [SQSEvent - Typescript](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/sqs.d.ts)

Full event handler

- [SQS Batch Handler - Python](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/) - PIP `aws-lambda-powertools`
- [SQS Events - Ruby](https://rubyonjets.com/docs/events/sqs/) - GEM `jets`
- [on_sqs_message - Python](https://aws.github.io/chalice/topics/events.html#sqs-events) - PIP `chalice`

### Code Examples

```python title="Example S3 batch handler using AWS Lambda Powertools (Python)"
import json

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, batch_processor
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord
from aws_lambda_powertools.utilities.typing import LambdaContext

processor = BatchProcessor(event_type=EventType.SQS)
tracer = Tracer()
logger = Logger()

@tracer.capture_method
def record_handler(record: SQSRecord):
    payload: str = record.body
    if payload:
        item: dict = json.loads(payload)
    ...

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@batch_processor(record_handler=record_handler, processor=processor)
def lambda_handler(event, context: LambdaContext):
    return processor.response()
```

## Reference Docs

- [Using Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
- [Tutorial: Using Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-example.html)
