# Application Load Balancer

Elastic Load Balancing invokes your Lambda function synchronously with an event that contains the request body and metadata.

## Input

```json title="Application Load Balance GET request"
{
  "requestContext": {
    "elb": {
      "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/lambda-279XGJDqGZ5rsrHC2Fjr/49e9d65c45c6791a"
    }
  },
  "httpMethod": "GET",
  "path": "/lambda",
  "queryStringParameters": {
    "query": "1234ABCD"
  },
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "host": "lambda-alb-123578498.us-east-2.elb.amazonaws.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "x-amzn-trace-id": "Root=1-5c536348-3d683b8b04734faae651f476",
    "x-forwarded-for": "72.12.164.125",
    "x-forwarded-port": "80",
    "x-forwarded-proto": "http",
    "x-imforwards": "20"
  },
  "body": "Test",
  "isBase64Encoded": false
}
```

### Getting the correlation id

JSON path to correlation id: `headers."x-amzn-trace-id"`

### Generating sample events via SAM CLI

```shell
sam local generate-event TODO
```

## Output

```json title="Example 200 html response"
{
    "statusCode": 200,
    "statusDescription": "200 OK",
    "isBase64Encoded": False,
    "headers": {
        "Content-Type": "text/html"
    },
    "body": "<h1>Hello from Lambda!</h1>"
}
```

## Libraries

- [Python - data class and parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#application-load-balancer) - Pip `aws-lambda-powertools`
- [Typescript - alb.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/alb.d.ts) - NPM `@types/aws-lambda`
- [Rust - alb/mod.rs traits](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/alb/mod.rs) - Cargo `aws_lambda_events`
- [Go - ALBTargetGroupEvents typing](https://github.com/aws/aws-lambda-go/blob/main/events/README_ALBTargetGroupEvents.md) - Crate `github.com/aws/aws-lambda-go/events`
- [Java - ApplicationLoadBalancerRequestEvent data classes](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/ApplicationLoadBalancerRequestEvent.javaa) - Maven `aws-lambda-java-events`
- [DoNet - ApplicationLoadBalancerEvents data classes](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.ApplicationLoadBalancerEvents) - NuGet `Amazon.Lambda.ApplicationLoadBalancerEvents`

Event Handlers by Language

- [AWS Lambda Powertools Python - ALBResolver](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)
- [Serverless Java container](https://github.com/awslabs/aws-serverless-java-container)

## Reference Docs

- [Using AWS Lambda with an Application Load Balancer](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html)
- [ALB - Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)
