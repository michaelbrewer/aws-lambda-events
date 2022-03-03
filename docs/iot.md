# IOT

## Request

```json
{
    "row" : "10",
    "pos" : "23",
    "moisture" : "75"
}
```

## Response

```json
{
    "Statement": "{\"Sid\":\"iot-events\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"iot.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-west-2:123456789012:function:my-function\"}"
}
```

## Resources

## Documentation

- [Using AWS Lambda with AWS IoT](https://docs.aws.amazon.com/lambda/latest/dg/services-iot.html)
