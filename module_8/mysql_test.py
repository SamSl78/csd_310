CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MYSQL8IsGreat!';


GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';

DROP USER IF EXISTS 'pysports_user'@'localhost';







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


DROP TABLE IF EXISTS player;

SELECT team_id FROM team WHERE team_name = 'Team Sauron'




import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()

