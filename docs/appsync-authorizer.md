# AppSync Authorizer

Event driven, invoked synchronously.

## Limits

- Lambda authorizers have a timeout of 10 seconds.
- An authorization token must not exceed 2048 characters
- A Lambda function must not return more than 5MB of contextual data for resolvers.

## Input

```json
{
    "authorizationToken": "BE9DC5E3-D410-4733-AF76-70178092E681",
    "requestContext": {
        "apiId": "giy7kumfmvcqvbedntjwjvagii",
        "accountId": "254688921111",
        "requestId": "b80ed838-14c6-4500-b4c3-b694c7bef086",
        "queryString": "mutation MyNewTask($desc: String!) {\n  createTask(description: $desc, owner: \"ccc\", taskStatus: \"cc\", title: \"ccc\") {\n    id\n  }\n}\n",
        "operationName": "MyNewTask",
        "variables": {
            "desc": "Foo"
        }
    }
}
```

## Response

`isAuthorized` (Required, Boolean)
: A boolean value indicating if the value in authorizationToken is authorized to make calls to the GraphQL API.
If this value is true, execution of the GraphQL API continues. If this value is false, an `UnauthorizedException` is raised

`deniedFields` (Optional, Array)
: A list of which are forcibly changed to null, even if a value was returned from a resolver.
Each item is either a fully qualified field ARN in the form of `arn:aws:appsync:us-east-1:111122223333:apis/GraphQLApiId/types/TypeName/fields/FieldName` or
a short form of `TypeName.FieldName`. The full ARN form should be used when two APIs share a lambda function authorizer and there might be ambiguity 
between common types and fields between the two APIs.

`resolverContext` (Optional, Object)
: A JSON object visible as `$ctx.identity.resolverContext` in resolver templates.

`ttlOverride` (Optional, Number)
: The number of seconds that the response should be cached for. If no value is returned, the value from the API (if configured) or the default of 
300 seconds (five minutes) is used. If this is 0, the response is not cached.

```json title="Example response"
{
    "isAuthorized": true,
    "resolverContext": {
        "name": "Foo Man",
        "balance": 100
    },
    "deniedFields": ["Mutation.createEvent"],
    "ttlOverride": 15
}
```

## Libraries

AppSync typed handler and response builder by language

- [Python - AppSyncAuthorizerEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#application-load-balancer)

### Code Example

```python title="app.py"
from typing import Dict

from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.logging.logger import Logger
from aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event import (
    AppSyncAuthorizerEvent,
    AppSyncAuthorizerResponse,
)
from aws_lambda_powertools.utilities.data_classes.event_source import event_source

logger = Logger()


def get_user_by_token(token: str):
    """Look a user by token"""
    ...


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_AUTHORIZER)
@event_source(data_class=AppSyncAuthorizerEvent)
def lambda_handler(event: AppSyncAuthorizerEvent, context) -> Dict:
    user = get_user_by_token(event.authorization_token)

    if not user:
        # No user found, return not authorized
        return AppSyncAuthorizerResponse().asdict()

    return AppSyncAuthorizerResponse(
        authorize=True,
        resolver_context={"id": user.id},
        # Only allow admins to delete events
        deny_fields=None if user.is_admin else ["Mutation.deleteEvent"],
    ).asdict()
```

## Reference Docs

- [AppSync Authorizer - AWS_LAMBDA Authorization](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#aws-lambda-authorization)
- [Amplify - AWS Lambda Authorization](https://docs.amplify.aws/lib/graphqlapi/authz/q/platform/js/#aws-lambda)
- [Introducing Lambda authorization for AWS AppSync GraphQL APIs](https://aws.amazon.com/blogs/mobile/appsync-lambda-auth/)
