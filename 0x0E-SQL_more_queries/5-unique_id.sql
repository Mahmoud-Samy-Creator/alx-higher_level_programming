-- Create unique_id table with unique attribute
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);