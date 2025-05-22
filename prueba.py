import os

# listado_path = "C:/Users/alu_torre1/Desktop/hola/listado.txt"
# archivo_salida = "C:/Users/alu_torre1/Desktop/hola/documento.md"

listado_path = "F:\Proyecto de NEGOCIO\listado.txt"
archivo_salida = "F:\Proyecto de NEGOCIO\documento.md"

# Asegurarse de que la carpeta exista (por si acaso)
os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

# Leer listado de palabras sugeridas
with open(listado_path, "r", encoding="utf-8") as f:
    palabras_sugeridas = [line.strip() for line in f if line.strip()]

print("Escribe tu texto línea por línea.")
print("Si quieres autocompletar una palabra, escribe el inicio + '*' (ej: 'docu*').")
print("Escribe 'SALIR' para terminar.\n")

# Escritura en el archivo de salida
with open(archivo_salida, "w", encoding="utf-8") as f:
    while True:
        try:
            linea = input("> ").strip()
        except EOFError:
            break  # Por si se usa en entornos sin stdin interactivo

        if linea.upper() == 'SALIR':
            print("Guardado.")
            break

        palabras = linea.split()
        nueva_linea = []

        for palabra in palabras:
            if palabra.endswith("*"):
                base = palabra[:-1]
                coincidencias = [p for p in palabras_sugeridas if p.startswith(base)]
                if coincidencias:
                    print(f"Sugerencia: usando '{coincidencias[0]}'")
                    nueva_linea.append(coincidencias[0])
                else:
                    print(f"No hay sugerencia para '{base}', usando tal cual.")
                    nueva_linea.append(base)
            else:
                nueva_linea.append(palabra)

        linea_final = " ".join(nueva_linea)
        f.write(linea_final + "\n")