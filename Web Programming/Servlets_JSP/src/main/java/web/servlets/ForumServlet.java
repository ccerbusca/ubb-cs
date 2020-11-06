package web.servlets;

import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.ServletRequestUtils;
import web.domain.Comment;
import web.domain.Topic;
import web.domain.User;
import web.repositories.TopicRepository;
import web.repositories.UserRepository;
import web.servlets.utils.ServletUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/forum")
public class ForumServlet extends HttpServlet {

    @Autowired
    private ServletUtils servletUtils;

    @Autowired
    private TopicRepository topicRepository;

    @Autowired
    private UserRepository userRepository;


    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Boolean logged = (Boolean) req.getSession().getAttribute("logged");
        if (logged != null && logged)
        {
            req.setAttribute("topics", topicRepository.findAll());
            req.getRequestDispatcher("forum.jsp").forward(req, resp);
        }
        else
        {
            resp.sendRedirect(req.getContextPath() + "/login.jsp");
        }
    }

    @Override
    @SneakyThrows
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
        Boolean logged = (Boolean) req.getSession().getAttribute("logged");
        if (logged != null && logged)
        {
            String title = ServletRequestUtils.getStringParameter(req, "title");
            String body = ServletRequestUtils.getStringParameter(req, "body");
            Long userId = (Long) req.getSession().getAttribute("user_id");
            User user = userRepository.findById(userId).orElseThrow();
            if (title == null || body == null) {
                servletUtils.badRequest(resp, "Error happened. Go back try again");
            }
            Topic build = Topic.builder().title(title).body(body).author(user).build();
            topicRepository.save(build);
            req.setAttribute("topic", build);
            req.getRequestDispatcher("topic.jsp").forward(req, resp);
        }
        else
        {
            resp.sendRedirect(req.getContextPath() + "/login.jsp");
        }
    }
}
