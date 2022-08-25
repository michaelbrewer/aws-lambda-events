# Lambda layers of defense

> DRAFT: Methods, Ideas, Practices to improve your Lambda's security / reliability

You are responsible for maintaining control over your content that is hosted on this infrastructure.

## Event Sources

### Synch flow (API GW, AppSync)

- Event source can authorize requests
    - [rest/http - Standard AWS IAM roles and policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html){target="_blank"}
    - [rest - cognito](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html)
    - [http - jwt](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html){target="_blank"}
    - [graphql - oidc](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#openid-connect-authorization)
    - [rest/http/graphql - custom](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html){target="_blank"}
    - [rest - IAM tags to control access](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging-iam-policy.html))
    - [rest/http - mutual TLS authentication](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html)
    - [rest/graphql - x-api-key](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-key-with-restapi.html)

- Event source can only be available within a [VPC](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)

- Event source can limit by sourceIp or VPC 
    - [Controlling access to an API with API Gateway resource policies](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html)


```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:region:account-id:*"
        },
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:region:account-id:*",
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "123.4.5.6/24"
                }
            }
        }
    ]
}
```

- Event source can be linked to a waf (AWS Shield, [AWS WAF](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html)) or cdn (CloudFront)

- Event source can add usage limits and [throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) per api client per endpoint

- Event source can include request validation

```mermaid
flowchart LR
    Client <--> id1(Event Source) <--> id2(Lambda Service) <--> id3(Lambda Function) <--> id4(Down Stream)
```

### Asynch flow (S3, EventBridge)

- Event source can do batching
- Event source can have filtering

```mermaid
flowchart LR
    Client --> id1(Event Source) --> id5(Requests) <--> id2(Lambda Service) <--> id3(Lambda Function) <--> id4(Down Stream)
```

### Asynch flow (Dynamodb)

- Updates can be filtered
- Updates can be sent to EventBridge to further filtering

```mermaid
flowchart LR
    Client --> id1(Event Source) --> id5(Changes) <--> id2(Lambda Service) <--> id3(Lambda Function) <--> id4(Down Stream)
```

## Ideas to be documented

- [Data protection in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-dataprotection.html){target="_blank"}
    - `Encryption in transit` - Lambda API endpoints only support secure connections over HTTPS.
    - `Encryption at rest` - On a per-function basis, you can configure Lambda to use a [customer managed key to encrypt your environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption){target="_blank"}. Conterary to the AWS docs, i would not recommended using environments variables for secrets, but rather secret manager (or parameter store).
    Lambda always encrypts files that you upload to Lambda, including deployment packages and layer archives. Amazon CloudWatch Logs and AWS X-Ray also encrypt data by default.

- "Identity and access management for Lambda" - least priviledge
    - [Identity and access management for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-iam.html)
    - [IAM condition key, lambda:SourceFunctionArn](https://aws.amazon.com/about-aws/whats-new/2022/07/aws-lambda-iam-condition-key-lambda-source-function-arn/) - "This capability allows you to implement advanced security controls for the AWS API calls taken by your Lambda function code. For example, you can write conditional policies using the new lambda:SourceFunctionArn together with existing condition keys such as aws:SourceIP or aws:SourceVPC to grant permissions to AWS API calls only if those originate from inside the customer’s VPC."
    - [Working with Lambda execution environment credentials](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html?icmpid=docs_lambda_rss#permissions-executionrole-source-function-arn)

```json5
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExampleSourceFunctionArn",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::lambda_bucket/*",
            "Condition": {
                "ArnEquals": {
                    "lambda:SourceFunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:source_lambda"
                }
            }
        }
    ]
}
```

- "Compliance validation for AWS Lambda"
    - SOC1, SOC2, SOC3, PCI, FedRAMP, HIPAA, ISMAP etc..
    - [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/)
    - [AWS Artifact](https://aws.amazon.com/artifact/)

- [Resilience in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-resilience.html){target="_blank"}
    - AWS Lambda is always multi-az within a region

- "Managed runtimes"
    - AWS will patch a managed runtime like python3.9 or nodejs16.x

- "Limiting concurrency" / "Throttling"
    - [Creating and using usage plans with API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html)
    - [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html)

- "Authentication"
    - JWT, Cognito etc..

- "Input / Output validation"
    - Docs [Enable request validation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html)
    - Example [API Gateway data validation](https://serverlessland.com/patterns/apigw-data-validation)

- "VPC"
    - [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)

- "Observability" (Logging, Metrics, Tracing)
    - [Powertools Tracer](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/)
    - [Powertools Structured logging](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/)
    - [Powertools Metrics](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/)

- "Event sourcing" - Locking down the event source
    - Limit what can call your lambda function example below for API GW

```json
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "nodejs-apig-functiongetEndpointPermissionProd-BWDBXMPLXE2F",
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-2:111122223333:function:nodejs-apig-function-1G3MXMPLXVXYI",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:execute-api:us-east-2:111122223333:ktyvxmpls1/prodStage/GET/image"
        }
      }
    }
  ]
}
```

- Patching library dependencies
    - [Snyk – Commercial Vulnerability DB and Dependency Check](https://snyk.io/)

- Static code analysis (code complexity, code style, code quality, security, etc ...)

- Lambda versioning and aliases
    - Can help enable blue/green deployments
    - [Perform a canary-based deployment using the blue/green strategy and AWS Lambda](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/perform-a-canary-based-deployment-using-the-blue-green-strategy-and-aws-lambda.html)
    - [Implementing Canary Deployments of AWS Lambda Functions with Alias Traffic Shifting](https://aws.amazon.com/blogs/compute/implementing-canary-deployments-of-aws-lambda-functions-with-alias-traffic-shifting/)

- Idempotency (best practices)

- Code Signing
    - [Code Signing, a Trust and Integrity Control for AWS Lambda](https://aws.amazon.com/blogs/aws/new-code-signing-a-trust-and-integrity-control-for-aws-lambda/)

- Secrets management
    - No hard coding of secrets and use SST where possible
    - [Monitor AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html)
    - [Deploy Serverless Applications with AWS Lambda and API Gateway](https://learn.hashicorp.com/tutorials/terraform/lambda-api-gateway)

- Limit function to single use case, keep code simple and small

- Validate input / output via Jmepath / Pydantic
    - Using framework code like Pydantic or JMESchema

## Resources

- [Security Overview of AWS Lambda](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/security-overview-aws-lambda.pdf){target="_blank"}
- [Security pillar](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/security-pillar.html)
- [aws-serverless-security-workshop](https://github.com/aws-samples/aws-serverless-security-workshop)
- [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [lumigo - AWS Lambda Security](https://lumigo.io/aws-lambda-deployment/aws-lambda-security/)
