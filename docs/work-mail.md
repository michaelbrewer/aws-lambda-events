# Amazon WorkMail

Can be invoked synchrously or asynchrously.

## Input

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

## Output

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

## Reference Docs

- [Configuring AWS Lambda for Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html)
