# Lambda Lifecycle

![Invoke Lifecyle](./media/overview-lnvoke-light.png#gh-light-mode-only)
![Invoke Lifecyle](./media/overview-lnvoke-dark.png#gh-dark-mode-only)

## Init phase

In the `Init` phase, Lambda performs three tasks:

- Start all extensions (`Extension init`)
- Bootstrap the runtime (`Runtime init`)
- Run the function's static code (`Function init`)

The `Init` phase ends when the runtime and all extensions signal that they are ready by sending a `Next` API request. The `Init` phase is limited to 10 seconds. If all three tasks do not complete within 10 seconds, Lambda retries the `Init` phase at the time of the first function invocation.

## Invoke

When a Lambda function is invoked in response to a `Next` API request, Lambda sends an `Invoke` event to the runtime and to each extension.

The function's timeout setting limits the duration of the entire `Invoke` phase.

## Shutdown

When Lambda is about to shut down the runtime, it sends a `Shutdown` event to the runtime and to each external extension. Extensions can use this time for final cleanup tasks. The `Shutdown` event is a response to a `Next` API request.

**Duration:** The entire Shutdown phase is capped at 2 seconds. If the runtime or any extension does not respond, Lambda terminates it via a signal (`SIGKILL`).

## Documentation

- [AWS Lambda execution environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html){target="_blank"}
- [Lambda Cold Starts and Bootstrap Code](https://bitesizedserverless.com/bite/lambda-cold-start-bootstrap/){target="_blank"}
- [When is the Lambda Init Phase Free, and when is it Billed?](https://bitesizedserverless.com/bite/when-is-the-lambda-init-phase-free-and-when-is-it-billed/){target="_blank"}
