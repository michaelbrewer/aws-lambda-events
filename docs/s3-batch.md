# S3 Batch

When the batch job starts, Amazon S3 invokes the Lambda function synchronously for each object in the manifest. The event parameter includes the names of the bucket and the object.

## Input

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

## Libraries

- [S3 Batch - Typescript](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/s3-batch.d.ts) - NPM `@types/aws-lambda`

## Reference Docs

- [Using AWS Lambda with Amazon S3 batch operations](https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html)
- [S3 Batch - Invoke AWS Lambda function](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html)
