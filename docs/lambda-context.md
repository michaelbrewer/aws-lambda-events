---
description: When Lambda runs your function, it passes a context object to the handler.
---

# Lambda Context

When Lambda runs your function, it passes a context object to the handler. This object provides methods and properties that provide information 
about the invocation, function, and execution environment.

???+ NOTE
    During asynchronous invokes, the lambda context field `clientContext` will not be populated.

## Docs

- [DotNet - Lambda Context Docs](https://docs.aws.amazon.com/lambda/latest/dg/csharp-context.html)
- [Python - Lambda Context Docs](https://docs.aws.amazon.com/lambda/latest/dg/python-context.html)
- [Go - Lambda Context Docs](https://docs.aws.amazon.com/lambda/latest/dg/golang-context.html)
- [Java - Lambda Context Docs](https://docs.aws.amazon.com/lambda/latest/dg/java-context.html)
- [NodeJS - Lambda Context Docs](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html)

## Resources

- [DotNet - ILambdaContext](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.Core) - NuGet `Amazon.Lambda.Core`
- [Java - Context](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java) - Maven `aws-lambda-java-core`
- [Python - LambdaContext](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/typing/) - Pip `aws-lambda-powertools`
- [Typescript - Context](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/handler.d.ts) - NPM `@types/aws-lambda`
- [Go - LambdaContext](https://github.com/aws/aws-lambda-go/blob/main/lambdacontext/context.go) - Go `github.com/aws/aws-lambda-go/lambdacontext`
- [Rust - Context](https://github.com/awslabs/aws-lambda-rust-runtime/blob/master/lambda-runtime/src/types.rs) - Cargo `aws-lambda-rust-runtime`
- [Php - Bref\Context](https://github.com/brefphp/bref/blob/master/src/Context/Context.php) - Composer `bref/bref`
