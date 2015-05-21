import pandas as pd
import data_utils as du
train = pd.read_csv("data/train.csv" )

import pygmaps 

mymap = pygmaps.maps( 41.141412, -8.618643, 16)
mymap.addpath( du.stringpolyline_to_listpolyline(train.POLYLINE[0]) )
mymap.addpath( du.stringpolyline_to_listpolyline(train.POLYLINE[1]) )
mymap.draw('mymap.html')