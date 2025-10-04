import  flet    as  ft

class   page_save:

    def __init__(self, color, font, dimentions, dir_data_intro):
        self.page   =   None
        self.color  =   color
        self.font   =   font
        self.dimentions =   dimentions
        self.dir_data_intro =   dir_data_intro

    ##########################################################
    ###--------------------def_fuctions--------------------###
    ##########################################################
    def float_window(self):
       
        intro_data  =   ft.TextField(
            label="Auto adjusted height with max lines",
            multiline=True,
            min_lines=1,
            max_lines=1000,
            width=600,
            height=400,
        )

        contenedor   =   ft.Container(
            content=intro_data, 
            width=self.dimentions[0]*0.5, 
            height=self.dimentions[1]*0.3, 
            bgcolor=self.color[2],
            border_radius=10,
            border=ft.border.all(2, self.color[0]),
            shadow=ft.BoxShadow(color=self.color[2], blur_radius=15)
        )

        dlg_modal = ft.AlertDialog(
            modal=True,
            elevation=20,
            bgcolor=self.color[3], 

            title=ft.Container(
                ft.Row(
                    [
                        ft.Text("x", font_family=self.font[2], size=self.dimentions[0]*0.1, color=self.color[0]),
                        ft.Text("coordinates", font_family=self.font[0], size=self.dimentions[0]*0.04, color=self.color[0])
                    ]
                )
            ),

            content=contenedor,
            actions=[
                ft.FilledButton(
                    content=ft.Text("s", font_family=self.font[2], size=self.dimentions[0]*0.05, color=self.color[3]),
                    tooltip="save and exit",
                    bgcolor=self.color[0],
                    on_click=lambda e: self.page.close(dlg_modal)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        
        return  self.page.open(dlg_modal)



# coordinates     =   os.path.join(data_input, "input_coordinates" + ".dat")
# constants       =   os.path.join(data_input, "input_constants" + ".dat")
# metric_tensor   =   os.path.join(data_input, "input_metric_tensor" + ".dat")

