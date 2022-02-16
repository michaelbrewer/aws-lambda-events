# S3 Object Lambda

## Input

```json
{
    "xAmzRequestId": "1a5ed718-5f53-471d-b6fe-5cf62d88d02a",
    "getObjectContext": {
        "inputS3Url": "https://myap-123412341234.s3-accesspoint.us-east-1.amazonaws.com/s3.txt?X-Amz-Security-Token=...",
        "outputRoute": "io-iad-cell001",
        "outputToken": "..."
    },
    "configuration": {
        "accessPointArn": "arn:aws:s3-object-lambda:us-east-1:123412341234:accesspoint/myolap",
        "supportingAccessPointArn": "arn:aws:s3:us-east-1:123412341234:accesspoint/myap",
        "payload": "test"
    },
    "userRequest": {
        "url": "/s3.txt",
        "headers": {
            "Host": "myolap-123412341234.s3-object-lambda.us-east-1.amazonaws.com",
            "Accept-Encoding": "identity",
            "X-Amz-Content-SHA256": "e3b0c44297fc1c149afbf4c8995fb92427ae41e4649b934ca495991b7852b855"
        }
    },
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "...",
        "arn": "arn:aws:iam::123412341234:user/myuser",
        "accountId": "123412341234",
        "accessKeyId": "...",
        "userName": "Alice"
    },
    "protocolVersion": "1.00"
}
```

### Getting the correlation id

JSON path to correlation id: `xAmzRequestId`

## Output

```json
{"status_code": 200}
```

## Libraries

- [Python - data class and utilities](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#s3-object-lambda) - Pip `aws-lambda-powertools`

### Examples

Example using AWS Lambda Powertools to upper case the file

```python
import boto3
import requests

from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging.correlation_paths import S3_OBJECT_LAMBDA
from aws_lambda_powertools.utilities.data_classes.s3_object_event import S3ObjectLambdaEvent

logger = Logger()
session = boto3.Session()
s3 = session.client("s3")

@logger.inject_lambda_context(correlation_id_path=S3_OBJECT_LAMBDA, log_event=True)
def lambda_handler(event, context):
    event = S3ObjectLambdaEvent(event)

    # Get object from S3
    response = requests.get(event.input_s3_url)
    original_object = response.content.decode("utf-8")

    # Make changes to the object about to be returned
    transformed_object = original_object.upper()

    # Write object back to S3 Object Lambda
    s3.write_get_object_response(
        Body=transformed_object, RequestRoute=event.request_route, RequestToken=event.request_token
    )

    return {"status_code": 200}
```

## Reference Docs

- [Transforming S3 Objects with S3 Object Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-s3-object-lambda.html)
- [Introducing Amazon S3 Object Lambda – Use Your Code to Process Data as It Is Being Retrieved from S3](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-object-lambda-use-your-code-to-process-data-as-it-is-being-retrieved-from-s3/)
