# AWS Lambda Event Resources

This site tries to collect as many resources on AWS Lambda events from schema, examples to code libraries.

??? tip - "Objectives of this site"

    Objective is to collect resources on lambda inputs (requests) and outputs (responses) as well as the following:

    - Invocation type (synchronous, asynchronous or polling)
    - Limitations of each type of lambda
    - Input schema
    - Response schema
    - Example events
    - Libraries for typing, data structures, and other utilities
    - Event handlers libraries by language
    - Response handlers by language
    - Documentation and blog posts
    - Code examples

## Lambda Event Sources

Directory of lambda events and resources

- [X] [API Gateway - Http API](./http-api.md) - synchronously invokes
    - [X] [API Gateway - HTTP API - Custom Authorizer](./http-api-custom-authorizer.md) - synchronously invokes
- [x] [API Gateway - Rest API](./rest-api.md) - synchronously invokes
    - [X] [API Gateway - Rest API - Custom Authorizer](./rest-api-custom-authorizer.md) - synchronously invokes
- [X] [Alexa Smart Home](./alexa-smart-home.md) - synchronously invokes
- [X] [AppSync - Resolver](./appsync-resolver.md) - synchronously invokes
    - [X] [AppSync - Custom Authorizer](./appsync-authorizer.md) - synchronously invokes
- [X] [Amazon EventBridge - CloudWatch Event](./event-bridge.md) - asynchronously invokes
    - [X] [CloudWatch Event - Amazon EC2](./event-bridge.md#ec2-instance-state-change-event) - asynchronously invokes
- [X] [CloudWatch Logs](./cloudwatch-logs.md) - asynchronously invokes
- [X] [CloudFormation - Custom Resource](./cloudformation.md) - asynchronously invokes
- [X] [CloudFront - Lambda@Edge](./cloudfront-lambda-edge.md) - synchronously invokes
- [X] [CloudFront - CloudFront Functions](./cloudfront-function.md) - synchronously invokes
- [X] [CodeCommit](./code-commit.md) - asynchronously invokes
- [X] [CodePipeline - Job](./code-pipeline-job.md) - asynchronously invokes
- [X] [Amazon Cognito - User Pool](./cognito-user-pool.md) - synchronously invokes
    - [X] [AWS Cognito - Sync](./cognito-events.md) - synchronously invokes
- [X] [AWS Config](./config.md) - asynchronously invokes
- [X] [Amazon Connect](./connect.md) - synchronously invokes
- [X] [Amazon DynamoDB](./dynamodb.md) - poll-based invokes (synchronously)
- [X] [Application Load Balancer](./alb.md) - synchronously invokes
- [ ] [AWS IoT](./iot.md) - asynchronously invokes
- [ ] [AWS IoT - Events](./iot-events.md) - asynchronously invokes
- [X] [Apache Kafka](./apache-kafka.md) - poll-based invokes (synchronously)
- [X] [Amazon Kinesis - Data Firehose](./kinesis-firehose.md) - poll-based invokes (synchronously)
- [X] [Amazon Kinesis - Streams](./kinesis-streams.md) - poll-based invokes (synchronously)
- [X] [Amazon Lex](./lex.md) - synchronously invokes
- [X] [Amazon Lex V2](./lex-v2.md) - synchronously invokes
- [X] [Amazon MQ](./mq.md) - Active MQ and Rabbit MQ - poll-based invokes (synchronously)
- [X] [Amazon MSK](./amazon-msk.md) - poll-based invokes (synchronously)
- [X] [S3](./s3.md) - asynchronously invokes
    - [X] [S3 - Batch Operations](./s3-batch.md) - synchronously invokes
    - [X] [S3 - Object Lambda](./s3-object-lambda.md) - synchronously invokes
- [X] [Secrets Manager](./secrets-manager.md) - synchronously invokes
- [X] [Amazon SES](./ses.md) - configurable as asynchronously invokes or synchronously invokes
- [X] [Amazon SNS](./sns.md) - asynchronously invokes
- [X] [Amazon SQS](./sqs.md) - asynchronously invokes
- [X] [Amazon WorkMail](./work-mail.md) - asynchronously or synchronously invokes

## Invocation Types

### Synchronous Invokes

Synchronous invocations are the most straight forward way to invoke your Lambda functions. In this model, your functions execute immediately when you perform the Lambda Invoke API call. For testing, when invoking directly use invoke type of `RequestResponse`.

### Asynchronous Invokes

Asynchronous invokes place your invoke request in Lambda service queue and we process the requests as they arrive. For testing, when invoking directly use invoke type of `Event`.

???+ NOTE
    During asynchronous invokes, the lambda context field `clientContext` will not be populated.

### Poll-Based Invokes

AWS will manage the poller on your behalf and perform Synchronous invokes of your function with this type of integration. The retry behavior for this model is based on data expiration in the data source.

- [Understanding the Different Ways to Invoke Lambda Functions](https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/){target="_blank"}
