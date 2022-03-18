# Amazon Connect

Amazon Connect invokes your Lambda function synchronously with an event that contains the request body and metadata.

Event-driven, synchronous invocation

## Request

### Example event

Amazon Connect invokes your Lambda function synchronously with an event that contains the request body and metadata.

```json title="Example Amazon Connect request event"
--8<-- "docs/events/amazon-connect/amazon-connect.json"
```

## Response

No required response format

```json
{
    "Name": "CustomerName",
    "Address": "1234 Main Road",
    "CallerType": "Patient"
}
```

## Resources

- [Typescript - ConnectContactFlowEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/connect-contact-flow.d.ts) - NPM `@types/aws-lambda`
- [Java - ConnectEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/ConnectEvent.java) - Maven `aws-lambda-java-events`
- [Python - ConnectContactFlowEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#verify-auth-challenge-response-example) - pip `aws-lambda-powertools`
- [DotNet - ContactFlowEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.ConnectEvents) - Nuget `Amazon.Lambda.ConnectEvents`

## Documentation

- [Using Lambda with Amazon Connect](https://docs.aws.amazon.com/lambda/latest/dg/services-connect.html)
- [Config - Invoke AWS Lambda functions](https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions.html)
