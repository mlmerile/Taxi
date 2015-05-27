import pandas as pd
import data_utils as du
import numpy as np
train = pd.read_csv("Data/train.csv" )

from sklearn.neighbors import NearestNeighbors
import mathTools as mt

i_max = 1000
X_train = np.array( map( du.stringpolyline_to_listpolyline, train.POLYLINE[0:i_max] ) )
ind_train = np.array( range(i_max) )
ind_train = ind_train.reshape( i_max, 1 )
nearestNeighbors = NearestNeighbors(n_neighbors=20,algorithm="brute",\
    metric=lambda ix,iy : mt.stupid_squareddist(X_train[int(ix[0])],X_train[int(iy[0])])   \
    ).fit(ind_train)
    

(dist_nearest,ind_nearest) = nearestNeighbors.kneighbors(ind_train[0])

#plot neighbor
import visualization as vi
mymap = vi.pygmaps.maps( 41.141412, -8.618643, 16)
vi.plot_path( X_train[ind_nearest[0]] , mymap  )
mymap.draw('mymap.html')