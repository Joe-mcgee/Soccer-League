#league_builder.py
import csv
import random

#non-execute on import
if __name__ == "__main__":
    
    leagueteamkeys = ['Sharks', 'Dragons', 'Raptors']
    leagueteamvalues = [ [], [], [] ]
    
    # Create an orderedDict of players from the CSV file
    with open('soccer_players.csv', newline='') as csvfile:
            soccerreader = csv.DictReader(csvfile, delimiter=',')
            league = list(soccerreader)

    # Shuffle the order of the list of players
    random.shuffle(league)
    
    # Logic which separates the experinced and inexperienced into 3 teams evenly.
    count = 0
    #point to player in league
    for player in league:
        # if this player's soccer experience key has a value yes
        if player['Soccer Experience'] == 'YES':
            # append this player too a list of lists, which list given by the count, which iterates to evenly distribute
            leagueteamvalues[count].append(player)
            count += 1    
            #resets the count
            if count == 3:
                count = 0
             
    for player in league:
        if player['Soccer Experience'] != 'YES':
            leagueteamvalues[count].append(player)
            count += 1
            if count ==3:
                count = 0
                    
    # makes a dictionary of the league. teams are keys and players are values
    leagueteams = dict(zip(leagueteamkeys, leagueteamvalues))
        
    # writes the league into a text file in a format similar to instructions
    with open("teams.txt", "w+") as writer:
        for key, value in leagueteams.items():
            if key == 'Sharks':
                writer.writelines('Sharks: \n')
                for player in value:
                    writer.writelines('{}\n'.format(player))
            if key == 'Raptors':
                writer.writelines('\nRaptors: \n')
                for player in value:
                    writer.writelines('{}\n'.format(player))
            if key == 'Dragons':
                writer.writelines('\nDragons: \n')
                for player in value:
                    writer.writelines('{}\n'.format(player))
                
                
    writer.close()
        
    
        
    
    
