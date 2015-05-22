import numpy as np
import pandas as pd

    
def stringpolyline_to_listpolyline( stringpolyline ):
    if stringpolyline == '[]':
        return []
    return map( lambda l : ( float(l[1]), float(l[0])), \
    [ a.split(',') for a in stringpolyline[2:-2].split('],[') ] )
    
    
def min_latitute( listpolyline ):
    return min( listpolyline, key = lambda x : x[0] )[0]
    
def max_latitute( listpolyline ):
    return max( listpolyline, key = lambda x : x[0] )[0]
    
def max_longitude( listpolyline ):
    return max( listpolyline, key = lambda x : x[1] )[1]
    
def min_longitude( listpolyline ):
    return min( listpolyline, key = lambda x : x[1] )[1]

