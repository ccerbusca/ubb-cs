<%--
  Created by IntelliJ IDEA.
  User: crist
  Date: 2020-05-21
  Time: 3:51 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Create Topic</title>
</head>
<body>
    <form action="forum" method="post">
        <div>
            <label for="title">Title: </label>
            <input type="text" id="title" name="title" required>
        </div>
        <label for="title" for="body">Text: </label>
        <textarea id="body" name="body" required></textarea>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
