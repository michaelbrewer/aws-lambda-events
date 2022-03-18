# API Gateway Http Authorizer

You use a Lambda authorizer to use a Lambda function to control access to your HTTP API. Then, when a client calls your API, API Gateway invokes your Lambda function. API Gateway uses the response from your Lambda function to determine whether the client can access your API.

Event driven, synchronous.

## Limits

- Authorizers per API limit of 10, but can be increased.
- Audiences per authorizer of 50, and can not be increased.

## Request

### API Gateway Authorizer Request Event Format 1.0

Same as [API Gateway Rest Authorizer - Request](./rest-api-custom-authorizer.md)

```json
--8<-- "docs/events/api-gateway/api-gateway-authorizer-format-1.json"
```

### API Gateway Authorizer Request Event Format 2.0

```json
--8<-- "docs/events/api-gateway/api-gateway-authorizer-format-2.json"
```

## Response

### IAM Policy

```json
{
  "principalId": "abcdef", // The principal user identification associated with the token sent by the client.
  "policyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "execute-api:Invoke",
        "Effect": "Allow|Deny",
        "Resource": "arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/{httpVerb}/[{resource}/[{child-resources}]]"
      }
    ]
  },
  "context": {
    "exampleKey": "exampleValue"
  }
}
```

### Simple response

```json
{
  "isAuthorized": true/false,
  "context": {
    "exampleKey": "exampleValue"
  }
}
```

## Resources

- [Python - APIGatewayAuthorizerEventV2](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#api-gateway-authorizer-v2)

### Code examples

```python
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event import (
    APIGatewayAuthorizerEventV2,
    APIGatewayAuthorizerResponseV2,
)
from secrets import compare_digest


def get_user_by_token(token):
    if compare_digest(token, "Foo"):
        return {"name": "Foo"}
    return None


@event_source(data_class=APIGatewayAuthorizerEventV2)
def handler(event: APIGatewayAuthorizerEventV2, context):
    user = get_user_by_token(event.get_header_value("x-token"))

    if user is None:
        # No user was found, so we return not authorized
        return APIGatewayAuthorizerResponseV2().asdict()

    # Found the user and setting the details in the context
    return APIGatewayAuthorizerResponseV2(authorize=True, context=user).asdict()
```

## Documentation

- [Working with AWS Lambda authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html){target="_blank"}
- [Introducing IAM and Lambda authorizers for Amazon API Gateway HTTP APIs](https://aws.amazon.com/blogs/compute/introducing-iam-and-lambda-authorizers-for-amazon-api-gateway-http-apis/){target="_blank"}
