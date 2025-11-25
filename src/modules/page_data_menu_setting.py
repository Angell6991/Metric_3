import flet as ft
import shutil
import os

def menu_conf(page, color, font, s, dir_data_save, dimentions, label, refresh_list_callback, contraccion_container_callback):


    ##########################################################
    ###-----------def_action_open_bow_down-----------------###
    ##########################################################
    def open(e):
        contraccion_container_callback()
        page.close(bs)
        return page.update()


    ##########################################################
    ###------------def_action_rename_item_list-------------###
    ##########################################################
    def insert_name(label):
        
        def save_and_exit(e):
            def rename_directory(new_name):
                os.rename(f"{dir_data_save}/{label}", f"{dir_data_save}/{new_name}")
                return refresh_list_callback()

            if dlg_modal.content.value == "":
                return print("vacio")
            elif dlg_modal.content.value != "":
                page.close(dlg_modal)
                return rename_directory(dlg_modal.content.value)

        dlg_modal = ft.AlertDialog(
            modal=True,
            elevation=20,
            bgcolor=color[3],

            title=ft.Text(
                "rename",
                font_family=font[0],
                size=s * 0.35,
                color=color[0]
            ),

            content=ft.TextField(
                label=f"{label}",
                color=color[2],
                bgcolor=color[0],
                label_style=ft.TextStyle(color=color[2]),
                border_color=color[2],
                border_radius=10,
                border_width=1,
                cursor_color=color[2],
                cursor_height=20,
                cursor_radius=10,
                cursor_width=1,
                selection_color=color[1],
                text_style=ft.TextStyle(font_family=font[1]),
            ),

            actions=[
                ft.FilledButton(
                    content=ft.Text("Back", font_family=font[1], size=s * 0.5, color=color[0]),
                    bgcolor=color[3],
                    on_click=lambda e: page.close(dlg_modal),
                ),
                ft.FilledButton(
                    content=ft.Text("Save", font_family=font[1], size=s * 0.5, color=color[3]),
                    bgcolor=color[0],
                    on_click=save_and_exit,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        return page.open(dlg_modal)

    def rename(label):
        page.close(bs)
        insert_name(label)
        return page.update()


    ##########################################################
    ###---------------open_window_settings-----------------###
    ##########################################################
    def confir(label):

        def remove_exit(e):
            shutil.rmtree(f"{dir_data_save}/{label}")
            page.close(dlg_modal)
            return refresh_list_callback()

        dlg_modal = ft.AlertDialog(
            modal=True,
            elevation=20,
            bgcolor=color[3],

            title=ft.Text(
                "Delete:",
                font_family=font[1],
                size=s * 0.6,
                color=color[7]
            ),

            content=ft.Text(f"{label}", font_family=font[1], size=s * 0.5, color=color[0]),

            actions=[
                ft.FilledButton(
                    content=ft.Text("No", font_family=font[1], size=s * 0.5, color=color[0]),
                    bgcolor=color[3],
                    on_click=lambda e: page.close(dlg_modal),
                ),
                ft.FilledButton(
                    content=ft.Text("Yes", font_family=font[1], size=s * 0.5, color=color[3]),
                    bgcolor=color[0],
                    on_click=remove_exit,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        return page.open(dlg_modal)    

    def delete(label):
        page.close(bs)
        confir(label)
        return  page.update()


    ##########################################################
    ###---------------open_window_settings-----------------###
    ##########################################################
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text(str(label), color=color[1], font_family=font[1], size=s * 0.5),
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
                                ft.Icon(ft.Icons.REMOVE_RED_EYE_SHARP, size=s * 0.5, color=color[2]),
                                ft.Text("Open", color=color[2], font_family=font[1], size=s * 0.4)
                            ],
                            spacing=20,
                        ),
                        width=dimentions[0] * 0.6,
                        padding=10,
                        on_click=open
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.EDIT, size=s * 0.5, color=color[2]),
                                ft.Text("Rename", color=color[2], font_family=font[1], size=s * 0.4)
                            ],
                            spacing=20,
                        ),
                        width=dimentions[0] * 0.6,
                        padding=10,
                        on_click=lambda e: rename(label)
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.DELETE, size=s * 0.5, color=color[2]),
                                ft.Text("Delete", color=color[2], font_family=font[1], size=s * 0.4)
                            ],
                            spacing=20,
                        ),
                        width=dimentions[0] * 0.6,
                        padding=10,
                        on_click=lambda e: delete(label)
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


    ##########################################################
    ###--------------return_function_menu_conf-------------###
    ##########################################################
    return page.open(bs)


