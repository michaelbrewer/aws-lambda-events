---
title: Cognito
description: Cognito User Pool Triggers
---

# Cognito User Pool Triggers

You can create a Lambda function and then activate that function during user pool operations such as user sign-up, confirmation, and sign-in (authentication) with a Lambda trigger. You can add authentication challenges, migrate users, and customize verification messages.

| User Pool Flow                      | Operation                           | Description                                                           |
|-------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| Custom Authentication Flow          | Define Auth Challenge               | Determines the next challenge in a custom auth flow                   |
|                                     | Create Auth Challenge               | Creates a challenge in a custom auth flow                             |
|                                     | Verify Auth Challenge Response      | Determines if a response is correct in a custom auth flow             |
| Authentication Events               | Pre authentication Lambda trigger   | Custom validation to accept or deny the sign-in request               |
|                                     | Post authentication Lambda trigger  | Logs events for custom analytics                                      |
|                                     | Pre token generation Lambda trigger | Augments or suppresses token claims                                   |
| Sign-Up                             | Pre sign-up Lambda trigger          | Performs custom validation that accepts or denies the sign-up request |
|                                     | Post confirmation Lambda trigger    | Adds custom welcome messages or event logging for custom analytics    |
|                                     | Migrate user Lambda trigger         | Migrates a user from an existing user directory to user pools         |
| Messages                            | Custom message Lambda trigger       | Performs advanced customization and localization of messages          |
| Token Creation                      | Pre token generation Lambda trigger | Adds or removes attributes in Id tokens                               |
| Email and SMS third-party providers | Custom sender Lambda triggers       | Uses a third-party provider to send SMS and email messages            |

## Common Reqest Fields

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

### Pre Sign-up Request

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
--8<-- "docs/events/cognito-user-pool/pre-signup.json"
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

## Post Confirmation

Amazon Cognito invokes this trigger after a new user is confirmed, allowing you to send custom messages or to add custom logic. For example, you could use this trigger to gather new user data.

- [Post confirmation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html) documentation

### Post Confirmation Request

```json title="Post Confirmation Request"
--8<-- "docs/events/cognito-user-pool/post-confirmation.json"
```

### Post Confirmation Response

No additional return information is expected in the response.

## Pre Authentication

Amazon Cognito invokes this trigger when a user attempts to sign in, allowing custom validation to accept or deny the authentication request.

- [Pre authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html) documentation

### Pre Authentication Request

```json title="Pre Authentication Request"
--8<-- "docs/events/cognito-user-pool/pre-authentication.json"
```

### Pre Authentication Response

No additional return information is expected in the response.

## Custom Authentication

These Lambda triggers issue and verify their own challenges as part of a user pool custom authentication flow.

**[Define auth challenge](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-define-auth-challenge.html){target="_blank"}**
: Amazon Cognito invokes this trigger to initiate the custom authentication flow.

**[Create auth challenge](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-create-auth-challenge.html){target="_blank"}**
: Amazon Cognito invokes this trigger after Define Auth Challenge to create a custom challenge.

**[Verify auth challenge response](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-verify-auth-challenge-response.html){target="_blank"}**
: Amazon Cognito invokes this trigger to verify if the response from the end user for a custom challenge is valid or not.

| Trigger               | triggerSource value                        | Triggering event                |
|-----------------------|--------------------------------------------|---------------------------------|
| Define auth challenge | DefineAuthChallenge_Authentication         | Define Auth Challenge.          |
| Create auth challenge | CreateAuthChallenge_Authentication         | Create Auth Challenge.          |
| Verify auth challenge | VerifyAuthChallengeResponse_Authentication | Verify Auth Challenge Response. |

### Auth Challenge Requests

```json title="Define Auth Challenge Request"
--8<-- "docs/events/cognito-user-pool/define-auth-challenge.json"
```

```json title="Create Auth Challenge Request"
--8<-- "docs/events/cognito-user-pool/create-auth-challenge.json"
```

### Auth Challenge Responses

```json title="Verify auth challenge response"
--8<-- "docs/events/cognito-user-pool/verify-auth-challenge-response.json"
```

## Pre Token Generation

Amazon Cognito invokes this trigger before token generation which allows you to customize identity token claims.

- [Pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) documentation

### Pre Token Generation Request

