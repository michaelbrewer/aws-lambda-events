# AWS Lambda Events

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

Collection of resources and tools on the different request inputs and response outputs that the event sources for AWS Lambda expect.

## AWS Lambda Publish Sharable Events

[AWS Lambda Publish Sharable Events](./event-schema/README.md) is a tool that allows you to publish events to the AWS Lambda console.

## AWS Lambda Quick Start Tool

- [Build Project](https://michaelbrewer.github.io/aws-lambda-events/build-project/) - A web based tool to quickly build a new AWS Lambda project. Either via [AWS SAM CLI Application Templates](https://github.com/aws/aws-sam-cli-app-templates) or a [Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/) generator using [Quick start for AWS Lambda](https://github.com/michaelbrewer/aws-lambda-quickstart)

## Event Sources Docs

Some documented event sources are as follows:

- [API Gateway Rest API](https://michaelbrewer.github.io/aws-lambda-events/rest-api)
- [API Gateway Rest API Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/rest-api-custom-authorizer/)
- [API Gateway Http API](https://michaelbrewer.github.io/aws-lambda-events/http-api)
- [API Gateway Http API Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/http-api-custom-authorizer/)
- [AWS Lambda Function URLs](https://michaelbrewer.github.io/aws-lambda-events/function-url/)
- [AppSync Resolvers](https://michaelbrewer.github.io/aws-lambda-events/appsync-resolver/)
- [AppSync Custom Authorizer](https://michaelbrewer.github.io/aws-lambda-events/appsync-authorizer/)
- [Alexa Skills Kit](https://michaelbrewer.github.io/aws-lambda-events/alexa-skills-kit/)
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

## Build and testing the documentation site

To run a local server for the docs.

```bash
make dev serve
```

This will install pipenv, mkdocs and run the server, you will need to have Python 3.9+ installed.

## Objectives

- General docs, invoke types, limits
- Request docs, samples, libraries
- Response docs, samples and libraries
- Document handlers and full solutions
- Share or provide tools to make working with AWS Lambda easier
- Articles, documentations and example repos
