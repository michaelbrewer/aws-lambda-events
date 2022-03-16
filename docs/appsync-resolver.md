# AppSync Resolver


**Direct Lambda Resolvers**
: With Direct Lambda Resolvers, you can circumvent the use of VTL mapping templates when using AWS Lambda data sources.

**Amplify GraphQL direct `@function`**
: The Amplify `@function` directive allows you to quickly & easily configure a AWS Lambda resolvers with your GraphQL API. 

Event driven, invoked synchronously.

!!! WARNING "Note"
    AppSync Resolver Events can come in various shapes this data class supports both Amplify GraphQL directive `@function` and Direct Lambda Resolver

## Limits

- Request execution timeout of 30 seconds
- Payload size limit of 1MB

## Request

### Amplify GraphQL directive

List of fields

`typeName` (String)
: The name of the parent object type of the field being resolver.

`fieldName` (String)
: The name of the field being resolved.

`arguments` (Map)
: A map containing the arguments passed to the field being resolved.

`identity` (Object)
: A map containing identity information for the request. Contains a nested key 'claims' that will contains the JWT claims if they exist.

`source` (Map)
: A map that contains the resolution of the parent field. When resolving a nested field in a query, the source contains parent value at runtime. 
For example when resolving `Post.comments`, the source will be the `Post` object.

`request` (String)
: The AppSync request object. Contains header information.

`next` (String)
: When using pipeline resolvers, this contains the object returned by the previous function. You can return the previous value for auditing use cases.

```json title="Amplify GraphQL directive"
{
  "typeName": "Merchant",
  "fieldName": "locations",
  "arguments": {
    "page": 2,
    "size": 1,
    "name": "value"
  },
  "identity": {
    "claims": {
      "sub": "07920713-4526-4642-9c88-2953512de441",
      "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_POOL_ID",
      "aud": "58rc9bf5kkti90ctmvioppukm9",
      "event_id": "7f4c9383-abf6-48b7-b821-91643968b755",
      "token_use": "id",
      "auth_time": 1615366261,
      "name": "Michael Brewer",
      "exp": 1615369861,
      "iat": 1615366261
    },
    "defaultAuthStrategy": "ALLOW",
    "groups": null,
    "issuer": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_POOL_ID",
    "sourceIp": [
      "11.215.2.22"
    ],
    "sub": "07920713-4526-4642-9c88-2953512de441",
    "username": "mike"
  },
  "source": {
    "name": "Value",
    "nested": {
      "name": "value",
      "list": []
    }
  },
  "request": {
    "headers": {
      "x-forwarded-for": "11.215.2.22, 64.44.173.11",
      "cloudfront-viewer-country": "US",
      "cloudfront-is-tablet-viewer": "false",
      "via": "2.0 SOMETHING.cloudfront.net (CloudFront)",
      "cloudfront-forwarded-proto": "https",
      "origin": "https://console.aws.amazon.com",
      "content-length": "156",
      "accept-language": "en-US,en;q=0.9",
      "host": "SOMETHING.appsync-api.us-east-1.amazonaws.com",
      "x-forwarded-proto": "https",
      "sec-gpc": "1",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) etc.",
      "accept": "*/*",
      "cloudfront-is-mobile-viewer": "false",
      "cloudfront-is-smarttv-viewer": "false",
      "accept-encoding": "gzip, deflate, br",
      "referer": "https://console.aws.amazon.com/",
      "content-type": "application/json",
      "sec-fetch-mode": "cors",
      "x-amz-cf-id": "Fo5VIuvP6V6anIEt62WzFDCK45mzM4yEdpt5BYxOl9OFqafd-WR0cA==",
      "x-amzn-trace-id": "Root=1-60488877-0b0c4e6727ab2a1c545babd0",
      "authorization": "AUTH-HEADER",
      "sec-fetch-dest": "empty",
      "x-amz-user-agent": "AWS-Console-AppSync/",
      "cloudfront-is-desktop-viewer": "true",
      "sec-fetch-site": "cross-site",
      "x-forwarded-port": "443"
    }
  },
  "prev": {
    "result": {}
  }
}
```

### Direct Lambda Resolver

List of fields

`info.parentTypeName` (String)
: The name of the parent object type of the field being resolver.

`info.fieldName` (String)
: The name of the field being resolved.

`arguments` (Map)
: A map containing the arguments passed to the field being resolved.

`identity` (Object)
: A map containing identity information for the request. Contains a nested key 'claims' that will contains the JWT claims if they exist.

`source` (Map)
: A map that contains the resolution of the parent field. When resolving a nested field in a query, the source contains parent value at runtime. 
For example when resolving `Post.comments`, the source will be the `Post` object.

`request` (String)
: The AppSync request object. Contains header information.

`next` (String)
: When using pipeline resolvers, this contains the object returned by the previous function. You can return the previous value for auditing use cases.

