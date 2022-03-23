# AWS Lambda Publish Sharable Events
[![codecov](https://codecov.io/gh/michaelbrewer/aws-lambda-events/branch/main/graph/badge.svg?token=J433NUHYNT)](https://codecov.io/gh/michaelbrewer/aws-lambda-events)
[![aws-lambda-publish-shared-event](https://github.com/michaelbrewer/aws-lambda-events/actions/workflows/python.yml/badge.svg)](https://github.com/michaelbrewer/aws-lambda-events/actions/workflows/python.yml)

## Installation

With pip installed, run: `pip install aws-lambda-publish-shared-event`

## Features

- Publish your locally defined tests
- Publish standard test events into the lambda console for over 100 different examples
- Set test name or use the test event file name
- List of supported test events

## Usage

Once installed run `publish-shared-event --help` for the list of commands.

Listing supported events for cognito user pool:

```script
publish-shared-event --filtered-list cognito-user
Filtered list of supported event sources:
cognito-user-pool/create-auth-challenge.json
cognito-user-pool/custom-email-sender.json
cognito-user-pool/custom-message.json
cognito-user-pool/define-auth-challenge.json
cognito-user-pool/post-authentication.json
cognito-user-pool/post-confirmation.json
cognito-user-pool/pre-authentication.json
cognito-user-pool/pre-signup.json
cognito-user-pool/pre-token-generation.json
cognito-user-pool/user-migration.json
cognito-user-pool/verify-auth-challenge-response.json
```

Publishing a `ses/ses.json` test event as a shareable event for the lambda function named `full-lambda-name`

```script
publish-shared-event -e ses/ses.json -f full-lambda-name -r us-east-1
```

Publishes a locally defined test event `events/yourOwnDefinedEvent.json` to the lambda console

```script
publish-shared-event -e events/yourOwnDefinedEvent.json -f your-function -r us-west-2
```

Publish two different tests with custom names.

> **NOTE:** Both tests must share the same schema

```script
publish-shared-event -n createCustomerPass -e eventOne.json -f full-lambda-name -r us-east-1
publish-shared-event -n createCustomerFailure -e eventTwo.json -f full-lambda-name -r us-east-1
```

Using the interactive cli tool:

```
publish-shared-event
Lambda Name: <Full Lambda Name>
Select Event:
* alb/alb.json
    alexa/alex-smart-home-skill-v1.json
    alexa/alex-smart-home-skill-v3.json
    amazon-config/amazon-config.json
    ...
```

## Resources

See [Lambda Events](https://lambda.101i.de/) for documentation on the different AWS Lambda event structures 
and see the official docs on the [AWS Lambda Shareable test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html#creating-shareable-events)
