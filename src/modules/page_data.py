import  flet    as  ft
import  os

class   page_data:

    def __init__(self, color, font, dimentions, dir_imagen, dir_data_save):
        self.page   =   None

        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            w   =   dimentions[0]*0.82
            s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            w   =   dimentions[0]*0.82
            s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            w   =   dimentions[0]*0.82
            s   =   dimentions[1]*0.9*0.09


        ##########################################################
        ###--------------------def_fuctions--------------------###
        ##########################################################
        def contraccion_container_up(e):
            box_up.height   =   dimentions[1]*0.4
            box_down.height =   dimentions[1]*0.48
            box_up.content  =   ft.Column([box_title, boton_back_expan])
            return  self.page.update()

        def expan_container_up(e):
            box_up.height   =   dimentions[1]*0.9
            box_down.height =   dimentions[1]*0 
            box_up.content  =   ft.Column([box_title, boton_expan])
            return  self.page.update()

        ###-------------------buttons_actions------------------###
        def cont_button(label):
            cont_button =   ft.Container(
                content=ft.Row(
                    [
                        ft.Text("a", font_family=font[2], color=color[7], size=s*0.9),
                        ft.Text(str(label), font_family=font[1], color=color[0], size=s*0.5)
                    ],
                    spacing=w*0.05
                ),
                bgcolor=color[8],
                border_radius=15,
                padding=ft.padding.only(left=20, right=20, top=0, bottom=0),       
                alignment=ft.alignment.center_left,
                on_click=contraccion_container_up,
                height=dimentions[1]*0.9*0.1
            )
            return  cont_button

        lista   =   sorted(os.listdir(dir_data_save))
        lista   =   [cont_button(i) for i   in  lista]
        data_list   =   ft.Container(
            content=ft.Container(
                content=ft.Column(lista, scroll=ft.ScrollMode.HIDDEN, spacing=3),
                border_radius=15,
            ),
            alignment=ft.alignment.top_center,
            border_radius=15,
            padding=ft.padding.only(left=10, right=10, top=3, bottom=3),
            width=w,
            height=dimentions[1]*0.9*0.6,
        )



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
            ft.Image(src=str(dir_imagen)),
            shadow=ft.BoxShadow(color=color[2], blur_radius=10),
            bgcolor=color[2], 
            border_radius=15,
            width=dimentions[0]*0.82,
            padding=10,
            expand=True,
        )
        title   =   ft.Container(
            ft.Text("database", font_family=font[0], color=color[7], size=s*0.35),
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
            border=ft.border.all(4, color[2]),
            width=dimentions[0]*0.82,
            height=dimentions[1]*0.9*0.35,
        )

        ###-------------------contet_box_down------------------###
        
        ###--------------------construc_box--------------------###
        box_up  =   ft.Container(
            content=ft.Column([box_title, data_list]), 
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
            content=ft.Column([box_up, box_down], spacing=dimentions[1]*0.02), 
            padding=0,
            width=w,
            height=dimentions[1]*0.9,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        self.page_data  =   page_data


