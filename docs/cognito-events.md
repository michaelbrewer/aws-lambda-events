# Amazon Cognito Events

Event-driven; synchronous invocation

## Input

```json
{
  "version": 2,
  "eventType": "SyncTrigger",
  "region": "us-east-1",
  "identityPoolId": "identityPoolId",
  "identityId": "identityId",
  "datasetName": "datasetName",
  "datasetRecords": {
    "SampleKey1": {
      "oldValue": "oldValue1",
      "newValue": "newValue1",
      "op": "replace"
    },
    "SampleKey2": {
      "oldValue": "oldValue2",
      "newValue": "newValue2",
      "op": "replace"
    },
    ...
  }
}
```

## Response

N/A

## Libraries

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

## Reference Docs

- [Amazon Cognito Events](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-events.html)
