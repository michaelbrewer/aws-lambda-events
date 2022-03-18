# Amazon Config

You can use AWS Lambda functions to evaluate whether your AWS resource configurations comply with your custom Config rules. As resources are created, deleted, or changed, AWS Config records these changes and sends the information to your Lambda functions. Your Lambda functions then evaluate the changes and report results to AWS Config.

Event-driven asynchronous invocation

## Request

```json
--8<-- "docs/events/amazon-config/amazon-config.json"
```

## Response

N/A

## Resources

Resources and templates for AWS Config rules

- [AWS Config Rules Repository](https://github.com/awslabs/aws-config-rules) - AWS Community repository of custom Config rules.
- [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html)
- [Blog - Introducing the AWS Config Rule Development Kit (RDK)](https://aws.amazon.com/blogs/mt/introducing-the-aws-config-rule-development-kit-rdk/)

## Documentation

- [Using AWS Lambda with AWS Config](https://docs.aws.amazon.com/lambda/latest/dg/services-config.html)
- [Developing a Custom Rule for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs.html)
