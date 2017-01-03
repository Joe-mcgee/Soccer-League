#league_builder.py
import csv
import random

#non-execute on import
if __name__ == "__main__":
    
    leagueteamkeys = ['Sharks', 'Dragons', 'Raptors']
    leagueteamvalues = [ [], [], [] ]
    
    with open('soccer_players.csv', newline='') as csvfile:
            soccerreader = csv.DictReader(csvfile, delimiter=',')
            league = list(soccerreader)

    
    random.shuffle(league)
    count = 0
    for player in league:
        if player['Soccer Experience'] == 'YES':
            leagueteamvalues[count].append(player)
            count += 1    
            
            if count == 3:
                count = 0
             
    for player in league:
        if player['Soccer Experience'] != 'YES':
            leagueteamvalues[count].append(player)
            count += 1
            if count ==3:
                count = 0
                    
    leagueteams = dict(zip(leagueteamkeys, leagueteamvalues))
        
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
        
    
        
    
    
