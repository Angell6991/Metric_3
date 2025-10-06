import  flet    as  ft

class   page_save:

    def __init__(self, color, font, dimentions, dir_data_intro):
        self.page   =   None
        self.color  =   color
        self.font   =   font
        self.dimentions =   dimentions
        self.dir_data_intro =   dir_data_intro

        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            self.s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            self.s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            self.s   =   dimentions[1]*0.9*0.09


    ##########################################################
    ###--------------------def_fuctions--------------------###
    ##########################################################
    def float_window(self, label):

        ###------------------def_condicionales-----------------###
        if  label   ==  "coordinates":
            titulo  =   "coordinates"
            icon    =   "x"
            dir     =   self.dir_data_intro[0]
            sizee   =   self.s*0.45

        elif  label   ==  "constants":
            titulo  =   "constant \n parameters"
            icon    =   "c"
            dir     =   self.dir_data_intro[1]
            sizee   =   self.s*0.4

        elif  label   ==  "metric_tensor":
            titulo  =   "metric tensor"
            icon    =   "g"
            dir     =   self.dir_data_intro[2]
            sizee   =   self.s*0.45

        ###---------------def_function_of_save_data------------###        
        def guardar_archivo(e):
            with    open(str(dir), "w", encoding="utf-8")    as  f:
                f.write(intro_data.value)
            return  self.page.update()
     
        ###----------------def_space_intro_data----------------###
        intro_data  =   ft.TextField(
            label=None,
            multiline=True,
            min_lines=1,
            max_lines=None,
            width=self.dimentions[0]*0.5, 
            height=self.dimentions[1]*0.3, 
            border=ft.InputBorder.NONE,
            cursor_color=self.color[0],
            selection_color=self.color[3],
            color=self.color[0],
            text_style=ft.TextStyle(font_family=self.font[1]),
        )

        contenedor   =   ft.Container(
            content=intro_data, 
            width=self.dimentions[0]*0.5, 
            height=self.dimentions[1]*0.3, 
            bgcolor=self.color[2],
            border_radius=10,
            border=ft.border.all(2, self.color[0]),
            shadow=ft.BoxShadow(color=self.color[2], blur_radius=15),
            padding=5,
        )

        dlg_modal = ft.AlertDialog(
            modal=True,
            elevation=20,
            bgcolor=self.color[3], 

            title=ft.Container(
                ft.Row([
                    ft.Text(icon, font_family=self.font[2], size=self.s*1.3, color=self.color[0]),
                    ft.Text(titulo, font_family=self.font[0], size=sizee, color=self.color[0])
                ])
            ),

            content=contenedor,
            actions=[
                ft.FilledButton(
                    content=ft.Text("s", font_family=self.font[2], size=self.s*0.5, color=self.color[3]),
                    tooltip="save and exit",
                    bgcolor=self.color[0],
                    on_click=lambda e: self.page.close(dlg_modal),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            on_dismiss=guardar_archivo,
        )

        ###------------abrir_contenido_del_input_data----------###
        with    open(str(dir), "r", encoding="utf-8")   as  f:
            texto=f.read()
            intro_data.value=texto
            self.page.update()


        return  self.page.open(dlg_modal)


