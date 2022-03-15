---
title: API Gateway Http API
description: Amazon API Gateway invokes your function synchronously with an event that contains a JSON representation of the HTTP request.
---

# API Gateway V2 - Http API

Amazon API Gateway invokes your function synchronously with an event that contains a JSON representation of the HTTP request.

Event driven, synchronously invokes

## Limits

Lambda specific hard limitations

- Payload limit of 6mb for the lambda
- Maximum timeout of 30 seconds

???+ note "NOTE: General limits and differents from Rest API"

    Large things missing IMO is `AWS X-Ray`, `Usage Plans` and `API Keys`

    - [Choosing between HTTP APIs and REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html){target="_blank"}
    - [HTTP API quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html#http-api-quotas){target="_blank"}

## Request

### Getting the correlation id

JSON path to correlation id: `requestContext.requestId`

### Generating sample events

Via [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html){target="_blank"}
you can generate sample events

```shell
# PR open with sam cli repo (https://github.com/aws/aws-sam-cli/pull/3655)
```

### Request Stucture format 2.0

!!! NOTE
    Format 2.0 doesn't have `multiValueHeaders` or `multiValueQueryStringParameters` fields. Duplicate headers
    are combined with commas and included in the headers field. Duplicate query strings are combined with
    commas and included in the queryStringParameters field.

    Format 2.0 includes a new cookies field. All cookie headers in the request are combined with commas and
    added to the cookies field. In the response to the client, each cookie becomes a set-cookie header.

```json title="Http api format 2.0"
--8<-- "docs/events/api-gateway/http-api-format-2.json"
```

### Request Stucture format 1.0

???+ note
    This is the same format as API Gateway V1 - Rest API

```json title="Http api format 1.0"
--8<-- "docs/events/api-gateway/http-api-format-1.json"
```

## Response

Base64 encoded response example

```json
{
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Content-Encoding": "gzip"
    },
    "body": "H4sIAAAAAAACE6tWKkktLlGyUlAqS8wpTVWqBQCJ88g/EQAAAA==",
    "isBase64Encoded": true
}
```

### Response for format 2.0

```json title="Lambda function response for format 2.0"
{
    "cookies" : ["cookie1", "cookie2"],
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "body": "Hello from Lambda!"
}
```

### Response for format 1.0

```json title="Lambda function response for format 1.0"
{
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "multiValueHeaders": { "headername": ["headervalue", "headervalue2", ...], ... },
    "body": "..."
}
```

## Resources

Typed Lambda handlers by Language

- [Python - data class and parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#api-gateway-proxy-v2) - Pip `aws-lambda-powertools`
- [Typescript - api-gateway-proxy.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/api-gateway-proxy.d.ts) - NPM `@types/aws-lambda`
- [Go - ApiGatewayEvent typing](https://github.com/aws/aws-lambda-go/blob/main/events/README_ApiGatewayEvent.md) - Crate `github.com/aws/aws-lambda-go/events`
- [DoNet - APIGatewayEvents data classes](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.APIGatewayEvents) - NuGet `Amazon.Lambda.APIGatewayEvents`
- [Rust - apigw/mod.rs traits](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/apigw/mod.rs) - Cargo `aws_lambda_events`
- [Java - APIGatewayV2HTTPEvent data classes](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/APIGatewayV2HTTPEvent.java) - Maven `aws-lambda-java-events`
- [PHP - typing](https://bref.sh/docs/function/handlers.html#api-gateway-http-events) - Composer `bref/bref`

Event Handlers by Language

- [AWS Lambda Powertools Python - APIGatewayHttpResolver](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)
- [PHP Bref for webapps](https://bref.sh/docs/runtimes/http.html)
- [Java - Serverless Java container](https://github.com/awslabs/aws-serverless-java-container){target="_blank"} - Makes it easy to run Java applications written with frameworks such as Spring, Spring Boot, Apache Struts, Jersey, or Spark in AWS Lambda
- [AWS Lambda Adapter](https://github.com/aws-samples/aws-lambda-adapter){target="_blank"} - A tool to run any web applications on AWS Lambda. Written in Rust.

### Code examples

Example handler for API Gateway V2 (Http API), payload format v2

```python title="example on how we can handle the /hello path."
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver

tracer = Tracer()
logger = Logger()
app = APIGatewayHttpResolver()

@app.get("/hello")
@tracer.capture_method
def get_hello_universe():
    return {"message": "hello universe"}

# You can continue to use other utilities just as before
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
```

## Documention

- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html){target="_blank"}
- [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html){target="_blank"}
