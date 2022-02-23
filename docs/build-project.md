# Build Project

## Introduction

A simple tool to generate a starter project based on a template.

!!!WARNING
    This is still in progress.. :)

<script>
function buildProject(form, path) {
    const prjName = form.elements["name"].value || "foo-service";
    const prjType = form.elements["type"].value;
    const prjRuntime = form.elements["runtime"].value;
    const prjTrigger = form.elements["trigger"].value;
    const prjMemory = form.elements["memory"].value || "512";
    const prjTimeout = form.elements["timeout"].value || "25";
    const prjArchitecture = form.elements["architecture"].value || "x86_64";

    let prjTemplate = form.elements["template"].value;
    if (prjTemplate !== "") {
      prjTemplate = "aws-sam-cli-app-templates/" + prjTemplate;
    }

    const baseUrl = 'https://4v2ies7g1m.execute-api.us-east-2.amazonaws.com/Prod';
    const uri = '/' + path + '?name=' + prjName + '&type=' + prjType + '&runtime=' + prjRuntime + '&trigger=' + prjTrigger + '&memory=' + prjMemory + '&timeout=' + prjTimeout + '&template=' + prjTemplate + '&architecture=' + prjArchitecture;

    fetch(baseUrl + uri)
        .then(resp => resp.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'generated-project.zip';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(() => alert('Failed to generate project!'));
}
</script>
<style>
#buildProjectForm label{
    float: left;
    width: 190px;
}
#buildProjectForm input{
    background-color: var(--md-code-bg-color);
    color: var(--md-code-fg-color);
}
#buildSamProjectForm label{
    float: left;
    width: 190px;
}
#buildSamProjectForm input{
    background-color: var(--md-code-bg-color);
    color: var(--md-code-fg-color);
}
</style>

## AWS Lambda Project Initializer

[AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/) templates

<form id="buildProjectForm">
  <input id="template" type="hidden" value=""/>
  <input id="architecture" type="hidden" value=""/>

  <label for="projectName">Project Name :</label><input id="projectName" name="name" value="example-service"><br/>
  <label for="projectType">Type :</label>
  <select id="projectType" name="type">
    <option value="sam" selected>SAM Template</option>
    <option value="cdk">AWS CDK project</option>
  </select>
  <br/>
  <label for="projectType">Runtime :</label>
  <select id="projectRuntime" name="runtime">
    <option value="python3.9" selected>Python 3.9</option>
    <option value="typescript">Typescript (Node 14)</option>
  </select>
  <br/>
  <label for="projectTrigger">Trigger :</label>
  <select id="projectTrigger" name="trigger">
    <option value="rest-api" selected>API GW Rest API</option>
    <option value="http-api">API GW Rest API</option>
    <option value="s3">S3 Event Notification</option>
  </select>
  <br/>
  <label for="projectArchitecture">Architecture :</label>
  <select id="projectArchitecture" name="architecture" required=false>
    <option value="x86_64" selected>x86_64</option>
    <option value="arm64">arm64</option>
  </select>
  <br/>
  <label for="projectMemory">Memory in MB :</label> <input id="projectMemory" name="memory" value="512"><br/>
  <label for="projectTimeout">Timeout in seconds :</label> <input id="projectTimeout" name="timeout" value="25"><br/>
  <br/><a href="#" onclick="javascript:buildProject(document.getElementById('buildProjectForm'), 'project.zip')" class="md-button md-button--primary">Generate Project</a>
</form>

## AWS Sam template

