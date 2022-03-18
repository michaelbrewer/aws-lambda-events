# Kinesis Data Firehose

Event-driven, synchronous invocation. Kinesis Data Firehose can invoke your Lambda function to transform incoming source data and deliver the transformed data to destinations.

Kinesis Data Firehose is a streaming ETL solution. It is the easiest way to load streaming data into data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

## Limits

- Kinesis Data Firehose supports a Lambda invocation time of up to 5 minutes.

## Request

### Request Example

```json title="Example Amazon Kinesis Data Firehose message event"
--8<-- "docs/events/kinesis-firehose/kinesis-firehose-message.json"
```

### Getting the correlation id

JSON path to correlation id: `invocationId`

### Generating sample events

```shell
# To get the list of supported events to generate
sam local generate-event kinesis
# Various other events generated via SAM CLI
sam local generate-event kinesis kinesis-firehose
sam local generate-event kinesis streams-as-source
sam local generate-event kinesis syslog
sam local generate-event kinesis apachelog
```

## Response

### Response Fields

`recordId` (String)
: The record ID is passed from Kinesis Data Analytics to Lambda during the invocation. The transformed record must contain the same record ID. Any mismatch between the ID of the original record and the ID of the transformed record is treated as a data preprocessing failure.

`result` (String)
: The status of the data transformation of the record.
The possible values are:

- `Ok`: The record was transformed successfully. Kinesis Data Analytics ingests the record for SQL processing.
- `Dropped`: The record was dropped intentionally by your processing logic. Kinesis Data Analytics drops the record from SQL processing. The data payload field is optional for a Dropped record.
- `ProcessingFailed`: The record could not be transformed. Kinesis Data Analytics considers it unsuccessfully processed by your Lambda function and writes an error to the error stream. For more information about the error stream, see Error Handling. The data payload field is optional for a ProcessingFailed record.

`data` (String)
: The transformed data payload, after base64-encoding. Each data payload can contain multiple JSON documents if the application ingestion data format is JSON. Or each can contain multiple CSV rows (with a row delimiter specified in each row) if the application ingestion data format is CSV. The Kinesis Data Analytics service successfully parses and processes data with either multiple JSON documents or CSV rows within the same data payload.

`metadata` (Object, Optional)
: Optional used for [dynamic partitioning](https://aws.amazon.com/blogs/big-data/kinesis-data-firehose-now-supports-dynamic-partitioning-to-amazon-s3/){target="_blank"} containing `partitionKeys` map.

### Response Example

```json
{
  "records": [
    {
      "recordId": "49572672223665514422805246926656954630972486059535892482",
      "result": "Ok",
      "data": "SEVMTE8gV09STEQ=",
      "metadata": {
        "partitionKeys": {
          "customerId": "customerId",
          "year": "2017",
          "month": "01",
          "date": "01",
          "hour": "01",
          "minute": "01"
        }
      }
    }
  ]
}
```

## Resources

- [TypeScript - FirehoseTransformationEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/kinesis-firehose-transformation.d.ts) - NPM `@types/aws-lambda`
- [DotNet - KinesisFirehoseEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.KinesisFirehoseEvents) - NuGet `Amazon.Lambda.KinesisFirehoseEvents`
- [Java - KinesisFirehoseEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/KinesisFirehoseEvent.java)
- [Go - KinesisFirehoseEvent](https://github.com/aws/aws-lambda-go/blob/main/events/firehose.go)

AWS Samples

- [aws-serverless-stream-ingest-transform-load](https://github.com/aws-samples/aws-serverless-stream-ingest-transform-load)

### Code Examples

```csharp
public class Function
{

    public KinesisFirehoseResponse FunctionHandler(KinesisFirehoseEvent evnt, ILambdaContext context)
    {
        context.Logger.LogLine($"InvocationId: {evnt.InvocationId}");
        context.Logger.LogLine($"DeliveryStreamArn: {evnt.DeliveryStreamArn}");
        context.Logger.LogLine($"Region: {evnt.Region}");

        var response = new KinesisFirehoseResponse
        {
            Records = new List<KinesisFirehoseResponse.FirehoseRecord>()
        };

        foreach (var record in evnt.Records)
        {
            context.Logger.LogLine($"\tRecordId: {record.RecordId}");
            context.Logger.LogLine($"\t\tApproximateArrivalEpoch: {record.ApproximateArrivalEpoch}");
            context.Logger.LogLine($"\t\tApproximateArrivalTimestamp: {record.ApproximateArrivalTimestamp}");
            context.Logger.LogLine($"\t\tData: {record.DecodeData()}");

            // Transform data: For example ToUpper the data
            var transformedRecord = new KinesisFirehoseResponse.FirehoseRecord
            {
                RecordId = record.RecordId,
                Result = KinesisFirehoseResponse.TRANSFORMED_STATE_OK                    
            };
            transformedRecord.EncodeData(record.DecodeData().ToUpperInvariant());

            response.Records.Add(transformedRecord);
        }

        return response;
    }
}
```

## Documentation

- [Using AWS Lambda with Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html)
- [Preprocessing Data Using a Lambda Function](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/lambda-preprocessing.html)
- [Blog - Amazon Kinesis Firehose Data Transformation with AWS Lambda](https://aws.amazon.com/blogs/compute/amazon-kinesis-firehose-data-transformation-with-aws-lambda/)
- [Amazon Kinesis Data Firehose Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
- [Dynamic Partitioning in Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)
- [Blog - Kinesis Data Firehose now supports dynamic partitioning to Amazon S3](https://aws.amazon.com/blogs/big-data/kinesis-data-firehose-now-supports-dynamic-partitioning-to-amazon-s3/)
