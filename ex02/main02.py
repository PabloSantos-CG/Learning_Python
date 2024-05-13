from typing import Tuple

def create_team(team_name: str, *players: Tuple[str]):
  return { "Name": team_name, "Players": players }

def execute():
  teams = []
  new_teams = create_team(22, "Mike", "Tyson Jr.", "Brand Jr.")
  teams.append(new_teams)
  print(teams)

execute()