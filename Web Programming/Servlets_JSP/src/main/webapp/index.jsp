<%--
  Created by IntelliJ IDEA.
  User: crist
  Date: 2020-05-20
  Time: 6:44 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
  Boolean logged = (Boolean) session.getAttribute("logged");
  if(logged != null && logged) {
    response.sendRedirect(request.getContextPath() + "/forum.jsp");
  } else {
    response.sendRedirect(request.getContextPath() + "/register.jsp");
  }
%>
