import pandas as pd
import data_utils as du
train = pd.read_csv("Data/train.csv" )

import visualization as vi


mymap = vi.pygmaps.maps( 41.141412, -8.618643, 16)
polylines = map( du.stringpolyline_to_listpolyline, train.POLYLINE[0:100] )
vi.plot_startpoints( polylines, mymap  )
vi.plot_endpoints( polylines, mymap  )
vi.plot_path( polylines, mymap  )
mymap.draw('mymap.html')


#Visualize test set
test = pd.read_csv("Data/test.csv" )
mymap = vi.pygmaps.maps( 41.141412, -8.618643, 16)
polylines = map( du.stringpolyline_to_listpolyline, test.POLYLINE[1:100] )
vi.plot_startpoints( polylines, mymap  )
vi.plot_path( polylines, mymap  )
mymap.draw('mymap.html')

#Visualize bounding box
polylines = map( du.stringpolyline_to_listpolyline, train.POLYLINE )
minlat = min( map( du.min_latitute, polylines ) )
maxlat = max( map( du.max_latitute, polylines ) )

minlong = min( map( du.min_longitude, polylines ) )
maxlong = max( map( du.max_longitude, polylines ) )
mymap = vi.pygmaps.maps( 41.141412, -8.618643, 16)
mymap.addpoint( minlat, minlong, "#FF0000")
mymap.addpoint( minlat, maxlong, "#FF0000")
mymap.addpoint( maxlat, minlong, "#FF0000")
mymap.addpoint( maxlat, maxlong, "#FF0000")
mymap.draw('mymap.html')