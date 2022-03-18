# DynamoDB

Amazon DynamoDB stream, Lambda reads records from the stream and invokes your function synchronously with an event that contains stream records. 
Lambda reads records in batches and invokes your function to process records from the batch.

## Request

### Generating sample events

```shell
sam local generate-event dynamodb update
```

### Input Event structure

```json
--8<-- "docs/events/dynamodb/dynamodb.json"
```

## Response

```json title="Response schema"
{ 
  "batchItemFailures": [ 
        {
            "itemIdentifier": "<id>"
        }
    ]
}
```

## Resources

Typing and data classes

- [Python - DynamoDBStreamEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#dynamodb-streams){target="_blank"} - Pip `aws-lambda-powertools`
- [Go - DynamoDBEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_DynamoDB.md){target="_blank"} - Go `github.com/aws/aws-lambda-go/events`
- [Typescript - DynamoDBStreamEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/dynamodb-stream.d.ts){target="_blank"} - NPM `@types/aws-lambda`
- [Java - DynamodbEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/DynamodbEvent.java){target="_blank"} - Java `aws-lambda-java-events`
- [Rust - aws_lambda_events::dynamodb::Event](https://docs.rs/aws_lambda_events/latest/aws_lambda_events/dynamodb/index.html){target="_blank"} - Rust `aws_lambda_events`
- [Ruby - DynamodbEvent](https://rubyonjets.com/docs/events/dynamodb/) - Gem `jets`

Batch handler

- [Python - BatchProcessor](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/#processing-messages-from-dynamodb){target="_blank"} - pip `aws-lambda-powertools`
- [Python - on_dynamodb_record](https://aws.github.io/chalice/topics/events.html#dynamodb-events) - pip `chalice`

### Code Examples

```python title="Example using AWS Lambda Powertool (Python)"
import json

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, batch_processor
from aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event import DynamoDBRecord
from aws_lambda_powertools.utilities.typing import LambdaContext


processor = BatchProcessor(event_type=EventType.DynamoDBStreams)
tracer = Tracer()
logger = Logger()


@tracer.capture_method
def record_handler(record: DynamoDBRecord):
    logger.info(record.dynamodb.new_image)
    payload: dict = json.loads(record.dynamodb.new_image.get("Message").get_value)
    # alternatively:
    # changes: Dict[str, dynamo_db_stream_event.AttributeValue] = record.dynamodb.new_image
    # payload = change.get("Message").raw_event -> {"S": "<payload>"}
    ...

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@batch_processor(record_handler=record_handler, processor=processor)
def lambda_handler(event, context: LambdaContext):
    return processor.response()
```

## Documentation

- [Using AWS Lambda with Amazon DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html)
