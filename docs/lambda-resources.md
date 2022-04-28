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
- [Rust - aws_lambda_events](https://github.com/LegNeato/aws-lambda-events){target="_blank"} - structs for most Lambda events
- [Ruby - Jets](https://rubyonjets.com){target="_blank"} - Ruby Serverless Framework 

## Lambda shareable test events

With [AWS Lambda Shareable test events](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html#creating-shareable-events) you can now share test events with other AWS Lambda developers.

**Installing the cli `publish-shared-event` tool.**

Recommended to install via pipx, see the [pipx installation](https://pypa.github.io/pipx/installation/) guide for more.:

```script
pipx install aws-lambda-publish-shared-event
```

**Examples of running the cli tool.**

=== "Generate test event"

    Generates a new local test event:

    ```script
    generate-test-event ses/ses.json > event.json
    ```

=== "Interactive example"

    Running as an interactive cli tool:

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

=== "List of cognito user pull events"

    Listing all the cognito user pull events:

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

=== "Using CLI arguments"

    Publishing a `ses/ses.json` test event as a shareable event for the Lambda function named `full-lambda-name`

    ```script
    publish-shared-event -e ses/ses.json -f full-lambda-name -r us-east-1
    ```
