CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    area_id VARCHAR(50) NOT NULL,
    collection_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS collections (
    collection_id INT AUTO_INCREMENT PRIMARY KEY,
    schedule_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    collection_time DATETIME NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS disposalsites (
    site_id INT AUTO_INCREMENT PRIMARY KEY,
    site_name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    max_capacity INT NOT NULL,
    current_utilization INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);

INSERT INTO schedules (area_id, collection_date)
VALUES
    ('A001 - Downtown', '2025-01-15'),
    ('A002 - Uptown', '2025-01-16'),
    ('A003 - Suburban Heights', '2025-01-17'),
    ('A004 - Riverside', '2025-01-18'),
    ('A005 - Midtown', '2025-01-19'),
    ('A006 - West End', '2025-01-20');

INSERT INTO collections (schedule_id, status, collection_time)
VALUES
    (1, 'Completed', '2025-01-15 10:00:00'),
    (2, 'Missed', '2025-01-16 12:00:00'),
    (3, 'Completed', '2025-01-17 09:30:00'),
    (4, 'Completed', '2025-01-18 11:15:00'),
    (5, 'Completed', '2025-01-19 08:45:00'),
    (6, 'Missed', '2025-01-20 14:00:00');

INSERT INTO disposalsites (site_name, location, max_capacity, current_utilization)
VALUES
    ('Central Disposal', '123 Main Street', 1000, 500),
    ('Eastside Site', '456 East Avenue', 800, 300),
    ('West End Site', '789 West Blvd', 1200, 700),
    ('South Park Site', '101 South Road', 900, 400),
    ('North Valley Site', '202 North Street', 1100, 600);

INSERT INTO notifications (message, created_at)
VALUES
    ('Collection missed for schedule ID 2', '2025-01-16 12:00:00'),
    ('Collection completed for schedule ID 1', '2025-01-15 10:00:00'),
    ('Collection completed for schedule ID 3', '2025-01-17 09:30:00'),
    ('Collection completed for schedule ID 4', '2025-01-18 11:15:00'),
    ('Collection completed for schedule ID 5', '2025-01-19 08:45:00'),
    ('Collection missed for schedule ID 6', '2025-01-20 14:00:00');
