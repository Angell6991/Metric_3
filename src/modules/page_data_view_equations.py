from typing import Container
import  flet    as  ft 
import  os


#####################################################
###------------def_part_of_box_down---------------###
#####################################################

###---------------title_calculate-----------------###
def title(page, label, color, font, dimentions, s):
    contet  =   ft.Container(
        content=ft.Text(str(label), color=color[7], font_family=font[1], size=dimentions[1]*0.48*0.2*0.3),
        bgcolor=color[2],
        border_radius=15,
        alignment=ft.alignment.center,
        shadow=[
            ft.BoxShadow(
                color=color[2],
                blur_radius=10,
            )
        ],
    )
    return contet

###----------------generit_title------------------###
def generit_title(color, font, s, icon, title, icon_size, left, right, top, bottom):
    content   =   ft.Row(
        [
            ft.Container(
                ft.Text(f"{icon}", font_family=font[2], size=s*icon_size, color=color[2]), 
                bgcolor=color[1],
                padding=ft.padding.only(left=left, right=right, top=top, bottom=bottom),
                border_radius=5,
                alignment=ft.alignment.center,
            ),
            ft.Text(f"{title}", font_family=font[1], size=s*0.4, color=color[0])
        ],
        spacing=10,
    )
    return  content

###----------------view_equations-----------------###
def equation_static(label, color, font, dimentions, s, dir_save, name_imagen):

    ###------------------var_init---------------------###
    box_equation    =   ft.Container(
        content=ft.Row([ ft.Text(" ") ], scroll=ft.ScrollMode.HIDDEN),
        bgcolor=color[2],
        border_radius=5,
        width=dimentions[0]*0.8,
        alignment=ft.alignment.center,
        padding=ft.padding.only(left=0, right=0, top=-10, bottom=-10),
        shadow=[
            ft.BoxShadow(
                color=color[2],
                blur_radius=5,
            )
        ],
    )

    box_title   = ft.Container(
        content=ft.Text(" "),
        width=dimentions[0]*0.8,
        alignment=ft.alignment.center_right,
        padding=ft.padding.only(left=0, right=5, top=0, bottom=0),
    )
    
    ###--------search_imagen_and_conditionals---------###
    def imagen(label, dir_save, name_imagen, dimentions, item):
        return ft.Image(
            src=f"{dir_save}/{label}/cache/{name_imagen}/{item}", 
            height=dimentions[1]*0.1,
            width=dimentions[0]*0.1,
        )

    lista   =   sorted(os.listdir(f"{dir_save}/{label}/cache/{name_imagen}"))
    lista   =   [imagen(label, dir_save, name_imagen, dimentions, i) for i   in  lista]
    box_equation.content=ft.Row(lista, scroll=ft.ScrollMode.HIDDEN, spacing=0)
     
    if  name_imagen ==  "escalar_curvatura":    
        box_title.content=ft.Row([])
    
    else:
        box_title.content=ft.Text(f"{name_imagen}", font_family=font[0], color=color[2], size=s*0.25)

    ###-------------------return----------------------###
    content =   ft.Container(
        content=ft.Column( [box_title, box_equation], spacing=2 ),
        bgcolor=color[1],
        border_radius=5,
        padding=5,

    )
    return  content

###-----------------view_result-------------------###
def view_result(page, label, color, font, dimentions, s, dir_save):
    content =   ft.Column(
        [
            generit_title(color, font, s, "y", "Constants and coordinates", 0.6, 6, 6, 3, 3),
            equation_static(label, color, font, dimentions, s, dir_save, "constants"),
            equation_static(label, color, font, dimentions, s, dir_save, "coordinates"),
            ft.Divider(),
            
            generit_title(color, font, s, "n", "Metric tensor", 1, 6, 6, -10, -10),
            ft.Divider(),

            generit_title(color, font, s, "o", "Inverse metric tensor", 1, 6, 6, -10, -10),
            ft.Divider(),

            generit_title(color, font, s, "p", "Connections", 1.1, 6, 6, -10, -10),
            ft.Divider(),

            generit_title(color, font, s, "q", "Riemann tensor", 1.5, 6, 6, -20, -20),
            ft.Divider(),

            generit_title(color, font, s, "r", "Ricci tensor", 1, 6, 6, -10, -10),
            ft.Divider(),

            generit_title(color, font, s, "t", "Scalar curvature", 0.5, 6, 6, 3, 3),
            equation_static(label, color, font, dimentions, s, dir_save, "escalar_curvatura"),
        ],
        spacing=5, 
        scroll=ft.ScrollMode.HIDDEN
    )
    return  content


#####################################################
###--------------def_contet_box_down--------------###
#####################################################
def contet_box_down(page, label, color, font, dimentions, s, dir_save):
    content=ft.Column(
        [
            ft.Container(
                content=title(page, label, color, font, dimentions, s), 
                bgcolor=color[3], 
                border_radius=15,
                width=dimentions[0]*0.82,
                height=dimentions[1]*0.48*0.2,
                border=ft.border.all(4, color[2]),
                padding=10
            ),
            ft.Container(
                content=view_result(page, label, color, font, dimentions, s, dir_save), 
                padding=ft.padding.only(left=20, right=20, top=5, bottom=5),
                width=dimentions[0]*0.82,
                height=dimentions[1]*0.48*0.8,
            )
        ], 
        spacing=0, 
        scroll=ft.ScrollMode.HIDDEN
    )
    return  content


