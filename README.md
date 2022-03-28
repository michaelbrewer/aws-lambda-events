# AWS Lambda Events

Collection of resources and tools on the different input and outputs that AWS Lambda expects.

## Build and testing the docs locally

To run a local server for the docs.

```shell
make dev serve
```

This will install pipenv, mkdocs and run the server, you will need to have Python 3.9+ installed.

## Event Sources

Some of the documented event sources

- [API Gateway Rest API](https://michaelbrewer.github.io/aws-lambda-events/rest-api)
- [API Gateway Rest API Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/rest-api-custom-authorizer/)
- [API Gateway Http API](https://michaelbrewer.github.io/aws-lambda-events/http-api)
- [API Gateway Http API Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/http-api-custom-authorizer/)
- [AppSync Resolvers](https://michaelbrewer.github.io/aws-lambda-events/appsync-resolver/)
- [AppSync Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/appsync-authorizer/)
- [Alexa Smart Home](https://michaelbrewer.github.io/aws-lambda-events/alexa-smart-home)
- [Amazon EventBridge (CloudWatch Events)](https://michaelbrewer.github.io/aws-lambda-events/event-bridge)
- [CloudWatch Logs](https://michaelbrewer.github.io/aws-lambda-events/cloudwatch-logs)
- [CloudFormation](https://michaelbrewer.github.io/aws-lambda-events/cloudformation)
- [CloudFront Lambda@Edge](https://michaelbrewer.github.io/aws-lambda-events/cloudfront-lambda-edge)
- [CodeCommit](https://michaelbrewer.github.io/aws-lambda-events/code-commit)
- [CodePipeline](https://michaelbrewer.github.io/aws-lambda-events/code-pipeline-job)
- [Amazon Cognito User Pool](https://michaelbrewer.github.io/aws-lambda-events/cognito-user-pool)
- [AWS Config](https://michaelbrewer.github.io/aws-lambda-events/config)
- [Amazon Connect](https://michaelbrewer.github.io/aws-lambda-events/connect)
- [Amazon DynamoDB](https://michaelbrewer.github.io/aws-lambda-events/dynamodb)
- [CloudWatch Event - Amazon EC2](https://michaelbrewer.github.io/aws-lambda-events/event-bridge#ec2-instance-state-change-event)
- [Application Load Balancer](https://michaelbrewer.github.io/aws-lambda-events/alb)
- [AWS IoT](https://michaelbrewer.github.io/aws-lambda-events/iot)
- [AWS IoT Events](https://michaelbrewer.github.io/aws-lambda-events/iot-events)
- [Apache Kafka](https://michaelbrewer.github.io/aws-lambda-events/apache-kafka)
- [Amazon Kinesis Data Firehose](https://michaelbrewer.github.io/aws-lambda-events/kinesis-firehose)
- [Amazon Kinesis](https://michaelbrewer.github.io/aws-lambda-events/kinesis-streams)
- [Amazon Lex](https://michaelbrewer.github.io/aws-lambda-events/lex)
- [Amazon Lex V2](https://michaelbrewer.github.io/aws-lambda-events/lex-v2)
- [Amazon MQ](https://michaelbrewer.github.io/aws-lambda-events/mq)
- [Amazon MSK](https://michaelbrewer.github.io/aws-lambda-events/amazon-msk)
- [Amazon S3](https://michaelbrewer.github.io/aws-lambda-events/s3)
- [Amazon S3 batch operations](https://michaelbrewer.github.io/aws-lambda-events/s3-batch)
- [S3 Object Lambda](https://michaelbrewer.github.io/aws-lambda-events/s3-object-lambda)
- [Secrets Manager](https://michaelbrewer.github.io/aws-lambda-events/secrets-manager)
- [Amazon SES](https://michaelbrewer.github.io/aws-lambda-events/ses)
- [Amazon SNS](https://michaelbrewer.github.io/aws-lambda-events/sns)
- [Amazon SQS](https://michaelbrewer.github.io/aws-lambda-events/sqs)
- [Amazon WorkMail](https://michaelbrewer.github.io/aws-lambda-events/work-mail)

## AWS Lambda Publish Sharable Events

[AWS Lambda Publish Sharable Events](./event-schema/README.md) is a tool that allows you to publish events to the AWS Lambda console.

## Objectives

- General docs, invoke types, limits
- Request docs, samples, libraries
- Response docs, samples and libraries
- Handlers and full solutions
- Provide tools to make working with AWS Lambda easier
- Articles, documentations and example repos
