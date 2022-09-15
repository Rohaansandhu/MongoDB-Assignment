import pymongo as pm
import json

client = pm.MongoClient()
tim_db = client.tim_db
tim_collection = tim_db.tim_collection

with open("example_tim_data.json") as tim_json:
    tim_dict = json.load(tim_json)

tim_collection.insert_many(tim_dict)

class Team:
    def __init__(self, team_num):
        self.team_num = team_num
    def return_info(self):
        self.balls_scored = []
        self.matches = []
        self.climb_success = []

        for tim in tim_collection.find():
            if tim["team_num"] == self.team_num:
                self.balls_scored.append(tim["num_balls"])
                self.matches.append(tim["match_num"])
                self.climb_success.append(tim["climbed"])
        return {"team_num": self.team_num,  "avg_balls_scored": sum(self.balls_scored) / len(self.balls_scored), "least_balls_scored": min(self.balls_scored), "most_balls_scored": max(self.balls_scored), "num_matches_played": len(self.matches), "percent_climb_success": self.climb_success.count(True) / len(self.climb_success)}

teams = []

for tim in tim_collection.find():
    teams.append(tim["team_num"])

tim_info_collection = tim_db.tim_info_collection

for team in teams:
    team_obj = Team(team)
    tim_info_collection.insert_one(team_obj.return_info())