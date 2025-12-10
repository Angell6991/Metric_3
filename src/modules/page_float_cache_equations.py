import  pandas  as  pd
import  sympy   as  sp 
import  os

from    .latex_render   import  LaTeX


##########################################################
###-----------------created_dir_cache------------------###
##########################################################
def cache_dir(dir_create_cache):

    data_save   =   [
        "coordinates",
        "constants",
        "metric_tensor",
        "inverse_metric_tensor",
        "symbol_christofell",
        "riemann_tensor",
        "ricci_tensor",
        "escalar_curvatura",
    ]

    os.makedirs(f"{dir_create_cache}/cache", exist_ok=True)
    for name    in  data_save:
        path    =   os.path.join(f"{dir_create_cache}/cache", name)
        os.makedirs(path, exist_ok=True)


##########################################################
###-------------created_img_coordinates----------------###
##########################################################
def cache_coordinates(dir_create_cache, color):
    coordinates_dat   =   pd.read_pickle(f"{dir_create_cache}/coordinates.dat")
    coordinates_dat   =   coordinates_dat.loc[0, "arr"]
    for i    in  range(len(coordinates_dat)):
        text    =   sp.latex(sp.symbols(coordinates_dat[i]))
        LaTeX(f"{text}", f"{dir_create_cache}/cache/coordinates/{i}", color)


##########################################################
###--------------created_img_constants-----------------###
##########################################################
def cache_constants(dir_create_cache, color):
    constants_dat   =   pd.read_pickle(f"{dir_create_cache}/constants.dat")
    constants_dat   =   constants_dat.loc[0, "arr"]
    for i   in  range(len(constants_dat)):
        text    =   sp.latex(sp.symbols(constants_dat[i]))
        LaTeX(f"{text}", f"{dir_create_cache}/cache/constants/{i}", color)
   

##########################################################
###-----------created_img_escalar_curvature------------###
##########################################################
def cache_es_curvature(dir_create_cache, color):
    escalar_curvatura_dat   =   pd.read_pickle(f"{dir_create_cache}/escalar_curvatura.dat")
    escalar_curvatura_dat   =   escalar_curvatura_dat.loc[0, "arr"]
    text_es    =   sp.latex(escalar_curvatura_dat)
    LaTeX(f"{text_es}", f"{dir_create_cache}/cache/escalar_curvatura/0", color)


