# Alexa Skills

Event-driven, synchronous invocation

## Request

## Generating sameple events

```shell
sam local generate-event alexa-skills-kit end-session
sam local generate-event alexa-skills-kit intent-answer
sam local generate-event alexa-skills-kit intent-getnewfact
sam local generate-event alexa-skills-kit intent-mycoloris
sam local generate-event alexa-skills-kit intent-recipe
sam local generate-event alexa-skills-kit start-session
```

## Event Example

```json title="Amazon Alexa Intent Recipe Event"
--8<-- "docs/events/alexa-skills-kit/intent-recipe.json"
```

## Response

## Resources

Language SDK

- [Python SDK](https://github.com/alexa/alexa-skills-kit-sdk-for-python)
- [NodeJS SDK](https://github.com/alexa/alexa-skills-kit-sdk-for-nodejs)
- [Java SDK](https://github.com/alexa/alexa-skills-kit-sdk-for-java)

Sample projects

- [Python - skill-sample-python-fact](https://github.com/alexa-samples/skill-sample-python-fact)

## Documentation

- [Host a Custom Skill as an AWS Lambda Function](https://developer.amazon.com/en-US/docs/alexa/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html)
