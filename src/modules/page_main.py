import  flet    as  ft

class   page_main:

    def __init__(self, color, font, dimentions, dir_imagen, data_button_action):

        ##########################################################
        ###--------------------def_fuctions--------------------###
        ##########################################################
        
        ###---------------------button_apps--------------------###
        def button(icon, label, colorr, action):
            button  =   ft.Container(
                content=ft.TextButton(
                    content=ft.Text(str(icon), font_family=font[2], size=dimentions[0]*0.1, color=colorr), 
                    on_click=action,
                    tooltip=str(label),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=3),
                ),
                shadow=ft.BoxShadow(color=color[2], blur_radius=10),
                bgcolor=color[2],
                padding=2,
                border_radius=10,
            )
            return  button

        ###------------------button_apps_glass-----------------###
        def button_glass(icon, label, colorr, action): 
            button  =   ft.Container(
                content=ft.TextButton(
                    content=ft.Text(str(icon), font_family=font[2], size=dimentions[0]*0.1, color=colorr), 
                    on_click=action,
                    tooltip=str(label),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=2),
                ),
                shadow=ft.BoxShadow(color=color[2], blur_radius=10),
                bgcolor=color[3],
                padding=2,
                border_radius=10,
            )
            return  button


        ##########################################################
        ###--------------------def_box_page--------------------###
        ##########################################################

        ###------------------construc_box_title----------------###
        imagen  =   ft.Container(
            ft.Image(src=str(dir_imagen), width=dimentions[0]*0.6),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[2], 
            border_radius=15, 
            padding=10,       
        )
        title   =   ft.Container(
            ft.Text("Metric 3", font_family=font[0], color=color[5], size=dimentions[0]*0.04),
            padding=ft.padding.only(left=10, right=10, top=0, bottom=0),       
        )
        box_title   =   ft.Container(
            content=ft.Column(
                controls=[title, imagen], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.END,
                spacing=5
            ),
            bgcolor=color[3], 
            border_radius=15, 
            padding=5,
        )

        ###-----------------construc_box_buttons---------------###
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
                button_glass("d", "Data base", color[2], data_button_action)
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

        ###---------------construc_button_calculate------------###
        calculate   =   ft.Container(
            content= ft.Column([]),
            bgcolor=color[3],
            padding=2,
            border_radius=50,
            on_click=None,
            width=dimentions[0]*0.12,
            height=dimentions[1]*0.15,
        )

        ###---------------construc_button_git_hub--------------###
        git_hub =   ft.TextButton(
            content=ft.Text("h", font_family=font[2], size=dimentions[0]*0.06, color=color[7]), 
            url     =   "https://github.com/Angell6991/Metric_3",
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=5),
        )

        
        ##########################################################
        ###------------------construc_page_main----------------###
        ##########################################################
        box_buttons_and_calculate   =   ft.Container(
            content=ft.Column(
                controls=[
                    box_buttons, 
                    ft.Container(
                        content=ft.Column([calculate,git_hub], 
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER 
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=dimentions[0]*0.05
            )
        )

        page_main   =   ft.Column(
            controls=[box_title, box_buttons_and_calculate],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=dimentions[1]*0.05,
        )

        ###---------------------return_class-------------------###
        self.page_main  =   page_main


