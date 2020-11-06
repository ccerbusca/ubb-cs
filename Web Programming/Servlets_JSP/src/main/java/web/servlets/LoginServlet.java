package web.servlets;

import lombok.SneakyThrows;
import web.services.AuthService;
import web.servlets.utils.ServletUtils;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {

    private final AuthService authService;
    private final ServletUtils servletUtils;

    public LoginServlet(AuthService authService, ServletUtils servletUtils)
    {
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
            Long id = authService.login(username, password);
            if (id != null)
            {
                req.getSession().setAttribute("logged", true);
                req.getSession().setAttribute("user_id", id);
                req.getSession().setAttribute("username", username);
                resp.sendRedirect(req.getContextPath() + "/forum");
            }
            else
            {
                servletUtils.badRequest(resp, "Wrong username or password");
            }
        }
        else
        {
            servletUtils.badRequest(resp, "No username/password sent");
        }
    }
}
