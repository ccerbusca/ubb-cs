package web.servlets;

import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.ServletRequestUtils;
import web.domain.Comment;
import web.domain.Topic;
import web.domain.TopicDTO;
import web.domain.User;
import web.repositories.CommentRepository;
import web.repositories.TopicRepository;
import web.repositories.UserRepository;
import web.servlets.utils.ServletUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/topic")
@Slf4j
public class TopicServlet extends HttpServlet {

    @Autowired
    private TopicRepository topicRepository;

    @Autowired
    private CommentRepository commentRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private ServletUtils servletUtils;

    @Override
    @SneakyThrows
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
        Long id = ServletRequestUtils.getLongParameter(req, "id");
        if (id != null) {
            Topic topic = topicRepository.findById(id).orElseThrow();
            TopicDTO build = TopicDTO.builder()
                    .id(topic.getId())
                    .author(topic.getAuthor())
                    .body(topic.getBody())
                    .title(topic.getTitle())
                    .comments(commentRepository.findByTopic_IdOrderByTimestampDesc(id))
                    .build();
            req.setAttribute("topic", build);
            req.setAttribute("id", topic.getId());
            req.getRequestDispatcher("topic.jsp?id=" + topic.getId()).forward(req, resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Long id = ServletRequestUtils.getLongParameter(req, "id");
        String text = ServletRequestUtils.getStringParameter(req, "text");
        if (id != null && text != null) {
            Long userId = (Long) req.getSession().getAttribute("user_id");
            User user = userRepository.findById(userId).orElseThrow();
            Topic topic = topicRepository.findById(id).orElseThrow();
            Comment comment = Comment.builder().author(user).topic(topic).content(text).build();
            commentRepository.save(comment);
            resp.sendRedirect("topic?id=" + topic.getId());
        } else {
            servletUtils.badRequest(resp, "csf");
        }
    }
}
