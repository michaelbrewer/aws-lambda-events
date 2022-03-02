# Amazon Connect

Event-driven, synchronous invocation

## Request

### Example event

Amazon Connect invokes your Lambda function synchronously with an event that contains the request body and metadata.

```json title="Example Amazon Connect request event"
{
  "Details": {
      "ContactData": {
          "Attributes": {},
          "Channel": "VOICE",
          "ContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXXX",
          "CustomerEndpoint": {
              "Address": "+1234567890",
              "Type": "TELEPHONE_NUMBER"
          },
          "InitialContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXXX",
          "InitiationMethod": "INBOUND | OUTBOUND | TRANSFER | CALLBACK",
          "InstanceARN": "arn:aws:connect:aws-region:1234567890:instance/c8c0e68d-2200-4265-82c0-XXXXXXXXXX",
          "PreviousContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXXX",
          "Queue": {
             "ARN": "arn:aws:connect:eu-west-2:111111111111:instance/cccccccc-bbbb-dddd-eeee-ffffffffffff/queue/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
             "Name": "PasswordReset"
           },
          "SystemEndpoint": {
              "Address": "+1234567890",
              "Type": "TELEPHONE_NUMBER"
          }
      },
      "Parameters": {
          "sentAttributeKey": "sentAttributeValue"
      }
  },
  "Name": "ContactFlowEvent"
}
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

## Libraries

- [Typescript - ConnectContactFlowEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/connect-contact-flow.d.ts) - NPM `@types/aws-lambda`
- [Java - ConnectEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/ConnectEvent.java) - Maven `aws-lambda-java-events`
- [Python - ConnectContactFlowEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#verify-auth-challenge-response-example) - pip `aws-lambda-powertools`
- [DotNet - ContactFlowEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.ConnectEvents) - Nuget `Amazon.Lambda.ConnectEvents`

## Documentation

- [Using Lambda with Amazon Connect](https://docs.aws.amazon.com/lambda/latest/dg/services-connect.html)
- [Config - Invoke AWS Lambda functions](https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions.html)
