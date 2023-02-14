import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="R45fhIps45",
  database="pysports"
)


  



mycursor = mydb.cursor()

mycursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = mycursor.fetchall()

print("DISPLAYING TEAM RECORDS")

for team in teams: 
    print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

mycursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = mycursor.fetchall()

print ("DISPLAYING PLAYER RECORDS")

for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

mycursor.close()

mydb.close()
    
input("Press any key to continue")
