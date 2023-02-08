import requests
from bs4 import BeautifulSoup

URL = 'https://www.espn.com/nba/standings'

response = requests.get(URL)
page = response.text

soup = BeautifulSoup(page, "html.parser")
teams = soup.find_all(class_='hide-mobile')
wins = soup.find_all(class_='stat-cell')

start = 0
end = 13
num = 1

eastern_teams = {}
for eastern_team in teams[0:15]:
    eastern_teams[f"{num}. {eastern_team.text}"] = [x.text for x in wins[start:end]]
    start += 13
    end += 13
    num += 1
print("Eastern Conference")
print(eastern_teams)

num = 1
western_teams = {}
for western_team in teams[15:31]:
    western_teams[f"{num}. {western_team.text}"] = [x.text for x in wins[start:end]]
    start += 13
    end += 13
    num += 1

print("Western Conference")
print(western_teams)
