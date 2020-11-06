<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    Boolean logged = (Boolean) session.getAttribute("logged");
    if(logged != null && logged) {
        response.sendRedirect(request.getContextPath() + "/forum.jsp");
    }
%>
<form action="register" method="post">
    <div>
        <label for="username">Username: </label>
        <input type="text" id="username" name="username">
    </div>
    <label for="password">Password: </label>
    <input type="password" id="password" name="password">
    <input type="submit" value="Register">
</form>
<p>
    Already have an account? Click <a href="login.jsp">here</a> to log in.
</p>
