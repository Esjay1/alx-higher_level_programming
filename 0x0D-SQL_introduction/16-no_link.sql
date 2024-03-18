-- This script lists all records of the table
-- second_table of the hbtn_0c_0 database and does 
-- not list rows without a name value.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

