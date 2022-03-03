# CloudWatch Log

CloudWatch Logs invokes your function asynchronously with an event that contains log data.

## Request

### Cloudwatch log structure

`data` (String)
: The value of the `data` field is a Base64 encoded ZIP archive.

```json title="CloudWatch Logs message event example"
{
  "awslogs": {
    "data": "H4sIAAAAAAAAAHWPwQqCQBCGX0Xm7EFtK+smZBEUgXoLCdMhFtKV3akI8d0bLYmibvPPN3wz00CJxmQnTO41whwWQRIctmEcB6sQbFC3CjW3XW8kxpOpP+OC22d1Wml1qZkQGtoMsScxaczKN3plG8zlaHIta5KqWsozoTYw3/djzwhpLwivWFGHGpAFe7DL68JlBUk+l7KSN7tCOEJ4M3/qOI49vMHj+zCKdlFqLaU2ZHV2a4Ct/an0/ivdX8oYc1UVX860fQDQiMdxRQEAAA=="
  }
}
```

CloudWatch Logs message data (decoded) example

```json title="CloudWatch Logs message data (decoded) example"
{
    "messageType": "DATA_MESSAGE",
    "owner": "123456789012",
    "logGroup": "/aws/lambda/echo-nodejs",
    "logStream": "2019/03/13/[$LATEST]94fa867e5374431291a7fc14e2f56ae7",
    "subscriptionFilters": [
        "LambdaStream_cloudwatchlogs-node"
    ],
    "logEvents": [
        {
            "id": "34622316099697884706540976068822859012661220141643892546",
            "timestamp": 1552518348220,
            "message": "REPORT RequestId: 6234bffe-149a-b642-81ff-2e8e376d8aff\tDuration: 46.84 ms\tBilled Duration: 47 ms \tMemory Size: 192 MB\tMax Memory Used: 72 MB\t\n"
        }
    ]
}
```

### Generating sample events

```shell
sam local generate-event cloudwatch logs
```

## Response

N/A

## Resources

- [Python - CloudWatchLogsEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#cloudwatch-logs) - Pip `aws-lambda-powertools`
- [Typescript - CloudWatchLogsEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/cloudwatch-logs.d.ts) - NPM `@types/aws-lambda`
- [DotNet - CloudWatchLogsEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.CloudWatchLogsEvents) - Nuget `Amazon.Lambda.CloudWatchLogsEvents`
- [Java - CloudWatchLogsEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CloudWatchLogsEvent.java) - Maven `aws-lambda-java-events`
- [Rust - CloudwatchLogsEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/cloudwatch_logs.rs) - Cargo `aws-lambda-events`
- [Ruby - LogJob](https://rubyonjets.com/docs/events/cloudwatch-log/) - gem `jets`

### Code Example

Python code example using the data class to decode the log data payload

```python title="app.py"
from aws_lambda_powertools.utilities.data_classes import event_source, CloudWatchLogsEvent
from aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event import CloudWatchLogsDecodedData

@event_source(data_class=CloudWatchLogsEvent)
def lambda_handler(event: CloudWatchLogsEvent, context):
    decompressed_log: CloudWatchLogsDecodedData = event.parse_logs_data
    log_events = decompressed_log.log_events
    for log_event in log_events:
        do_something_with(log_event.timestamp, log_event.message)
```

- [NodeJS code example](https://github.com/awsdocs/aws-lambda-developer-guide/blob/main/sample-apps/error-processor/processor/index.js)

## Documentation

- [Using Lambda with CloudWatch Logs](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchlogs.html)
- [Error processor sample application for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/samples-errorprocessor.html)
