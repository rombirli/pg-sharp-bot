import matplotlib.pyplot as plt

from pgsharp.actions import open_pokestop
from processing import filtering, clustering
from android.controller import play_record
play_record('turn_pokestop')