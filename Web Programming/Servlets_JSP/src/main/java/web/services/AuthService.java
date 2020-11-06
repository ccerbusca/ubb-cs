package web.services;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import web.domain.User;
import web.repositories.UserRepository;

import javax.servlet.http.HttpServletResponse;

@Component
public class AuthService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public AuthService(UserRepository userRepository, PasswordEncoder passwordEncoder)
    {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public boolean register(String username, String password)
    {
        if (userRepository.findUserByUsername(username) == null)
        {
            userRepository.save(User.builder()
                    .username(username).password(passwordEncoder.encode(password)).build());
            return true;
        }
        return false;
    }

    public Long login(String username, String password) {
        User user = userRepository.findUserByUsername(username);
        if (user != null)
        {
            return passwordEncoder.matches(password, user.getPassword()) ? user.getId() : null;
        }
        else
            return null;
    }
}
