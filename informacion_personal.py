# Diccionario con la información de una persona
informacion_personal = {
    "nombre": "Paulina Garcia",
    "edad": 24,
    "ciudad": "Quito",
    "profesion": "Odontologa"
}

# Cambiar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Agregar o cambiar la profesión
informacion_personal["profesion"] = "Odontologa General"

# Verificar si existe el teléfono, si no lo agrego
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0984007872"

# Eliminar la edad
del informacion_personal["edad"]

# Mostrar el resultado final
print(informacion_personal)
