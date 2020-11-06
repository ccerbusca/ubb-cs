package web.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import web.domain.Comment;

import java.util.List;

public interface CommentRepository extends JpaRepository<Comment, Long> {

    List<Comment> findByTopic_IdOrderByTimestampDesc(Long topic_id);

}
