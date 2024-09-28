# Paso 1: Crear un Diccionario
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
print("Diccionario inicial:", informacion_personal)

# Paso 2: Acceder y Modificar Valores
ciudad_actual = informacion_personal["ciudad"]
print("Ciudad actual:", ciudad_actual)
informacion_personal["ciudad"] = "Guayaquil"
print("Diccionario después de modificar la ciudad:", informacion_personal)

# Paso 3: Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"
print("Diccionario después de agregar 'telefono':", informacion_personal)

# Paso 4: Eliminar una Clave
informacion_personal.pop("edad", None)
print("Diccionario después de eliminar 'edad':", informacion_personal)

# Paso 5: Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)
