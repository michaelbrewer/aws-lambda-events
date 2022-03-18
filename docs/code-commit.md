# Code Commit

Event-driven, asynchronous invocation. CodeCommit repository events in the repository invoke a Lambda function

## Request

### Getting the correlation id

JSON patch `Records[*].eventId`

### Generating sample events

```shell
sam local generate-event codecommit repository
```

### Request example

```json title="AWS CodeCommit message event example"
--8<-- "docs/events/code-commit/code-commit.json"
```

## Response

N/A

## Resources

Typed Lambda handlers by Language

- [Java - CodeCommitEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CodeCommitEvent.java) - Maven `aws-lambda-java-events`
- [Go - CodeCommitEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_CodeCommit.md)
- [Rust - CodeCommitEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/code_commit.rs)

### Code Example

```python title="example prints repo url message to cloudwatch logs"
import json
import boto3

codecommit = boto3.client('codecommit')

def lambda_handler(event, context):
    #Log the updated references from the event
    references = { reference['ref'] for reference in event['Records'][0]['codecommit']['references'] }
    print("References: "  + str(references))
    
    #Get the repository from the event and show its git clone URL
    repository = event['Records'][0]['eventSourceARN'].split(':')[5]
    try:
        response = codecommit.get_repository(repositoryName=repository)
        print("Clone URL: " +response['repositoryMetadata']['cloneUrlHttp'])
        return response['repositoryMetadata']['cloneUrlHttp']
    except Exception as e:
        print(e)
        print('Error getting repository {}. Make sure it exists and that your repository is in the same region as this function.'.format(repository))
        raise e
```

Code examples in Python and NodeJS:

- [AWS Lambda Functions Code Samples for AWS CodeCommit](https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-lambda_functions-codecommit.html)

???+ tip "Tip: Monitoring commits"
    
    See [CodeCommit Repository State Change](./event-bridge.md#codecommit-repository-state-change) for better alternatives to monitoring CodeCommit.

## Documentation

- [Create an AWS CodeCommit trigger for an AWS Lambda function](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-lambda.html)
- [Using AWS Lambda with AWS CodeCommit](https://docs.aws.amazon.com/lambda/latest/dg/services-codecommit.html)
