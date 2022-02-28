# S3 Object Lambda

With S3 Object Lambda you can add your own code to S3 GET requests to modify and process data as it is returned to an application.
Calls are made synchronously.

## Request

### Fields

`xAmzRequestId` (String)
: The Amazon S3 request ID for this request. We recommend that you log this value to help with debugging.

`protocolVersion` (String)
: The version ID of the context provided.

`getObjectContext` (Map)
: The input and output details for connections to Amazon S3 and S3 Object Lambda.

- `inputS3Url` - String - A pre-signed URL that can be used to fetch the original object from Amazon S3.
The URL is signed using the original caller’s identity, and their permissions
will apply when the URL is used. If there are signed headers in the URL, the
Lambda function must include these in the call to Amazon S3, except for the Host.
- `outputRoute` - String - A routing token that is added to the S3 Object Lambda URL when the Lambda function
calls `WriteGetObjectResponse`.
- `outputToken` - String - An opaque token used by S3 Object Lambda to match the WriteGetObjectResponse call
with the original caller.

`configuration` (Map)
: Configuration information about the S3 Object Lambda access point.

- `accessPointArn` - String - The Amazon Resource Name (ARN) of the S3 Object Lambda access point that received
this request.
- `supportingAccessPointArn` - String - The ARN of the supporting access point that is specified in the S3 Object Lambda
access point configuration.
- `payload` - String - Custom data that is applied to the S3 Object Lambda access point configuration.
S3 Object Lambda treats this as an opaque string, so it might need to be decoded
before use.

`userRequest` (Map)
: Information about the original call to S3 Object Lambda.

- `url` - String - The decoded URL of the request as received by S3 Object Lambda, excluding any
authorization-related query parameters.
- `headers` - Map - A map of string to strings containing the HTTP headers and their values from the original call,
excluding any authorization-related headers.
If the same header appears multiple times, their values are combined into a comma-delimited list.
The case of the original headers is retained in this map.

`userIdentity` (Map)
: Map - Details about the identity that made the call to S3 Object Lambda.

- `type` - Strimg - The source of the temporary security credentials, such as Root, IAMUser, or Role.
- `principalId` - String - The internal ID of the entity that was used to get credentials.
- `arn` - String - The ARN of the principal that made the call. The last section of the ARN contains the user or role that made the call.
- `accountId` - String - The account that owns the entity that granted permissions for the request. If the request was made with temporary security credentials, this is the account that owns the IAM user or role that was used to obtain credentials.
- `accessKeyId` - String - The access key ID that was used to sign the request.
If the request was made with temporary security credentials, this is the access key ID of
the temporary credentials. For security reasons, accessKeyId might not be present, or might
be displayed as an empty string.
- `userName` - String - TThe friendly name of the identity that made the call.
- `sessionContext` - Optional - If the request was made with temporary security credentials, this element provides information about the 
    session that was created for those credentials.
    - `attributes` - Session attributes.
        - `creationDate` - String - The date and time when the temporary security credentials were issued.
        Represented in ISO 8601 basic notation.
        - `mfaAuthenticated` - Boolean - The value is true if the root user or IAM user whose credentials were used for the request also was
        authenticated with an MFA device; otherwise, false
    - `sessionIssuer` - If the request was made with temporary security credentials, an element that provides information
    about how the credentials were obtained.
        - `type` - String - The source of the temporary security credentials, such as Root, IAMUser, or Role.
        - `userName` - String - The friendly name of the user or role that issued the session.
        - `principalId` - String - The internal ID of the entity that was used to get credentials.
        - `arn` - String - The ARN of the source (account, IAM user, or role) that was used to get temporary security credentials.
        - `accountId` - String - The account that owns the entity that was used to get credentials.

### Getting the correlation id

JSON path to correlation id: `xAmzRequestId`

### Examples

```json title="IAM User"
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

```json title="Temp Credentials"
{
    "xAmzRequestId": "requestId",
    "getObjectContext": {
        "inputS3Url": "https://my-s3-ap-111122223333.s3-accesspoint.us-east-1.amazonaws.com/example?X-Amz-Security-Token=<snip>",
        "outputRoute": "io-use1-001",
        "outputToken": "OutputToken"
    },
    "configuration": {
        "accessPointArn": "arn:aws:s3-object-lambda:us-east-1:111122223333:accesspoint/example-object-lambda-ap",
        "supportingAccessPointArn": "arn:aws:s3:us-east-1:111122223333:accesspoint/example-ap",
        "payload": "{}"
    },
    "userRequest": {
        "url": "https://object-lambda-111122223333.s3-object-lambda.us-east-1.amazonaws.com/example",
        "headers": {
            "Host": "object-lambda-111122223333.s3-object-lambda.us-east-1.amazonaws.com",
            "Accept-Encoding": "identity",
            "X-Amz-Content-SHA256": "e3b0c44298fc1example"
        }
    },
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "principalId",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/example",
        "accountId": "111122223333",
        "accessKeyId": "accessKeyId",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "Wed Mar 10 23:41:52 UTC 2021"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "principalId",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            }
        }
    },
    "protocolVersion": "1.00"
}
```

## Response

No specific response is required

```json
{"status_code": 200}
```

## Libraries

- [Python - data class and utilities](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#s3-object-lambda) - Pip `aws-lambda-powertools`
- [Java - S3ObjectLambdaEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/S3ObjectLambdaEvent.java) - Maven `aws-lambda-java-events`

### Code Examples

Example using AWS Lambda Powertools to upper case the file

```python title="app.py"
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

## Documentation

- [Writing and debugging AWS Lambda functions for Amazon S3 Object Lambda Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-writing-lambda.html)
- [Transforming objects with S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html)
- [Introducing Amazon S3 Object Lambda – Use Your Code to Process Data as It Is Being Retrieved from S3](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-object-lambda-use-your-code-to-process-data-as-it-is-being-retrieved-from-s3/)
- [S3 Object Lambda Workshop](https://github.com/aws-samples/s3-object-lambda-workshop)
