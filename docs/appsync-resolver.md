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
--8<-- "docs/events/appsync/amplify-graphql-directive.json"
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
--8<-- "docs/events/appsync/appsync-direct-resolver.json"
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
