# Amazon WorkMail

Can be invoked synchrously or asynchrously.

## Input

```json
{
    "summaryVersion": "2018-10-10",
    "envelope": {
        "mailFrom" : {
            "address" : "from@example.com"
        },
        "recipients" : [
           { "address" : "recipient1@example.com" },
           { "address" : "recipient2@example.com" }
        ]
    },
    "sender" : {
        "address" :  "sender@example.com"
    },
    "subject" : "Hello From Amazon WorkMail!",
    "messageId": "00000000-0000-0000-0000-000000000000",
    "invocationId": "00000000000000000000000000000000",
    "flowDirection": "INBOUND",
    "truncated": false
}
```

## Output

### Synchronous Run Lambda response schema

```json
{
      'actions': [                          
      {
        'action' : {                       
          'type': 'string',                 
          'parameters': { various }       
        },
        'recipients': list of strings,      
        'allRecipients': boolean            
      }
    ]
}
```

## Libraries

## Reference Docs
