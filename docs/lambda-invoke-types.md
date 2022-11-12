# Lambda Invocation Types

![Lambda invokes types](./media/invoke-type-light.png#gh-light-mode-only)
![Lambda invokes types](./media/invoke-type-dark.png#gh-dark-mode-only)

## Synchronous Invokes

Synchronous invocations are the most straight forward way to invoke your Lambda functions. In this model, your functions execute immediately when you perform the Lambda Invoke API call. For testing, when invoking directly use invoke type of `RequestResponse`.

## Asynchronous Invokes

Asynchronous invokes place your invoke request in Lambda service queue and we process the requests as they arrive. For testing, when invoking directly use invoke type of `Event`.

???+ NOTE
    During asynchronous invokes, the Lambda context field `clientContext` will not be populated.

## Poll-Based Invokes

AWS will manage the poller on your behalf and perform Synchronous invokes of your function with this type of integration. The retry behavior for this model is based on data expiration in the data source.

- [Understanding the Different Ways to Invoke Lambda Functions](https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/){target="_blank"}
