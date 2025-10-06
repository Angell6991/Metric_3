import  modules.calculate   as  cal 
import  flet    as  ft
import  os

class   page_float:

    def __init__(self, color, font, dimentions, dir_data_intro, data_save):
        self.page   =   None
        self.color  =   color
        self.font   =   font
        self.data_save  =   data_save
        self.dimentions =   dimentions
        self.dir_data_intro =   dir_data_intro

        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            self.w   =   dimentions[1]*0.9*0.1
            self.h   =   dimentions[1]*0.9*0.1
            self.s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            self.w   =   dimentions[0]*0.9*0.15
            self.h   =   dimentions[0]*0.9*0.15
            self.s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            self.w   =   dimentions[1]*0.9*0.15
            self.h   =   dimentions[1]*0.9*0.15
            self.s   =   dimentions[1]*0.9*0.09


    ##########################################################
    ###--------------------def_fuctions--------------------###
    ##########################################################
    def button_calculate(self):
        
        ###----------------------------------------------------###
        def calculate(e):
            up.content  =   cont_load
            self.page.update()

            for i   in  range(101):
                cont_load.value =   i/100
                self.page.update()

            up.content  =   cont_icon
            return  self.page.update()

        ###----------------------------------------------------###
        cont_icon   =   ft.Container(
            ft.Text("w", font_family=self.font[2], color=self.color[4], size=self.s*0.65),
            on_click=calculate,
            tooltip="Calculate"
        )
        cont_load   =   ft.ProgressRing(
            width=self.w*0.7, 
            height=self.h*0.7, 
            stroke_width=self.s*0.08,
            color=self.color[4],
        )

        up  =   ft.Container(
            content=cont_icon, 
            bgcolor=self.color[2],
            padding=5,
            width=self.w*0.8,
            height=self.h*0.8,
            border_radius=50,
            shadow=ft.BoxShadow(color=self.color[2], blur_radius=10),
            alignment=ft.alignment.center,
        )

        ###----------------------------------------------------###
        list_data   =   os.listdir(self.data_save)

        down  =   ft.Container(
            content=ft.Text(f"{len(list_data)}", font_family=self.font[0], color=self.color[0], size=self.s*0.3), 
            alignment=ft.alignment.center,
        )

        ###----------------------------------------------------###
        contenedor  =   ft.Container(content=ft.Column([up, down], spacing=5), padding=5)

        return  contenedor


