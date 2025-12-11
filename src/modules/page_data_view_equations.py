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

###-----------------view_result-------------------###
def view_result(page, label, color, font, dimentions, s, dir_save):
 
    ###-----------------------------------------------###
    title_coordenades   =   ft.Row(
            [
                ft.Container(
                    ft.Text("y", font_family=font[2], size=s*0.6, color=color[2]), 
                    bgcolor=color[1],
                    padding=ft.padding.only(left=6, right=6, top=3, bottom=3),
                    border_radius=5,
                    alignment=ft.alignment.center,
                    shadow=[
                        ft.BoxShadow(
                            color=color[1],
                            blur_radius=4,
                        )
                    ],
                ),
                ft.Text("constants and coordinates", font_family=font[1], size=s*0.4, color=color[0])
            ],
            spacing=10,
    )
   
    ###-----------------------------------------------###
    title_escalar   =   ft.Row(
            [
                ft.Container(
                    ft.Text("t", font_family=font[2], size=s*0.5, color=color[2]), 
                    bgcolor=color[1],
                    padding=ft.padding.only(left=6, right=6, top=3, bottom=3),
                    border_radius=5,
                    alignment=ft.alignment.center,
                    shadow=[
                        ft.BoxShadow(
                            color=color[1],
                            blur_radius=4,
                        )
                    ],
                ),
                ft.Text("Scalar curvature", font_family=font[1], size=s*0.4, color=color[0])
            ],
            spacing=10,
    )
    
    ###-----------------------------------------------###
    content =   ft.Column(
        [
            title_coordenades,
            ft.Divider(),
            title_escalar,
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
                padding=ft.padding.only(left=20, right=20, top=10, bottom=0),
                width=dimentions[0]*0.82,
                height=dimentions[1]*0.48*0.8,
            )
        ], 
        spacing=0, 
        scroll=ft.ScrollMode.HIDDEN
    )
    return  content






