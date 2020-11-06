<%--
  Created by IntelliJ IDEA.
  User: crist
  Date: 2020-05-21
  Time: 1:35 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<c:set var="req" value="${pageContext.request}" />

<%
    Boolean logged = (Boolean) session.getAttribute("logged");
    if(logged == null || !logged) {
        response.sendRedirect(request.getContextPath() + "/register.jsp");
    }
%>
<html>
<head>
    <title>Forum</title>
    <script src="jquery-3.5.0.min.js"></script>
</head>
<body>
    <form action="logout" method="post">
        <input type="submit" value="Logout">
    </form>
    <form action="create_topic.jsp" method="post">
        <input type="submit" value="Create topic">
    </form>
    <c:forEach items="${topics}" var="topic">
        <div>
            <p>${topic.title}</p>
            <form action="topic">
                <button type="submit"  name="id" value="${topic.id}" style="display: block">Browse</button>
            </form>
            <c:if test="${sessionScope.user_id == topic.author.id}">
                <form action="topic/delete" method="post">
                    <button type="submit" name="id" value="${topic.id}">Delete</button>
                </form>
            </c:if>
        </div>
        <hr/>
    </c:forEach>
</body>
</html>
