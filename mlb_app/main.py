from pybaseball import  playerid_lookup
from pybaseball import  statcast_pitcher

id = playerid_lookup('ohtani', 'shohei')
id = id.iloc[0]['key_mlbam']

ohtani_stats = statcast_pitcher('2017-06-01', '2017-07-01', id)

print(ohtani_stats)

