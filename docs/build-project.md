# Build Project

<script>
function buildProject() {
    const baseUrl = 'https://4v2ies7g1m.execute-api.us-east-2.amazonaws.com/Prod';
    fetch(baseUrl + '/project.zip?name=mouse')
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

<a href="#" onclick="javascript:buildProject()">Build project</a>
