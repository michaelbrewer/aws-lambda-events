# Kinesis Data Streams

Lambda reads records from the data stream and invokes your function synchronously with an event that contains stream records.

Amazon Kinesis Data Streams is a fully managed streaming data service. You can continuously add various types of data such as clickstreams, application logs, and social media to a Kinesis stream from hundreds of thousands of sources.

??? TIP "TIP: Kinesis streams vs firehose"
    Read [AWS Kinesis Data Streams vs Kinesis Data Firehose](https://jayendrapatil.com/aws-kinesis-data-streams-vs-kinesis-firehose/) for when to use Kinesis streams vs Kinesis Data Firehose.

## Request

### Request fields

`Records` - An array of records.

`awsRegion` (String)
: AWS region where the event originated eg: us-east-1

`eventID` (String)
: A globally unique identifier for the event that was recorded in this stream record.

`eventName` (String)
: Event type eg: aws:kinesis:record

`eventSource` (String)
: The AWS service from which the Kinesis event originated. For Kinesis, this is aws:kinesis

`eventSourceARN` (String)
: The Amazon Resource Name (ARN) of the event source

`eventVersion` (String)
: The eventVersion key value contains a major and minor version in the form <major>.<minor>.

`invokeIdentityArn` (String)
: The ARN for the identity used to invoke the Lambda Function

`kinesis` (Object)
: Kinesis payload

- `approximateArrivalTimestamp` (Number) - The approximate time that the record was inserted into the stream
- `data` (String) - The data contained in the record
- `kinesisSchemaVersion` (String) - The version of the Kinesis data record format
- `partitionKey` (String) - The partition key of the record
- `sequenceNumber` (String) - The sequence number of the record

### Request Example

```json
--8<-- "docs/events/kinesis-streams/kinesis-streams.json"
```

## Response

```json title="Reporting batch item failures"
{
   "batchItemFailures":[
      {
         "itemIdentifier":"<id>"
      }
   ]
}
```

## Resources

Typing by language

- [PHP - KinesisEvent](https://bref.sh/docs/function/handlers.html#kinesis-events) - Composer `bref/bref`
- [Python - KinesisEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#kinesis-streams) - Pip `aws-lambda-powertools`
- [Rust - KinesisEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/kinesis.rs) - Cargo `aws-lambda-events`
- [Java - KinesisEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/KinesisEvent.java) - Maven `aws-lambda-java-events`
- [Typescript - KinesisEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/kinesis-stream.d.ts) - NPM `@types/aws-lambda`
- [Go - KinesisEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_Kinesis.md) - `github.com/aws/aws-lambda-go/events`

Handlers by language

- [Python - BatchProcessor](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/#processing-messages-from-kinesis) - Pip `aws-lambda-powertools`
- [Ruby - kinesis_event](https://rubyonjets.com/docs/events/kinesis/) - GEM `jets`
- [Python - on_kinesis_record](https://aws.github.io/chalice/topics/events.html#kinesis-events) - Pip `chalice`

### Code Examples

```python title="Batch Processing via AWS Lambda Powertools"
import json

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, batch_processor
from aws_lambda_powertools.utilities.data_classes.kinesis_stream_event import KinesisStreamRecord
from aws_lambda_powertools.utilities.typing import LambdaContext


processor = BatchProcessor(event_type=EventType.KinesisDataStreams)
tracer = Tracer()
logger = Logger()


@tracer.capture_method
def record_handler(record: KinesisStreamRecord):
    logger.info(record.kinesis.data_as_text)
    payload: dict = record.kinesis.data_as_json()
    ...

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@batch_processor(record_handler=record_handler, processor=processor)
def lambda_handler(event, context: LambdaContext):
    return processor.response()
```

## Documentation

- [Using AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html)
