# This seems to work after I modified seq.py so that it works with Python3.  Maybe I should just use Python2.7 for this project.
import nflgame

games = nflgame.games(2018, week=None)
plays = nflgame.combine_plays(games)  # GenPlays object
player_data = plays.players()  # GenPlayerStats object
player_data.csv('player_data.csv')