AWS Sam templates used at [aws-sam-cli-app-templates](https://github.com/aws/aws-sam-cli-app-templates) github repo.

<form id="buildSamProjectForm">
  <input name="type" type="hidden" value="sam"/>
  <input id="trigger" type="hidden" value=""/>
  <input id="runtime" type="hidden" value=""/>

  <label for="projectName">Project Name :</label><input id="projectName" name="name" value="example-service"><br/>
  <label for="projectTemplate">Template :</label>
  <select id="projectTemplate" name="template">
  </select>
  <br/>
  <label for="projectArchitecture">Architecture :</label>
  <select id="projectArchitecture" name="architecture" required=false>
    <option value="x86_64" selected>x86_64</option>
    <option value="arm64">arm64</option>
  </select>
  <br/>
  <label for="projectMemory">Memory in MB :</label> <input id="projectMemory" name="memory" value="512"><br/>
  <label for="projectTimeout">Timeout in seconds :</label> <input id="projectTimeout" name="timeout" value="25"><br/>
  <br/><a href="#" onclick="javascript:buildProject(document.getElementById('buildSamProjectForm'), 'sam-project.zip')" class="md-button md-button--primary">Generate Project</a>
</form>

<script>
const templates = [
  "nodejs12.x/cookiecutter-typescript-app-template",
  "nodejs12.x/cookiecutter-aws-sam-hello-nodejs",
  "nodejs12.x/cookiecutter-quick-start-cloudwatch-events",
  "nodejs12.x/cookiecutter-aws-sam-step-functions-sample-app",
  "nodejs12.x/cookiecutter-quick-start-from-scratch",
  "nodejs12.x/cookiecutter-quick-start-sns",
  "nodejs12.x/cookiecutter-quick-start-s3",
  "nodejs12.x/cookiecutter-quick-start-sqs",
  "nodejs12.x/cookiecutter-quick-start-web",
  "nodejs14.x/cookiecutter-aws-sam-hello-nodejs",
  "nodejs14.x/cookiecutter-quick-start-cloudwatch-events",
  "nodejs14.x/cookiecutter-aws-sam-step-functions-sample-app",
  "nodejs14.x/cookiecutter-quick-start-from-scratch",
  "nodejs14.x/cookiecutter-quick-start-sns",
  "nodejs14.x/cookiecutter-quick-start-s3",
  "nodejs14.x/cookiecutter-quick-start-sqs",
  "nodejs14.x/cookiecutter-aws-sam-hello-typescript-nodejs",
  "nodejs14.x/cookiecutter-quick-start-web",
  "java8.al2/cookiecutter-aws-sam-hello-java-maven",
  "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-maven",
  "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-maven",
  "java8.al2/cookiecutter-aws-sam-step-functions-sample-app-gradle",
  "java8.al2/cookiecutter-aws-sam-hello-java-gradle",
  "java8.al2/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle",
  "java8.al2/cookiecutter-aws-sam-step-functions-sample-app-maven",
  "java8.al2/cookiecutter-aws-sam-eventbridge-hello-java-gradle",
  "java11/cookiecutter-aws-sam-hello-java-maven",
  "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-maven",
  "java11/cookiecutter-aws-sam-eventbridge-hello-java-maven",
  "java11/cookiecutter-aws-sam-step-functions-sample-app-gradle",
  "java11/cookiecutter-aws-sam-hello-java-gradle",
  "java11/cookiecutter-aws-sam-eventbridge-schema-app-java-gradle",
  "java11/cookiecutter-aws-sam-step-functions-sample-app-maven",
  "java11/cookiecutter-aws-sam-eventbridge-hello-java-gradle",
  "ruby2.7/cookiecutter-aws-sam-step-functions-sample-app",
  "ruby2.7/cookiecutter-aws-sam-hello-ruby",
  "python3.7/cookiecutter-aws-sam-eventbridge-schema-app-python",
  "python3.7/cookiecutter-aws-sam-hello-python",
  "python3.7/cookiecutter-aws-sam-step-functions-sample-app",
  "python3.7/cookiecutter-aws-sam-eventBridge-python",
  "python3.8/cookiecutter-aws-sam-eventbridge-schema-app-python",
  "python3.8/cookiecutter-aws-sam-hello-python",
  "python3.8/cookiecutter-aws-sam-step-functions-sample-app",
  "python3.8/cookiecutter-aws-sam-eventBridge-python",
  "python3.8/cookiecutter-aws-sam-efs-python",
  "python3.9/cookiecutter-aws-sam-eventbridge-schema-app-python",
  "python3.9/cookiecutter-aws-sam-hello-python",
  "python3.9/cookiecutter-aws-sam-step-functions-sample-app",
  "python3.9/cookiecutter-aws-sam-step-functions-etl-python",
  "python3.9/cookiecutter-aws-sam-eventBridge-python",
  "python3.9/cookiecutter-aws-sam-efs-python",
  "go1.x/cookiecutter-aws-sam-hello-golang",
  "go1.x/cookiecutter-aws-sam-hello-step-functions-sample-app",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-s3-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-cloudwatch-events-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-step-functions-sample-app",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-powershell",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sns-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-web-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-from-scratch-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sqs-dotnet"
];
const templateSelect = document.getElementById("projectTemplate");
templates.forEach(template => {
  const option = document.createElement("option");
  option.value = template;
  option.text = template;
  templateSelect.add(option);
});
</script>

## AWS Lambda Quickstart

- [aws-lambda-quickstart](https://github.com/michaelbrewer/aws-lambda-quickstart) - A simple webservice to generate projects from various templates.
