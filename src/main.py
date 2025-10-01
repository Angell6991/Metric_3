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

    
    ###--------------------------------------------------###
    def contraccion_container_rigth(e):
        container_right.width   =   dimentions[0]*0.09
        container_right.height  =   dimentions[1]*0.9
        container_right.border_radius   =   15

        container_left.width    =   dimentions[0]*0.8
        container_right.content =   ft.Column([])
        return  page.update()

    def expan_container_rigth(e):
        container_right.width   =   dimentions[0]
        container_right.height  =   dimentions[1]
        container_right.border_radius   =   0
        
        container_left.width    =   dimentions[0]*0
        container_right.content =   page_main_bring
        return  page.update()


    ###--------------------------------------------------###
    pgm =   page_main.page_main(color, font, dimentions, dir_imagen_title, contraccion_container_rigth)  
    page_main_bring   =   pgm.page_main

    ###--------------------------------------------------###
    boton_back  =   ft.FilledButton("back", on_click=expan_container_rigth)

    container_left  =   ft.Container(
        content=ft.Row([boton_back]), 
        bgcolor=color[3], 
        padding=10,
        width=dimentions[0]*0,
        height=dimentions[1],
        animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
    )
    container_right =   ft.Container(
        content=page_main_bring, 
        bgcolor=color[2], 
        padding=0,
        width=dimentions[0],
        height=dimentions[1],
        animate=ft.Animation(300, ft.AnimationCurve.DECELERATE),
    )
    container_main  =   ft.Container(
        content=ft.Row(
            [container_left, container_right], 
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=0,
        ), 
        padding=0
    )

    ###--------------------------------------------------###


    page.bgcolor    =   color[3]
    page.padding    =   0
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    return  page.add(container_main)

ft.app(main)


