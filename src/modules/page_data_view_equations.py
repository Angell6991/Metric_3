import  flet    as  ft 
import  os

#####################################################
###------------def_part_of_box_down---------------###
#####################################################

###-----------------def_function------------------###
def title(page, label, color, font, dimentions, s):
    
    contet  =   ft.Container(
        content=ft.Text(str(label), color=color[1], font_family=font[1], size=s * 0.5),
        bgcolor=color[2],
        border_radius=15,
        width=dimentions[0],
        padding=10,
        border=ft.border.all(2, color[1]),
        alignment=ft.alignment.center,
        shadow=[
            ft.BoxShadow(
                color=color[2],
                blur_radius=10,
                spread_radius=2,
            )
        ],
    )

    return contet


#####################################################
###--------------def_contet_box_down--------------###
#####################################################
def contet_box_down(page, label, color, font, dimentions, s):
    contet  =   ft.Container(
        content=title(page, label, color, font, dimentions, s)
    )
    return  contet






