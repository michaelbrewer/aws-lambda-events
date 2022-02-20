# AWS Lambda Event Resources

Objective is to collect resources on lambda inputs (requests) and outputs (responses) as well as the following:

- Input schema
- Output schema
- Example event inputs
- Libraries for typing, data structures, and other utilities
- Event handlers libraries by language
- Response handlers
- Limitations of each type of lambda
- Documentation
- Code examples

## Directory of AWS Lambda Events

Directory of lambda events and resources

- [x] [API Gateway - Rest API](./api-rest.md)
- [X] [API Gateway - Http API](./api-http-api.md)
    - [X] [API Gateway - Rest API - Custom Authorizer](./api-customer-authorizer-rest.md)
    - [X] [API Gateway - HTTP API - Custom Authorizer](./api-customer-authorizer-http.md)
- [X] [Alexa Smart Home](./alex-smart-home.md)
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
    - [ ] [AWS Cognito - Sync](./cognito-events.md)
- [X] [AWS Config](./config.md)
- [X] [Amazon Connect](./connect.md)
- [ ] [Amazon DynamoDB](./dynamodb.md)
- [X] [Application Load Balancer](./alb.md)
- [ ] [AWS IoT](./iot.md)
- [ ] [AWS IoT - Events](./iot-events.md)
- [ ] [Apache Kafka](./apache-kafka.md)
- [X] [Amazon Kinesis - Data Firehose](./kinesis-firehose.md)
- [X] [Amazon Kinesis - Streams](./kinesis-streams.md)
- [X] [Amazon Lex](./lex.md)
- [X] [Amazon Lex V2](./lex-v2.md)
- [X] [Amazon MQ](./mq.md) - Active MQ and Rabbit MQ
- [X] [Amazon MSK](./amazon-msk.md)
- [ ] [S3](./s3.md)
    - [X] [S3 - Batch Operations](./s3-batch.md)
    - [X] [S3 - Object Lambda](./s3-object-lambda.md)
- [ ] [Secrets Manager](./secrets-manager.md)
- [X] [Amazon SES](./ses.md)
- [X] [Amazon SNS](./sns.md)
- [X] [Amazon SQS](./sqs.md)
- [X] [Amazon WorkMail](./work-mail.md)

## General Resources

List of resources that are used in AWS Lambda

- [AWS Lambda Context](./lambda-context.md) - List of resources on the Lambda Context
- [AWS Lambda Powertools - Python](https://awslabs.github.io/aws-lambda-powertools-python/latest/){target="_blank"}
- [AWS Lambda Powertools - Typescript](https://awslabs.github.io/aws-lambda-powertools-typescript/latest/){target="_blank"}
- [AWS Lambda Powertools - Java](https://awslabs.github.io/aws-lambda-powertools-java/){target="_blank"}
- [Bref - Php](https://bref.sh/){target="_blank"}
