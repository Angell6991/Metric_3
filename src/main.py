# suport_data    =   os.path.join(os.getcwd(), ".metric3_data_list")
# os.makedirs(suport_data, exist_ok=True)
# dir_suport = suport_data


diccionary  =   {
    "name":   "sara",
    "age":    31,
}

print(diccionary["name"])
print(diccionary["age"])



# import flet as ft


# def main(page: ft.Page):

#     page.fonts = {
#         "open": "assets/fonts/angell-font.ttf",
#     }

#     texto   =   ft.Text("a c l m g h x d", font_family="open", size=50, color="#ffffff")
#     cont    =   ft.Container(ft.Row([texto]), padding=10, bgcolor="#2e2e2e", border_radius=15)

#     return  page.add(cont)

# ft.app(main)
