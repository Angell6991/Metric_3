import  flet    as  ft
import  os

from .page_data_menu_setting import menu_conf

class   page_data:

    def __init__(self, color, font, dimentions, dir_imagen, dir_data_save):
        self.color  =   color
        self.font   =   font
        self.dimentions =   dimentions
        self.dir_imagen =   dir_imagen
        self.dir_data_save  =   dir_data_save
        self.page   =   None
        
        # Creamos el contenedor principal vacío que contendrá la lista
        self.container_list = ft.Container()
        
        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            self.w   =   dimentions[0]*0.85
            self.s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            self.w   =   dimentions[0]*0.85
            self.s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            self.w   =   dimentions[0]*0.85
            self.s   =   dimentions[1]*0.9*0.09


        ##########################################################
        ###----------------------page_data---------------------###
        ##########################################################
        
        ###--------------------contet_box_up-------------------###
        imagen  =   ft.Container(
            ft.Image(src=str(self.dir_imagen)),
            shadow=ft.BoxShadow(color=self.color[2], blur_radius=10),
            bgcolor=self.color[2], 
            border_radius=15,
            width=self.dimentions[0]*0.82,
            padding=10,
            expand=True,
        )
        title   =   ft.Container(
            ft.Text("database", font_family=self.font[0], color=self.color[7], size=self.s*0.35),
            padding=ft.padding.only(left=10, right=10, top=0, bottom=0),       
        )
        self.box_title   =   ft.Container(
            content=ft.Column(
                controls=[title, imagen], 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.END,
                spacing=10
            ),
            bgcolor=self.color[3], 
            border_radius=15, 
            padding=10,
            border=ft.border.all(4, self.color[2]),
            width=self.dimentions[0]*0.82,
            height=self.dimentions[1]*0.9*0.35,
        )

        ###-------------------contet_box_down------------------###
        

        ##########################################################
        ###--------------------construc_box--------------------###
        ##########################################################
        self.container_list.content = self.data_list()

        self.box_up  =   ft.Container(
            content=ft.Column([self.box_title, self.container_list]), 
            bgcolor=self.color[2], 
            padding=0,
            width=self.dimentions[0]*0.8,
            height=self.dimentions[1]*0.9,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )

        self.box_down    =   ft.Container(
            content=ft.Column([]), 
            bgcolor=self.color[2], 
            padding=0,
            width=self.dimentions[0]*0.8,
            height=self.dimentions[1]*0,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )


    ##########################################################
    ###-------------------actions_buttons------------------###
    ##########################################################
    def contraccion_container_up(self):
        self.box_up.height   =   self.dimentions[1]*0.4
        self.box_down.height =   self.dimentions[1]*0.48
        self.box_up.content  =   ft.Column([self.box_title, self.boton_back_expan()])
        return  self.page.update()

    def expan_container_up(self):
        self.box_up.height   =   self.dimentions[1]*0.9
        self.box_down.height =   self.dimentions[1]*0 
        self.box_up.content  =   ft.Column([self.box_title, self.container_list])
        return  self.page.update()
    
    def boton_back_expan(self):
        boton  =   ft.Container(
            content=ft.Text("v", font_family=self.font[2], color=self.color[7], size=self.s*0.5),
            on_click=lambda e:  self.expan_container_up(),
            padding=10,
            alignment=ft.alignment.center,
            expand=True
        )
        return boton


    ##########################################################
    ###------------------data _list------------------------###   
    ##########################################################
    def data_list(self):

        def cont_button(label):
            cont_button =   ft.Container(
                content=ft.Row(
                    [
                        ft.Text("a", font_family=self.font[2], color=self.color[7], size=self.s*0.9),
                        ft.Text(str(label), font_family=self.font[1], color=self.color[0], size=self.s*0.5)
                    ],
                    spacing=self.w*0.05
                ),
                bgcolor=self.color[8],
                border_radius=15,
                padding=ft.padding.only(left=20, right=20, top=0, bottom=0),       
                alignment=ft.alignment.center_left,
                on_click=lambda e: self.contraccion_container_up(),
                on_long_press=lambda    e: self.menu_conf(label),
                height=self.dimentions[1]*0.9*0.1
            )
            return  cont_button


        lista   =   sorted(os.listdir(self.dir_data_save))
        lista   =   [cont_button(i) for i   in  lista]
        data_list   =   ft.Container(
            content=ft.Container(
                content=ft.Column(lista, scroll=ft.ScrollMode.HIDDEN, spacing=3),
                border_radius=15,
            ),
            alignment=ft.alignment.top_center,
            border_radius=15,
            padding=ft.padding.only(left=10, right=10, top=3, bottom=3),
            width=self.w,
            height=self.dimentions[1]*0.9*0.6,
        )

        return data_list

    def refresh_list(self):
        self.container_list.content = self.data_list()
        return  self.page.update()


    ##########################################################
    ###-------------def_menu_open_rename_delete------------###
    ##########################################################
    def menu_conf(self, label):
        menu    =   menu_conf(
            page=self.page,
            color=self.color,
            font=self.font,
            s=self.s,
            dir_data_save=self.dir_data_save,
            dimentions=self.dimentions,
            label=label,
            refresh_list_callback=self.refresh_list,
            contraccion_container_callback=self.contraccion_container_up,
        )
        return  menu


    ##########################################################
    ###------------------construc_page_data----------------###
    ##########################################################
    def page_data(self):
        page_data = ft.Container(
            content=ft.Column(
                [self.box_up, self.box_down],
                spacing=self.dimentions[1] * 0.02,
                horizontal_alignment=ft.CrossAxisAlignment.END
            ),
            padding=0,
            width=self.w,
            height=self.dimentions[1] * 0.9,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        return page_data


