# AWS Lambda Event Resources

This site tries to collect as many resources on AWS Lambda events from schema, examples to code libraries.

??? tip - "Objectives of this site"

    Objective is to collect resources on Lambda inputs (requests) and outputs (responses) as well as the following:

    - Invocation type (synchronous, asynchronous or polling)
    - Limitations of each type of Lambda
    - Input schema
    - Response schema
    - Example events
    - Libraries for typing, data structures, and other utilities
    - Event handlers libraries by language
    - Response handlers by language
    - Documentation and blog posts
    - Code examples

## Lambda Event Sources

Directory of AWS Lambda events sources and resources

- [API Gateway - Http API](./http-api.md) - synchronously invokes
- [API Gateway - HTTP API - Custom Authorizer](./http-api-custom-authorizer.md) - synchronously invokes
- [API Gateway - Rest API](./rest-api.md) - synchronously invokes
- [API Gateway - Rest API - Custom Authorizer](./rest-api-custom-authorizer.md) - synchronously invokes
- [AWS Lambda Function URLs](./function-url.md) - synchronously invokes
- [Alexa Skills](./alexa-skills-kit.md) - synchronously invokes
- [Alexa Smart Home](./alexa-smart-home.md) - synchronously invokes
- [AppSync - Resolver](./appsync-resolver.md) - synchronously invokes
- [AppSync - Custom Authorizer](./appsync-authorizer.md) - synchronously invokes
- [Amazon EventBridge - CloudWatch Event](./event-bridge.md) - asynchronously invokes
- [CloudWatch Logs](./cloudwatch-logs.md) - asynchronously invokes
- [CloudFormation - Custom Resource](./cloudformation.md) - asynchronously invokes
- [CloudFront - Lambda@Edge](./cloudfront-lambda-edge.md) - synchronously invokes
- [CloudFront - CloudFront Functions](./cloudfront-function.md) - synchronously invokes
- [CodeCommit](./code-commit.md) - asynchronously invokes
- [CodePipeline - Job](./code-pipeline-job.md) - asynchronously invokes
- [Amazon Cognito - User Pool](./cognito-user-pool.md) - synchronously invokes
- [AWS Cognito - Sync](./cognito-events.md) - synchronously invokes
- [AWS Config](./config.md) - asynchronously invokes
- [Amazon Connect](./connect.md) - synchronously invokes
- [Amazon DynamoDB](./dynamodb.md) - poll-based invokes (synchronously)
- [Application Load Balancer](./alb.md) - synchronously invokes
- [AWS IoT](./iot.md) - asynchronously invokes
- [AWS IoT - Events](./iot-events.md) - asynchronously invokes
- [Apache Kafka](./apache-kafka.md) - poll-based invokes (synchronously)
- [Amazon Kinesis - Data Firehose](./kinesis-firehose.md) - poll-based invokes (synchronously)
- [Amazon Kinesis - Data Streams](./kinesis-streams.md) - poll-based invokes (synchronously)
- [Amazon Lex](./lex.md) - synchronously invokes
- [Amazon Lex V2](./lex-v2.md) - synchronously invokes
- [Amazon MQ](./mq.md) - Active MQ and Rabbit MQ - poll-based invokes (synchronously)
- [Amazon MSK](./amazon-msk.md) - poll-based invokes (synchronously)
- [S3 - Notifications](./s3.md) - asynchronously invokes
- [S3 - Batch Operations](./s3-batch.md) - synchronously invokes
- [S3 - Object Lambda](./s3-object-lambda.md) - synchronously invokes
- [Secrets Manager](./secrets-manager.md) - synchronously invokes
- [Amazon SES](./ses.md) - configurable as asynchronously invokes or synchronously invokes
- [Amazon SNS](./sns.md) - asynchronously invokes
- [Amazon SQS](./sqs.md) - asynchronously invokes
- [Amazon WorkMail](./work-mail.md) - configurable as asynchronously invokes or synchronously invokes
