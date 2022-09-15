from statistics import mean
import pymongo
from pymongo.collection import Collection
import json
#setup
'''
client = pymongo.MongoClient("mongodb+srv://eshel:eshel2007@cluster0.qdsghtg.mongodb.net/assignment1")
print("client done")
db = client["assignment1"]
tim: Collection = db["tim"]
team_data = db["team_data"]
'''
with open("MongoDB-Assignment\example_tim_data.json") as f:
    data = json.load(f)

print("json open done")
###tim.insert_many(data)
print("setup done")
#class
class Team():
    def __init__(self, team_number):
        self.team_number = int(team_number)
    def average_balls_scored(self):
        return mean([x["num_balls"] for x in data if x["team_num"]==self.team_number])
    def least_balls_scored(self):
        return min([x["num_balls"] for x in data if x["team_num"]==self.team_number])
    def most_balls_scored(self):
        return max([x["num_balls"] for x in data if x["team_num"]==self.team_number])
    def number_of_matches_played(self):
        return len([x["num_balls"] for x in data if x["team_num"]==self.team_number])
    def percent_climb_sucess(self):
        climbs=[]
        for x in data:
            if x["team_num"]==self.team_number:
                climbs.append(int(x["climbed"]))
        return mean(climbs)
print("team def done")
list_of_teams =[]
for match in data:
    if match["team_num"] not in list_of_teams:
        list_of_teams.append(match["team_num"])
teams=[]
for team in list_of_teams:
    tm = Team(team)
    teams.append({
        "team":tm,
        "team_num":tm.team_number,
        "average_balls_scored":tm.average_balls_scored(),
        "least_balls_scored":tm.least_balls_scored(),
        "most_balls_scored": tm.most_balls_scored(),
        "number_of_matches_played": tm.number_of_matches_played(),
        "percent_climb_success": tm.percent_climb_sucess()})
print(teams)
#team_data.insert_many(teams)