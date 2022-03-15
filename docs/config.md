# Amazon Config

You can use AWS Lambda functions to evaluate whether your AWS resource configurations comply with your custom Config rules. As resources are created, deleted, or changed, AWS Config records these changes and sends the information to your Lambda functions. Your Lambda functions then evaluate the changes and report results to AWS Config. 

Event-driven asynchronous invocation

## Request

```json
{ 
    "invokingEvent": "{\"configurationItem\":{\"configurationItemCaptureTime\":\"2016-02-17T01:36:34.043Z\",\"awsAccountId\":\"000000000000\",\"configurationItemStatus\":\"OK\",\"resourceId\":\"i-00000000\",\"ARN\":\"arn:aws:ec2:us-east-1:000000000000:instance/i-00000000\",\"awsRegion\":\"us-east-1\",\"availabilityZone\":\"us-east-1a\",\"resourceType\":\"AWS::EC2::Instance\",\"tags\":{\"Foo\":\"Bar\"},\"relationships\":[{\"resourceId\":\"eipalloc-00000000\",\"resourceType\":\"AWS::EC2::EIP\",\"name\":\"Is attached to ElasticIp\"}],\"configuration\":{\"foo\":\"bar\"}},\"messageType\":\"ConfigurationItemChangeNotification\"}",
    "ruleParameters": "{\"myParameterKey\":\"myParameterValue\"}",
    "resultToken": "myResultToken",
    "eventLeftScope": false,
    "executionRoleArn": "arn:aws:iam::012345678912:role/config-role",
    "configRuleArn": "arn:aws:config:us-east-1:012345678912:config-rule/config-rule-0123456",
    "configRuleName": "change-triggered-config-rule",
    "configRuleId": "config-rule-0123456",
    "accountId": "012345678912",
    "version": "1.0"
}
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
