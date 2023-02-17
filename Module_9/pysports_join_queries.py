import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="R45fhIps45",
  database="pysports"
)

mycursor = mydb.cursor()



mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")


players = mycursor.fetchall()

print("DISPLAYING PLAYER RECORDS")

for player in players:
    print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))




input("Press any key to continue")




mycursor.close()

mydb.close()
