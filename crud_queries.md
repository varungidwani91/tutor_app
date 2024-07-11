## Create Operations

### Insert a New Course
```bash
INSERT INTO course_tutor_course (title, videoUrl, details, transcript, image_link) VALUES ('Introduction to React', 'https://www.youtube.com/embed/Tn6-PIqc4UM', 'React is a popular JavaScript library for building user interfaces. This introductory topic covers the basics of React, its core concepts, and why it\'s widely used in modern web development.', 'Welcome to the Introduction to React. In this video, we\'ll cover the fundamental concepts of React, including components, JSX, and the virtual DOM. We\'ll also discuss why React has become so popular among developers and how it can help you build efficient, scalable user interfaces.', 'https://asktech.io/wp-content/uploads/2023/05/10003.png');
```

### Insert a New Question
```bash
INSERT INTO course_tutor_question (course_id, question_text) VALUES (1, 'What is React?');
```

### Insert a New Choice
```bash
INSERT INTO course_tutor_choice (question_id, choice_text, is_correct) VALUES (1, 'A JavaScript library for building user interfaces', TRUE);
```

### Insert a New Submission
```bash
INSERT INTO course_tutor_submission (user_id, question_id, selected_choice_id, is_correct) VALUES (1, 1, 1, TRUE);
```

## Read Operations

### Select All Courses
```bash
SELECT id, title, videoUrl, details, transcript, image_link FROM course_tutor_course;
```

### Select a Specific Course by ID
```bash
SELECT id, title, videoUrl, details, transcript, image_link FROM course_tutor_course WHERE id = 1;
```

### Select All Questions for a Specific Course
```bash
SELECT id, course_id, question_text FROM course_tutor_question WHERE course_id = 1;
```

### Select All Choices for a Specific Question
```bash
SELECT id, question_id, choice_text, is_correct FROM course_tutor_choice WHERE question_id = 1;
```

## Update Operations

### Update a Course
```bash
UPDATE course_tutor_course SET title = 'Advanced React', videoUrl = 'https://www.youtube.com/embed/advanced-react', details = 'This course covers advanced topics in React.', transcript = 'Welcome to the Advanced React course.', image_link = 'https://asktech.io/wp-content/uploads/2023/05/10004.png' WHERE id = 1;
```

### Update a Question
```bash
UPDATE course_tutor_question SET question_text = 'What is the virtual DOM?' WHERE id = 1;
```

### Update a Choice
```bash
UPDATE course_tutor_choice SET choice_text = 'A lightweight copy of the actual DOM', is_correct = TRUE WHERE id = 1;
```

### Update a Submission
```bash
UPDATE course_tutor_submission SET selected_choice_id = 2, is_correct = FALSE WHERE id = 1;
```

## Delete Operations

### Delete a Course
```bash
DELETE FROM course_tutor_course WHERE id = 1;
```

### Delete a Question
```bash
DELETE FROM course_tutor_question WHERE id = 1;
```

### Delete a Choice
```bash
DELETE FROM course_tutor_choice WHERE id = 1;
```

### Delete a Submission
```bash
DELETE FROM course_tutor_submission WHERE id = 1;
```
