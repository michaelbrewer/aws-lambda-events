---
description: List of general resources that could be used with all AWS Lambda by programming language
---

# General Resources

Some general resources around AWS Lambda event requests and responses.

## Libraries by language

List of general resources that could be used with all AWS Lambda by language.

- [Python - AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/){target="_blank"}
- [Java - AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-java/){target="_blank"}
- [Bref - Php](https://bref.sh/){target="_blank"} - php runtime and libraries
- [Go - AWS Lambda for Go](https://github.com/aws/aws-lambda-go){target="_blank"} - Event typing, Libraries, samples, and tools to help Go developers develop AWS Lambda functions.
- [Typescript - AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-typescript/latest/){target="_blank"}
- [Typescript - @types/aws-lambda](https://www.npmjs.com/package/@types/aws-lambda){target="_blank"} - NPM `@types/aws-lambda`
- [Rust - aws-lambda-rust-runtime](https://github.com/awslabs/aws-lambda-rust-runtime){target="_blank"} - runtime and framework and will soon include `aws_lambda_events` 
- [Rust - aws_lambda_events](https://github.com/LegNeato/aws-lambda-events){target="_blank"} - structs for most lambda events
- [Ruby - Jets](https://rubyonjets.com){target="_blank"} - Ruby Serverless Framework 

## Lambda shareable test events

Installing the cli tool

=== "Installing"

```script
pip install aws-lambda-publish-shared-event
```

Examples of running the cli tool.

=== "Interactive example"

Running as an interactive cli tool:

```script
publish-shared-event
Lambda Name: <Full Lambda Name>
Select Event:
* alb/alb.json
    alexa/alex-smart-home-skill-v1.json
    alexa/alex-smart-home-skill-v3.json
    amazon-config/amazon-config.json
    ...
```

=== "List of cognito user pull events"

Listing all the cognito user pull events:

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

=== "Using CLI arguments"

Publishing a `ses/ses.json` test event as a shareable event for the lambda function named `full-lambda-name`

```script
publish-shared-event -e ses/ses.json -f full-lambda-name -r us-east-1
```

**Ideaslog**

- [x] Prototyped example using `appsync-authorizer`
- [x] Generate schema from json examples in `docs/events` folder
- [x] Create Github issue for SAM CLI [Lambda shareable events](https://github.com/aws/aws-sam-cli/issues/3763)
- [x] Create Github issue for AWS CDK: [(aws-lambda): Lambda shareable events](https://github.com/aws/aws-cdk/issues/19471)
- [x] Create Github issue for Cloudformation [Lambda shareable events](https://github.com/aws-cloudformation/cloudformation-coverage-roadmap/issues/1113)
- [x] Complete extraction of sample events into `docs/events` folder (124 test events so far!!!)
- [x] Create the EventBridge `lambda-testevent-schemas` registry if it doesn't exist
- [x] Support relative paths to allow users to bring their own events
- [x] Support create or update of a test event
- [x] Add cli args
    - [x] `--help` - prints cli help
    - [x] `--list` - prints the list of support event sources
    - [x] `--filtered-list=<begins-with-filter>` - prints a filtered list of support event sources
    - [x] `-e=<event_source_name>` - set the event source (supported)
    - [x] `-e=<event_source_name>` - set the event source (relative)
    - [x] `-f=<function-name>` - set the aws lambd function name
    - [x] `-r=<region>` - override the aws region
    - [ ] `--template-var-name=<template-var-value>` - override the template variable name (BONUS)
- [x] UI: Drop _OR_ Extend the console ui and use [textual](https://github.com/Textualize/textual)
    - [x] UI: Auto discover the different lambdas and show a list or do code completion.
    - [x] UI: Show list of supported event sources. [event source examples](https://github.com/michaelbrewer/aws-lambda-events/tree/main/docs/events)
- [ ] Add some templated parameters for the event source, to allow for flexibility. (BONUS)
- [x] Publish as pip package (if SAM or CDK support does not progress)
    - [x] Setup a cli packaged (`setup.py`?)
    - [x] Package the events
    - [x] Publish the package to pip [aws-lambda-publish-shared-event](https://pypi.org/project/aws-lambda-publish-shared-event/)

**Documentation**

- [AWS Lambda Shareable test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html#creating-shareable-events)
