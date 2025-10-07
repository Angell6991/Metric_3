import  flet    as  ft

class   page_main:

    def __init__(self, color, font, dimentions, dir_imagen, data_button_action):
        self.page   =   None

        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            w   =   dimentions[1]*0.9*0.1
            h   =   dimentions[1]*0.9*0.1
            s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            w   =   dimentions[0]*0.9*0.15
            h   =   dimentions[0]*0.9*0.15
            s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            w   =   dimentions[1]*0.9*0.15
            h   =   dimentions[1]*0.9*0.15
            s   =   dimentions[1]*0.9*0.09


        ##########################################################
        ###--------------------def_fuctions--------------------###
        ##########################################################
        
        ###---------------------button_apps--------------------###
        def button(icon, label, colorr, action):
            button  =   ft.Container(
                content=ft.TextButton(
                    content=ft.Text(str(icon), font_family=font[2], size=s, color=colorr), 
                    on_click=action,
                    tooltip=str(label),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=3),
                ),
                shadow=ft.BoxShadow(color=color[2], blur_radius=10),
                bgcolor=color[2],
                padding=2,
                border_radius=10,
                width=w,
                height=h,
                alignment=ft.alignment.center
            )
            return  button

        ###------------------button_apps_glass-----------------###
        def button_glass(icon, label, colorr, action): 
            button  =   ft.Container(
                content=ft.TextButton(
                    content=ft.Text(str(icon), font_family=font[2], size=s, color=colorr), 
                    on_click=action,
                    tooltip=str(label),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=2),
                ),
                shadow=ft.BoxShadow(color=color[2], blur_radius=10),
                bgcolor=color[3],
                padding=2,
                border_radius=10,
                width=w,
                height=h,
                alignment=ft.alignment.center
            )
            return  button


        ##########################################################
        ###--------------------def_box_page--------------------###
        ##########################################################

        ###------------------construc_box_title----------------###
        imagen  =   ft.Container(
            ft.Image(src=str(dir_imagen)),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[2], 
            border_radius=15, 
            padding=10,
            expand=True,
        )
        title   =   ft.Container(
            ft.Text("metric  3", font_family=font[0], color=color[5], size=s*0.35),
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
            width=h*5.5,
            height=w*3,
        )

        ###-----------------construc_box_buttons---------------###
        up  =   ft.Row(
            controls=[
                button("x", "Coordinates", color[1], data_button_action[0]), 
                button("g", "Metric tensor", color[1], data_button_action[1])
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
            tight=True
        )
        down  =   ft.Row(
            controls=[
                button("c", "Constants", color[1], data_button_action[2]), 
                button_glass("d", "Database", color[2], data_button_action[3])
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
            content=data_button_action[4],
            bgcolor=color[3],
            padding=2,
            border_radius=50,
            width=h*0.9,
            height=w*1.5,
        )

        ###---------------construc_button_git_hub--------------###
        git_hub =   ft.TextButton(
            content=ft.Text("h", font_family=font[2], size=s*0.6, color=color[7]), 
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
                spacing=dimentions[0]*0.9*0.05
            )
        )

        page_main   =   ft.Container(
            ft.Column(
                controls=[box_title, box_buttons_and_calculate],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=dimentions[1]*0.9*0.09,
            ),
            padding=30,
        )

        ###---------------------return_class-------------------###
        self.page_main  =   page_main


