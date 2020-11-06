package web.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import web.domain.Topic;

public interface TopicRepository extends JpaRepository<Topic, Long> {
}
