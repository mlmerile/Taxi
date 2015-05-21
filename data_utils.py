import numpy as np

def stringpolyline_to_arraypolyline( stringpolyline ): 
    return np.array( map( lambda l : [ float(a) for a in l ], \
    [ a.split(',') for a in stringpolyline[2:-2].split('],[') ] ) )
    
    
