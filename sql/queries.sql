-- 1. Завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- 2. Завдання зі статусом 'new'
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновити статус
UPDATE tasks SET status_id = 2 WHERE id = 1;

-- 4. Користувачі без завдань
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5. Додати нове завдання
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task', 'Test desc', 1, 3);

-- 6. Завдання, які не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити завдання
DELETE FROM tasks WHERE id = 1;

-- 8. Користувачі за доменом
SELECT * FROM users WHERE email LIKE '%@example.com';

-- 9. Оновити ім’я
UPDATE users SET fullname = 'New Name' WHERE id = 2;

-- 10. Кількість завдань по статусу
SELECT s.name, COUNT(t.id) FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 11. Завдання користувачів з email доменом
SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 12. Завдання без опису
SELECT * FROM tasks WHERE description IS NULL;

-- 13. Користувачі з завданнями 'in progress'
SELECT u.fullname, t.title FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

-- 14. Кількість завдань кожного користувача
SELECT u.fullname, COUNT(t.id) FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
