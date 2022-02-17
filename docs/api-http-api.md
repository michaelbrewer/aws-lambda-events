# API Gateway Http API

## Input

Http api format 2.0

```json
{
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/my/path",
  "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {
    "Header1": "value1",
    "Header2": "value1,value2"
  },
  "queryStringParameters": {
    "parameter1": "value1,value2",
    "parameter2": "value"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "api-id",
    "authentication": {
      "clientCert": {
        "clientCertPem": "CERT_CONTENT",
        "subjectDN": "www.example.com",
        "issuerDN": "Example issuer",
        "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
        "validity": {
          "notBefore": "May 28 12:30:02 2019 GMT",
          "notAfter": "Aug  5 09:36:04 2021 GMT"
        }
      }
    },
    "authorizer": {
      "jwt": {
        "claims": {
          "claim1": "value1",
          "claim2": "value2"
        },
        "scopes": [
          "scope1",
          "scope2"
        ]
      }
    },
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "http": {
      "method": "POST",
      "path": "/my/path",
      "protocol": "HTTP/1.1",
      "sourceIp": "192.168.0.1/32",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "$default",
    "stage": "$default",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "{\"message\": \"hello world\", \"username\": \"tom\"}",
  "pathParameters": {
    "parameter1": "value1"
  },
  "isBase64Encoded": false,
  "stageVariables": {
    "stageVariable1": "value1",
    "stageVariable2": "value2"
  }
}
```

### Getting the correlation id

JSON path to correlation id: `requestContext.requestId`

### Generating sample events via SAM CLI

```shell
sam local generate-event TODO
```

## Output

### Lambda function response for format 1.0

```json
{
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "multiValueHeaders": { "headername": ["headervalue", "headervalue2", ...], ... },
    "body": "..."
}
```

### Lambda function response for format 2.0

```json
{
    "cookies" : ["cookie1", "cookie2"],
    "isBase64Encoded": true|false,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "body": "Hello from Lambda!"
}
```

## Libraries

Typed Lambda handlers by Language

- [Python - data class and parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#api-gateway-proxy-v2) - Pip `aws-lambda-powertools`
- [Typescript - api-gateway-proxy.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/api-gateway-proxy.d.ts) - NPM `@types/aws-lambda`
- [Rust - apigw/mod.rs traits](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/apigw/mod.rs) - Cargo `aws_lambda_events`
- [Go - ApiGatewayEvent typing](https://github.com/aws/aws-lambda-go/blob/main/events/README_ApiGatewayEvent.md) - Crate `github.com/aws/aws-lambda-go/events`
- [Java - APIGatewayV2HTTPEvent data classes](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/APIGatewayV2HTTPEvent.java) - Maven `aws-lambda-java-events`
- [PHP - typing](https://bref.sh/docs/function/handlers.html#api-gateway-http-events) - Composer `bref/bref`
- [DoNet - APIGatewayEvents data classes](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.APIGatewayEvents) - NuGet `Amazon.Lambda.APIGatewayEvents`

Event Handlers by Language

- [AWS Lambda Powertools Python - APIGatewayHttpResolver](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)
- [PHP Bref for webapps](https://bref.sh/docs/runtimes/http.html)
- [Serverless Java container](https://github.com/awslabs/aws-serverless-java-container)

## Reference Docs

- [Working with AWS Lambda proxy integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html)
