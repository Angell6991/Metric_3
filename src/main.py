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



##########################################################
###------------------create_app_flet-------------------###
##########################################################

# def main(page: ft.Page):

#     page.fonts = {
#         "open": "assets/fonts/angell-font.ttf",
#     }

#     texto   =   ft.Text("a c l m g h x d", font_family="open", size=50, color="#ffffff")
#     cont    =   ft.Container(ft.Row([texto]), padding=10, bgcolor="#2e2e2e", border_radius=15)

#     return  page.add(cont)

# ft.app(main)


