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
{
  "directive": {
    "header": {
      "namespace": "Alexa.Discovery",
      "name": "Discover",
      "payloadVersion": "3",
      "messageId": "1bd5d003-31b9-476f-ad03-71d471922820"
    },
    "payload": {
      "scope": {
        "type": "BearerToken"
      }
    }
  }
}
```

```json title="Example Alexa smart home event version 1"
{
  "header": {
    "payloadVersion": "1",
    "namespace": "Control",
    "name": "SwitchOnOffRequest"
  },
  "payload": {
    "switchControlAction": "TURN_ON",
    "appliance": {
      "additionalApplianceDetails": {
        "key2": "value2",
        "key1": "value1"
      },
      "applianceId": "sampleId"
    },
    "accessToken": "sampleAccessToken"
  }
}
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

## Libraries

Lambda handlers by Language

- [Python SDK](https://github.com/alexa/alexa-skills-kit-sdk-for-python)
- [Python - alexa smart home example](https://github.com/alexa/alexa-smarthome/tree/master/sample_lambda/python)
- [NodeJS](https://github.com/alexa/alexa-skills-kit-sdk-for-nodejs)
- [Java SDK](https://github.com/alexa/alexa-skills-kit-sdk-for-java)
- [Serverless - Alexa Smart Home](https://www.serverless.com/framework/docs/providers/aws/events/alexa-smart-home)

## Documentation

- [Using AWS Lambda with Alexa](https://docs.aws.amazon.com/lambda/latest/dg/services-alexa.html){target="_blank"}
- [Host a Custom Skill as an AWS Lambda Function](https://developer.amazon.com/en-US/docs/alexa/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html){target="_blank"}
- [Alexa Smart Home - Workshop](https://alexaworkshop.com/en/smart-home.html)
