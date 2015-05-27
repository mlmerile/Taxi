import numpy as np


def stupid_squareddist( a,b ):
    if( len(a)-len(b)>0) :
        i_max=len(b)
    else :
        i_max=len(a)
    return sum( [ (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) \
    for ((x1,y1),(x2,y2)) in zip(a[0:i_max],b[0:i_max]) ] )

