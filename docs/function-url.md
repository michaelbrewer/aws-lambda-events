# Function URL

Uses the same Request and Response structures as the [API Gateway Http API](./http-api.md), but has some different limits.

## Limits

Lambda specific hard limitations

- Payload limit of 6mb for the Lambda
- Maximum timeouts up to 900 seconds (15 minutes)


## Resources

Typed Lambda handlers by Language

- [Go - LambdaFunctionURLRequest typing](https://github.com/aws/aws-lambda-go/blob/main/events/lambda_function_urls.go) - Go `github.com/aws/aws-lambda-go/events`

## Documention

- [Blog: AWS Lambda Function URLs: Built-in HTTPS Endpoints for Single-Function Microservices](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-function-urls-built-in-https-endpoints-for-single-function-microservices/)
