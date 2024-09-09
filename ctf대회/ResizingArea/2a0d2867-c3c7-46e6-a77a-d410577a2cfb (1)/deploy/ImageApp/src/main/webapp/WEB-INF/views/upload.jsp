<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>File Upload</title>
</head>
<body>
<h2>File Upload Form</h2>
<form method="post" action="/image/upload" enctype="multipart/form-data">
    <input type="file" name="file" />
    <input type="submit" value="Upload" />
</form>

<c:if test="${not empty message}">
    <p>${message}</p>
</c:if>
</body>
</html>
