# API Gateway Http API

Amazon API Gateway invokes your function synchronously with an event that contains a JSON representation of the HTTP request.

## Limits

Payload limit of 6mb for the lambda
Maximum timeout of 30 seconds

## Input

### Getting the correlation id

JSON path to correlation id: `requestContext.requestId`

### Generating sample events via SAM CLI

```shell
# PR open with sam cli (https://github.com/aws/aws-sam-cli/pull/3655)
```

### Input Stucture format 2.0

!!! NOTE
    Format 2.0 doesn't have multiValueHeaders or multiValueQueryStringParameters fields. Duplicate headers
    are combined with commas and included in the headers field. Duplicate query strings are combined with
    commas and included in the queryStringParameters field.

    Format 2.0 includes a new cookies field. All cookie headers in the request are combined with commas and
    added to the cookies field. In the response to the client, each cookie becomes a set-cookie header.

```json title="Http api format 2.0"
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

### Input Stucture format 1.0

```json title="Http api format 1.0"
{
  "version": "1.0",
  "resource": "/my/path",
  "path": "/my/path",
  "httpMethod": "GET",
  "headers": {
    "header1": "value1",
    "header2": "value2"
  },
  "multiValueHeaders": {
    "header1": [
      "value1"
    ],
    "header2": [
      "value1",
      "value2"
    ]
  },
  "queryStringParameters": {
    "parameter1": "value1",
    "parameter2": "value"
  },
  "multiValueQueryStringParameters": {
    "parameter1": [
      "value1",
      "value2"
    ],
    "parameter2": [
      "value"
    ]
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "id",
    "authorizer": {
      "claims": null,
      "scopes": null
    },
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "extendedRequestId": "request-id",
    "httpMethod": "GET",
    "identity": {
      "accessKey": null,
      "accountId": null,
      "caller": null,
      "cognitoAuthenticationProvider": null,
      "cognitoAuthenticationType": null,
      "cognitoIdentityId": null,
      "cognitoIdentityPoolId": null,
      "principalOrgId": null,
      "sourceIp": "IP",
      "user": null,
      "userAgent": "user-agent",
      "userArn": null,
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
    "path": "/my/path",
    "protocol": "HTTP/1.1",
    "requestId": "id=",
    "requestTime": "04/Mar/2020:19:15:17 +0000",
    "requestTimeEpoch": 1583349317135,
    "resourceId": null,
    "resourcePath": "/my/path",
    "stage": "$default"
  },
  "pathParameters": null,
  "stageVariables": null,
  "body": "Hello from Lambda!",
  "isBase64Encoded": false
}
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
- [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)
