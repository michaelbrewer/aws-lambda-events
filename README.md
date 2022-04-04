# AWS Lambda Events

Collection of resources and tools on the different input and outputs that AWS Lambda expects.

## AWS Lambda Publish Sharable Events

[AWS Lambda Publish Sharable Events](./event-schema/README.md) is a tool that allows you to publish events to the AWS Lambda console.

## Event Sources

Some of the documented event sources

- [API Gateway Rest API](https://lambda.101i.de/rest-api)
- [API Gateway Rest API Custom Authorizer](https://lambda.101i.de/rest-api-custom-authorizer/)
- [API Gateway Http API](https://lambda.101i.de/http-api)
- [API Gateway Http API Custom Authorizer](https://lambda.101i.de/http-api-custom-authorizer/)
- [AppSync Resolvers](https://lambda.101i.de/appsync-resolver/)
- [AppSync Custom Authorizer](https://lambda.101i.de/appsync-authorizer/)
- [Alexa Skills Kit](https://lambda.101i.de/alexa-skills-kit/)
- [Alexa Smart Home](https://lambda.101i.de/alexa-smart-home)
- [Amazon EventBridge (CloudWatch Events)](https://lambda.101i.de/event-bridge)
- [CloudWatch Logs](https://lambda.101i.de/cloudwatch-logs)
- [CloudFormation](https://lambda.101i.de/cloudformation)
- [CloudFront Lambda@Edge](https://lambda.101i.de/cloudfront-lambda-edge)
- [CodeCommit](https://lambda.101i.de/code-commit)
- [CodePipeline](https://lambda.101i.de/code-pipeline-job)
- [Amazon Cognito User Pool](https://lambda.101i.de/cognito-user-pool)
- [AWS Config](https://lambda.101i.de/config)
- [Amazon Connect](https://lambda.101i.de/connect)
- [Amazon DynamoDB](https://lambda.101i.de/dynamodb)
- [CloudWatch Event - Amazon EC2](https://lambda.101i.de/event-bridge#ec2-instance-state-change-event)
- [Application Load Balancer](https://lambda.101i.de/alb)
- [AWS IoT](https://lambda.101i.de/iot)
- [AWS IoT Events](https://lambda.101i.de/iot-events)
- [Apache Kafka](https://lambda.101i.de/apache-kafka)
- [Amazon Kinesis Data Firehose](https://lambda.101i.de/kinesis-firehose)
- [Amazon Kinesis](https://lambda.101i.de/kinesis-streams)
- [Amazon Lex](https://lambda.101i.de/lex)
- [Amazon Lex V2](https://lambda.101i.de/lex-v2)
- [Amazon MQ](https://lambda.101i.de/mq)
- [Amazon MSK](https://lambda.101i.de/amazon-msk)
- [Amazon S3](https://lambda.101i.de/s3)
- [Amazon S3 batch operations](https://lambda.101i.de/s3-batch)
- [S3 Object Lambda](https://lambda.101i.de/s3-object-lambda)
- [Secrets Manager](https://lambda.101i.de/secrets-manager)
- [Amazon SES](https://lambda.101i.de/ses)
- [Amazon SNS](https://lambda.101i.de/sns)
- [Amazon SQS](https://lambda.101i.de/sqs)
- [Amazon WorkMail](https://lambda.101i.de/work-mail)

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
