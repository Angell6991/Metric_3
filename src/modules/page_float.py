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

    ##########################################################
    ###--------------------def_fuctions--------------------###
    ##########################################################
    def button_calculate(self):
        
        list_data   =   os.listdir(self.data_save)

        up  =   ft.Container(
            content=ft.Container(ft.Text("w", font_family=self.font[2], color=self.color[4], size=self.dimentions[0]*0.07)), 
            bgcolor=self.color[2],
            padding=5,
            width=self.dimentions[0]*0.1,
            height=self.dimentions[1]*0.08,
            border_radius=50,
            shadow=ft.BoxShadow(color=self.color[2], blur_radius=10),
            alignment=ft.alignment.center,
        )

        down  =   ft.Container(
            content=ft.Text(f"{len(list_data)}", font_family=self.font[0], color=self.color[0], size=self.dimentions[0]*0.03), 
            width=self.dimentions[0]*0.1,
            height=self.dimentions[1]*0.05,
            border_radius=50,
            alignment=ft.alignment.center,
        )

        contenedor  =   ft.Container(content=ft.Column([up, down], spacing=5), padding=5)

        return  contenedor