```json title="AppSync direct resolver"
{
  "arguments": {
    "id": "my identifier"
  },
  "identity": {
    "claims": {
      "sub": "192879fc-a240-4bf1-ab5a-d6a00f3063f9",
      "email_verified": true,
      "iss": "https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx",
      "phone_number_verified": false,
      "cognito:username": "jdoe",
      "aud": "7471s60os7h0uu77i1tk27sp9n",
      "event_id": "bc334ed8-a938-4474-b644-9547e304e606",
      "token_use": "id",
      "auth_time": 1599154213,
      "phone_number": "+19999999999",
      "exp": 1599157813,
      "iat": 1599154213,
      "email": "jdoe@email.com"
    },
    "defaultAuthStrategy": "ALLOW",
    "groups": null,
    "issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-xxxxxxxxxxx",
    "sourceIp": [
      "1.1.1.1"
    ],
    "sub": "192879fc-a240-4bf1-ab5a-d6a00f3063f9",
    "username": "jdoe"
  },
  "source": null,
  "request": {
    "headers": {
      "x-forwarded-for": "1.1.1.1, 2.2.2.2",
      "cloudfront-viewer-country": "US",
      "cloudfront-is-tablet-viewer": "false",
      "via": "2.0 xxxxxxxxxxxxxxxx.cloudfront.net (CloudFront)",
      "cloudfront-forwarded-proto": "https",
      "origin": "https://us-west-1.console.aws.amazon.com",
      "content-length": "217",
      "accept-language": "en-US,en;q=0.9",
      "host": "xxxxxxxxxxxxxxxx.appsync-api.us-west-1.amazonaws.com",
      "x-forwarded-proto": "https",
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
      "accept": "*/*",
      "cloudfront-is-mobile-viewer": "false",
      "cloudfront-is-smarttv-viewer": "false",
      "accept-encoding": "gzip, deflate, br",
      "referer": "https://us-west-1.console.aws.amazon.com/appsync/home?region=us-west-1",
      "content-type": "application/json",
      "sec-fetch-mode": "cors",
      "x-amz-cf-id": "3aykhqlUwQeANU-HGY7E_guV5EkNeMMtwyOgiA==",
      "x-amzn-trace-id": "Root=1-5f512f51-fac632066c5e848ae714",
      "authorization": "eyJraWQiOiJScWFCSlJqYVJlM0hrSnBTUFpIcVRXazNOW...",
      "sec-fetch-dest": "empty",
      "x-amz-user-agent": "AWS-Console-AppSync/",
      "cloudfront-is-desktop-viewer": "true",
      "sec-fetch-site": "cross-site",
      "x-forwarded-port": "443"
    }
  },
  "prev": null,
  "info": {
    "selectionSetList": [
      "id",
      "field1",
      "field2"
    ],
    "selectionSetGraphQL": "{\n  id\n  field1\n  field2\n}",
    "parentTypeName": "Mutation",
    "fieldName": "createSomething",
    "variables": {}
  },
  "stash": {}
}
```

## Response

Response is based on the expected GraphQL response.

## Resources

Typed handlers by language

- [Python - AppSyncResolverEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#appsync-authorizer)

Lambda handlers by language

- [Python - AppSyncResolver](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/appsync/) - pip `aws-lambda-powertools`

### Code Examples

```python title="AppSync resolver using AWS Lambda Powertools"
from aws_lambda_powertools import Logger, Tracer

from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.utilities.data_classes.appsync import scalar_types_utils

tracer = Tracer(service="sample_resolver")
logger = Logger(service="sample_resolver")
app = AppSyncResolver()

# Note that `creation_time` isn't available in the schema
# This utility also takes into account what info you make available at API level vs what's stored
TODOS = [
    {
        "id": scalar_types_utils.make_id(), # type ID or String
        "title": "First task",
        "description": "String",
        "done": False,
        "creation_time": scalar_types_utils.aws_datetime(),  # type AWSDateTime
    },
    {
        "id": scalar_types_utils.make_id(),
        "title": "Second task",
        "description": "String",
        "done": True,
        "creation_time": scalar_types_utils.aws_datetime(),
    },
]


@app.resolver(type_name="Query", field_name="getTodo")
def get_todo(id: str = ""):
    logger.info(f"Fetching Todo {id}")
    todo = [todo for todo in TODOS if todo["id"] == id]

    return todo


@app.resolver(type_name="Query", field_name="listTodos")
def list_todos():
    return TODOS


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
```

## Documentation

- [AppSync - Resolver mapping template context reference](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html)
- [AppSync - Tutorial: Lambda resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-lambda-resolvers.html)
- [Amplify - Configure Lambda resolvers](https://docs.amplify.aws/cli-legacy/graphql-transformer/function/#structure-of-the-function-event)
- [Blog - Introducing Direct Lambda Resolvers: AWS AppSync GraphQL APIs without VTL](https://aws.amazon.com/blogs/mobile/appsync-direct-lambda/)
- [Serverlessland - AppSync to Lambda](https://serverlessland.com/patterns/appsync-direct-lambda-resolver)
