---
title: S3 Batch
---

# S3 Batch Operations

When the batch job starts, Amazon S3 invokes the Lambda function synchronously for each object in the manifest. The event parameter includes the names of the bucket and the object.

## Request

```json title="Example Amazon S3 batch request event"
{
   "invocationSchemaVersion":"1.0",
   "invocationId":"YXNkbGZqYWRmaiBhc2RmdW9hZHNmZGpmaGFzbGtkaGZza2RmaAo",
   "job":{
      "id":"f3cc4f60-61f6-4a2b-8a21-d07600c373ce"
   },
   "tasks":[
      {
         "taskId":"dGFza2lkZ29lc2hlcmUK",
         "s3Key":"customerImage1.jpg",
         "s3VersionId":"1",
         "s3BucketArn":"arn:aws:s3:us-east-1:0123456788:examplebucket"
      }
   ]
}
```

## Response

`resultCode` is the result of the Lambda function.
: `Succeeded`, `TemporaryFailure` or `PermanentFailure`

```json title="Example Amazon S3 batch response"
{
  "invocationSchemaVersion": "1.0",
  "treatMissingKeysAs" : "PermanentFailure",
  "invocationId" : "YXNkbGZqYWRmaiBhc2RmdW9hZHNmZGpmaGFzbGtkaGZza2RmaAo",
  "results": [
    {
      "taskId": "dGFza2lkZ29lc2hlcmUK",
      "resultCode": "Succeeded",
      "resultString": "["Alice", "Bob"]"
    }
  ]
}
```

## Resources

- [S3 Batch - Typescript](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/s3-batch.d.ts) - NPM `@types/aws-lambda`
- [S3 Batch - Go](https://github.com/aws/aws-lambda-go/blob/main/events/s3_batch_job.go) - `github.com/aws/aws-lambda-go/events`
- [S3BatchEvent - Java](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/S3BatchEvent.java) - Maven `aws-lambda-java-events`
- [S3BatchJobEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/s3_batch_job.rs) - Crate `aws-lambda-events`
- The `serverless-s3-batch` plugin is designed to make it easy to work with S3 Batch operations. NPM `serverless-s3-batch`

## Documentation

- [Using AWS Lambda with Amazon S3 batch operations](https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html)
- [S3 Batch - Invoke AWS Lambda function](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html)
- [A Guide to S3 Batch on AWS](https://www.alexdebrie.com/posts/s3-batch/)
