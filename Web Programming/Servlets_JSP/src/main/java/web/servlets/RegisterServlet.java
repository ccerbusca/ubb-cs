package web.servlets;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.ServletRequestUtils;
import web.services.AuthService;
import web.servlets.utils.ServletUtils;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {

    private final ObjectMapper objectMapper;
    private final AuthService authService;
    private final ServletUtils servletUtils;

    public RegisterServlet(ObjectMapper objectMapper, AuthService authService, ServletUtils servletUtils)
    {
        this.objectMapper = objectMapper;
        this.authService = authService;
        this.servletUtils = servletUtils;
    }

    @Override
    @SneakyThrows
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        if (username != null && password != null)
        {
            if (authService.register(username, password))
            {
                resp.sendRedirect(req.getContextPath() + "/login.jsp");
            }
            else
            {
                servletUtils.badRequest(resp, "User already exists");
            }
        }
        else
        {
            servletUtils.badRequest(resp, "No username/password sent");
        }
    }
}
