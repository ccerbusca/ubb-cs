package web.servlets;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.ServletRequestUtils;
import web.domain.Comment;
import web.domain.Topic;
import web.repositories.CommentRepository;
import web.repositories.TopicRepository;
import web.servlets.utils.ServletUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/comment/delete")
public class DeleteComment extends HttpServlet {

    @Autowired
    private CommentRepository commentRepository;

    @Autowired
    private TopicRepository topicRepository;

    @Autowired
    private ServletUtils servletUtils;

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Long id = ServletRequestUtils.getLongParameter(req, "id");
        if (id != null) {
            Comment comment = commentRepository.findById(id).orElseThrow();
            commentRepository.delete(comment);
            resp.sendRedirect(req.getContextPath() + "/topic?id="+comment.getTopic().getId());
        } else {
            servletUtils.badRequest(resp, "csf");
        }
    }


}
