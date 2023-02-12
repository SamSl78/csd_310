DROP USER IF EXISTS 'pysports_user'@'localhost';



CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';


GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';



DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;



CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(100)     NOT NULL,
    mascot      VARCHAR(100)     NOT NULL,
    PRIMARY KEY(team_id)
); 


CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(100)     NOT NULL,
    last_name   VARCHAR(100)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);



INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');



INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Thorin', 'Oakenshield', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Saruman', 'The White', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-king', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Azog', 'The Defiler', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));


import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}




try:
  

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

   
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

     
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")

    
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

   
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    

    db.close()
