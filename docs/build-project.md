# Build Project

!!! info
    A simple tool to generate a starter project based on a template.

<script>
function buildProject() {
    const form = document.getElementById("buildProjectForm");
    const prjName = form.elements["name"].value || "foo-service";
    const prjType = form.elements["type"].value;
    const prjRuntime = form.elements["runtime"].value;
    const prjTrigger = form.elements["trigger"].value;
    const prjMemory = form.elements["memory"].value || "512";
    const prjTimeout = form.elements["timeout"].value || "25";

    const baseUrl = 'https://4v2ies7g1m.execute-api.us-east-2.amazonaws.com/Prod';
    const uri = '/project.zip?name=' + prjName + '&type=' + prjType + '&runtime=' + prjRuntime + '&trigger=' + prjTrigger + '&memory=' + prjMemory + '&timeout=' + prjTimeout;

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
</style>
<form id="buildProjectForm">
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
    <option value="rest-api" selected>API Gateway Rest API</option>
    <option value="http-api">API Gateway Rest API</option>
    <option value="s3">S3 Bucket Event Notification</option>
  </select>
  <br/>
  <label for="projectMemory">Memory in MB :</label> <input id="projectMemory" name="memory" value="512"><br/>
  <label for="projectTimeout">Timeout in seconds :</label> <input id="projectTimeout" name="timeout" value="25"><br/>
  <br/><a href="#" onclick="javascript:buildProject()" class="md-button md-button--primary">Generate Project</a>
</form>

## AWS Lambda Quickstart

- [aws-lambda-quickstart](https://github.com/michaelbrewer/aws-lambda-quickstart) - A simple webservice to generate projects from various templates.
