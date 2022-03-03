# Secrets Manager

Secrets Manager uses a Lambda function to rotate the secret for a secured service or database. Event-driven and synchronous invocation

## Request

### Request structure

```json
{
  "Step" : "request.type",
  "SecretId" : "string",
  "ClientRequestToken" : "string"
}
```

### Request fields

`Step` (String)
: One of `createSecret`, `setSecret`, `testSecret` or `finishSecret`

- `createSecret` - The first step of rotation is to create a new version of the secret. Depending on your rotation strategy,
the new version can contain a new password, a new username and password, or more secret information. Secrets
Manager labels the new version with the staging label `AWSPENDING`.
- `setSecret` - Second step, rotation changes the credentials in the database or service to match the new credentials in the
`AWSPENDING` version of the secret.
- `testSecret` - Third step, rotation tests the `AWSPENDING` version of the secret by using it to access the database or service.
- `finishSecret` - Final step, rotation moves the label `AWSCURRENT` from the previous secret version to this version.
Secrets Manager adds the `AWSPREVIOUS` staging label to the previous version, so that you retain the last known
good version of the secret.

`SecretId` (String)
: The secret ARN or other identifier

`ClientRequestToken` (String)
: The ClientRequestToken of the secret version

## Response

N/A

## Resources

- [Typescript - SecretsManagerRotationEvent](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/secretsmanager.d.ts) - NPM `@types/aws-lambda`
- [Java - SecretsManagerRotationEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/SecretsManagerRotationEvent.java)
- [Python - Secrets Manager rotation function templates](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-rotation-templates.html)

## Documentation

- [Using AWS Lambda with Secrets Manager](https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html)
- [How log rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html)
- [Customize a Lambda rotation function for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_customize.html)
