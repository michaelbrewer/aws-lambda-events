# Function URL

Uses the same Request and Response structures as the [API Gateway Http API](./http-api.md), but has some different limits.

See [AWS Lambda Function URLs vs. Amazon API Gateway](https://www.serverlessguru.com/blog/aws-lambda-function-urls-vs-amazon-api-gateway) 
for a comparison to API Gateway.

## Limits

Lambda specific hard limitations

- Payload limit of 6mb for the Lambda
- Maximum timeouts up to 900 seconds (15 minutes)


## Request

```json
{
  "version": "2.0",
  "rawPath": "/my/path",
  "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
  "cookies": [
    "cookie1",
    "cookie2"
  ],
  "headers": {
    "header1": "value1",
    "header2": "value1,value2"
  },
  "queryStringParameters": {
    "parameter1": "value1,value2",
    "parameter2": "value"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "<urlid>",
    "authorizer": {
      "iam": {
        "accessKey": "AKIA...",
        "accountId": "111122223333",
        "callerId": "AIDA...",
        "userArn": "arn:aws:iam::111122223333:user/example-user",
        "userId": "AIDA..."
      }
    },
    "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
    "domainPrefix": "<url-id>",
    "http": {
      "method": "POST",
      "path": "/my/path",
      "protocol": "HTTP/1.1",
      "sourceIp": "123.123.123.123",
      "userAgent": "agent"
    },
    "requestId": "id",
    "time": "12/Mar/2020:19:03:58 +0000",
    "timeEpoch": 1583348638390
  },
  "body": "Hello from client!",
  "isBase64Encoded": false
}
```

## Response

```json
{
   "statusCode": 201,
    "headers": {
        "Content-Type": "application/json",
        "My-Custom-Header": "Custom Value"
    },
    "body": "{ \"message\": \"Hello, world!\" }",
    "cookies": [
        "Cookie_1=Value1; Expires=21 Oct 2021 07:48 GMT",
        "Cookie_2=Value2; Max-Age=78000"
    ],
    "isBase64Encoded": false
}
```

## Resources

Typed Lambda handlers by Language

- [Go - LambdaFunctionURLRequest typing](https://github.com/aws/aws-lambda-go/blob/main/events/lambda_function_urls.go) - Go `github.com/aws/aws-lambda-go/events`

## Documention

- [Blog: AWS Lambda Function URLs: Built-in HTTPS Endpoints for Single-Function Microservices](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices/){target="_blank"}
- [Blog: AWS Lambda: function URL is live! - By Yan Cui](https://lumigo.io/blog/aws-lambda-function-url-is-live/){target="_blank"}
