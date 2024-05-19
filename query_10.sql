SELECT subjects.name AS subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Ім\'я студента' AND teachers.name = 'Ім\'я викладача';
