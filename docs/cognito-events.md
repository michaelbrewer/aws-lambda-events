---
title: Cognito Events
---

# Amazon Cognito Events

Amazon Cognito Events allows you to execute an AWS Lambda function in response to important events in Amazon Cognito.

Event-driven, synchronous invocation

## Request

```json
--8<-- "docs/events/cognito-events/cognito-event.json"
```

## Response

N/A

## Resources

- [DotNet - CognitoEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.CognitoEvents) - NuGet `Amazon.Lambda.CognitoEvents`
- [Java - CognitoEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CognitoEvent.java) - Maven `aws-lambda-java-events`

### Code Examples

```javascript
exports.handler = function(event, context) {
    //Check for the event type
    if (event.eventType === 'SyncTrigger') {
        //Modify value for a key
        if('SampleKey1' in event.datasetRecords){
            event.datasetRecords.SampleKey1.newValue = 'ModifyValue1';
            event.datasetRecords.SampleKey1.op = 'replace';
        }

        //Remove a key
        if('SampleKey2' in event.datasetRecords){
            event.datasetRecords.SampleKey2.op = 'remove';
        }

        //Add a key
        if(!('SampleKey3' in event.datasetRecords)){
            event.datasetRecords.SampleKey3={'newValue':'ModifyValue3', 'op' : 'replace'};
        }
    }

context.done(null, event);
};
```

## Documentation

- [Amazon Cognito Events](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-events.html)
