import pygmaps

def plot_startpoints( polylines, mymap ):
    """
    Plot start points in file startpoints.html

    :param l: list of polyline
    :param 2: the pygmaps map
    """
    map( \
    lambda start : mymap.addpoint( start[0][0], start[0][1], "#FF0000") if start != [] else [],
    polylines)

    
def plot_endpoints( polylines, mymap ):
    """
    Plot start points in file startpoints.html

    :param l: list of polyline
    :param 2: the pygmaps map
    """
    map( \
    lambda start : mymap.addpoint( start[-1][0], start[-1][1], "#0000FF") if start != [] else [],
    polylines)
    
    
def plot_path( polylines, mymap ):
    """
    Plot start points in file startpoints.html

    :param l: list of polyline
    :param 2: the pygmaps map
    """
    #remark : there is bug in lib pymaps : it change path....
    map( \
    lambda path : mymap.addpath(list(path),"#00FF00"),
    polylines)
    
    
    
