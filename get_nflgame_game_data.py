import os
os.chdir('nflgame')  # TODO: Relative import not working from top level directory, so this is a hack around it.
import nflgame

years = [2017, 2018]
weeks = [i+1 for i in range(17)]

for y in years:
	for w in weeks:
		# TODO: Figure out why y=2018 with w=4 doesn't work here.
		games = nflgame.games(y, w)
		plays = nflgame.combine_plays(games)
		player_data = plays.players()
		player_data.csv('../data/nflgame/game-level-raw/'+str(y)+'-'+str(w)+'-'+'game-level-data.csv')