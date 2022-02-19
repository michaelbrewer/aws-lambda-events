# CodePipeline Job

CodePipeline invokes your function asynchronously with an event that contains details about the job.

## Input

!!!WARNING
        TODO: Fields still need to be fully documented

### Example event

```json title="Example CodePipeline event"
{
    "CodePipeline.job": {
        "id": "c0d76431-b0e7-xmpl-97e3-e8ee786eb6f6",
        "accountId": "123456789012",
        "data": {
            "actionConfiguration": {
                "configuration": {
                    "FunctionName": "my-function",
                    "UserParameters": "{\"KEY\": \"VALUE\"}"
                }
            },
            "inputArtifacts": [
                {
                    "name": "my-pipeline-SourceArtifact",
                    "revision": "e0c7xmpl2308ca3071aa7bab414de234ab52eea",
                    "location": {
                        "type": "S3",
                        "s3Location": {
                            "bucketName": "us-west-2-123456789012-my-pipeline",
                            "objectKey": "my-pipeline/test-api-2/TdOSFRV"
                        }
                    }
                }
            ],
            "outputArtifacts": [
                {
                    "name": "invokeOutput",
                    "revision": null,
                    "location": {
                        "type": "S3",
                        "s3Location": {
                            "bucketName": "us-west-2-123456789012-my-pipeline",
                            "objectKey": "my-pipeline/invokeOutp/D0YHsJn"
                        }
                    }
                }
            ],
            "artifactCredentials": {
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "secretAccessKey": "6CGtmAa3lzWtV7a...",
                "sessionToken": "IQoJb3JpZ2luX2VjEA...",
                "expirationTime": 1575493418000
            }
        }
    }
}
```

### Getting the correlation id

JSON path to correlation id: `"CodePipeline.job".id`

### Generating sample events via SAM CLI

```shell
sam local generate-event codepipeline job
```

## Response

N/A

## Libraries

- [Go - codepipeline_job.go](https://github.com/aws/aws-lambda-go/blob/main/events/codepipeline_job.go)
- [Typescript - CodePipelineEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/codepipeline.d.ts) - NPM `@types/aws-lambda`
- [Rust - CodePipelineJobEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/codepipeline_job.rs)

### Code Examples

- [Sample Python function that uses an AWS CloudFormation template](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-samples-python-cloudformation)
- [AWS Lambda Functions Code Samples for AWS CodePipeline - NodeJS and Python](https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-lambda_functions-codepipeline.html)

## Reference Docs

- [Using AWS Lambda with AWS CodePipeline](https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html)
- [Invoke an AWS Lambda function in a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html)
