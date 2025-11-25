import  flet    as  ft
import  os

class   page_data:

    def __init__(self, color, font, dimentions, dir_imagen, dir_data_save):
        self.page   =   None

        ###---------------------condicional--------------------###
        if  dimentions[0]   >   dimentions[1]:
            w   =   dimentions[0]*0.85
            s   =   dimentions[1]*0.9*0.07

        elif    dimentions[0]   <   dimentions[1]:
            w   =   dimentions[0]*0.85
            s   =   dimentions[0]*0.9*0.1
        
        elif    dimentions[0]   ==   dimentions[1]:
            w   =   dimentions[0]*0.85
            s   =   dimentions[1]*0.9*0.09


        ##########################################################
        ###--------------------def_fuctions--------------------###
        ##########################################################
        def contraccion_container_up(e):
            box_up.height   =   dimentions[1]*0.4
            box_down.height =   dimentions[1]*0.48
            box_up.content  =   ft.Column([box_title, boton_back_expan("hola")])
            return  self.page.update()

        def expan_container_up(e):
            box_up.height   =   dimentions[1]*0.9
            box_down.height =   dimentions[1]*0 
            box_up.content  =   ft.Column([box_title, data_list])
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
                on_long_press=lambda    e: menu_conf(label),
                height=dimentions[1]*0.9*0.1
            )
            return  cont_button
        
        def menu_conf(label):

            def open(e):
                contraccion_container_up(e)
                self.page.close(bs)
                return  self.page.update()

            def insert_name(label):

                def save_and_exit(e):

                    def rename_directory(new_name):
                        os.rename(f"{dir_data_save}/{label}" , f"{dir_data_save}/{new_name}")
                        # implementation reload page
                        # box_up.content  =   ft.Column([box_title, data_list])
                        return  self.page.update()

                    if  dlg_modal.content.value ==  "":
                        return  print("vacio")
                    elif    dlg_modal.content.value !=  "":
                        self.page.close(dlg_modal)
                        return rename_directory(dlg_modal.content.value)

                dlg_modal = ft.AlertDialog(
                    modal=True,
                    elevation=20,
                    bgcolor=color[3], 

                    title=ft.Text(
                        "rename", 
                        font_family=font[0], 
                        size=s*0.35, 
                        color=color[0]
                    ),

                    content=ft.TextField(
                        label   =   f"{label}", 
                        color   =   color[2], 
                        bgcolor =   color[0], 
                        label_style =   ft.TextStyle(color=color[2]),
                        border_color    =   color[2], 
                        border_radius   =   10,
                        border_width    =   1,
                        cursor_color    =   color[2],
                        cursor_height   =   20,
                        cursor_radius   =   10,
                        cursor_width    =   1,
                        selection_color =   color[1],
                        text_style=ft.TextStyle(font_family=font[1]),
                    ),

                    actions=[
                        ft.FilledButton(
                            content=ft.Text("Back", font_family=font[1], size=s*0.5, color=color[0]),
                            bgcolor=color[3],
                            on_click=lambda e: self.page.close(dlg_modal),
                        ),
                        ft.FilledButton(
                            content=ft.Text("Save", font_family=font[1], size=s*0.5, color=color[3]),
                            bgcolor=color[0],
                            on_click=save_and_exit,
                        ),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                return  self.page.open(dlg_modal)
            
            def rename(label):
                self.page.close(bs)
                insert_name(label)
                return self.page.update()


            bs = ft.BottomSheet(
                ft.Container(
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Text(str(label), color=color[1], font_family=font[1], size=s*0.5),
                                bgcolor=color[2],
                                border_radius=15,
                                width=dimentions[0],
                                padding=10,
                                border=ft.border.all(2, color[1]),
                                alignment=ft.alignment.center,
                                shadow=[
                                    ft.BoxShadow(
                                        color=color[2],
                                        blur_radius=10,
                                        spread_radius=2,
                                    )
                                ],
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.REMOVE_RED_EYE_SHARP, size=s*0.5, color=color[2]),
                                        ft.Text("Open", color=color[2], font_family=font[1], size=s*0.4)
                                    ],
                                    spacing=20,
                                ),
                                width=dimentions[0]*0.6,
                                padding=10,
                                on_click=open
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.EDIT, size=s*0.5, color=color[2]),
                                        ft.Text("Rename", color=color[2], font_family=font[1], size=s*0.4)
                                    ],
                                    spacing=20,
                                ),
                                width=dimentions[0]*0.6,
                                padding=10,
                                on_click=lambda e:rename(label)
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.DELETE, size=s*0.5, color=color[2]),
                                        ft.Text("Delete", color=color[2], font_family=font[1], size=s*0.4)
                                    ],
                                    spacing=20,
                                ),
                                width=dimentions[0]*0.6,
                                padding=10,
                                on_click=lambda e: self.page.close(bs)
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        tight=True,
                    ),
                    padding=20,
                ),
                bgcolor=color[1],
                open=False,
            )
            return  self.page.open(bs)


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
        
        def boton_back_expan(label):
            boton  =   ft.Container(
                content=ft.Text("v", font_family=font[2], color=color[7], size=s*0.5),
                on_click=expan_container_up,
                padding=10,
                alignment=ft.alignment.center,
                expand=True
            )
            return boton

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
            width=dimentions[0]*0.8,
            height=dimentions[1]*0.9,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        box_down=   ft.Container(
            content=ft.Column([]), 
            bgcolor=color[2], 
            padding=0,
            width=dimentions[0]*0.8,
            height=dimentions[1]*0,
            border_radius=15,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )

        ##########################################################
        ###------------------construc_page_data----------------###
        ##########################################################
        page_data =   ft.Container(
            content=ft.Column(
                [box_up, box_down], 
                spacing=dimentions[1]*0.02, 
                horizontal_alignment=ft.CrossAxisAlignment.END
            ),
            padding=0,
            width=w,
            height=dimentions[1]*0.9,
            animate=ft.Animation(400, ft.AnimationCurve.DECELERATE),
        )
        self.page_data  =   page_data


