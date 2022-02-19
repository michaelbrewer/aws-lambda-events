# CloudFormation

AWS CloudFormation invokes your Lambda function asynchronously with an event that includes a callback URL.

## Input

## Input fields

`RequestType` (String)
: The request type is set by the AWS CloudFormation stack operation (create-stack, update-stack, or delete-stack) that was initiated by
the template developer for the stack that contains the custom resource.
Must be one of: `Create`, `Update`, or `Delete`.

`ResponseURL` (String)
: The response URL identifies a presigned S3 bucket that receives responses from the custom resource provider to AWS CloudFormation.

`StackId` (String)
: The Amazon Resource Name (ARN) that identifies the stack that contains the custom resource. Combining the `StackId` with the `RequestId`
forms a value that you can use to uniquely identify a request on a particular custom resource.

`RequestId` (String)
A unique ID for the request. Combining the `StackId` with the `RequestId` forms a value that you can use to uniquely identify a request
on a particular custom resource.

`ResourceType` (String)
: The template developer-chosen resource type of the custom resource in the AWS CloudFormation template. Custom resource type names can
be up to 60 characters long and can include alphanumeric and the following characters: `_@-.`

`LogicalResourceId` (String)
: The template developer-chosen name (logical ID) of the custom resource in the AWS CloudFormation template. This is provided to
facilitate communication between the custom resource provider and the template developer.

`PhysicalResourceId` (String)
: A required custom resource provider-defined physical ID that is unique for that provider. _Required_: Always sent with Update and Delete requests; never sent with Create.

`ResourceProperties` (Optional, Object)
: This field contains the contents of the Properties object sent by the template developer. Its contents are defined by the custom resource provider.

`OldResourceProperties` (Object)
: Used only for `Update` requests. Contains the resource properties that were declared previous to the update request.

## Input examples

```json title="Create event"
{
    "RequestType": "Create",
    "ServiceToken": "arn:aws:lambda:us-east-2:123456789012:function:lambda-error-processor-primer-14ROR2T3JKU66",
    "ResponseURL": "https://cloudformation-custom-resource-response-useast2.s3-us-east-2.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-2%3A123456789012%3Astack/lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456%7Cprimerinvoke%7C5d478078-13e9-baf0-464a-7ef285ecc786?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Expires=1555451971&Signature=28UijZePE5I4dvukKQqM%2F9Rf1o4%3D",
    "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456",
    "RequestId": "5d478078-13e9-baf0-464a-7ef285ecc786",
    "LogicalResourceId": "primerinvoke",
    "ResourceType": "AWS::CloudFormation::CustomResource",
    "ResourceProperties": {
        "ServiceToken": "arn:aws:lambda:us-east-2:123456789012:function:lambda-error-processor-primer-14ROR2T3JKU66",
        "FunctionName": "lambda-error-processor-randomerror-ZWUC391MQAJK"
    }
}
```

```json title="Update event"
{
  "RequestType": "Update",
  "ResponseURL": "http://pre-signed-S3-url-for-response",
  "StackId": "arn:aws:cloudformation:eu-central-1:123456789012:stack/MyStack/guid",
  "RequestId": "unique id for this create request",
  "ResourceType": "Custom::TestResource",
  "LogicalResourceId": "MyTestResource",
  "PhysicalResourceId": "MyTestResourceId",
  "ServiceToken": "abcd",
  "ResourceProperties": {
    "StackName": "MyStack",
    "List": [
      "1",
      "2",
      "3"
    ]
  },
  "OldResourceProperties": {
    "StackName": "MyStack",
    "List": [
      "1"
    ]
  }
}
```

```json title="Delete event"
{
   "RequestType" : "Delete",
   "RequestId" : "unique id for this delete request",
   "ResponseURL" : "pre-signed-url-for-delete-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "name of resource in template",
   "StackId" : "arn:aws:cloudformation:us-east-2:namespace:stack/stack-name/guid",
   "PhysicalResourceId" : "custom resource provider-defined physical id",
   "ResourceProperties" : {
      "key1" : "string",
      "key2" : [ "list" ],
      "key3" : { "key4" : "map" }
   }
}
```

## Response

Responses are submitted via the pre-signed URL in the `ResponseURL` field of the request via the cfn-response module.

`Status` (String)
: The status value sent by the custom resource provider in response to an AWS CloudFormation-generated request.
Must be either `SUCCESS` or `FAILED`.

`Reason` (String)
: Describes the reason for a failure response.
_Required_: Required if Status is `FAILED`. It's optional otherwise.

