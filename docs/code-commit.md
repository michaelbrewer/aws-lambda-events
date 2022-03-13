# Code Commit

Event-driven, asynchronous invocation. CodeCommit repository events in the repository invoke a Lambda function

## Request

### Getting the correlation id

JSON patch `Records[*].eventId`

### Generating sample events

```shell
sam local generate-event codecommit repository
```

### AWS CodeCommit message event example

```json title="AWS CodeCommit message event example"
{
    "Records": [
        {
            "awsRegion": "us-east-2",
            "codecommit": {
                "references": [
                    {
                        "commit": "5e493c6f3067653f3d04eca608b4901eb227078",
                        "ref": "refs/heads/master"
                    }
                ]
            },
            "eventId": "31ade2c7-f889-47c5-a937-1cf99e2790e9",
            "eventName": "ReferenceChanges",
            "eventPartNumber": 1,
            "eventSource": "aws:codecommit",
            "eventSourceARN": "arn:aws:codecommit:us-east-2:123456789012:lambda-pipeline-repo",
            "eventTime": "2019-03-12T20:58:25.400+0000",
            "eventTotalParts": 1,
            "eventTriggerConfigId": "0d17d6a4-efeb-46f3-b3ab-a63741badeb8",
            "eventTriggerName": "index.handler",
            "eventVersion": "1.0",
            "userIdentityARN": "arn:aws:iam::123456789012:user/intern"
        }
    ]
}
```

## Response

N/A

## Resources

Typed Lambda handlers by Language

- [Java - CodeCommitEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CodeCommitEvent.java) - Maven `aws-lambda-java-events`
- [Go - CodeCommitEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_CodeCommit.md)
- [Rust - CodeCommitEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/code_commit.rs)

## Documentation

- [Create an AWS CodeCommit trigger for an AWS Lambda function](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-lambda.html)
- [Using AWS Lambda with AWS CodeCommit](https://docs.aws.amazon.com/lambda/latest/dg/services-codecommit.html)
