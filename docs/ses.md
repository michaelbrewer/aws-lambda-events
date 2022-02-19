# SES

Event-driven, asynchronous invocation. The service can then invoke your Lambda function by passing in the incoming
email event, which in reality is an Amazon SES message in an Amazon SNS event, as a parameter.

!!! Note
    There is a 30-second timeout on RequestResponse invocations.

## Input

### Generating sample events via SAM CLI

```shell
sam local generate-event ses email-receiving
```

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

`commonHeaders.cc` (List of strings)
: The values in the CC header of the email.

`commonHeaders.bcc` (List of strings)
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

`receipt.action.topicArn` (String)
: String that contains the Amazon Resource Name (ARN) of the Amazon SNS topic to which the
notification was published

`receipt.action.functionArn` (String)
: String that contains the ARN of the Lambda function that was triggered.
Present only for the Lambda action type.

### Example event

```json title="Example Amazon SES message event"
{
  "Records": [
    {
      "eventVersion": "1.0",
      "ses": {
        "mail": {
          "commonHeaders": {
            "from": [
              "Jane Doe <janedoe@example.com>"
            ],
            "to": [
              "johndoe@example.com"
            ],
            "returnPath": "janedoe@example.com",
            "messageId": "<0123456789example.com>",
            "date": "Wed, 7 Oct 2015 12:34:56 -0700",
            "subject": "Test Subject"
          },
          "source": "janedoe@example.com",
          "timestamp": "1970-01-01T00:00:00.000Z",
          "destination": [
            "johndoe@example.com"
          ],
          "headers": [
            {
              "name": "Return-Path",
              "value": "<janedoe@example.com>"
            },
            {
              "name": "Received",
              "value": "from mailer.example.com (mailer.example.com [203.0.113.1]) by inbound-smtp.us-west-2.amazonaws.com with SMTP id o3vrnil0e2ic for johndoe@example.com; Wed, 07 Oct 2015 12:34:56 +0000 (UTC)"
            },
            {
              "name": "DKIM-Signature",
              "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=example.com; s=example; h=mime-version:from:date:message-id:subject:to:content-type; bh=jX3F0bCAI7sIbkHyy3mLYO28ieDQz2R0P8HwQkklFj4=; b=sQwJ+LMe9RjkesGu+vqU56asvMhrLRRYrWCbV"
            },
            {
              "name": "MIME-Version",
              "value": "1.0"
            },
            {
              "name": "From",
              "value": "Jane Doe <janedoe@example.com>"
            },
            {
              "name": "Date",
              "value": "Wed, 7 Oct 2015 12:34:56 -0700"
            },
            {
              "name": "Message-ID",
              "value": "<0123456789example.com>"
            },
            {
              "name": "Subject",
              "value": "Test Subject"
            },
            {
              "name": "To",
              "value": "johndoe@example.com"
            },
            {
              "name": "Content-Type",
              "value": "text/plain; charset=UTF-8"
            }
          ],
          "headersTruncated": false,
          "messageId": "o3vrnil0e2ic28tr"
        },
        "receipt": {
          "recipients": [
            "johndoe@example.com"
          ],
          "timestamp": "1970-01-01T00:00:00.000Z",
          "spamVerdict": {
            "status": "PASS"
          },
          "dkimVerdict": {
            "status": "PASS"
          },
          "processingTimeMillis": 574,
          "action": {
            "type": "Lambda",
            "invocationType": "Event",
            "functionArn": "arn:aws:lambda:us-west-2:012345678912:function:Example"
          },
          "spfVerdict": {
            "status": "PASS"
          },
          "virusVerdict": {
            "status": "PASS"
          }
        }
      },
      "eventSource": "aws:ses"
    }
  ]
}
```

## Response

`disposition` (String)

- `STOP_RULE` - No further actions in the current receipt rule will be processed, but further receipt rules can be processed.
- `STOP_RULE_SET` - No further actions or receipt rules will be processed.
- `CONTINUE` - This means that further actions and receipt rules can be processed.

```json
{
  "disposition": "STOP_RULE_SET"
}
```

## Libraries

- [DotNet - SimpleEmailEvent](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.SimpleEmailEvents) - NuGet package: `Amazon.Lambda.SimpleEmailEvents`
- [Typescript - SESEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/ses.d.ts) - NPM package: `@types/aws-lambda`
- [Python - SESEvent](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#s3-object-lambda) - PIP package: `aws-lambda-powertools`
- [Go - SimpleEmailEvent](https://github.com/aws/aws-lambda-go/blob/main/events/README_SES.md) - `github.com/aws/aws-lambda-go/events`
- [Rust - SimpleEmailEvent](https://github.com/LegNeato/aws-lambda-events/blob/master/aws_lambda_events/src/generated/ses.rs)

## Reference Docs

- [Using AWS Lambda with Amazon SES](https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html)
- [SES - Invoke Lambda function action](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html)