`PhysicalResourceId` (String)
: This value should be an identifier unique to the custom resource vendor, and can be up to 1 KB in size.
The value must be a non-empty string and must be identical for all responses for the same resource.

`StackId` (String)
: The Amazon Resource Name (ARN) that identifies the stack that contains the custom resource. This response value should be 
copied verbatim from the request.

`RequestId` (String)
: A unique ID for the request. This response value should be copied verbatim from the request.

`LogicalResourceId` (String)
: The template developer-chosen name (logical ID) of the custom resource in the AWS CloudFormation template.
This response value should be copied verbatim from the request.

`NoEcho` (Optional, Boolean)
: Optional. Indicates whether to mask the output of the custom resource when retrieved by using the `Fn::GetAtt` function.
If set to true, all returned values are masked with asterisks (`*****`), except for those stored in the _Metadata_ section of
the template. AWS CloudFormation does not transform, modify, or redact any information you include in the Metadata section.
The default value is `false`.

`Data` (Optional, Object)
: Optional. The custom resource provider-defined name-value pairs to send with the response.
You can access the values provided here by name in the template with `Fn::GetAtt`.

```json title="The following is an example of a custom resource response"
{
   "Status" : "SUCCESS",
   "PhysicalResourceId" : "Tester1",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/stack-name/guid",
   "RequestId" : "unique id for this create request",
   "LogicalResourceId" : "MySeleniumTester",
   "Data" : {
      "resultsPage" : "http://www.myexampledomain/test-results/guid",
      "lastUpdate" : "2012-11-14T03:30Z",
   }
}
```

## Libraries

Custom Resource handlers

- [Custom Resource Helper - Python](https://github.com/aws-cloudformation/custom-resource-helper) - pip `crhelper`
- [Custom Resources Handler - Java](https://awslabs.github.io/aws-lambda-powertools-java/utilities/custom_resources/) - Maven `software.amazon.lambda:powertools-cloudformation`
- [cfn-response module](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html)

Custom resource typing and data classes

- [Java - CloudFormationCustomResourceEvent](https://github.com/aws/aws-lambda-java-libs/blob/master/aws-lambda-java-events/src/main/java/com/amazonaws/services/lambda/runtime/events/CloudFormationCustomResourceEvent.java)
- [Go -](https://github.com/aws/aws-lambda-go/blob/main/cfn/README.md) - `github.com/aws/aws-lambda-go/cfn`

### Code Examples

```python title="app.py"
from __future__ import print_function
from crhelper import CfnResource
import logging

logger = logging.getLogger(__name__)
# Initialise the helper, all inputs are optional, this example shows the defaults
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=120, ssl_verify=None)

try:
    ## Init code goes here
    pass
except Exception as e:
    helper.init_failure(e)


@helper.create
def create(event, context):
    logger.info("Got Create")
    # Optionally return an ID that will be used for the resource PhysicalResourceId, 
    # if None is returned an ID will be generated. If a poll_create function is defined 
    # return value is placed into the poll event as event['CrHelperData']['PhysicalResourceId']
    #
    # To add response data update the helper.Data dict
    # If poll is enabled data is placed into poll event as event['CrHelperData']
    helper.Data.update({"test": "testdata"})

    # To return an error to cloudformation you raise an exception:
    if not helper.Data.get("test"):
        raise ValueError("this error will show in the cloudformation events log and console.")
    
    return "MyResourceId"


@helper.update
def update(event, context):
    logger.info("Got Update")
    # If the update resulted in a new resource being created, return an id for the new resource. 
    # CloudFormation will send a delete event with the old id when stack update completes


@helper.delete
def delete(event, context):
    logger.info("Got Delete")
    # Delete never returns anything. Should not fail if the underlying resources are already deleted.
    # Desired state.


@helper.poll_create
def poll_create(event, context):
    logger.info("Got create poll")
    # Return a resource id or True to indicate that creation is complete. if True is returned an id 
    # will be generated
    return True


def handler(event, context):
    helper(event, context)
```

## Reference Docs

- [Using AWS Lambda with AWS CloudFormation](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudformation.html)
- [AWS CloudFormation custom resource creation with Python, AWS Lambda, and crhelper](https://aws.amazon.com/blogs/infrastructure-and-automation/aws-cloudformation-custom-resource-creation-with-python-aws-lambda-and-crhelper/)
- [Custom resource provider request fields](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html)
- [Custom resource response objects](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-responses.html)
