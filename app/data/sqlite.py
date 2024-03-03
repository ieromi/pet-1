import sqlite3


connection = sqlite3.connect('pet-1.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_first_name VARCHAR NOT NULL,
user_patronymic VARCHAR NOT NULL,
user_last_name VARCHAR NOT NULL,
user_dob DATE NOT NULL
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS telephones (
user_tel_num VARCHAR NOT NULL,
is_primary BOOLEAN,
user_id INTEGER
CONSTRAINT fk_users
    FOREIGN KEY (user_id)
    REFERENCES users (user_id)    
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS emails (
user_email VARCHAR NOT NULL,
is_primary BOOLEAN,
user_id INTEGER
CONSTRAINT fk_users
    FOREIGN KEY (user_id)
    REFERENCES users (user_id)    
);
''')


connection.commit()
connection.close()
