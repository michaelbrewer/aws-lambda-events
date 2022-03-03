# Apache Kafka

Lambda internally polls for new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the messages in batches and provides these to your function as an event payload. The maximum batch size is configurable. (The default is 100 messages.)

## Request

!!! NOTE
      Shares the same structure as [Amazon MSK](./amazon-msk.md), except for the eventSource field is set to "aws:SelfManagedKafka".

```json title="Self managed kafka example"
{
   "eventSource":"aws:SelfManagedKafka",
   "bootstrapServers":"b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
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

## Response

## Resources

- [Go - KafkaEvent](https://github.com/aws/aws-lambda-go/blob/main/events/kafka.go)
- [Java - KafkaEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/KafkaEvent.java)

## Documentation

- [Using Lambda with self-managed Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)
- [Using self-hosted Apache Kafka as an event source for AWS Lambda](https://aws.amazon.com/blogs/compute/using-self-hosted-apache-kafka-as-an-event-source-for-aws-lambda/)
