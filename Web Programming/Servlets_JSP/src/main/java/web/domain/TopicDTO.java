package web.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.ToString;

import java.util.List;

@Builder
@AllArgsConstructor
@Data
public class TopicDTO {
    private Long id;

    private String title;
    private String body;

    @ToString.Exclude
    private List<Comment> comments;

    private User author;
}
