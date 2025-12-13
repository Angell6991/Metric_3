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
def equation_search(page, label, color, font, dimentions, s, dir_save, name_imagen):

    ###-----------------init_search-------------------###
    def save_and_exit(e):
        if  dlg_modal.content.value ==  "":
            return  print("vacio")
        elif    dlg_modal.content.value !=  "":
            page.close(dlg_modal)
            return  print("hi")

    dlg_modal = ft.AlertDialog(
        modal=True,
        elevation=20,
        bgcolor=color[3], 

        title=ft.Text(
            "Search matrix component", 
            font_family=font[1], 
            size=s*0.5, 
            color=color[0]
        ),

        content=ft.TextField(
            color   =   color[2], 
            bgcolor =   color[0], 
            label_style =   ft.TextStyle(color=color[2]),
            border_color    =   color[2], 
            border_radius   =   10,
            border_width    =   1,
            cursor_color    =   color[2],
            cursor_height   =   20,
            cursor_radius   =   10,
            cursor_width    =   1,
            selection_color =   color[1],
            text_style=ft.TextStyle(font_family=font[1]),
        ),

        actions=[
            ft.FilledButton(
                content=ft.Text("Back", font_family=font[1], size=s*0.5, color=color[0]),
                bgcolor=color[3],
                on_click=lambda e: page.close(dlg_modal),
            ),
            ft.FilledButton(
                content=ft.Text("Start", font_family=font[1], size=s*0.5, color=color[3]),
                bgcolor=color[0],
                on_click=save_and_exit,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    ###------------------var_init---------------------###
    box_equation    =   ft.Container(
        content=ft.Row([ ft.Text("· · · · · ", color=color[0], font_family=font[1], size=s*0.5) ], scroll=ft.ScrollMode.HIDDEN),
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
        on_click=lambda e:  page.open(dlg_modal),
    )

    ###-------------------return----------------------###
    content =   ft.Container(
        content=ft.Column( [box_title, box_equation], spacing=2 ),
        bgcolor=color[1],
        border_radius=5,
        padding=5,

    )
    return  content


