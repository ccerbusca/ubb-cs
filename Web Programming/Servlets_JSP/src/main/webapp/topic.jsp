<%--
  Created by IntelliJ IDEA.
  User: crist
  Date: 2020-05-21
  Time: 4:20 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    Boolean logged = (Boolean) session.getAttribute("logged");
    if(logged == null || !logged) {
        response.sendRedirect(request.getContextPath() + "/register.jsp");
    }
%>
<html>
<head>
    <title>${topic.title}</title>
</head>
<body>
    <form action="forum">
        <input type="submit" value="Back to forum">
    </form>
    <div style="border-style: solid">
        <p>"${topic.title}" started by ${topic.author.username}</p>
        <br/>
        <p>${topic.body}</p>
    </div>
    <c:forEach items="${topic.comments}" var="comment">
        <div style="margin-left: 4rem; border-style: dashed">
            <p>${comment.content}</p>
            <br/>
            <p style="font-size: small">Author: ${comment.author.username}</p>
            <c:if test="${sessionScope.user_id == comment.author.id}">
                <form action="comment/delete" method="post">
                    <button type="submit" name="id" value="${comment.id}">Delete</button>
                </form>
            </c:if>
        </div>
    </c:forEach>
    <form action="topic" method="post">
        <label for="text" style="display: block">Comment:</label>
        <textarea id="text" name="text" required></textarea>
        <button type="submit" name="id" value="${topic.id}">Post</button>
    </form>
</body>
</html>
