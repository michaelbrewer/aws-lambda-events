---
title: WorkMail
description: Amazon WorkMail
---

# Amazon WorkMail

Can be configured to invoke your function synchrously (Use this configuration to modify email content, and to control inbound or outbound email flow for use cases such as blocking delivery of sensitive email messages, removing attachment, adding disclaimers, and so on.) or asynchrously (This configuration does not affect email delivery and is used for tasks such as collecting metrics for inbound or outbound email messages.).

## Limits

Payload limit

- Payload size limit 128 KB, before being trancated

Synchronous Run Lambda action limits

- Lambda functions must respond within **15 seconds**, or be treated as failed invocations.
- Lambda function **responses up to 256 KB** are allowed.
- Up to **10 unique actions** are allowed in the response. Actions greater than 10 are subject to the configured Fallback action.
- Up to **500 recipients** are allowed for outbound Lambda functions.
- The **maximum value for Rule timeout is 240 minutes**. If the minimum value of 0 is configured, there are no retries before Amazon WorkMail applies the fallback action.

## Request

### Request structure

```json
--8<-- "docs/events/work-mail/work-mail.json"
```

### Request fields

`summaryVersion` (String)
: AWS WorkMail Message Summary Version

`mailFrom` (Object)
: Mail from email address

`recipients` (List)
: List of all of the email recipients

`sender` (Object)
: Sender email address

`subject` (String)
: Email subject (Truncated to first 256 chars)"

`messageId` (String)
: Message id for retrieval using workmail flow API

`invocationId` (String)
: Id of this Lambda invocation. Useful for detecting retries and avoiding duplication

`flowDirection` (String)
: Indicating direction of email flow. Value is either "INBOUND" or "OUTBOUND"

`truncated` (Boolean)
: Boolean indicating if any field in message was truncated due to size limitations

### Getting the correlation id

JSON path to correlation id: `invocationId`

### Generating sample events

```shell
sam local generate-event workmail email
```

## Response

Response format only applies to synchronous invocations.

### Response schema

```json title="Synchronous Run Lambda response schema"
{
      "actions": [                          
      {
        "action" : {
          "type": "string",
          "parameters": { various }
        },
        "recipients": list of strings,      
        "allRecipients": boolean            
      }
    ]
}
```

`actions` (Array)
: Required, should contain at least 1 list element

`type` (String)
: Required. Can be "BOUNCE", "DROP" or "DEFAULT"

`parameters` (String)
: Optional. For bounce, `various` can be `{"bounceMessage": "message that goes in bounce mail"}`

`recipients` (Optional, list of strings)
: Optional. Indicates list of recipients for which this action applies

`allRecipients` (Optional, boolean)
: Optional. Indicates whether this action applies to all recipients

### Response examples

```json title="Example bounce response"
{
  "actions": [
    {
      "action": {
        "type": "BOUNCE",
        "parameters": {
          "bounceMessage": "Email in breach of company policy."
        }
      },
      "allRecipients": true
    }
  ]
}
```

```json title="Example response"
{
  "actions": [
    {
      "action": {
        "type": "DEFAULT"
      },
      "allRecipients": true
    },
    {
      "action": {
        "type": "DROP"
      },
      "recipients": [
        "drop-recipient@example.com"
      ]
    }
  ]
}
```

## Resources

- [GitHub - Amazon WorkMail Lambda Templates - Python](https://github.com/aws-samples/amazon-workmail-lambda-templates) - Serverless applications for Amazon WorkMail.

## Documentation

- [Configuring AWS Lambda for Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html)
