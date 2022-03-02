# Amazon MSK

Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that you can use to build and run applications that use Apache Kafka to
process streaming data.

Lambda internally polls for new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the messages in 
batches and provides these to your function as an event payload.

## Limits

- The maximum batch size is configurable. (The default is 100 messages.)
- Lambda can run your function for up to 14 minutes.

## Request

!!! Note
      Shares the same structure as [Self managed Apache Kafka](./apache-kafka.md), except for the eventSource field is set to "aws:msk".

```json title="Managed Kafka"
{
   "eventSource":"aws:kafka",
   "eventSourceArn":"arn:aws:kafka:sa-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
   "records":{
      "mytopic-0":[
         {
            "topic":"mytopic",
            "partition":"0",
            "offset":15,
            "timestamp":1545084650987,
            "timestampType":"CREATE_TIME",
            "value":"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
            "headers":[
               {
                  "headerKey":[
                     104,
                     101,
                     97,
                     100,
                     101,
                     114,
                     86,
                     97,
                     108,
                     117,
                     101
                  ]
               }
            ]
         }
      ]
   }
}
```

```json title="Another managed Kafka example"
{
  "eventSource": "aws:kafka",
  "eventSourceArn": "arn:aws:kafka:us-west-2:012345678901:cluster/ExampleMSKCluster/e9f754c6-d29a-4430-a7db-958a19fd2c54-4",
  "bootstrapServers": "b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
  "records": {
    "AWSKafkaTopic-0": [
      {
        "topic": "AWSKafkaTopic",
        "partition": 0,
        "offset": 0,
        "timestamp": 1595035749700,
        "timestampType": "CREATE_TIME",
        "key": "OGQ1NTk2YjQtMTgxMy00MjM4LWIyNGItNmRhZDhlM2QxYzBj",
        "value": "OGQ1NTk2YjQtMTgxMy00MjM4LWIyNGItNmRhZDhlM2QxYzBj",
        "headers": [
          {
            "headerKey": "aGVhZGVyVmFsdWU="
          }
        ]
      }
    ]
  }
}
```

## Response

## Libraries

Typed Lambda handlers by Language

- [Typescript - MSKEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/msk.d.ts) - NPM `@types/aws-lambda`

### Code examples

- [Amazon MSK AWS Lambda Integration Lab - Code](https://github.com/aws-samples/integration-sample-lambda-msk)

## Documentation

- [Using Lambda with Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
- [Using Amazon MSK as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-msk-as-an-event-source-for-aws-lambda/)
