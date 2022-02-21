# Secrets Manager

Event-driven; synchronous invocation

## Input

```json
{
  "Step" : "request.type",
  "SecretId" : "string",
  "ClientRequestToken" : "string"
}
```

## Response

N/A

## Libraries

- [Secrets Manager rotation function templates](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_available-rotation-templates.html)

## Reference Docs

- [Using AWS Lambda with Secrets Manager](https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html)
- [How log rotation works](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html)
