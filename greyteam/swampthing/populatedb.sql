-- CREATE DATABASE IF NOT EXISTS hauntedhouse;
-- USE hauntedhouse;

CREATE TABLE IF NOT EXISTS visitors (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    reason_for_visit VARCHAR(100)
);

INSERT IGNORE INTO visitors (name, reason_for_visit) VALUES
('Alice', 'Research paranormal activity'),
('Ben', 'Curiosity'),
('Cindy', 'Covering a spooky event'),
('David', 'Studying house’s history'),
('Eve', 'Filming for social media'),
('Frank', 'Working shift'),
('Grace', 'Leading group tour'),
('Hank', 'Complained about noise'),
('Ivy', 'Looking for closure'),
('Jack', 'Checking on property');

CREATE TABLE IF NOT EXISTS room_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    visitor_id INT,
    room_name VARCHAR(50),
    time_entered TIME,
    time_left TIME,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id)
);

INSERT IGNORE INTO room_logs (visitor_id, room_name, time_entered, time_left) VALUES
(1, 'Attic', '21:00', '21:45'),
(2, 'Dining Hall', '21:30', '22:15'),
(3, 'Basement', '22:00', '22:45'),
(4, 'Library', '21:45', '22:30'),
(5, 'Living Room', '22:00', '23:00'),
(6, 'Kitchen', '21:15', '21:45'),
(7, 'Ballroom', '21:30', '22:15'),
(8, 'Garage', '22:00', '22:45'),
(9, 'Garden', '22:15', '22:30'),
(10, 'Study', '21:00', '21:30');

CREATE TABLE found_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(200),
    room_name VARCHAR(50),
    visitor_id INT,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id)
);

INSERT IGNORE INTO found_items (description, room_name, visitor_id) VALUES
('Camera with missing footage', 'Attic', 1),
('Broken vase', 'Dining Hall', 2),
('Blood-stained cloth', 'Basement', 3),
('Old book with torn pages', 'Library', 4),
('Dropped phone', 'Living Room', 5),
('Knife from kitchen set', 'Kitchen', 6),
('Scratched mask', 'Ballroom', 7),
('Screwdriver set', 'Garage', 8),
('Flower pot tipped over', 'Garden', 9),
('Key to locked room', 'Study', 10);