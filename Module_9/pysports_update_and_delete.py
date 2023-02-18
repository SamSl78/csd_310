mport mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="R45fhIps45",
  database="pysports"
)

mycursor = mydb.cursor()

def show_players(mycursor, title):
    """ method to execute an inner join on the player and team table, 
        iterate over the dataset and output the results to the terminal window.
    """

  
    mycursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    
    players = mycursor.fetchall()

    print("\n  -- {} --".format(title))
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))


    
    mycursor = mydb.cursor()

    
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

   
    player_data = ("Smeagol", "Shire Folk", 1)

    mycursor.execute(add_player, player_data)

    
    mydb.commit()

    
    show_players(mycursor, "DISPLAYING PLAYERS AFTER INSERT")

    
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    
    mycursor.execute(update_player)

    
    show_players(mycursor, "DISPLAYING PLAYERS AFTER UPDATE")

    
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    mycursor.execute(delete_player)

 
    show_players(mycursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("Press any key to continue")



mycursor.close()

mydb.close()
