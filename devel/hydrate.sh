#!/bin/bash

echo "WAITING FOR MYSQL SERVER..."
sleep 10
mysql -h 127.0.0.1 -f --user='root' --password='secret' -D dbmigrate -e "
    CREATE TABLE IF NOT EXISTS dbmigrate.accounts (
        id INT NOT NULL AUTO_INCREMENT,
        username VARCHAR(255) NOT NULL,
        fname VARCHAR(255) NOT NULL,
        lname VARCHAR(255) NOT NULL,
        is_active TINYINT DEFAULT 1,
        PRIMARY KEY (id)
    );
    ALTER TABLE dbmigrate.accounts ADD UNIQUE KEY uk_accounts_user (username, fname, lname);
    ALTER TABLE dbmigrate.accounts ADD UNIQUE KEY uk_accounts_username (username);
    INSERT INTO dbmigrate.accounts (username, fname, lname) VALUES ('username-01', 'John', 'Doe');
    INSERT INTO dbmigrate.accounts (username, fname, lname) VALUES ('username-02', 'Jane', 'Doe');
    INSERT INTO dbmigrate.accounts (username, fname, lname) VALUES ('username-03', 'Billy', 'Doe');
    INSERT INTO dbmigrate.accounts (username, fname, lname) VALUES ('username-04', 'Sally', 'Doe');
    INSERT INTO dbmigrate.accounts (username, fname, lname) VALUES ('username-05', 'Ruff', 'Doe');

    CREATE TABLE IF NOT EXISTS dbmigrate.events (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        user_id INT NOT NULL,
        PRIMARY KEY (id)
    );
    INSERT INTO dbmigrate.events (name, user_id) VALUES ('Test Event 1', 2);
    INSERT INTO dbmigrate.events (name, user_id) VALUES ('Test Event 1 - Updated', 2);
    INSERT INTO dbmigrate.events (name, user_id) VALUES ('Test Event 3', 4);
"
