---
title: SES
description: The Lambda action calls your code through a Lambda function and, optionally, notifies you through Amazon SNS.
---

# AWS SES - Receiving emails

The Lambda action calls your code through a Lambda function and, optionally, notifies you through Amazon SNS.

**Invocation type**, the invocation type of the Lambda function. An invocation type of `RequestResponse` means that the execution of the function results in an immediate response. An invocation type of Event means that the function is invoked asynchronously. We recommend that you use Event invocation type unless synchronous execution is required for your use case..

Requirements

- The Lambda function that you choose must be in the same AWS Region as the Amazon SES endpoint that you use to receive email.
- The Amazon SNS topic that you choose must be in the same AWS Region as the Amazon SES endpoint that you use to receive email.

## Limits

- There is a 30-second timeout on `RequestResponse` invocations.
- Not available in all regions support [receiving emails](https://docs.aws.amazon.com/ses/latest/dg/regions.html#region-receive-email){target=_blank}

| Region Name            | Email Receiving Endpoint              |
|------------------------|---------------------------------------|
| US East (N. Virginia)  | inbound-smtp.us-east-1.amazonaws.com  |
| US West (Oregon)       | inbound-smtp.us-west-2.amazonaws.com  |
| Europe (Ireland)       | inbound-smtp.eu-west-1.amazonaws.com  |

## Soft Limits

| Resource                  | Default quota | Description                                                                                   |
|---------------------------|---------------|-----------------------------------------------------------------------------------------------|
| Maximum message size (MB) | 30            | The maximum message size that can be sent to your identity and stored in an Amazon S3 bucket. |

## Request

### Generating sample event

Via [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html){target=_blank} you can generate sample
events

```shell
# Get help via following command
sam local generate-event ses email-receiving -h
# Generate event do custom region
sam local generate-event ses email-receiving  --region us-west-1  --dns-suffix us-west-1.amazonaws.com
```

### Getting the correlation id

JSON path to correlation id: `Records[*].mail.messageId`

### Request fields

`Records` - array of Amazon SES events

`eventSource` (String)
: The AWS service from which the SES event record originated. For SES, this is `aws:ses`

`eventVersion` (String)
: The eventVersion key value contains a major and minor version in the form <major>.<minor>.

`mail` (Object)
: The mail object contains the email message.

`mail.timestamp` (String)
: String that contains the time at which the email was received, in ISO8601 format.

`mail.source` (String)
: String that contains the email address (specifically, the envelope MAIL FROM address)
that the email was sent from.

`mail.messageId` (String)
: String that contains the unique ID assigned to the email by Amazon SES.
If the email was delivered to Amazon S3, the message ID is also the Amazon S3 object key that was
used to write the message to your Amazon S3 bucket.

`mail.destination` (List of strings)
: A complete list of all recipient addresses (including To: and CC: recipients)
from the MIME headers of the incoming email.

`mail.headersTruncated` (Boolean)
: String that specifies whether the headers were truncated in the notification, which will happen
if the headers are larger than 10 KB. Possible values are true and false.

`mail.headers` (Object)
: A list of Amazon SES headers and your custom headers. Each header in the list has a name field and a value field

`mail.commonHeaders` (Object)
: A list of headers common to all emails. Each header in the list is composed of a name and a value.

`commonHeaders.returnPath` (String)
: The values in the Return-Path header of the email.

`commonHeaders.from` (String)
: The values in the From header of the email.

`commonHeaders.date` (String)
: The date and time when Amazon SES received the message.

`commonHeaders.to` (List of strings)
: The values in the To header of the email.

`commonHeaders.messageId` (String)
: The ID of the original message.

`commonHeaders.subject` (String)
: The value of the Subject header for the email.

`commonHeaders.cc` (Optional, List of strings)
: The values in the CC header of the email.

`commonHeaders.bcc` (Optional, List of strings)
: The values in the BCC header of the email.

`commonHeaders.sender` (Optional, list of strings)
: The values in the Sender header of the email.

`commonHeaders.replyTo` (Optional, list of strings)
: The values in the replyTo header of the email.

`receipt` (Object)
: The receipt object contains information about the email message.

`receipt.timestamp` (String)
: String that specifies the date and time at which the action was triggered, in ISO 8601 format.

`receipt.processingTimeMillis` (Integer)
: String that specifies the period, in milliseconds, from the time Amazon SES received the message
to the time it triggered the action.

`receipt.recipients` (List of strings)
: A list of recipients (specifically, the envelope RCPT TO addresses) that were matched by the
active receipt rule. The addresses listed here may differ from those listed by the destination
field in the mail object.

`receipt.spamVerdict` (Object)
: Object that indicates whether the message is spam.
Possible values: `PASS`, `FAIL`, `GRAY`, `PROCESSING_FAILED`, `DISABLED`

`receipt.virusVerdict` (Object)
: Object that indicates whether the message contains a virus.
Possible values: `PASS`, `FAIL`, `GRAY`, `PROCESSING_FAILED`, `DISABLED`

`receipt.spfVerdict` (Object)
: Object that indicates whether the Sender Policy Framework (SPF) check passed.
Possible values: `PASS`, `FAIL`, `GRAY`, `PROCESSING_FAILED`, `DISABLED`

`receipt.dkimVerdict` (Object)
: Object that indicates whether the DomainKeys Identified Mail (DKIM) check passed
Possible values: `PASS`, `FAIL`, `GRAY`, `PROCESSING_FAILED`, `DISABLED`

`receipt.dmarcVerdict` (Object)
: Object that indicates whether the Domain-based Message Authentication, Reporting & Conformance (DMARC) check passed.
Possible values: `PASS`, `FAIL`, `GRAY`, `PROCESSING_FAILED`, `DISABLED`

`receipt.dmarcPolicy` (String)
: ndicates the Domain-based Message Authentication, Reporting & Conformance (DMARC) settings for
the sending domain. This field only appears if the message fails DMARC authentication.
Possible values for this field are: `none`, `quarantine`, `reject`

`receipt.action` (Object)
: Object that encapsulates information about the action that was executed.

`receipt.action.type` (String)
: The type of action that was executed. Possible values are `S3`, `SNS`, `Bounce`, `Lambda`, `Stop`, and `WorkMail`

`receipt.action.topicArn` (Optional, String)
: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. You can find the ARN of a topic by using the ListTopics operation in Amazon SNS.

`receipt.action.functionArn` (String)
: String that contains the ARN of the Lambda function that was triggered.
Present only for the Lambda action type.

### Example event

```json title="Example Amazon SES message event"
--8<-- "docs/events/ses/ses.json"
```

## Response

Response when doing a synchronous `RequestResponse` invocations must be in the follow format 

`disposition` (String)

- `STOP_RULE` - No further actions in the current receipt rule will be processed, but further receipt rules can be processed.
- `STOP_RULE_SET` - No further actions or receipt rules will be processed.
- `CONTINUE` - This means that further actions and receipt rules can be processed.

```json
{
  "disposition": "STOP_RULE_SET"
}
```

## Resources

Typing and utility class

- [Typescript - SESEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/ses.d.ts) - NPM package: `@types/aws-lambda`
- [Go - SimpleEmailEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_SES.md) - `github.com/aws/aws-lambda-go/events`
- [Python - SESEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#s3-object-lambda) - PIP package: `aws-lambda-powertools`
- [DotNet - SimpleEmailEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.SimpleEmailEvents) - NuGet package: `Amazon.Lambda.SimpleEmailEvents`
- [Rust - SimpleEmailEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/ses.rs)

Full solutions

- [NodeJS - AWS Lambda SES Email Forwarder](https://github.com/arithmetric/aws-lambda-ses-forwarder) - A Node.js script for AWS Lambda that uses the inbound/outbound capabilities of AWS Simple Email Service (SES) to run a "serverless" email forwarding service.

Code examples

- [Serverless Framework - node - email receiving](https://github.com/serverless/examples/tree/master/aws-node-ses-receive-email-header){target=_blank}

### Example

Example use case of filtering incoming emails by subject and forwarding to a different email address.

![AWS SES Diagram](./media/aws-ses-example-light.png#gh-light-mode-only)
![AWS SES Diagram](./media/aws-ses-example-dark.png#gh-dark-mode-only)

CDK infrastucture code setting up the receipt rules

```kotlin title="CDK code for receipt rules"
ReceiptRuleSet(
  this,
  "RecipientRuleSet",
  ReceiptRuleSetProps
    .builder()
    .receiptRuleSetName("RevieveReceipt-$namespace")
    .dropSpam(true)
    .rules(
      listOf(
        ReceiptRuleOptions
          .builder()
          // List of recipients to forward
          .recipients(listOf(recipientEmail))
          .scanEnabled(true)
          .actions(
            listOf(
                // Filter out emails by subject line
                Lambda(
                    LambdaProps
                        .builder()
                        .function(subjectFilterLambda)
                        .invocationType(LambdaInvocationType.REQUEST_RESPONSE)
                        .build()
                ),
                // Save email to S3
                S3(
                    S3Props
                        .builder()
                        .bucket(emailBucket)
                        .objectKeyPrefix("ar")
                        .build()
                ),
                // Forward email to recipients
                Lambda(
                    LambdaProps
                        .builder()
                        .function(receiveLambda)
                        .invocationType(LambdaInvocationType.EVENT)
                        .build()
                )
            )
          )
          .build()
      )
    )
    .build()
)
```

Example subject filtering Lambda

```python title="subjectFilterLambda.py"
import os
from aws_lambda_powertools import Tracer, Logger

tracer = Tracer(service="example-ses-filter")
logger = Logger(service="example-ses-filter")
allow_mail_source = os.environ["MAIL_SOURCE"]
allow_subjects = os.environ["MAIL_SUBJECTS"].split(";")


@tracer.capture_lambda_handler
@logger.inject_lambda_context
def lambda_handler(event: dict, _) -> dict:
    """Simple Lambda that filters out emails that does not match `MAIL_SOURCE` and `MAIL_SUBJECTS`"""

    records = event.get("Records")
    if records is None or len(records) == 0:
        return {"disposition": "STOP_RULE_SET"}

    record = records[0]
    mail = record["ses"]["mail"]

    mail_source: str = mail["source"]
    if mail_source != allow_mail_source:
        logger.info("SKIP(source not handled) mail_source: %s", mail_source)
        return {"disposition": "STOP_RULE_SET"}

    mail_subject: str = mail["commonHeaders"]["subject"]
    tracer.put_metadata(key="mail_subject", value=mail_subject)
    if any(allow_subject.strip() in mail_subject for allow_subject in allow_subjects):
        return {"disposition": "CONTINUE"}

    logger.info("SKIP(subject not handled) mail_subject: %s", mail_subject)
    return {"disposition": "STOP_RULE_SET"}
```

## Documentation

- [Using AWS Lambda with Amazon SES](https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html){target=_blank}
- [SES - Invoke Lambda function action](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html){target=_blank}
- [Blog - Replace traditional email mailbox polling with real-time reads using Amazon SES and Lambda](https://aws.amazon.com/blogs/messaging-and-targeting/replace-traditional-email-mailbox-polling-with-real-time-reads-using-amazon-ses-and-lambda/){target=_blank}
- [Blog - Forward Incoming Email to an External Destination](https://aws.amazon.com/blogs/messaging-and-targeting/forward-incoming-email-to-an-external-destination/){target=_blank}
- [Blog - Receive and Process Incoming Email with Amazon SES](https://aws.amazon.com/blogs/aws/new-receive-and-process-incoming-email-with-amazon-ses/){target=_blank}
