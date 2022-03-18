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

Create initial [Amazon EventBridge (CloudWatch Events) schema registry](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-registry.html) for your Lambda functions.

```script
aws schemas create-registry --registry-name lambda-testevent-schemas --description "List of tests events for AWS Lambda" --tags comment=lambda-testevent-schemas
```

Setup the cli tool to create shared test events.

```script
git clone https://github.com/michaelbrewer/aws-lambda-events.git
cd aws-lambda-events/event-schema
make dev
```

Run the cli tool to create shared test events, currently just json files from `docs/events/` is supported eg: cloudformation/cloudformation-delete.json

```bash
./publish-shared-event.sh
Lambda Name: <Full Lambda Name>
Select Event:
 * alb/alb.json
   alexa/alex-smart-home-skill-v1.json
   alexa/alex-smart-home-skill-v3.json
   amazon-config/amazon-config.json
   ...
```

**Ideaslog**

- [x] Prototyped example using `appsync-authorizer`
- [x] Generate schema from json examples in `docs/events` folder
- [ ] Create Github issue for SAM CLI
- [ ] Complete extraction of sample events into `docs/events` folder
- [ ] Support relative paths
- [ ] Add cli args (`--e=<relative_path_to_event>`, `-f=<function-name>`, `-r=<region>`, `--template-var-name=<template-var-value>`)
- [ ] Add cli help (`publish-shared-event --help`)
- [ ] Drop _OR_ extend the ui to use [textual](https://github.com/Textualize/textual)
- [ ] Discover the different lambdas and show a list or do code completion.
- [x] Show list of supported event sources. [event source examples](https://github.com/michaelbrewer/aws-lambda-events/tree/main/docs/events)
- [ ] Offer some parameters for the event source. To allow for flexibility.
- [ ] Publish as pip package (if this makes sense)

**Documentation**

- [AWS Lambda Shareable test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html#creating-shareable-events)
