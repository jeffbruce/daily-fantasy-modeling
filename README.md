# daily-fantasy-modeling
Modeling daily fantasy NFL football to predict the amount of points players will score each week based on historical data.

## Contents
- data: A folder containing the data used for the modeling project.
- nflgame: An open API to pull raw NFL game, player, and play-level data.
- top level directory: Where the analyses are found.

## Updating the Data
- draftkings: Either run Airflow DAG or paste HTML files in the raw directory, then run parse_historic_draftkings_data.py.
- nflgame: Open up ipython in the top level directory.  Copy/paste the get_nflgame_game_data.py script to pull data files with the desired inputs.

## Analyses
Core analysis can be found in [draftkings_modeling.ipynb](https://github.com/jeffbruce/daily-fantasy-modeling/blob/master/draftkings_modeling.ipynb).  If the link doesn't work, try [nbviewer](https://nbviewer.jupyter.org/), it seems to be more consistently capable of rendering jupyter notebooks.