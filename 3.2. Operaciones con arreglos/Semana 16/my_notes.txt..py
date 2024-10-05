# Escritura de Archivo de Texto

# Abre (o crea si no existe) un archivo llamado 'my_notes.txt' en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de texto en el archivo
    file.write("Esta es la primera línea de mis notas personales.\n")
    file.write("Aquí está la segunda línea, aprendiendo Python.\n")
    file.write("Tercera línea: ¡Estoy trabajando con archivos en Python!\n")

# Lectura de Archivo de Texto

# Abre el archivo 'my_notes.txt' en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee cada línea del archivo utilizando un bucle
    line = file.readline()
    while line:
        # Muestra cada línea leída en la consola
        print(line.strip())  # .strip() elimina los saltos de línea extras
        line = file.readline()

# Nota: No es necesario cerrar el archivo manualmente porque usamos "with open",
# que se asegura de cerrar el archivo automáticamente después de completar las operaciones.
