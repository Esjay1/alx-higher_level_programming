-- This script converts hbtn_0c_0 database to 
-- UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Database conversion to utf8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- Table conversion to utf8mb4
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

--Column conversion to utf8mb4
ALTER TABLE first_table
change name name VARCHAR(255)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

