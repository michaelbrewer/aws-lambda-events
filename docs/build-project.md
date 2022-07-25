# Build Project

A simple tool to generate a starter project based on cookiecutter templates.

???+ WARNING "Warning: Still a work in progress"
    This is still in progress and is not yet ready for production use :).

<script>
function buildProject(form, path) {
    const name = form.elements["name"].value || "foo-service";
    const type = form.elements["type"].value || "sam";
    const memory = form.elements["memory"].value || "512";
    const timeout = form.elements["timeout"].value || "25";
    const architecture = form.elements["architecture"].value || "x86_64";
    const runtime = form.elements["runtime"].value;
    const trigger = form.elements["trigger"].value;
    let template = form.elements["template"].value;
    if (template !== "") {
      template = "aws-sam-cli-app-templates/" + template;
    }
    const baseUrl = 'https://4v2ies7g1m.execute-api.us-east-2.amazonaws.com/Prod';
    const uri = '/' + path + '?name=' + name + '&type=' + type + '&runtime=' + runtime + '&trigger=' + trigger + '&memory=' + memory + '&timeout=' + timeout + '&template=' + template + '&architecture=' + architecture;

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
  "nodejs14.x/cookiecutter-aws-sam-hello-powertools-typescript-nodejs",
  "nodejs14.x/cookiecutter-quick-start-cloudwatch-events",
  "nodejs14.x/cookiecutter-aws-sam-step-functions-sample-app",
  "nodejs14.x/cookiecutter-quick-start-from-scratch",
  "nodejs14.x/cookiecutter-quick-start-sns",
  "nodejs14.x/cookiecutter-quick-start-s3",
  "nodejs14.x/cookiecutter-quick-start-sqs",
  "nodejs14.x/cookiecutter-aws-sam-hello-typescript-nodejs",
  "nodejs14.x/cookiecutter-quick-start-web",
  "nodejs16.x-image/cookiecutter-aws-sam-hello-nodejs-lambda-image",
  "nodejs16.x/cookiecutter-aws-sam-hello-nodejs",
  "nodejs16.x/cookiecutter-aws-sam-hello-typescript-nodejs",
  "nodejs16.x/cookiecutter-aws-sam-step-functions-sample-app",
  "nodejs16.x/cookiecutter-quick-start-cloudwatch-events",
  "nodejs16.x/cookiecutter-quick-start-from-scratch",
  "nodejs16.x/cookiecutter-quick-start-s3",
  "nodejs16.x/cookiecutter-quick-start-sns",
  "nodejs16.x/cookiecutter-quick-start-sqs",
  "nodejs16.x/cookiecutter-quick-start-web",
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
  "go1.x/cookiecutter-aws-sam-eventbridge-hello-golang",
  "go1.x/cookiecutter-aws-sam-eventbridge-schema-app-golang",
  "go1.x/cookiecutter-aws-sam-hello-golang",
  "go1.x/cookiecutter-aws-sam-hello-step-functions-sample-app",
  "dotnet6/cookiecutter-aws-sam-hello-dotnet",
  "dotnet6/cookiecutter-aws-sam-hello-powershell",
  "dotnet6/cookiecutter-aws-sam-hello-step-functions-sample-app",
  "dotnet6/cookiecutter-aws-sam-quick-start-cloudwatch-events-dotnet",
  "dotnet6/cookiecutter-aws-sam-quick-start-from-scratch-dotnet",
  "dotnet6/cookiecutter-aws-sam-quick-start-sqs-dotnet",
  "dotnet6/cookiecutter-aws-sam-quick-start-web-dotnet",
  "dotnet6/cookiecutter-aws-sam-quickstart-sns-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-s3-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-cloudwatch-events-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-step-functions-sample-app",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-powershell",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sns-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-hello-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-web-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-from-scratch-dotnet",
  "dotnetcore3.1/cookiecutter-aws-sam-quick-start-sqs-dotnet",
  "provided.al2/graalvm/java11/cookiecutter-aws-sam-graalvm-gradle",
  "provided.al2/graalvm/java11/cookiecutter-aws-sam-graalvm-maven",
  "provided.al2/graalvm/java17/cookiecutter-aws-sam-graalvm-gradle",
  "provided.al2/graalvm/java17/cookiecutter-aws-sam-graalvm-maven"
];
function runtimeChange() {
  const form = document.getElementById('buildSamProjectForm');
  const selectedRuntime = form.elements["runtime"].value;
  const templateSelect = document.getElementById("projectTemplate");
  templateSelect.innerHTML = "";
  templates.forEach(template => {
    if (template.startsWith(selectedRuntime)) {
      const option = document.createElement("option");
      option.value = template;
      option.text = template.replace(selectedRuntime + "/", "");
      templateSelect.appendChild(option);
    }
  });
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

## Powertools Initializer

[AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/) project generator

<form id="buildProjectForm">
  <input id="template" type="hidden" value=""/>
  <label for="projectName">Project Name :</label><input id="projectName" name="name" value="example-service"><br/>
  <label for="projectType">Type :</label>
  <select id="projectType" name="type">
    <option value="sam" selected>SAM Template</option>
    <option value="cdk">AWS CDK (TODO)</option>
  </select>
  <br/>
  <label for="projectType">Runtime :</label>
  <select id="projectRuntime" name="runtime">
    <option value="python3.9" selected>Python 3.9</option>
    <option value="typescript">Java (TODO)</option>
    <option value="typescript">Typescript (TODO)</option>
  </select>
  <br/>
  <label for="projectTrigger">Trigger :</label>
  <select id="projectTrigger" name="trigger">
    <option value="s3" selected>S3</option>
    <option value="s3-object-lambda">S3 Object Lambda</option>
    <option value="rest-api">API GW Rest API</option>
    <option value="rest-api">AppSync Resolver (TODO)</option>
    <option value="rest-api">API GW Http API (TODO)</option>
    <option value="rest-api">AppSync Authorizer (TODO)</option>
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

## AWS SAM Initializer

AWS SAM templates used at [aws-sam-cli-app-templates](https://github.com/aws/aws-sam-cli-app-templates){target="_blank"} github repo.

<form id="buildSamProjectForm">
  <input name="type" type="hidden" value="sam"/>
  <input id="trigger" type="hidden" value=""/>
  <label for="projectName">Project Name :</label><input id="projectName" name="name" value="example-service"><br/>
  <label for="projectRuntime">Runtime :</label>
  <select id="projectRuntime" name="runtime" onchange="runtimeChange()">
    <option value="dotnetcore3.1">.NET Core 3.1</option>
    <option value="dotnet6">.NET 6</option>
    <option value="go1.x">Go 1.x</option>
    <option value="java8.al2">Java 8 (AL2)</option>
    <option value="java11">Java 11</option>
    <option value="nodejs12.x">Node 12</option>
    <option value="nodejs14.x">Node 14</option>
    <option value="nodejs16.x">Node 16</option>
    <option value="python3.7">Python 3.7</option>
    <option value="python3.8">Python 3.8</option>
    <option value="python3.9" selected>Python 3.9</option>
    <option value="ruby2.7">Ruby 2.7</option>
    <option value="provided.al2">Provided</option>
  </select>
  <br/>
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
  <br/><a href="#aws-sam-template" onclick="javascript:buildProject(document.getElementById('buildSamProjectForm'), 'sam-project.zip')" class="md-button md-button--primary">Generate Project</a>
</form>
<script>
runtimeChange();
</script>

## AWS Lambda Quickstart TODO

[aws-lambda-quickstart](https://github.com/michaelbrewer/aws-lambda-quickstart) is a simple webservice to generate projects from various templates.

- [X] Initial prototype webservice
- [X] Create basic UI and deploy via GitHub pages
- [X] Powertools template for s3 api (`quickstart-s3-sam-python`)
- [X] Powertools template for s3 object lambda api (`quickstart-s3-object-lambda-sam-python`)
- [ ] Powertools template for rest api (`quickstart-rest-api-sam-python`)
- [ ] Powertools template for http api (`quickstart-http-api-sam-python`)
- [ ] Mock a better UI mock using figma
- [ ] BONUS: Powertools template for rest api (`quickstart-rest-api-sam-typescript`)
- [ ] BONUS: Powertools template for http api (`quickstart-http-api-sam-typescript`)
- [ ] BONUS: Powertools template for s3 api (`quickstart-s3-sam-typescript`)
- [ ] BONUS: Powertools CDK templates
