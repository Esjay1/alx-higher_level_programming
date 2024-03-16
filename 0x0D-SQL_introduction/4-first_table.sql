-- Create a table in the current database. If the
-- table exists, this script will not fail.
DROP TABLE IF EXISTS first_table;
CREATE TABLE first_table(
	id INT,
	name VARCHAR(256)
);

