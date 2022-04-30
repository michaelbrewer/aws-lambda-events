# CloudFront Function

With CloudFront Functions, you can write lightweight functions in JavaScript for high-scale, latency-sensitive CDN customizations.
The CloudFront Functions runtime environment offers submillisecond startup times, scales immediately to handle millions of requests
per second, and is highly secure. CloudFront Functions is a native feature of CloudFront, which means you can build, test, and
deploy your code entirely within CloudFront.

!!!NOTE
    CloudFront Functions are at all like AWS Lambda functions, as they are JavaScript only and have no Lambda context.

![CloudFront Function Diagram](./media/cloudfront-function-light.png#gh-light-mode-only)
![CloudFront Function Diagram](./media/cloudfront-function-dark.png#gh-dark-mode-only)

## Limits

- JavaScript (ECMAScript 5.1 compliant)
- Event sources - Viewer request pr viewer response
- 10,000,000 requests per second or more
- Submillisecond duration
- 2 MB maximum memory
- 10 KB maximum size of a function
- No network access
- No file system access
- No access to request body
- Can access to geolocation and device data
- Can build and test entirely within CloudFront
- Function logging and metrics

## Request

`version` - (String, required)
: The `version` field contains a string that specifies the version of the CloudFront Functions event object. The current version is `1.0`.

`context` - (Object, required)
: The `context` object contains contextual information about the event. It includes the following fields:

- `distributionDomainName` - The CloudFront domain name (for example, `d111111abcdef8.cloudfront.net`) of the distribution that’s associated with the event.
- `distributionId` - The ID of the distribution (for example, `EDFDVBD6EXAMPLE`) that’s associated with the event.
- `eventType` - The event type, either `viewer-request` or `viewer-response`.
- `requestId` - A string that uniquely identifies a CloudFront request (and its associated response).

`viewer` - (Object, required)
The request object contains a representation of a viewer-to-CloudFront HTTP request. In the `event` object that’s passed to your function, the `request` object represents the actual request that CloudFront received from the viewer. The `request` object contains the following fields:

- `method` - The HTTP method of the request.
- `uri` - The URI of the request.
- `querystring` - An object that represents the query string in the request.
- `headers` - An object that represents the HTTP headers in the request.
- `cookies` - An object that represents the cookies in the request (`Cookie` headers).

```json title="Event Structure"
{
    "version": "1.0",
    "context": {
        <context object>
    },
    "viewer": {
        <viewer object>
    },
    "request": {
        <request object>
    },
    "response": {
        <response object>
    }
}
```

### Getting the correlation id

JSON path to correlation id: `context.requestId`

### Generating sample events

TODO

## Response

The response object contains a representation of a CloudFront-to-viewer HTTP response. In the `event` object that’s passed to your function, the `response` object represents CloudFront’s actual response to a viewer request.

If your function code returns a `response` object, it must use this same structure.

The `response` object contains the following fields:

`statusCode` (Integer, required)
: The HTTP status code of the response. This value is an integer, not a string.

`statusDescription` (String)
: The HTTP status description of the response. If your function code generates a response, this field is optional.

`headers` (Object)
: An object that represents the HTTP headers in the response. Cookies are represented separately in the cookies object.

`cookies` (Object)
: An object that represents the cookies in the response (`Set-Cookie` headers).

## Request Response Example

!!! Note
    The `event` object is the input to your function. Your function returns only the `request` or `response` object, not the complete event object.

```json title="The following example shows a complete event object."
{
  "version": "1.0",
  "context": {
    "distributionDomainName": "d111111abcdef8.cloudfront.net",
    "distributionId": "EDFDVBD6EXAMPLE",
    "eventType": "viewer-response",
    "requestId": "EXAMPLEntjQpEXAMPLE_SG5Z-EXAMPLEPmPfEXAMPLEu3EqEXAMPLE=="
  },
  "viewer": {
    "ip": "198.51.100.11"
  },
  "request": {
    "method": "GET",
    "uri": "/media/index.mpd",
    "querystring": {
      "ID": {
        "value": "42"
      },
      "Exp": {
        "value": "1619740800"
      },
      "TTL": {
        "value": "1440"
      },
      "NoValue": {
        "value": ""
      },
      "querymv": {
        "value": "val1",
        "multiValue": [
          {
            "value": "val1"
          },
          {
            "value": "val2,val3"
          }
        ]
      }
    },
    "headers": {
      "host": {
        "value": "video.example.com"
      },
      "user-agent": {
        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
      },
      "accept": {
        "value": "application/json",
        "multiValue": [
          {
            "value": "application/json"
          },
          {
            "value": "application/xml"
          },
          {
            "value": "text/html"
          }
        ]
      },
      "accept-language": {
        "value": "en-GB,en;q=0.5"
      },
      "accept-encoding": {
        "value": "gzip, deflate, br"
      },
      "origin": {
        "value": "https://website.example.com"
      },
      "referer": {
        "value": "https://website.example.com/videos/12345678?action=play"
      },
      "cloudfront-viewer-country": {
        "value": "GB"
      }
    },
    "cookies": {
      "Cookie1": {
        "value": "value1"
      },
      "Cookie2": {
        "value": "value2"
      },
      "cookie_consent": {
        "value": "true"
      },
      "cookiemv": {
        "value": "value3",
        "multiValue": [
          {
            "value": "value3"
          },
          {
            "value": "value4"
          }
        ]
      }
    }
  },
  "response": {
    "statusCode": 200,
    "statusDescription": "OK",
    "headers": {
      "date": {
        "value": "Mon, 04 Apr 2021 18:57:56 GMT"
      },
      "server": {
        "value": "gunicorn/19.9.0"
      },
      "access-control-allow-origin": {
        "value": "*"
      },
      "access-control-allow-credentials": {
        "value": "true"
      },
      "content-type": {
        "value": "application/json"
      },
      "content-length": {
        "value": "701"
      }
    },
    "cookies": {
      "ID": {
        "value": "id1234",
        "attributes": "Expires=Wed, 05 Apr 2021 07:28:00 GMT"
      },
      "Cookie1": {
        "value": "val1",
        "attributes": "Secure; Path=/; Domain=example.com; Expires=Wed, 05 Apr 2021 07:28:00 GMT",
        "multiValue": [
          {
            "value": "val1",
            "attributes": "Secure; Path=/; Domain=example.com; Expires=Wed, 05 Apr 2021 07:28:00 GMT"
          },
          {
            "value": "val2",
            "attributes": "Path=/cat; Domain=example.com; Expires=Wed, 10 Jan 2021 07:28:00 GMT"
          }
        ]
      }
    }
  }
}
```

## Resources

More code examples

- [Example code for CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-example-code.html)
- [Github - Amazon CloudFront Functions](https://github.com/aws-samples/amazon-cloudfront-functions)

???+ tip "TIP: Rather use Amazon CloudFront response headers policies"
    You no longer need to configure your origins or use custom Lambda@Edge or CloudFront functions to insert these headers. 
    
    See [Amazon CloudFront now supports configurable CORS, security, and custom HTTP response headers](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-cloudfront-supports-cors-security-custom-http-response-headers/){target="_blank"}

### Code Examples

Add security headers to the response

```javascript title="Add security headers to the response"
function handler(event) {
    var response = event.response;
    var headers = response.headers;

    // Set HTTP security headers
    // Since JavaScript doesn't allow for hyphens in variable names, we use the dict["key"] notation 
    headers['strict-transport-security'] = { value: 'max-age=63072000; includeSubdomains; preload'}; 
    headers['content-security-policy'] = { value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"}; 
    headers['x-content-type-options'] = { value: 'nosniff'}; 
    headers['x-frame-options'] = {value: 'DENY'}; 
    headers['x-xss-protection'] = {value: '1; mode=block'}; 

    // Return the response to viewers 
    return response;
}
```

## Documentation

- [Blog - Introducing CloudFront Functions – Run Your Code at the Edge with Low Latency at Any Scale](https://aws.amazon.com/blogs/aws/introducing-cloudfront-functions-run-your-code-at-the-edge-with-low-latency-at-any-scale/)
- [Docs - CloudFront Functions event structure](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html)
- [Blog - Migrating from Lambda@Edge to CloudFront Functions](https://dev.to/aws-builders/migrating-from-lambda-edge-to-cloudfront-functions-3k7k)
