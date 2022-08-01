# AWS Lambda Publish Sharable Events

[![Build status](https://github.com/michaelbrewer/aws-lambda-events/actions/workflows/python.yml/badge.svg)](https://github.com/michaelbrewer/aws-lambda-events/actions/workflows/python.yml)
[![Code Coverage](https://codecov.io/gh/michaelbrewer/aws-lambda-events/branch/main/graph/badge.svg?token=J433NUHYNT)](https://codecov.io/gh/michaelbrewer/aws-lambda-events)
[![Package version](https://img.shields.io/pypi/v/aws-lambda-publish-shared-event?color=%2334D058&label=pypi%20package)](https://pypi.org/project/aws-lambda-publish-shared-event/)
![Python version](https://img.shields.io/pypi/pyversions/aws-lambda-publish-shared-event.svg?color=%2334D058)

## Features

- Publish your locally defined test events to the Lambda Console (`publish-shared-event -e testEvent.json ..`)
- Publish 100 different examples (`publish-shared-event -e ses/ses.json ...`)
- Publish multiple events with the same schema structure for a single Lambda
- Set test name or use the test event file name (`publish-shared-event -n custom-name ...`)
- Get the list of built-in test events (`publish-shared-event --list`)
- Geneate a new test event (`generate-test-event ses/ses.json > event.json`)

## Installation

Recommended to install via pipx: `pipx install aws-lambda-publish-shared-event`, see the [pipx installation guide](https://pypa.github.io/pipx/installation/) for more.

Alternatively pip installed, run: `pip install aws-lambda-publish-shared-event`

## Usage

Once installed run `publish-shared-event --help` for the list of commands.

Listing supported events for cognito user pool:

```script
$ publish-shared-event --filtered-list cognito-user
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

Publishing a `ses/ses.json` test event as a shareable event for the Lambda function named `full-lambda-name`

```script
publish-shared-event -e ses/ses.json -f full-lambda-name -r us-east-1
```

Publishes a locally defined test event `events/yourOwnDefinedEvent.json` to the Lambda console

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

```script
$ publish-shared-event
Lambda Name: <Full Lambda Name>
Select Event:
* alb/alb.json
    alexa/alex-smart-home-skill-v1.json
    alexa/alex-smart-home-skill-v3.json
    amazon-config/amazon-config.json
    ...
```

Generate new local test event:

```script
generate-test-event ses/ses.json > event.json
```

## Resources

See [Lambda Events](https://lambda.101i.de/) for more documentation on the different AWS Lambda event structures 
and see the official docs on [AWS Lambda Shareable test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html#creating-shareable-events).

## Recent changes

### 0.17.0

- Bump deps for pick to 1.4.0

### 0.16.0

- Bump deps for pick to 1.3.0

### 0.15.0

- Add `--filtered-list` argument to `generate-test-event`

### 0.14.0

- Add `alexa-skills-kit` sample events

### 0.13.0

- Fix packaging to include `generate_test_event`

### 0.12.0

- Add `generate-test-event` support
- Add python 3.7 support

### 0.11.0

- Add support for python 3.8

### 0.10.0

- Add python 3.10 and dependabot
- Add security and linting
- Add coverage report

### 0.9.0

- Add long form cli arguments (`--region`, `--lambda-name`, `--event-name`)

### 0.8.0

- Update dependencies and clean up code
