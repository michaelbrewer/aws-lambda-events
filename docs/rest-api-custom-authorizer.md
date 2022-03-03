# API Gateway Rest Authorizer

A Lambda authorizer (formerly known as a *custom authorizer*) is an API Gateway feature that uses a Lambda function to control access to your API. Event driven and synchronous.

## Request

### Token authorizer

`methodArn` (String)
: ARN of the incoming method request and is populated by API Gateway in accordance with the Lambda authorizer configuration

```json title="Token schema"
{
    "type":"TOKEN",
    "authorizationToken":"{caller-supplied-token}",
    "methodArn":"arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/{httpVerb}/[{resource}/[{child-resources}]]"
}
```

```json title="Example get call for token authorizer"
{
    "type":"TOKEN",
    "authorizationToken":"allow",
    "methodArn":"arn:aws:execute-api:us-west-2:123456789012:ymy8tbxw7b/*/GET/"
}
```

- [Introducing custom authorizers in Amazon API Gateway](https://aws.amazon.com/blogs/compute/introducing-custom-authorizers-in-amazon-api-gateway/)

### Request authorizer

```json
{
  "type": "REQUEST",
  "methodArn": "arn:aws:execute-api:us-east-1:123456789012:abcdef123/test/GET/request",
  "resource": "/request",
  "path": "/request",
  "httpMethod": "GET",
  "headers": {
    "X-AMZ-Date": "20170718T062915Z",
    "Accept": "*/*",
    "HeaderAuth1": "headerValue1",
    "CloudFront-Viewer-Country": "US",
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Tablet-Viewer": "false",
    "CloudFront-Is-Mobile-Viewer": "false",
    "User-Agent": "..."
  },
  "queryStringParameters": {
    "QueryString1": "queryValue1"
  },
  "pathParameters": {},
  "stageVariables": {
    "StageVar1": "stageValue1"
  },
  "requestContext": {
    "path": "/request",
    "accountId": "123456789012",
    "resourceId": "05c7jb",
    "stage": "test",
    "requestId": "...",
    "identity": {
      "apiKey": "...",
      "sourceIp": "...",
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
    "resourcePath": "/request",
    "httpMethod": "GET",
    "apiId": "abcdef123"
  }
}
```

## Response

```json title="Response schema"
{
  "principalId": "yyyyyyyy", // The principal user identification associated with the token sent by the client.
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
    "stringKey": "value",
    "numberKey": "1",
    "booleanKey": "true"
  },
  "usageIdentifierKey": "{api-key}"
}
```

```json title="The example output contains a policy statement to block (Deny) calls to the GET method"
{
  "principalId": "user",
  "policyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "execute-api:Invoke",
        "Effect": "Deny",
        "Resource": "arn:aws:execute-api:us-west-2:123456789012:ymy8tbxw7b/dev/GET/"
      }
    ]
  }
}
```

## Resources

- [Amazon API Gateway - Custom Authorizer Blueprints for AWS Lambda](https://github.com/awslabs/aws-apigateway-lambda-authorizer-blueprints)
- [Python - APIGatewayAuthorizerTokenEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#api-gateway-authorizer) - pip `aws-lambda-powertools`
- [Typescript - APIGatewayTokenAuthorizerEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/api-gateway-authorizer.d.ts)
- [Java - APIGatewayCustomAuthorizerEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/APIGatewayCustomAuthorizerEvent.java)

### Code examples

```python title="Token authorizer"
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event import (
    APIGatewayAuthorizerTokenEvent,
    APIGatewayAuthorizerResponse,
)


@event_source(data_class=APIGatewayAuthorizerTokenEvent)
def handler(event: APIGatewayAuthorizerTokenEvent, context):
    arn = event.parsed_arn

    policy = APIGatewayAuthorizerResponse(
        principal_id="user",
        region=arn.region,
        aws_account_id=arn.aws_account_id,
        api_id=arn.api_id,
        stage=arn.stage
    )

    if event.authorization_token == "42":
        policy.allow_all_routes()
    else:
        policy.deny_all_routes()
    return policy.asdict()
```

```python title="Request authorizer"
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event import (
    DENY_ALL_RESPONSE,
    APIGatewayAuthorizerRequestEvent,
    APIGatewayAuthorizerResponse,
    HttpVerb,
)
from secrets import compare_digest


def get_user_by_token(token):
    if compare_digest(token, "admin-foo"):
        return {"id": 0, "name": "Admin", "isAdmin": True}
    elif compare_digest(token, "regular-foo"):
        return {"id": 1, "name": "Joe"}
    else:
        return None


@event_source(data_class=APIGatewayAuthorizerRequestEvent)
def handler(event: APIGatewayAuthorizerRequestEvent, context):
    user = get_user_by_token(event.get_header_value("Authorization"))

    if user is None:
        # No user was found
        # to return 401 - `{"message":"Unauthorized"}`, but pollutes lambda error count metrics
        # raise Exception("Unauthorized")
        # to return 403 - `{"message":"Forbidden"}`
        return DENY_ALL_RESPONSE

    # parse the `methodArn` as an `APIGatewayRouteArn`
    arn = event.parsed_arn

    # Create the response builder from parts of the `methodArn`
    # and set the logged in user id and context
    policy = APIGatewayAuthorizerResponse(
        principal_id=user["id"],
        context=user,
        region=arn.region,
        aws_account_id=arn.aws_account_id,
        api_id=arn.api_id,
        stage=arn.stage,
    )

    # Conditional IAM Policy
    if user.get("isAdmin", False):
        policy.allow_all_routes()
    else:
        policy.allow_route(HttpVerb.GET, "/user-profile")

    return policy.asdict()
```

## Documentation

- [Use API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html){target="_blank"}
- [The Complete Guide to Custom Authorizers with AWS Lambda and API Gateway](https://www.alexdebrie.com/posts/lambda-custom-authorizers/){target="_blank"}
