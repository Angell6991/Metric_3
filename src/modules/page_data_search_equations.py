import  pandas  as  pd
import  flet    as  ft 
import  os

from    .latex_render   import  LaTeX


#####################################################
###----------------def_functions------------------###
#####################################################

###----------------search_imagen------------------###
def imagen(label, dir_save, name_imagen, dimentions, item):
    return ft.Image(
        src=f"{dir_save}/{label}/cache/{name_imagen}/{item}", 
        height=dimentions[1]*0.48*0.1
    )

###---------------search_equations----------------###
def equation_search(label, color, font, dimentions, s, dir_save, name_imagen):

    ###------------------var_init---------------------###
    box_equation    =   ft.Container(
        content=ft.Row([ ft.Text("hola") ], scroll=ft.ScrollMode.HIDDEN),
        bgcolor=color[2],
        border_radius=5,
        height=dimentions[1]*0.48*0.13,
        width=dimentions[0]*0.8,
        alignment=ft.alignment.center,
        shadow=[
            ft.BoxShadow(
                color=color[2],
                blur_radius=5,
            )
        ],
    )

    title_icon  =   ft.Icon(ft.Icons.SEARCH, size=s*0.4, color=color[2])
    title_label =   ft.Text("search", font_family=font[0], color=color[2], size=s*0.25)   
    box_title   =   ft.Container(
        content=ft.Row([title_icon, title_label], spacing=4, alignment=ft.MainAxisAlignment.END,),
        width=dimentions[0]*0.8,
        alignment=ft.alignment.center_right,
        padding=ft.padding.only(left=0, right=5, top=0, bottom=0),
        # on_click=pass,
    )
   








    # box_title.content=ft.Text(f"{name_imagen}", font_family=font[0], color=color[2], size=s*0.25)



    ###-------------------return----------------------###
    content =   ft.Container(
        content=ft.Column( [box_title, box_equation], spacing=2 ),
        bgcolor=color[1],
        border_radius=5,
        padding=5,

    )
    return  content


