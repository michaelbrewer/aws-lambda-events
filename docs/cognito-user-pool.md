---
title: Cognito
description: Cognito User Pool Triggers
---

# Cognito User Pool Triggers

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

- [Pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) documentation

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

Amazon Cognito invokes this trigger when a user attempts to sign in, allowing custom validation to accept or deny the authentication request.

- [Pre authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html) documentation

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

### Pre Authentication Response

No additional return information is expected in the response.

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

Amazon Cognito invokes this trigger before token generation which allows you to customize identity token claims.

- [Pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) documentation

### Pre Token Generation Input

Pre token generation request parameters

`groupConfiguration` (Object)
: The input object containing the current group configuration. It includes `groupsToOverride`, `iamRolesToOverride`, and `preferredRole`.

`groupsToOverride` (Array, optional)
: A list of the group names that are associated with the user that the identity token is issued for.

`iamRolesToOverride` (Array, optional)
: A list of the current IAM roles associated with these groups.

`preferredRole` (String, optional)
: A string indicating the preferred IAM role.

`clientMetadata` (Object, optional)
: One or more key-value pairs that you can provide as custom input to the Lambda function that you specify for the pre token generation trigger. 

```json title="Example pre token generation request"
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

### Pre Token Generation Response

Pre token generation response parameters

`claimsToAddOrOverride` (Object, optional)
: A map of one or more key-value pairs of claims to add or override. For group related claims, use groupOverrideDetails instead.

`claimsToSuppress` (Array, optional)
: A list that contains claims to be suppressed from the identity token.

`groupOverrideDetails` (Object, optional)
: The output object containing the current group configuration. It includes `groupsToOverride`, `iamRolesToOverride`, and `preferredRole`.

```json title="Pre-token generation response structure"
{
    "request": {
        "userAttributes": {"string": "string"},
        "groupConfiguration": [
            {
                "groupsToOverride": [
                    "string",
                    "string"
                ],
                "iamRolesToOverride": [
                    "string",
                    "string"
                ],
                "preferredRole": "string"
            }
        ],
        "clientMetadata": {"string": "string"}
    },
    "response": {
        "claimsOverrideDetails": {
            "claimsToAddOrOverride": {"string": "string"},
            "claimsToSuppress": [
                "string",
                "string"
            ],
            "groupOverrideDetails": {
                "groupsToOverride": [
                    "string",
                    "string"
                ],
                "iamRolesToOverride": [
                    "string",
                    "string"
                ],
                "preferredRole": "string"
            }
        }
    }
}
```

## Post Authentication

- [Post authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html) documentation

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

### Post Authentication Response

No additional return information is expected in the response.

## Post Confirmation

Amazon Cognito invokes this trigger after a new user is confirmed, allowing you to send custom messages or to add custom logic. For example, you could use this trigger to gather new user data.

- [Post confirmation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html) documentation

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

### Post Confirmation Response

No additional return information is expected in the response.

## Custom Message

Amazon Cognito invokes this trigger before sending an email or phone verification message or a multi-factor authentication (MFA) code, allowing you to customize the message dynamically.

- [Custom message Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html) documentation

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

### Custom Message Response

Custom message response parameters

`smsMessage` (String, optional)
: The custom SMS message to be sent to your users. Must include the `codeParameter` value received in the request.

`emailMessage` (String, optional)
: The custom email message to be sent to your users. Must include the `codeParameter` value received in the request.

`emailSubject` (String, optional)
: The subject line for the custom message.

```json title="Custom Message Response Structure"
{
    "request": {
        "userAttributes": {
            "string": "string",
            . . .
        }
        "codeParameter": "####",
        "usernameParameter": "string",
        "clientMetadata": {
            "string": "string",
            . . .
        }
    },
    "response": {
        "smsMessage": "string",
        "emailMessage": "string",
        "emailSubject": "string"
    }
}
```

## User Migration

Amazon Cognito invokes this trigger when a user does not exist in the user pool at the time of sign-in with a password, or in the forgot-password flow. 
After the Lambda function returns successfully, Amazon Cognito creates the user in the user pool. 

- [Migrate user Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) documentation

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

### User Migration Response

```json title="User migration response structure"
{
    "userName": "string",
    "request": {
        "password": "string",
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
        "userAttributes": {
            "string": "string",
            . . .
        },
        "finalUserStatus": "string",
        "messageAction": "string",
        "desiredDeliveryMediums": [ "string", . . .],
        "forceAliasCreation": boolean
    }
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

## Documentation

Reference documentation and blog posts. 

- [Customizing user pool workflows with Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html){target="_blank"}
- [Anonymous User Identities with Cognito Lambda Triggers](https://bitesizedserverless.com/bite/anonymous-user-identities-with-cognito-lambda-triggers/)
