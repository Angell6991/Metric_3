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
        self.name_metric    =   "vacio"

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

            create  =   os.path.join(self.data_save, self.name_metric)
            os.makedirs(create, exist_ok=True)

            metric_data_save   =   [
                f"{create}/coordinates.dat",
                f"{create}/constants.dat",
                f"{create}/metric_tensor.dat",
                f"{create}/inverse_metric_tensor.dat",
                f"{create}/symbol_christofell.dat",
                f"{create}/riemann_tensor.dat",
                f"{create}/ricci_tensor.dat",
                f"{create}/escalar_curvatura.dat",
            ]
            gg  =   cal.relativity(self.dir_data_intro, metric_data_save)
            
            gg.save_coordinates()
            cont_load.value =   (1/8)*1
            self.page.update()

            gg.save_constants()
            cont_load.value =   (1/8)*2
            self.page.update()            

            gg.metric_tensor()
            cont_load.value =   (1/8)*3
            self.page.update()
            
            gg.inverse_metric()
            cont_load.value =   (1/8)*4
            self.page.update() 
            
            gg.christofell()
            cont_load.value =   (1/8)*5
            self.page.update()
            
            gg.riemann_tensor()
            cont_load.value =   (1/8)*6
            self.page.update()
            
            gg.ricci_tensor()
            cont_load.value =   (1/8)*7
            self.page.update()
            
            gg.e_curvatura()
            cont_load.value =   (1/8)*8
            self.page.update()
            
            up.content  =   cont_icon
            cont    =   ft.Container(
                ft.Row(
                    [
                        ft.Text(
                            "Completed calculation see the database", 
                            font_family=self.font[1], color=self.color[2], 
                            size=self.s*0.4
                        ),
                        ft.Text("d", font_family=self.font[2], color=self.color[2], size=self.s*0.5)
                    ],
                    spacing=self.w*0.2,
                )
            )
            self.page.open(ft.SnackBar(content=cont, bgcolor=self.color[0], duration=4000))
            
            self.name_metric    =   str("vacio")
            return  self.page.update()
        
        ###----------------------------------------------------###
        def insert_name(e):

            def save_and_exit(e):
                if  dlg_modal.content.value ==  "":
                    return  print("vacio")
                elif    dlg_modal.content.value !=  "":
                    self.page.close(dlg_modal)
                    self.name_metric    =   str(dlg_modal.content.value)
                    return calculate(e)

            dlg_modal = ft.AlertDialog(
                modal=True,
                elevation=20,
                bgcolor=self.color[3], 

                title=ft.Text(
                    "insert  the  name \n of  the  metric", 
                    font_family=self.font[0], 
                    size=self.s*0.35, 
                    color=self.color[0]
                ),

                content=ft.TextField(
                    label   =   "Name", 
                    color   =   self.color[2], 
                    bgcolor =   self.color[0], 
                    label_style =   ft.TextStyle(color=self.color[2]),
                    border_color    =   self.color[2], 
                    border_radius   =   10,
                    border_width    =   1,
                    cursor_color    =   self.color[2],
                    cursor_height   =   20,
                    cursor_radius   =   10,
                    cursor_width    =   1,
                    selection_color =   self.color[1],
                    text_style=ft.TextStyle(font_family=self.font[1]),
                ),

                actions=[
                    ft.FilledButton(
                        content=ft.Text("Back", font_family=self.font[1], size=self.s*0.5, color=self.color[0]),
                        bgcolor=self.color[3],
                        on_click=lambda e: self.page.close(dlg_modal),
                    ),
                    ft.FilledButton(
                        content=ft.Text("Start", font_family=self.font[1], size=self.s*0.5, color=self.color[3]),
                        bgcolor=self.color[0],
                        on_click=save_and_exit,
                    ),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            return  self.page.open(dlg_modal)

        ###----------------------------------------------------###
        cont_icon   =   ft.Container(
            ft.Text("w", font_family=self.font[2], color=self.color[4], size=self.s*0.65),
            on_click=insert_name,
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


