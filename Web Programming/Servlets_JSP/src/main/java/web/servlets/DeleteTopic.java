package web.servlets;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.ServletRequestUtils;
import web.repositories.TopicRepository;
import web.servlets.utils.ServletUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/topic/delete")
public class DeleteTopic extends HttpServlet {

    @Autowired
    private TopicRepository topicRepository;

    @Autowired
    private ServletUtils servletUtils;

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Long id = ServletRequestUtils.getLongParameter(req, "id");
        if (id != null) {
            topicRepository.deleteById(id);
            resp.sendRedirect(req.getContextPath() + "/forum");
        } else {
            servletUtils.badRequest(resp, "csf");
        }
    }
}
