import  modules.page_main   as  page_main
import  modules.page_data   as  page_data
import  modules.page_save   as  page_save
import  modules.page_float  as  page_float

import  flet    as  ft
import  os

##########################################################
###------------------create_suports--------------------###
##########################################################

###----------------rutas_de_diectorios-----------------###
dir_imagen_title    =   "assets/title.png"
dir_imagen_data     =   "assets/time_space_logo.png"

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
    "#333333"
]


##########################################################
###------------------create_app_flet-------------------###
##########################################################

def main(page: ft.Page):

    ###---------------------fonts--------------------------###
    page.fonts = {
        "title":    "assets/fonts/frank-font.ttf",
        "general":  "assets/fonts/Ubuntu-R.ttf",
        "icons":    "assets/fonts/angell-font.ttf",
    }
    font    =   ["title", "general", "icons"]

    ###--------------window_dimentions-------------------###
    w   =   page.width      #   ancho
    h   =   page.height     #   altura
    dimentions  =   [float(w), float(h)]


    ########################################################
    ###----------------def_functions---------------------###
    ########################################################
    def contraccion_container_rigth(e):
        container_right.width   =   dimentions[0]*0.15
        container_right.height  =   dimentions[1]*0.9
        container_right.border_radius   =   ft.border_radius.only(top_left=15, top_right=0, bottom_left=15, bottom_right=0)
        container_main.content.spacing  =   dimentions[0]*0.05
        container_main.padding  =   0

        container_left.width    =   dimentions[0]*0.85
        container_right.content =   ft.Column([boton_back_expan])
        return  page.update()

    def expan_container_rigth(e):
        container_right.width   =   dimentions[0]*0.9
        container_right.height  =   dimentions[1]*0.9
        container_right.border_radius   =   15
        container_main.content.spacing  =   dimentions[0]*0
        
        container_left.width    =   dimentions[0]*0
        container_right.content =   page_main_bring
        return  page.update()


    ########################################################
    ###--------------import_dependencies-----------------###
    ########################################################
    pgf =   page_float.page_float(color, font, dimentions, data_intro, data_save)
    pgf.page    =   page

    pgs =   page_save.page_save(color, font, dimentions, data_intro)
    pgs.page    =   page

    actions_buttons_main    =   [
        lambda  e:  pgs.float_window("coordinates"), 
        lambda  e:  pgs.float_window("metric_tensor"), 
        lambda  e:  pgs.float_window("constants"), 
        contraccion_container_rigth,
        pgf.button_calculate()
    ]

    pgm =   page_main.page_main(color, font, dimentions, dir_imagen_title, actions_buttons_main)  
    page_main_bring =   pgm.page_main
    pgm.page    =   page

    pgd =   page_data.page_data(color, font, dimentions, dir_imagen_data, data_save)
    page_data_bring =   pgd.page_data
    pgd.page    =  page 


    ########################################################
    ###-----------------construc_page--------------------###
    ########################################################
    boton_back_expan  =   ft.Container(
        content=ft.Text("u", font_family=font[2], size=dimentions[0]*0.9*0.06, color=color[3]), 
        on_click=expan_container_rigth,
        padding=10,
        alignment=ft.alignment.center_left,
        expand=True
    )

    container_left  =   ft.Container(
        content=ft.Row([page_data_bring]), 
        bgcolor=color[3], 
        padding=0,
        width=dimentions[0]*0,
        height=dimentions[1],
        animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
    )
    container_right =   ft.Container(
        content=page_main_bring, 
        bgcolor=color[2], 
        padding=0,
        width=dimentions[0]*0.9,
        height=dimentions[1]*0.9,
        border_radius=15,
        animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
    )
    container_main  =   ft.Container(
        content=ft.Row(
            [container_left, container_right],
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=dimentions[0]*0,
        ), 
        padding=0
    )

    ###-----------------page_settings--------------------###
    page.theme_mode =   "LIGHT"
    page.bgcolor    =   color[3]
    page.padding    =   0
    return  page.add(container_main)

ft.app(main)


