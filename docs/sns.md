# SNS

Amazon SNS invokes your function asynchronously with an event that contains a message and metadata.

## Request

`EventVersion` (String)
: Event version should be 1.0

`EventSubscriptionArn` (String)
: Event subscription arn

`EventSource` (String)
: The AWS service from which the SNS event record originated. For SNS, this is `aws:sns`

`Sns.SignatureVersion` (String)
: Version of the Amazon SNS signature used, should be 1

`Sns.Timestamp` (String)
: The time (GMT) when the subscription confirmation was sent.

`Sns.Signature` (String)
: Base64-encoded "SHA1withRSA" signature of the Message, MessageId, Type, Timestamp, and TopicArn values.

`Sns.SigningCertUrl` (String)
: The URL to the certificate that was used to sign the message.

`Sns.MessageId` (String)
: A Universally Unique Identifier, unique for each message published. For a message that Amazon SNS resends during a 
retry, the message ID of the original message is used.

`Sns.Message` (String)
: A string that describes the message.

`Sns.Type` (String)
: The type of message. For a subscription confirmation, the type is `SubscriptionConfirmation`.

`Sns.UnsubscribeUrl` (String)
: A URL that you can use to unsubscribe the endpoint from this topic. If you visit this URL, Amazon SNS unsubscribes 
the endpoint and stops sending notifications to this endpoint.

`Sns.TopicArn` (String)
: The Amazon Resource Name (ARN) for the topic that this endpoint is subscribed to.

`Sns.Subject` (String)
: The Subject parameter specified when the notification was published to the topic.

`Sns.MessageAttributes.Type` (String)
: The supported message attribute data types are `String`, `String.Array`, `Number`, and `Binary`.

`Sns.MessageAttributes.Value` (String)
: The user-specified message attribute value.

```json title="Example Amazon SNS message event"
{
  "Records": [
    {
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-east-2:123456789012:sns-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",
      "EventSource": "aws:sns",
      "Sns": {
        "SignatureVersion": "1",
        "Timestamp": "2019-01-02T12:45:07.000Z",
        "Signature": "tcc6faL2yUC6dgZdmrwh1Y4cGa/ebXEkAi6RibDsvpi+tE/1+82j...65r==",
        "SigningCertUrl": "https://sns.us-east-2.amazonaws.com/SimpleNotificationService-ac565b8b1a6c5d002d285f9598aa1d9b.pem",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "Message": "Hello from SNS!",
        "MessageAttributes": {
          "Test": {
            "Type": "String",
            "Value": "TestString"
          },
          "TestBinary": {
            "Type": "Binary",
            "Value": "TestBinary"
          }
        },
        "Type": "Notification",
        "UnsubscribeUrl": "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&amp;SubscriptionArn=arn:aws:sns:us-east-2:123456789012:test-lambda:21be56ed-a058-49f5-8c98-aedd2564c486",
        "TopicArn":"arn:aws:sns:us-east-2:123456789012:sns-lambda",
        "Subject": "TestInvoke"
      }
    }
  ]
}
```

### Generating sample events

Via [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) you can generate sample
events

```shell
# For help run
sam local generate-event sns notification -h
# Generating a sample event with defaults
sam local generate-event sns notification
```

### Getting the correlation id

JSON path to correlation id: `Sns.MessageId`

## Response

N/A

## Resources

Input types for Amazon SNS events

- [Java SNSEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/SNSEvent.java)
- [DotNet - SNSEvent](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.SNSEvents/SNSEvent.cs)
- [Go - SNS](https://github.com/aws/aws-lambda-go/blob/main/events/sns.go)
- [Python - SNSEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#sqs)
- [Php - SnsEvent](https://bref.sh/docs/function/handlers.html#sns-events) - Composer `bref/bref`

Full handler and infrastructure code solutions

- [Ruby - sns_event](https://rubyonjets.com/docs/events/sns/){target="_blank"} - Gem `jets`
- [Python - on_sns_message](https://aws.github.io/chalice/topics/events.html#sns-events){target="_blank"} - pip `chalice`

## Documentation

- [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html){target="_blank"}
- [Youtube - AWS SNS to Lambda Tutorial in Python | Step by Step](https://www.youtube.com/watch?v=PsJsP-7cydk){target="_blank"}
