# TESS_Footprints_CSV
Creates TESS RA, DEC Footprints and writes them to a dataframe &amp; csv file

# This notebook will:
 - create a pixel 'footprint' of a TESS CCD, tracing around the outer pixels
 - using tesspoint (tess_stars2px.py), create a list of tess ra, dec from the footprint for a given sector/camera/ccd
 - using a list of sectors/cameras/ccd's, iterate over all possibilities
 - write this to a file
 
 Currently this is using subprocess to call tess_stars2px.py and multipricessing across that.  
 A moderate speedup would be to  import tess_stars2px.py (see tesspoint repo) using the function 
 calls and running it that way.  A more significant speedup would be to use the  vectorized tess-point 
 development branch which can do this calculation on a whole footprint trivially.  
