<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Image Resize</title>
</head>
<body>
<h2>Image Resize</h2>
<form id="resizeForm" onsubmit="resizeImage(event)" enctype="multipart/form-data">
    <label for="width">Width:</label>
    <input type="number" id="width" name="width" required><br><br>

    <label for="height">Height:</label>
    <input type="number" id="height" name="height" required><br><br>

    <input type="hidden" id="filename" name="filename" value="${filename}">

    <button type="submit">Resize Image</button>
    <br>
    <a id="downloadButton" style="display:none;" download>Download Resized Image</a>
</form>

<script>
    async function resizeImage(e) {
        e.preventDefault();

        const form = document.getElementById('resizeForm');
        const formData = new FormData(form);

        const response = await fetch('${pageContext.request.contextPath}/api/image/resize', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.result === 'success') {
            document.getElementById('downloadButton').style.display = 'block';
            document.getElementById('downloadButton').href = result.downloadUrl;
        } else {
            alert('Image resize failed: ' + result.message);
        }
    }
</script>
</body>
</html>
