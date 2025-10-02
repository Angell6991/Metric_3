import  flet    as  ft

class   page_data:

    def __init__(self, color, font, dimentions, dir_imagen):
        self.page   =   None

        ##########################################################
        ###--------------------def_fuctions--------------------###
        ##########################################################
        def contraccion_container_up(e):
            box_up.height   =   dimentions[1]*0.45
            box_down.height =   dimentions[1]*0.435
            box_up.content  =   ft.Column([box_title, boton_back_expan])
            return  self.page.update()

        def expan_container_up(e):
            box_up.height   =   dimentions[1]*0.9
            box_down.height =   dimentions[1]*0 
            box_up.content  =   ft.Column([box_title, boton_expan])
            return  self.page.update()

        ###--------------------contet_box_up-------------------###
        boton_back_expan  =   ft.Container(
            content=ft.Text("v", font_family=font[2], size=dimentions[0]*0.07, color=color[3]), 
            on_click=expan_container_up,
            padding=10,
            alignment=ft.alignment.center_left,
            expand=True
        )
        boton_expan  =   ft.Container(
            content=ft.Text("v", font_family=font[2], size=dimentions[0]*0.07, color=color[3]), 
            on_click=contraccion_container_up,
            padding=10,
            alignment=ft.alignment.center_left,
            expand=True
        )
        imagen  =   ft.Container(
            ft.Image(src=str(dir_imagen), width=dimentions[0]*0.6),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[2], 
            border_radius=15,
            width=dimentions[0]*0.82,
            padding=10,       
        )
        title   =   ft.Container(
            ft.Text("Data base", font_family=font[0], color=color[5], size=dimentions[0]*0.04),
            padding=ft.padding.only(left=10, right=10, top=0, bottom=0),       
        )
        box_title   =   ft.Container(
            content=ft.Column(
                controls=[title, imagen], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.END,
                spacing=10
            ),
            bgcolor=color[3], 
            border_radius=15, 
            padding=10,
            border=ft.border.all(4, color[2])
        )

        ###-------------------contet_box_down------------------###
        
        ###--------------------construc_box--------------------###
        box_up  =   ft.Container(
            content=ft.Column([box_title, boton_expan]), 
            bgcolor=color[2], 
            padding=0,
            width=dimentions[0]*0.82,
            height=dimentions[1]*0.9,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        box_down=   ft.Container(
            content=ft.Column([]), 
            bgcolor=color[2], 
            padding=0,
            width=dimentions[0]*0.82,
            height=dimentions[1]*0,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )

        ##########################################################
        ###------------------construc_page_data----------------###
        ##########################################################
        page_data =   ft.Container(
            content=ft.Column([box_up, box_down]), 
            padding=0,
            width=dimentions[0]*0.82,
            height=dimentions[1]*0.9,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        self.page_data  =   page_data


