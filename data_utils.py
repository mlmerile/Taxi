import numpy as np

def stringpolyline_to_arraypolyline( stringpolyline ): 
    return np.array( map( lambda l : [ float(a) for a in l ], \
    [ a.split(',') for a in stringpolyline[2:-2].split('],[') ] ) )
    
    
def stringpolyline_to_listpolyline( stringpolyline ): 
    return map( lambda l : ( float(l[1]), float(l[0])), \
    [ a.split(',') for a in stringpolyline[2:-2].split('],[') ] )
    
    
