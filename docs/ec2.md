# EC2

EventBridge (CloudWatch Events) invokes your Lambda function asynchronously with the event document from Amazon EC2.

Amazon EC2

## Input

### Generating sample events via SAM CLI

```shell
sam local generate-event dynamodb update
```

## Input Event structure

```json title="EC2 Instance State-change Notification"
{
    "version": "0",
    "id": "b6ba298a-7732-2226-xmpl-976312c1a050",
    "detail-type": "EC2 Instance State-change Notification",
    "source": "aws.ec2",
    "account": "123456798012",
    "time": "2019-10-02T17:59:30Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ec2:us-east-2:123456798012:instance/i-0c314xmplcd5b8173"
    ],
    "detail": {
        "instance-id": "i-0c314xmplcd5b8173",
        "state": "running"
    }
}
```

## Output

## Libraries

## Reference Docs

- [Using AWS Lambda with Amazon EC2](https://docs.aws.amazon.com/lambda/latest/dg/services-ec2.html)