| triggerSource                        | Triggering event                                                                                                     |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| TokenGeneration_HostedAuth           | Called during authentication from the Amazon Cognito hosted UI sign-in page.                                         |
| TokenGeneration_Authentication       | Called after user authentication flows have completed.                                                               |
| TokenGeneration_NewPasswordChallenge | Called after the user is created by an admin. This flow is invoked when the user has to change a temporary password. |
| TokenGeneration_AuthenticateDevice   | Called at the end of the authentication of a user device.                                                            |
| TokenGeneration_RefreshTokens        | Called when a user tries to refresh the identity and access tokens.                                                  |

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
--8<-- "docs/events/cognito-user-pool/pre-token-generation.json"
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

### Post Authentication Request

```json title="Post Authentication Reqest"
--8<-- "docs/events/cognito-user-pool/post-authentication.json"
```

### Post Authentication Response

No additional return information is expected in the response.

## Custom Message

Amazon Cognito invokes this trigger before sending an email or phone verification message or a multi-factor authentication (MFA) code, allowing you to customize the message dynamically.

- [Custom message Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html) documentation

### Custom Message Request

| triggerSource                     | Triggering event                                                                                                                                       |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| CustomMessage_SignUp              | To send the confirmation code post sign-up.                                                                                                            |
| CustomMessage_AdminCreateUser     | To send the temporary password to a new user.                                                                                                          |
| CustomMessage_ResendCode          | To resend the confirmation code to an existing user.                                                                                                   |
| CustomMessage_ForgotPassword      | To send the confirmation code for Forgot Password request.                                                                                             |
| CustomMessage_UpdateUserAttribute | When a user's email or phone number is changed, this trigger sends a verification code automatically to the user. Cannot be used for other attributes. |
| CustomMessage_VerifyUserAttribute | This trigger sends a verification code to the user when they manually request it for a new email or phone number.                                      |
| CustomMessage_Authentication      | To send MFA code during authentication.                                                                                                                |

```json title="Custom Message Request"
--8<-- "docs/events/cognito-user-pool/custom-message.json"
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

### User Migration Request

| triggerSource                | Triggering event                            |
|------------------------------|---------------------------------------------|
| UserMigration_Authentication | User migration at sign-in.                  |
| UserMigration_ForgotPassword | User migration during forgot-password flow. |

```json title="User Migration Request"
--8<-- "docs/events/cognito-user-pool/user-migration.json"
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

## Custom Email Sender

| TriggerSource                                 | Triggering event                                                                                                      |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| CustomEmailSender_SignUp                      | A user signs up and Amazon Cognito sends a welcome message.                                                           |
| CustomEmailSender_ResendCode                  | A user requests a replacement code to reset their password.                                                           |
| CustomEmailSender_ForgotPassword              | A user requests a code to reset their password.                                                                       |
| CustomEmailSender_UpdateUserAttribute         | A user updates an email address or phone number attribute and Amazon Cognito sends a code to verify the attribute.    |
| CustomEmailSender_VerifyUserAttribute         | A user creates a new email address or phone number attribute and Amazon Cognito sends a code to verify the attribute. |
| CustomEmailSender_AdminCreateUser             | You create a new user in your user pool and Amazon Cognito sends them a temporary password.                           |
| CustomEmailSender_AccountTakeOverNotification | Amazon Cognito detects an attempt to take over a user account and sends the user a notification.                      |

```json title="Custom Email Sender Request"
--8<-- "docs/events/cognito-user-pool/custom-email-sender.json"
```

- [Send AWS Cognito emails with 3rd party Email Service Providers](https://www.maxivanov.io/send-aws-cognito-emails-with-3rd-party-esps/)

## Custom SMS Sender

| TriggerSource                       | Triggering event                                                                                                      |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| CustomSMSSender_SignUp              | A user signs up and Amazon Cognito sends a welcome message.                                                           |
| CustomSMSSender_ResendCode          | A user requests a replacement code to reset their password.                                                           |
| CustomSMSSender_ForgotPassword      | A user requests a code to reset their password.                                                                       |
| CustomSMSSender_UpdateUserAttribute | A user updates an email address or phone number attribute and Amazon Cognito sends a code to verify the attribute.    |
| CustomSMSSender_VerifyUserAttribute | A user creates a new email address or phone number attribute and Amazon Cognito sends a code to verify the attribute. |
| CustomSMSSender_Authentication      | A user with SMS MFA configured signs in.                                                                              |
| CustomSMSSender_AdminCreateUser     | You create a new user in your user pool and Amazon Cognito sends them a temporary password.                           |

## Resources

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
