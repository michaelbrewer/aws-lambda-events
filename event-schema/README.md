# AWS Lambda Publish Sharable Events

## Installation

With pip installed, run: `pip install aws-lambda-publish-shared-event`

## Usage

Once installed run `publish-shared-event --help` for the list of commands.

Listing supported events for cognito user pool:

```
./publish-shared-event --filtered-list cognito-user
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

```
./publish-shared-event -e ses/ses.json -f full-lambda-name -r us-east-1
```

Using the interactive cli tool:

```
./publish-shared-event
Lambda Name: <Full Lambda Name>
Select Event:
* alb/alb.json
    alexa/alex-smart-home-skill-v1.json
    alexa/alex-smart-home-skill-v3.json
    amazon-config/amazon-config.json
    ...
```