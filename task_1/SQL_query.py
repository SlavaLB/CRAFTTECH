import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.executescript(
    """
    DROP TABLE IF EXISTS Orders;
    DROP TABLE IF EXISTS Users;
    
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    );
    
    CREATE TABLE Orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        total_amount REAL,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );
    
    INSERT INTO Users (id, name, email) VALUES
    (1, 'Иван', 'ivan@example.com'),
    (2, 'Мария', 'maria@example.com'),
    (3, 'Алексей', 'alex@example.com'),
    (4, 'Ольга', 'olga@example.com');
    
    INSERT INTO Orders (id, user_id, total_amount) VALUES
    (1, 1, 500),
    (2, 1, 600),
    (3, 2, 200),
    (4, 2, 900),
    (5, 3, 300),
    (6, 4, 1100);
    """
)

cursor.execute(
    """
    SELECT u.name, SUM(o.total_amount) AS total_spent
    FROM Users u
    JOIN Orders o ON u.id = o.user_id
    GROUP BY u.id
    HAVING SUM(o.total_amount) > 1000;
    """
)

print("Пользователи с суммой заказов более 1000 рублей:")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
