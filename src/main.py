import  flet    as  ft
import  os

##########################################################
###------------------create_suports--------------------###
##########################################################

###----------------rutas_de_diectorios-----------------###
dir_suport  =   os.path.join(os.getcwd(), ".metric3_data")
data_input  =   os.path.join(dir_suport, "input_data")
data_save   =   os.path.join(dir_suport, "save_data")

coordinates     =   os.path.join(data_input, "input_coordinates" + ".dat")
constants       =   os.path.join(data_input, "input_constants" + ".dat")
metric_tensor   =   os.path.join(data_input, "input_metric_tensor" + ".dat")

data_intro  =   [coordinates, constants, metric_tensor]

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
    "#5AEDA3", "#aaffaa",
    "#ff44a0", "#00CCDE",
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

    ###--------------------------------------------------###
    texto   =   ft.Text("a c l m g h x d", font_family=font[2], size=40, color=color[0])

    def button(icon, label, colorr, action):
        button  =   ft.Container(
            content=ft.TextButton(
                content=ft.Text(str(icon), font_family=font[2], size=dimentions[0]*0.1, color=colorr), 
                on_click=action,
                tooltip=str(label),
                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=1),
            ),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[2],
            padding=2,
            border_radius=10,
        )
        return  button

    def button_0(icon, label, colorr, action): 
        button  =   ft.Container(
            content=ft.TextButton(
                content=ft.Text(str(icon), font_family=font[2], size=dimentions[0]*0.1, color=colorr), 
                on_click=action,
                tooltip=str(label),
                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=1),
            ),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[3],
            padding=2,
            border_radius=10,
        )
        return  button

    imagen  =   ft.Image(src=str("assets/title.png"), width=dimentions[0]*0.6)
    title   =   ft.Text("Metric 3", font_family=font[0], color=color[5], size=dimentions[0]*0.07)
    box_title   =   ft.Container(
        content=ft.Column(
            controls=[imagen, title], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=color[2], 
        border_radius=15, 
        padding=0,
    )
  
    up  =   ft.Row(
        controls=[
            button("x", "Coordinates", color[1], None), 
            button("g", "Metric tensor", color[1], None)
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        tight=True
    )
    down  =   ft.Row(
        controls=[
            button("c", "Constants", color[1], None), 
            button_0("d", "Data base", color[2], None)
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        tight=True
    )
    box_buttons =   ft.Container(
        content=ft.Column(
            controls=[up, down], 
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        shadow=ft.BoxShadow(color=color[3], blur_radius=10),
        bgcolor=color[3], 
        border_radius=15, 
        padding=10,
    )

    calculate   =   ft.Container(
        content=ft.TextButton(
                content=ft.Text("a", font_family=font[2], size=dimentions[0]*0.1, color=color[2]), 
                on_click=None,
                tooltip="Calculate",
                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=1),
            ),
            shadow=ft.BoxShadow(color=color[5], blur_radius=3),
            bgcolor=color[5],
            padding=2,
            border_radius=10,
    )

    git_hub =   ft.TextButton(
        content=ft.Text("h", font_family=font[2], size=dimentions[0]*0.06, color=color[7]), 
        url     =   "https://github.com/Angell6991/Metric_3",
        style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=5),
    )

    page_main  =   ft.Container(
        content=ft.Column(
            controls=[box_title, box_buttons, calculate, git_hub],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=dimentions[1]*0.05,
        ),
        bgcolor=color[2], 
        border_radius=15, 
        padding=10,
        width=dimentions[0],
        height=dimentions[1],
    )




    page.bgcolor    =   color[3]
    page.padding    =   10
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    return  page.add(page_main)

ft.app(main)


