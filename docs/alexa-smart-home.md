# Alexa Smart Home

Event-driven, synchronous invocation

## Request

### Generating sample events

```shell
sam local generate-event alexa-smart-home smart-home-control-turn-off-request
sam local generate-event alexa-smart-home smart-home-control-turn-on-request
```

### Event Example

```json title="Smart Home Skill V3 request"
--8<-- "docs/events/alexa/alex-smart-home-skill-v3.json"
```

```json title="Example Alexa smart home event version 1"
--8<-- "docs/events/alexa/alex-smart-home-skill-v1.json"
```

## Response

```json title="Smart Home Skill V3 response"
{
  "event": {
    "header": {
      "namespace": "Alexa.Discovery",
      "name": "Discover.Response",
      "messageId": "b5a1d155-3a97-479e-80fa-913b4afee758",
      "payloadVersion": "3"
    },
    "payload": {
      "endpoints": [
        {
          "capabilities": [
            {
              "type": "AlexaInterface",
              "interface": "Alexa",
              "version": "3"
            },
            {
              "type": "AlexaInterface",
              "interface": "Alexa.PowerController",
              "version": "3",
              "properties": {
                "supported": [
                  {
                    "name": "powerState"
                  }
                ],
                "proactivelyReported": false,
                "retrievable": false
              }
            }
          ],
          "description": "Sample Endpoint Description",
          "displayCategories": [
            "OTHER"
          ],
          "endpointId": "sample-switch-01",
          "friendlyName": "Sample Switch",
          "manufacturerName": "Sample Manufacturer"
        }
      ]
    }
  }
}
```

```json title="legacy v1.0"
{
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "SSML",
      "ssml": "<speak>Welcome to Premium Facts Sample. To hear a random fact you can say 'Tell me a fact', or to hear about the premium categories for purchase, say 'What can I buy'.  For help, say , 'Help me'... So, What can I help you with?</speak>"
    },
    "reprompt": {
      "outputSpeech": {
        "type": "SSML",
        "ssml": "<speak>I didn't catch that. What can I help you with?</speak>"
      }
    },
    "shouldEndSession": false
  },
  "userAgent": "ask-node/2.3.0 Node/v8.10.0",
  "sessionAttributes": {}
}
```

## Resources

Lambda examples by Language

- [Skill Sample : Smarthome Switch (Node.js)](https://github.com/alexa-samples/skill-sample-nodejs-smarthome-switch)
- [Skill Sample : Smarthome Switch (Python)](https://github.com/alexa-samples/skill-sample-python-smarthome-switch)
- [Skill Sample : Smarthome Switch (Java)](https://github.com/alexa-samples/skill-sample-java-smarthome-switch)
- [Skill Sample : Smarthome Switch (C#)](https://github.com/alexa-samples/skill-sample-csharp-smarthome-switch)
- [Python - alexa smart home example](https://github.com/alexa/alexa-smarthome/tree/master/sample_lambda/python)
- [Serverless - Alexa Smart Home](https://www.serverless.com/framework/docs/providers/aws/events/alexa-smart-home)

## Documentation

- [Using AWS Lambda with Alexa](https://docs.aws.amazon.com/lambda/latest/dg/services-alexa.html){target="_blank"}
- [Host a Custom Skill as an AWS Lambda function](https://developer.amazon.com/en-US/docs/alexa/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html){target="_blank"}
- [Alexa Smart Home - Workshop](https://alexaworkshop.com/en/smart-home.html)
