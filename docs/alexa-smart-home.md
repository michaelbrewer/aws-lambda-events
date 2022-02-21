---
title: Alexa Smart Home
---

# Alexa Smart Home

Event-driven, synchronous invocation

## Input

### Generating sample events via SAM CLI

```shell
sam local generate-event alexa-smart-home smart-home-control-turn-off-request
sam local generate-event alexa-smart-home smart-home-control-turn-on-request
```

### Event Example

```json title="Example Alexa smart home event"
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

!!! TODO
    Still need to verify response structure

```json
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

## Reference Docs

- [Using AWS Lambda with Alexa](https://docs.aws.amazon.com/lambda/latest/dg/services-alexa.html){target="_blank"}
- [Host a Custom Skill as an AWS Lambda Function](https://developer.amazon.com/en-US/docs/alexa/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html){target="_blank"}
- [Alexa Smart Home - Workshop](https://alexaworkshop.com/en/smart-home.html)
