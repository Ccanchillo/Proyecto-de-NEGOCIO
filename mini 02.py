import re

def convertir_a_markdown(texto):
    # Encabezados 1,2,3 pegados a la palabra, convierte "1Economia" en "# Economia"
    texto = re.sub(r'^1(\S)', r'# \1', texto, flags=re.MULTILINE)
    texto = re.sub(r'^2(\S)', r'## \1', texto, flags=re.MULTILINE)
    texto = re.sub(r'^3(\S)', r'### \1', texto, flags=re.MULTILINE)

    # Negrita 4:
    # 4Palabra → solo esa palabra en negrita
    texto = re.sub(r'4(\w+)', r'**\1**', texto)
    # 4...4 → toda la línea en negrita
    def negrita_linea(match):
        contenido = match.group(1)
        return f'**{contenido}**'
    texto = re.sub(r'^4(.+?)4$', negrita_linea, texto, flags=re.MULTILINE)

    # Cursiva 5:
    # 5Palabra → solo esa palabra en cursiva
    texto = re.sub(r'5(\w+)', r'*\1*', texto)
    # 5...5 → toda la línea en cursiva
    def cursiva_linea(match):
        contenido = match.group(1)
        return f'*{contenido}*'
    texto = re.sub(r'^5(.+?)5$', cursiva_linea, texto, flags=re.MULTILINE)

    # Enlaces 7texto url7
    def enlace_simplificado(match):
        texto_link = match.group(1)
        url = match.group(2)
        return f'[{texto_link}]({url})'
    texto = re.sub(r'7(\S+)\s+(\S+)7', enlace_simplificado, texto)

    # Imágenes 8alt ruta8
    def imagen_simplificada(match):
        alt = match.group(1)
        ruta = match.group(2)
        return f'![{alt}]({ruta})'
    texto = re.sub(r'8(\S+)\s+(\S+)8', imagen_simplificada, texto)

    return texto

def leer_entrada_multilinea():
    print("Escribe tu texto personalizado. Escribe 'FIN' en una línea para terminar.\n")
    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)
    return "\n".join(lineas)

def guardar_como_markdown_desde_consola(nombre_archivo="documentacion.md"):
    texto = leer_entrada_multilinea()
    markdown = convertir_a_markdown(texto)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ Markdown generado en: {nombre_archivo}")

# Para probarlo ejecuta esta función
if __name__ == "__main__":
    guardar_como_markdown_desde_consola()

    