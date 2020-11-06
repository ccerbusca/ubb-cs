package web.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import web.domain.User;

public interface UserRepository extends JpaRepository<User, Long> {

    User findUserByUsername(String username);

}
