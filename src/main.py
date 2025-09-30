import  modules.page_main   as  page_main

import  flet    as  ft
import  os

##########################################################
###------------------create_suports--------------------###
##########################################################

###----------------rutas_de_diectorios-----------------###
dir_imagen_title    =   "assets/title.png"

dir_suport  =   os.path.join(os.getcwd(), ".metric3_data")
data_input  =   os.path.join(dir_suport, "input_data")
data_save   =   os.path.join(dir_suport, "save_data")

coordinates     =   os.path.join(data_input, "input_coordinates" + ".dat")
constants       =   os.path.join(data_input, "input_constants" + ".dat")
metric_tensor   =   os.path.join(data_input, "input_metric_tensor" + ".dat")
data_intro      =   [coordinates, constants, metric_tensor]

###----------------sí_existe_la_ruta-------------------###
if  os.path.exists(dir_suport):
    dir_suport = dir_suport

###----------------sí_la_ruta_no_existe----------------###
else:
    os.makedirs(dir_suport, exist_ok=True)
    os.makedirs(data_input, exist_ok=True)
    os.makedirs(data_save, exist_ok=True)

    for i   in  data_intro:
        with open(i, "w") as archivo:
            pass  

###--------------------colors--------------------------###
color   =   [
    "#e2e2e2", "#a6a6a6",  
    "#2e2e2e", "#4a4a4a",
    "#80ff80", "#aaffaa",
    "#FF4444", "#00CCDE",
]


##########################################################
###------------------create_app_flet-------------------###
##########################################################

def main(page: ft.Page):

    ###---------------------fonts--------------------------###
    page.fonts = {
        "title":    "assets/fonts/NotoSerifDisplay-BoldItalic.ttf",
        "general":  "assets/fonts/Ubuntu-R.ttf",
        "icons":    "assets/fonts/angell-font.ttf",
    }
    font    =   ["title", "general", "icons"]

    ###--------------window_dimentions-------------------###
    w   =   page.width      #   ancho
    h   =   page.height     #   altura
    dimentions  =   [float(w), float(h)]

    ###-----------------construc_page--------------------###
    # texto   =   ft.Text("s u v w", font_family=font[2], size=40, color=color[0])

    pgm =   page_main.page_main(color, font, dimentions, dir_imagen_title)  
    page_main_bring   =   pgm.page_main

    
    ###--------------------------------------------------###

    page.bgcolor    =   color[3]
    page.padding    =   10
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    return  page.add(page_main_bring)

ft.app(main)


