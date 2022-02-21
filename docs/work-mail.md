---
title: WorkMail
description: Amazon WorkMail
---

# Amazon WorkMail

Can be invoked synchrously or asynchrously.

## Limits

Payload size limit 128 KB, before being trancated

## Input

### Input fields

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
: Id of this lambda invocation. Useful for detecting retries and avoiding duplication

`flowDirection` (String)
: Indicating direction of email flow. Value is either "INBOUND" or "OUTBOUND"

`truncated` (Boolean)
: Boolean indicating if any field in message was truncated due to size limitations

### Input event structure

```json
{
  "summaryVersion": "2018-10-10",
  "envelope": {
    "mailFrom": {
      "address": "from@example.com"
    },
    "recipients": [
      {
        "address": "recipient1@example.com"
      },
      {
        "address": "recipient2@example.com"
      }
    ]
  },
  "sender": {
    "address": "sender@example.com"
  },
  "subject": "Hello From Amazon WorkMail!",
  "messageId": "00000000-0000-0000-0000-000000000000",
  "invocationId": "00000000000000000000000000000000",
  "flowDirection": "INBOUND",
  "truncated": false
}
```

## Response

### Response fields

`actions` (Array)
: Required, should contain at least 1 list element

`type` (String)
: Required. Can be "BOUNCE", "DROP" or "DEFAULT"

`parameters` (String)
: Optional. For bounce, <various> can be `{"bounceMessage": "message that goes in bounce mail"}`

`recipients` (Optional, list of strings)
: Optional. Indicates list of recipients for which this action applies

`allRecipients` (Optional, boolean)
: Optional. Indicates whether this action applies to all recipients

### Synchronous Run Lambda response schema

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

## Libraries

- [Amazon WorkMail Lambda Templates - Python](https://github.com/aws-samples/amazon-workmail-lambda-templates)

## Reference Docs

- [Configuring AWS Lambda for Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html)
