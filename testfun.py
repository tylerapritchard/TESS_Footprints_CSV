import numpy as np
import pandas as pd
import subprocess

def footprint(npoints=20):
    """Gets the column and row points for CCD edges"""
    column = np.hstack(
        [
            np.ones(npoints)*0.5,
            np.linspace(0.5, 2047.5, npoints),
            np.linspace(0.5, 2047.5, npoints),
            np.ones(npoints) * 2047.5,
        ]
    )
    row = np.hstack(
        [
            np.linspace(0.5, 2047.5, npoints),
            np.ones(npoints)*0.5,
            np.ones(npoints) * 2047.5,
            np.linspace(0.5, 2047.5, npoints),
        ]
    )
    return np.vstack([column, row]).T

def multi_create_footie_df(SectorCameraCCD):
    Sector, Camera, CCD = SectorCameraCCD
    xy=footprint()
    tic=range(len(xy[:,0]))
    ra=[]
    dec=[]
    
    for tic, x, y in zip(tic, xy[:,0], xy[:,1]):
        point=subprocess.run(["python","/Users/tapritc2/tessgi/tesspoint/tess-point/tess_stars2px.py",
                        "-r",str(Sector),str(Camera),str(CCD),str(x),str(y)],capture_output=True,text=True)
        ra.append(float(point.stdout.split(' ')[0]))
        dec.append(float(point.stdout.split(' ')[1]))
    
    footie_df=pd.DataFrame(data={'id':tic, 'ra':ra, 'dec':dec, 'col':xy[:,0],'row':xy[:,1],
                        'sector':Sector,'camera':Camera,'ccd':CCD})
    return footie_df
    