#!/bin/bash

### Create Operations

# Insert a New Course
psql <<EOF
INSERT INTO course_tutor_course (title, videoUrl, details, transcript, image_link) VALUES ('Introduction to React', 'https://www.youtube.com/embed/Tn6-PIqc4UM', 'React is a popular JavaScript library for building user interfaces. This introductory topic covers the basics of React, its core concepts, and why it\'s widely used in modern web development.', 'Welcome to the Introduction to React. In this video, we\'ll cover the fundamental concepts of React, including components, JSX, and the virtual DOM. We\'ll also discuss why React has become so popular among developers and how it can help you build efficient, scalable user interfaces.', 'https://asktech.io/wp-content/uploads/2023/05/10003.png');
EOF

# Insert a New Question
psql <<EOF
INSERT INTO course_tutor_question (course_id, question_text) VALUES (1, 'What is React?');
EOF

# Insert a New Choice
psql <<EOF
INSERT INTO course_tutor_choice (question_id, choice_text, is_correct) VALUES (1, 'A JavaScript library for building user interfaces', TRUE);
EOF

# Insert a New Submission
psql <<EOF
INSERT INTO course_tutor_submission (user_id, question_id, selected_choice_id, is_correct) VALUES (1, 1, 1, TRUE);
EOF

### Read Operations

# Select All Courses
psql <<EOF
SELECT id, title, videoUrl, details, transcript, image_link FROM course_tutor_course;
EOF

# Select a Specific Course by ID
psql <<EOF
SELECT id, title, videoUrl, details, transcript, image_link FROM course_tutor_course WHERE id = 1;
EOF

# Select All Questions for a Specific Course
psql <<EOF
SELECT id, course_id, question_text FROM course_tutor_question WHERE course_id = 1;
EOF

# Select All Choices for a Specific Question
psql <<EOF
SELECT id, question_id, choice_text, is_correct FROM course_tutor_choice WHERE question_id = 1;
EOF

### Update Operations

# Update a Course
psql <<EOF
UPDATE course_tutor_course SET title = 'Advanced React', videoUrl = 'https://www.youtube.com/embed/advanced-react', details = 'This course covers advanced topics in React.', transcript = 'Welcome to the Advanced React course.', image_link = 'https://asktech.io/wp-content/uploads/2023/05/10004.png' WHERE id = 1;
EOF

# Update a Question
psql <<EOF
UPDATE course_tutor_question SET question_text = 'What is the virtual DOM?' WHERE id = 1;
EOF

# Update a Choice
psql <<EOF
UPDATE course_tutor_choice SET choice_text = 'A lightweight copy of the actual DOM', is_correct = TRUE WHERE id = 1;
EOF

# Update a Submission
psql <<EOF
UPDATE course_tutor_submission SET selected_choice_id = 2, is_correct = FALSE WHERE id = 1;
EOF

### Delete Operations

# Delete a Course
psql <<EOF
DELETE FROM course_tutor_course WHERE id = 1;
EOF

# Delete a Question
psql <<EOF
DELETE FROM course_tutor_question WHERE id = 1;
EOF

# Delete a Choice
psql <<EOF
DELETE FROM course_tutor_choice WHERE id = 1;
EOF

# Delete a Submission
psql <<EOF
DELETE FROM course_tutor_submission WHERE id = 1;
EOF
