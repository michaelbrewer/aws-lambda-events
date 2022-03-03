---
title: EventBridge
description: Amazon EventBridge (formerly called CloudWatch Events) invokes your function asynchronously with an event document that wraps the event from its source.
---

# Amazon EventBridge

Amazon EventBridge (formerly called CloudWatch Events) invokes your function asynchronously with an event document that wraps the event from its source.

## Request

### Example CloudWatch Event

- [CloudWatch Events Event Examples From Supported Services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html){target="_blank"}

#### EventBridge event example

```json title="EventBridge (CloudWatch Events) event example"
{
   "version":"0",
   "id":"fe8d3c65-xmpl-c5c3-2c87-81584709a377",
   "detail-type":"RDS DB Instance Event",
   "source":"aws.rds",
   "account":"123456789012",
   "time":"2020-04-28T07:20:20Z",
   "region":"us-east-2",
   "resources":[
      "arn:aws:rds:us-east-2:123456789012:db:rdz6xmpliljlb1"
   ],
   "detail":{
      "EventCategories":[
         "backup"
      ],
      "SourceType":"DB_INSTANCE",
      "SourceArn":"arn:aws:rds:us-east-2:123456789012:db:rdz6xmpliljlb1",
      "Date":"2020-04-28T07:20:20.112Z",
      "Message":"Finished DB Instance backup",
      "SourceIdentifier":"rdz6xmpliljlb1"
   }
}
```

#### EventBridge scheduled event

```json title="EventBridge (CloudWatch Events) message event"
{
   "version":"0",
   "account":"123456789012",
   "region":"us-east-2",
   "detail":{},
   "detail-type":"Scheduled Event",
   "source":"aws.events",
   "time":"2019-03-01T01:23:45Z",
   "id":"cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
   "resources":[
      "arn:aws:events:us-east-2:123456789012:rule/my-schedule"
   ]
}
```

#### EventBridge S3 event

```json title="EventBridge S3 event"
{
   "version":"0",
   "id":"2d4eba74-fd51-3966-4bfa-b013c9da8ff1",
   "detail-type":"Object Created",
   "source":"aws.s3",
   "account":"123456789012",
   "time":"2021-11-13T00:00:59Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:s3:::jbarr-public"
   ],
   "detail":{
      "version":"0",
      "bucket":{
         "name":"jbarr-public"
      },
      "object":{
         "key":"eb_create_rule_mid_1.png",
         "size":99797,
         "etag":"7a72374e1238761aca7778318b363232",
         "version-id":"a7diKodKIlW3mHIvhGvVphz5N_ZcL3RG",
         "sequencer":"00618F003B7286F496"
      },
      "request-id":"4Z2S00BKW2P1AQK8",
      "requester":"348414629041",
      "source-ip-address":"72.21.198.68",
      "reason":"PutObject"
   }
}
```

#### EC2 Instance State-change Event

EventBridge (CloudWatch Events) invokes your Lambda function asynchronously with the event document from Amazon EC2.

- [Using AWS Lambda with Amazon EC2](https://docs.aws.amazon.com/lambda/latest/dg/services-ec2.html){target="_blank"}

```json title="Amazon EC2 State Change Events"
{
    "version": "0",
    "id": "b6ba298a-7732-2226-xmpl-976312c1a050",
    "detail-type": "EC2 Instance State-change Notification",
    "source": "aws.ec2",
    "account": "123456798012",
    "time": "2019-10-02T17:59:30Z",
    "region": "us-east-2",
    "resources": [
        "arn:aws:ec2:us-east-2:123456798012:instance/i-0c314xmplcd5b8173"
    ],
    "detail": {
        "instance-id": "i-0c314xmplcd5b8173",
        "state": "running"
    }
}
```

### Getting the correlation id

JSON path to correlation id: `id`

### Generating sample events

```shell
sam local generate-event cloudwatch scheduled-event
```

## Response

N/A

## Resources

Typing and data classes

- [Typescript - EventBridgeEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/eventbridge.d.ts) - NPM `@types/aws-lambda`
- [Python - EventBridgeEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#eventbridge) - Pip `aws-lambda-powertools`
- [Go - CloudWatchEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_CloudWatch_Events.md)
- [DotNet - CloudWatchEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.CloudWatchEvents) - NuGet `Amazon.Lambda.CloudWatchEvents`
- [Php - EventBridgeEvent](https://bref.sh/docs/function/handlers.html#eventbridge-events) - Composer `bref/bref`
- [Rust - cloud_events](https://docs.rs/aws_lambda_events/latest/aws_lambda_events/cloudwatch_events/index.html) - `aws_lambda_events`

Handlers with infrastructure provisioning

- [Ruby - CloudWatch Rules Event](https://rubyonjets.com/docs/events/cloudwatch-rule/) - gem `jets`
- [Python - Chalice on_cw_event](https://aws.github.io/chalice/topics/events.html#cloudwatch-events) - pip `chalice`

### Code Examples

DotNet has a large number of handlers for CloudWatch Events.

```C# title="DotNet ECSTaskStateChangeEvent example"
public class Function
{
    public string Handler(ECSTaskStateChangeEvent ecsTaskStateChangeEvent)
    {
        Console.WriteLine($"ECS Task ARN - {ecsTaskStateChangeEvent.Detail.TaskArn}");
    }
}
```

[Jet - CloudWatch Rules Events](https://rubyonjets.com/docs/events/cloudwatch-rule/) allows you to define the infracture code next to the implementation

```ruby title="Ruby example might be getting notified when an unwanted security group port gets opened."
class SecurityJob < ApplicationJob
  rule_event(
    description: "Checks for security group changes",
    detail_type: ["AWS API Call via CloudTrail"],
    detail: {
      event_source: ["ec2.amazonaws.com"],
      event_name: [
        "AuthorizeSecurityGroupIngress",
        "AuthorizeSecurityGroupEgress",
        "RevokeSecurityGroupIngress",
        "RevokeSecurityGroupEgress",
        "CreateSecurityGroup",
        "DeleteSecurityGroup"
      ]
    }
  )
  def detect_security_group_changes
    puts "event: #{JSON.dump(event)}" # event is available
    # your logic
  end
end
```
[Chalice](https://aws.github.io/chalice/topics/events.html#cloudwatch-events) can also to the infrastructure provisioning along set the lambda handler

```python title="Example using Chalice to subscribe to code commit events"
app = chalice.Chalice(app_name='foo')

@app.on_cw_event({"source": ["aws.codecommit"]})
def on_code_commit_changes(event):
    print(event.to_dict())
```

```python title="Chalice scheduling ab hourly Cloudwatch event"
app = chalice.Chalice(app_name='foo')

@app.schedule('rate(1 hour)')
def every_hour(event):
    print(event.to_dict())
```

## Documentation

- [Amazon EventBridge (CloudWatch Events)](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html){target="_blank"}
- [Use Amazon S3 Event Notifications with Amazon EventBridge](https://aws.amazon.com/blogs/aws/new-use-amazon-s3-event-notifications-with-amazon-eventbridge/){target="_blank"}
- [CloudWatch Events Event Examples From Supported Services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html){target="_blank"}
