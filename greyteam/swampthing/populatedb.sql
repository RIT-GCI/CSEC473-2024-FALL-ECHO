-- CREATE DATABASE IF NOT EXISTS hauntedhouse;
-- USE hauntedhouse;

CREATE TABLE IF NOT EXISTS visitors (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    reason_for_visit VARCHAR(100)
);

INSERT IGNORE INTO visitors (name) VALUES
('Arianna S.'),
('Gavin F.'),
('Gavin H.'),
('Jacob S.'),
('Joseph C.'),
('Justin H.'),
('Luke M.'),
('Max F.'),
('Rachel L.'),
('Harrison T.');

CREATE TABLE IF NOT EXISTS room_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    visitor_id INT,
    room_name VARCHAR(50),
    time_entered TIME,
    time_left TIME,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id)
);

INSERT IGNORE INTO room_logs (visitor_id, room_name, time_entered, time_left) VALUES
(1, 'Living Room', '21:00', '21:45'),
(1, 'Office', '21:00', '21:45'),
(2, 'Shed', '21:30', '22:15'),
(2, 'Office', '22:30', '23:15'),
(3, 'Attic', '22:00', '22:15'),
(3, 'Office', '22:30', '23:00'),
(4, 'Office', '22:30', '23:15'),
(5, 'Murder Weapon Storage Room', '22:00', '23:00'),
(5, 'Basement', '21:00', '21:45'),
(6, 'The Perfect Place to Kill Someone', '21:15', '21:45'),
(6, 'Living Room', '22:00', '22:30'),
(7, 'Living Room', '21:30', '22:15'),
(7, 'Attic', '22:30', '22:45'),
(8, 'The Perfect Place to Kill Someone', '21:15', '22:00'),
(8, 'Shed', '22:15', '22:45'),
(9, 'Living Room', '21:00', '21:45'),
(9, 'Murder Weapon Storage Room', '22:00', '23:00'),
(10, 'Office', '21:00', '21:30');

CREATE TABLE IF NOT EXISTS found_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(200),
    room_name VARCHAR(50),
    visitor_id INT,
    FOREIGN KEY (visitor_id) REFERENCES visitors(visitor_id)
);

INSERT IGNORE INTO found_items (description, room_name) VALUES
('Candy', 'Office'),
('Pocket Knife', 'Shed'),
('Lockpick', 'Office'),
('Flashlight', 'Office'),
('Bloodstained Shirt', 'Murder Weapon Storage Room'),
('Rope', 'Living Room'),
('Jack-O-Lantern', 'Attic'),
('Mask', 'The Perfect Place to Kill Someone'),
('Lost Phone', 'Basement'),
('Gun', 'The Perfect Place to Kill Someone');

CREATE TABLE definitely_not_a_flag (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    flag VARCHAR(200),
);

INSERT IGNORE INTO definitely_not_a_flag (flag) VALUES
('FLAG<HOW_DID_YOU_FIND_ME>');
