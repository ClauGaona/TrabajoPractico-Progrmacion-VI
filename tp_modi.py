import flet as ft

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 500
    page.title = "Lista de compras"

    # Lista para almacenar las tareas
    task_list = []

    # Crear un campo de texto para la entrada
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300, color="#FFFFFF")  # Texto en blanco

    selected_task = None  # Para almacenar la tarea seleccionada

    def add_clicked(e):
        # Agregar una casilla de verificación con la etiqueta de la tarea
        if new_task.value:  # Asegúrate de que no esté vacío
            checkbox = ft.Checkbox(label=new_task.value, on_change=task_selected)
            task_list.append(checkbox)
            task_container.controls.append(checkbox)
            new_task.value = ""
            new_task.focus()
            page.update()

    def modify_clicked(e):
        # Modificar la tarea seleccionada
        nonlocal selected_task
        if selected_task:
            selected_task.label = new_task.value
            new_task.value = ""
            selected_task = None
            page.update()

    def delete_clicked(e):
        # Eliminar la tarea seleccionada
        nonlocal selected_task
        if selected_task:
            task_list.remove(selected_task)
            task_container.controls.remove(selected_task)
            new_task.value = ""
            selected_task = None
            page.update()

    def task_selected(e):
        # Seleccionar una tarea de la lista
        nonlocal selected_task
        selected_task = e.control

    # Contenedor para la lista de tareas
    task_container = ft.Column()

    # Logo y texto del encabezado
    logo = ft.Image(src=r"C:\Users\artur\OneDrive\Escritorio\ClaudiaGaona\Claudia Gaona -Programacion IV\TP\logo.jpeg", width=150, height=150)
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD, color="#FFFFFF")  # Texto blanco

    # Organizar el encabezado en una columna
    header = ft.Column([logo, header_text], alignment="center")

    # Botones de acción con iconos en blanco
    add_button = ft.IconButton(ft.icons.ADD, on_click=add_clicked, icon_color="#FFFFFF")  # Icono en blanco
    modify_button = ft.IconButton(ft.icons.EDIT, on_click=modify_clicked, icon_color="#FFFFFF")  # Icono en blanco
    delete_button = ft.IconButton(ft.icons.DELETE, on_click=delete_clicked, icon_color="#FFFFFF")  # Icono en blanco

    # Agregar elementos a la aplicación con un fondo y dimensiones ajustadas
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    header,
                    ft.Divider(height=20),  # Agrega un divisor
                    ft.Row([new_task], alignment="center"),
                    task_container,
                    ft.Divider(height=20),  # Agrega un divisor
                    ft.Row([add_button, modify_button, delete_button], alignment="center")  # Botones en la parte inferior
                ]
            ),
            bgcolor="#5f54ab",  # Fondo azul marino
            width=600,  # Ancho del contenedor
            height=400,  # Altura del contenedor
            padding=20,
            border_radius=10
        )
    )

# Ejecutar la aplicación
ft.app(target=main)



