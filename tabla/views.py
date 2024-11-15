from django.shortcuts import render

def mostrar_tabla(request):
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]
    apellidos = ["Pérez", "González", "Ramírez", "López", "Martínez"]
    edades = [25, 30, 22, 28, 35]

    personas = [
        {"nombre": nombres[i], "apellido": apellidos[i], "edad": edades[i]}
        for i in range(len(nombres))
    ]

    return render(request, "tabla.html", {"personas": personas})
