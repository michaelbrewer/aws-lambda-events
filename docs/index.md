# AWS Lambda Event Resources

## Objectives

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

## Directory of AWS Lambda Events

Directory of lambda events and resources

- [X] [API Gateway - Http API](./http-api.md)
    - [X] [API Gateway - HTTP API - Custom Authorizer](./http-api-custom-authorizer.md)
- [x] [API Gateway - Rest API](./rest-api.md)
    - [X] [API Gateway - Rest API - Custom Authorizer](./rest-api-custom-authorizer.md)
- [X] [Alexa Smart Home](./alexa-smart-home.md)
- [X] [AppSync - Resolver](./appsync-resolver.md)
    - [X] [AppSync - Custom Authorizer](./appsync-authorizer.md)
- [X] [Amazon EventBridge - CloudWatch Event](./event-bridge.md)
    - [X] [CloudWatch Event - Amazon EC2](./event-bridge.md#ec2-instance-state-change-event)
- [X] [CloudWatch Logs](./cloudwatch-logs.md)
- [X] [CloudFormation - Custom Resource](./cloudformation.md)
- [X] [CloudFront - Lambda@Edge](./cloudfront-lambda-edge.md)
- [X] [CodeCommit](./code-commit.md)
- [X] [CodePipeline - Job](./code-pipeline-job.md)
- [X] [Amazon Cognito - User Pool](./cognito-user-pool.md)
    - [X] [AWS Cognito - Sync](./cognito-events.md)
- [X] [AWS Config](./config.md)
- [X] [Amazon Connect](./connect.md)
- [X] [Amazon DynamoDB](./dynamodb.md)
- [X] [Application Load Balancer](./alb.md)
- [ ] [AWS IoT](./iot.md)
- [ ] [AWS IoT - Events](./iot-events.md)
- [X] [Apache Kafka](./apache-kafka.md)
- [X] [Amazon Kinesis - Data Firehose](./kinesis-firehose.md)
- [X] [Amazon Kinesis - Streams](./kinesis-streams.md)
- [X] [Amazon Lex](./lex.md)
- [X] [Amazon Lex V2](./lex-v2.md)
- [X] [Amazon MQ](./mq.md) - Active MQ and Rabbit MQ
- [X] [Amazon MSK](./amazon-msk.md)
- [X] [S3](./s3.md)
    - [X] [S3 - Batch Operations](./s3-batch.md)
    - [X] [S3 - Object Lambda](./s3-object-lambda.md)
- [X] [Secrets Manager](./secrets-manager.md)
- [X] [Amazon SES](./ses.md)
- [X] [Amazon SNS](./sns.md)
- [X] [Amazon SQS](./sqs.md)
- [X] [Amazon WorkMail](./work-mail.md)

## General Documentation

### Synchronous Invokes

Synchronous invocations are the most straight forward way to invoke your Lambda functions. In this model, your functions execute immediately when you perform the Lambda Invoke API call.

### Asynchronous Invokes

Asynchronous invokes place your invoke request in Lambda service queue and we process the requests as they arrive. 

### Poll-Based Invokes

AWS will manage the poller on your behalf and perform Synchronous invokes of your function with this type of integration. The retry behavior for this model is based on data expiration in the data source.

- [Understanding the Different Ways to Invoke Lambda Functions](https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/){target="_blank"}
