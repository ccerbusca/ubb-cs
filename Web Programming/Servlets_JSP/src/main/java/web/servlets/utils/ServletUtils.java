package web.servlets.utils;

import lombok.SneakyThrows;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletResponse;
import java.io.Writer;

@Component
public class ServletUtils {

    @SneakyThrows
    public void writeBody(HttpServletResponse response, int status, String body)
    {
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        response.setStatus(status);
        Writer writer = response.getWriter();
        writer.write(body);
        writer.flush();
    }

    public void authRequired(HttpServletResponse response)
    {
        writeBody(response, HttpServletResponse.SC_UNAUTHORIZED, "You need to log in");
    }

    public void badRequest(HttpServletResponse response, String reason)
    {
        writeBody(response, HttpServletResponse.SC_BAD_REQUEST, reason);
    }

}
