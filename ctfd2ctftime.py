import json

def scores():
    json1 = {'standings': []}

    #go through CSV file and grab place, team name, and score from columns 1, 2, and 4 and ignore the rest
    with open('scores.csv', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                place, team, teamid, score = line.split(',')[:4]
                if team == "":
                    #skip
                    continue
                json1['standings'].append({'pos': int(place), 'team': team, 'score': int(score)})

    #save to file
    with open('scores.json', 'w') as f:
        json.dump(json1, f)

scores()
print("Done")
