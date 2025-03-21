import numpy as np
import geopandas as geo
import matplotlib.pyplot as plt
from matplotlib import colormaps
import random
from pyInegi.generalizacion import WebMAP

color = list(colormaps)[random.randint(0,len(list(colormaps))-1)]

base = geo.read_file("CPV_9_cdmex/CPV_9_cdmex.shp",columns=["ID","POBTOT","geometry"])
CRS = base.crs.to_string()
base["ordenada"]=base.geometry.centroid.y
base["absisa"]=base.geometry.centroid.x
base["vtx"]=base.geometry.count_coordinates()
cant=base.index[-1]+1
base.set_index(["ordenada","absisa"],  inplace=True)
base.sort_index(inplace=True,ascending=[False,True])
print(base)
eliminar = [i for i,v in base.iterrows() if v[3]!=5]
res = base.drop(base.iat()).loc[:["ID","POBTOT","geometry","vtx"]]
print(res)

res.to_file("datosLimpios.shp")
#print(res.iloc[0])

#print(res)

WebMAP(datos=["datosLimpios.shp"],tipos=["POLYGON"],names=["Teselas CDMX"],color=["#FF0000"],web=1,rows=None)