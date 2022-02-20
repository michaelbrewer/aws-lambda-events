# Cognito User Pool

## Common Input

Common attributes shared by all User Pool Lambda Trigger Events

`version` (String, required)
: The version number of your Lambda function. example `1`

`region` (String, required)
: The AWS region where the event was triggered. example `us-east-1`

`userPoolId` (String, required)
: The user pool ID for the user pool where the event occurred. example `us-east-1_1234567890`

`triggerSource` (String, required)
: The name of the event that triggered the Lambda function. See [User pool Lambda trigger sources](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html#cognito-user-identity-pools-working-with-aws-lambda-trigger-sources){target="_blank"} example `PreSignUp_SignUp`

`userName` (String, required)
: The username of the current user. example `testuser`

`callerContext` (Object, required)
: The caller context, with `awsSdkVersion` and `clientId`. example `{"clientId":"app_client_id","custom":{},"awsSdkVersion":"aws-sdk-js-2.6.4"}`

## Pre Sign-up

The pre sign-up Lambda function is triggered just before Amazon Cognito signs up a new user. It allows you to perform custom validation to accept or deny the registration request as part of the sign-up process.

- [Pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html)

### Pre Sign-up Input

`triggerSource` can be one of the following:

- `PreSignUp_SignUp` Pre sign-up.
- `PreSignUp_AdminCreateUser` Pre sign-up when an admin creates a new user.
- `PreSignUp_ExternalProvider` Pre sign-up with external provider

`userAttributes` (Object, required)
: One or more name-value pairs representing user attributes. The attribute names are the keys.

`validationData` (Object, required)
: One or more name-value pairs containing the validation data in the request to register a user.

`clientMetadata` (Object, optional)
: One or more key-value pairs that you can provide as custom input to the Lambda function that you specify for the pre sign-up trigger.

```json title="Pre Sign-up Request"
{
  "version": "string",
  "triggerSource": "PreSignUp_SignUp",
  "region": "us-east-1",
  "userPoolId": "string",
  "userName": "userName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "userAttributes": {
      "email": "user@example.com",
      "phone_number": "+12065550100"
    }
  },
  "response": {}
}
```

### Pre Sign-up Response

Response fields include:

`autoConfirmUser` (Boolean, optional)
: Set to true to auto-confirm the user, or false otherwise.

`autoVerifyEmail` (Boolean, optional)
: Set to true to set as verified the email of a user who is signing up, or false otherwise.

`autoVerifyPhone` (Boolean, optional)
: Set to true to set as verified the phone number of a user who is signing up, or false otherwise.

```json title="Pre Sign-up Response Structure"
{
    "request": {
        "userAttributes": {
            "string": "string",
            . . .
        },
        "validationData": {
            "string": "string",
            . . .
         },
        "clientMetadata": {
            "string": "string",
            . . .
         }
    },

    "response": {
        "autoConfirmUser": "boolean",
        "autoVerifyPhone": "boolean",
        "autoVerifyEmail": "boolean"
    }
}
```

## Pre Authentication

### Pre Authentication Input

```json title="Pre Authentication Request"
{
  "version": "1",
  "triggerSource": "PreAuthentication_Authentication",
  "region": "us-east-1",
  "userPoolId": "us-east-1_example",
  "userName": "UserName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "userAttributes": {
      "sub": "4A709A36-7D63-4785-829D-4198EF10EBDA",
      "email_verified": "true",
      "name": "First Last",
      "email": "pre-auth@mail.com"
    }
  },
  "response": {}
}
```

## Auth Challenge

### Auth Challenge Input

```json title="Create Auth Challenge Request"
{
  "version": "1",
  "triggerSource": "CreateAuthChallenge_Authentication",
  "region": "us-east-1",
  "userPoolId": "us-east-1_example",
  "userName": "UserName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "userAttributes": {
      "sub": "4A709A36-7D63-4785-829D-4198EF10EBDA",
      "email_verified": "true",
      "name": "First Last",
      "email": "create-auth@mail.com"
    },
    "challengeName": "PASSWORD_VERIFIER",
    "session" : [
      {
        "challengeName": "CUSTOM_CHALLENGE",
        "challengeResult": true,
        "challengeMetadata": "CAPTCHA_CHALLENGE"
      }
    ],
    "userNotFound": false
  },
  "response": {}
}
```

```json title="Define Auth Challenge Request"
{
  "version": "1",
  "region": "us-east-1",
  "userPoolId": "us-east-1_example",
  "userName": "UserName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "triggerSource": "DefineAuthChallenge_Authentication",
  "request": {
    "userAttributes": {
      "sub": "4A709A36-7D63-4785-829D-4198EF10EBDA",
      "email_verified": "true",
      "name": "First Last",
      "email": "define-auth@mail.com"
    },
    "session" : [
      {
        "challengeName": "PASSWORD_VERIFIER",
        "challengeResult": true
      },
      {
        "challengeName": "CUSTOM_CHALLENGE",
        "challengeResult": true,
        "challengeMetadata": "CAPTCHA_CHALLENGE"
      }
    ],
    "userNotFound": true
  },
  "response": {}
}
```

### Auth Challenge Response

```json title="Verify auth challenge response"
{
  "version": "1",
  "region": "us-east-1",
  "userPoolId": "us-east-1_example",
  "userName": "UserName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "triggerSource": "VerifyAuthChallengeResponse_Authentication",
  "request": {
    "userAttributes": {
      "sub": "4A709A36-7D63-4785-829D-4198EF10EBDA",
      "email_verified": "true",
      "name": "First Last",
      "email": "verify-auth@mail.com"
    },
    "privateChallengeParameters": {
      "answer": "challengeAnswer"
    },
    "clientMetadata" : {
      "foo": "value"
    },
    "challengeAnswer": "challengeAnswer",
    "userNotFound": true
  },
  "response": {}
}
```

## Pre Token Generation

### Pre Token Generation Input

```json
{
  "triggerSource": "TokenGeneration_Authentication",
  "version": "1",
  "region": "us-west-2",
  "userPoolId": "us-west-2_example",
  "userName": "testqq",
  "callerContext": {
    "awsSdkVersion": "aws-sdk-unknown-unknown",
    "clientId": "71ghuul37mresr7h373b704tua"
  },
  "request": {
    "userAttributes": {
      "sub": "0b0a57c5-f013-426a-81a1-f8ffbfba21f0",
      "email_verified": "true",
      "cognito:user_status": "CONFIRMED",
      "email": "test@mail.com"
    },
    "groupConfiguration": {
      "groupsToOverride": [],
      "iamRolesToOverride": [],
      "preferredRole": null
    }
  },
  "response": {}
}
```

## Post Authentication

### Post Authentication Input

```json title="Post Authentication Reqest"
{
  "version": "1",
  "triggerSource": "PostAuthentication_Authentication",
  "region": "us-east-1",
  "userPoolId": "us-east-1_example",
  "userName": "UserName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "newDeviceUsed": true,
    "userAttributes": {
      "email": "post-auth@mail.com"
    }
  },
  "response": {}
}
```

## Post Confirmation

### Post Confirmation Input

```json title="Post Confirmation Request"
{
  "version": "string",
  "triggerSource": "PostConfirmation_ConfirmSignUp",
  "region": "us-east-1",
  "userPoolId": "string",
  "userName": "userName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "userAttributes": {
      "email": "user@example.com",
      "email_verified": true
    }
  },
  "response": {}
}
```

## Custom Message

### Custom Message Input

```json title="Custom Message Request"
{
  "version": "1",
  "triggerSource": "CustomMessage_AdminCreateUser",
  "region": "region",
  "userPoolId": "userPoolId",
  "userName": "userName",
  "callerContext": {
    "awsSdk": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "userAttributes": {
      "phone_number_verified": false,
      "email_verified": true
    },
    "codeParameter": "####",
    "usernameParameter": "username"
  },
  "response": {}
}
```

## User Migration

### User Migration Input

```json
{
  "version": "string",
  "triggerSource": "UserMigration_Authentication",
  "region": "us-east-1",
  "userPoolId": "string",
  "userName": "userName",
  "callerContext": {
    "awsSdkVersion": "awsSdkVersion",
    "clientId": "clientId"
  },
  "request": {
    "password": "password"
  },
  "response": {}
}
```

## Libraries

- [Python - Request and response utils](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/#cognito-user-pool) - Pip `aws-lambda-powertools`
- [Typescript - Typing for request and response](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/aws-lambda/trigger/cognito-user-pool-trigger) - NPM `@types/aws-lambda`
- [Java - Request and response classes for CognitoUserPool*](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CognitoUserPoolCreateAuthChallengeEvent.java) - Maven `aws-lambda-java-events`
- [Go - Request and response class](https://github.com/aws/aws-lambda-go/blob/main/events/cognito.go) - `github.com/aws/aws-lambda-go/events`

### Code Examples

```python title="Define Auth Challenge Example using AWS Lambda Powertools"
from aws_lambda_powertools.utilities.data_classes import event_source
from aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event import DefineAuthChallengeTriggerEvent

@event_source(data_class=DefineAuthChallengeTriggerEvent)
def handler(event: DefineAuthChallengeTriggerEvent, context) -> dict:
    if (
        len(event.request.session) == 1
        and event.request.session[0].challenge_name == "SRP_A"
    ):
        event.response.issue_tokens = False
        event.response.fail_authentication = False
        event.response.challenge_name = "PASSWORD_VERIFIER"
    elif (
        len(event.request.session) == 2
        and event.request.session[1].challenge_name == "PASSWORD_VERIFIER"
        and event.request.session[1].challenge_result
    ):
        event.response.issue_tokens = False
        event.response.fail_authentication = False
        event.response.challenge_name = "CUSTOM_CHALLENGE"
    elif (
        len(event.request.session) == 3
        and event.request.session[2].challenge_name == "CUSTOM_CHALLENGE"
        and event.request.session[2].challenge_result
    ):
        event.response.issue_tokens = True
        event.response.fail_authentication = False
    else:
        event.response.issue_tokens = False
        event.response.fail_authentication = True

    return event.raw_event
```

## Reference Docs

- [Customizing user pool workflows with Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html){target="_blank"}
